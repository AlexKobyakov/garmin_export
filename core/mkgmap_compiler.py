# -*- coding: utf-8 -*-
"""
Mkgmap Compiler for Garmin Export Plugin
Компилятор mkgmap для плагина экспорта в Garmin

Особенности:
  - валидация mkgmap.jar/splitter.jar по содержимому архива (без запуска Java);
  - автоопределение пути к Java (PATH, JAVA_HOME, типовые каталоги);
  - запуск без всплывающего консольного окна на Windows;
  - команда формируется модулем mkgmap_command строго по документации.

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

import glob
import os
import subprocess
import sys
import time
import zipfile

from . import mkgmap_command


def _subprocess_flags():
    """Флаги subprocess: не показывать консольное окно на Windows"""
    if sys.platform.startswith('win'):
        return {'creationflags': subprocess.CREATE_NO_WINDOW}
    return {}


def validate_jar(jar_path, required_prefix, check_extension=True):
    """Проверка, что файл является jar-архивом с нужными классами.

    Args:
        jar_path: путь к jar файлу
        required_prefix: префикс пути внутри архива,
            например 'uk/me/parabola/mkgmap'
        check_extension: требовать расширение .jar. Отключается при проверке
            промежуточного файла загрузки (*.jar.part), который ещё не
            переименован в итоговый .jar.
    """
    if not jar_path or not os.path.isfile(jar_path):
        return False
    if check_extension and not jar_path.lower().endswith('.jar'):
        return False
    try:
        with zipfile.ZipFile(jar_path) as jar:
            for name in jar.namelist():
                if name.startswith(required_prefix):
                    return True
    except (zipfile.BadZipFile, OSError):
        return False
    return False


def validate_mkgmap_jar(jar_path):
    """Проверка корректности mkgmap.jar"""
    return validate_jar(jar_path, 'uk/me/parabola/mkgmap')


def validate_splitter_jar(jar_path):
    """Проверка корректности splitter.jar"""
    return validate_jar(jar_path, 'uk/me/parabola/splitter')


def find_java():
    """Автоопределение пути к java.

    Возвращает путь к исполняемому файлу java или None.
    """
    exe = 'java.exe' if sys.platform.startswith('win') else 'java'

    candidates = []

    # 1. JAVA_HOME
    java_home = os.environ.get('JAVA_HOME', '')
    if java_home:
        candidates.append(os.path.join(java_home, 'bin', exe))

    # 2. PATH
    for path_dir in os.environ.get('PATH', '').split(os.pathsep):
        if path_dir:
            candidates.append(os.path.join(path_dir, exe))

    # 3. Типовые каталоги установки на Windows
    if sys.platform.startswith('win'):
        for env_key in ('ProgramFiles', 'ProgramFiles(x86)', 'ProgramW6432'):
            program_files = os.environ.get(env_key)
            if not program_files:
                continue
            for vendor in ('Java', 'Eclipse Adoptium', 'Amazon Corretto',
                           'Zulu', 'Microsoft', 'BellSoft', 'AdoptOpenJDK'):
                pattern = os.path.join(program_files, vendor, '*', 'bin', exe)
                candidates.extend(sorted(glob.glob(pattern), reverse=True))

    for candidate in candidates:
        if candidate and os.path.isfile(candidate):
            return candidate

    return None


def check_java_available(java_path=None):
    """Проверка доступности Java"""
    java = java_path or 'java'
    try:
        result = subprocess.run(
            [java, '-version'],
            capture_output=True, timeout=15, **_subprocess_flags())
        return result.returncode == 0
    except (subprocess.SubprocessError, OSError):
        return False


def get_java_version(java_path=None):
    """Строка версии Java или None"""
    java = java_path or 'java'
    try:
        result = subprocess.run(
            [java, '-version'],
            capture_output=True, text=True, timeout=15, **_subprocess_flags())
        # Java выводит версию в stderr
        output = result.stderr or result.stdout or ''
        for line in output.splitlines():
            if 'version' in line:
                return line.strip()
    except (subprocess.SubprocessError, OSError):
        pass
    return None


def get_mkgmap_version(jar_path, java_path=None):
    """Версия mkgmap (строка) или None"""
    java = java_path or 'java'
    try:
        result = subprocess.run(
            [java, '-jar', jar_path, '--version'],
            capture_output=True, text=True, timeout=30, **_subprocess_flags())
        output = (result.stderr or '') + (result.stdout or '')
        return output.strip().splitlines()[0] if output.strip() else None
    except (subprocess.SubprocessError, OSError, IndexError):
        return None


class MkgmapCompiler:
    """Компилятор для преобразования MP файлов в IMG через mkgmap"""

    def __init__(self):
        self.process = None
        self.is_cancelled = False

    # ------------------------------------------------------------------
    # Валидация (сохранены прежние имена методов для совместимости)
    # ------------------------------------------------------------------

    def validate_mkgmap(self, mkgmap_path):
        """Проверка корректности пути к mkgmap.jar"""
        return validate_mkgmap_jar(mkgmap_path)

    def check_java_available(self, java_path=None):
        return check_java_available(java_path)

    def get_java_version(self, java_path=None):
        return get_java_version(java_path)

    # ------------------------------------------------------------------
    # Компиляция
    # ------------------------------------------------------------------

    def compile_to_img(self, settings, progress_callback=None):
        """Компиляция MP файла в IMG.

        Args:
            settings: словарь с ключами:
                mkgmap_path, java_path, input_files (list), output_folder,
                output_filename, mkgmap_options (dict для mkgmap_command)
            progress_callback: функция (str) -> None
        Returns:
            путь к итоговому IMG файлу
        """
        mkgmap_path = settings['mkgmap_path']
        java_path = settings.get('java_path') or find_java() or 'java'
        input_files = settings['input_files']
        output_folder = settings['output_folder']
        output_filename = settings.get('output_filename') or ''

        for input_file in input_files:
            if not os.path.exists(input_file):
                raise Exception('Входной файл не найден: {0}'.format(input_file))

        if not os.path.isdir(output_folder):
            raise Exception('Выходная папка не найдена: {0}'.format(output_folder))

        options = dict(settings.get('mkgmap_options') or {})
        options['output_dir'] = output_folder

        cmd = mkgmap_command.build_command(
            java_path, mkgmap_path, options, input_files)

        if progress_callback:
            progress_callback('Команда: {0}'.format(
                subprocess.list2cmdline(cmd) if hasattr(subprocess, 'list2cmdline')
                else ' '.join(cmd)))

        started_at = time.time()

        self.is_cancelled = False
        self._execute(cmd, output_folder, progress_callback)

        output_file = self._find_output_file(
            output_folder, output_filename, started_at)
        if not output_file:
            raise Exception('Не удалось найти созданный IMG файл')

        return output_file

    def _execute(self, cmd, working_dir, progress_callback):
        """Выполнение команды mkgmap с потоковым чтением вывода"""
        try:
            self.process = subprocess.Popen(
                cmd,
                cwd=working_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                errors='replace',
                **_subprocess_flags())
        except FileNotFoundError:
            raise Exception(
                'Не удалось запустить Java. Установите Java (JRE 8+) или '
                'укажите путь к java в настройках плагина.')

        output_lines = []

        try:
            for line in self.process.stdout:
                line = line.rstrip()
                if line:
                    output_lines.append(line)
                    if progress_callback:
                        progress_callback(line)
                if self.is_cancelled:
                    break
        finally:
            if self.is_cancelled and self.process.poll() is None:
                self.process.terminate()
                time.sleep(1)
                if self.process.poll() is None:
                    self.process.kill()

        return_code = self.process.wait()

        if self.is_cancelled:
            raise Exception('Компиляция отменена пользователем')

        if return_code != 0:
            tail = '\n'.join(output_lines[-15:])
            raise Exception(
                'mkgmap завершился с ошибкой (код {0}):\n{1}'.format(
                    return_code, tail))

    def _find_output_file(self, output_folder, output_filename, started_at):
        """Поиск созданного IMG файла.

        Приоритет: gmapsupp.img -> <имя>.img -> самый свежий *.img,
        созданный после запуска компиляции.
        """
        gmapsupp = os.path.join(output_folder, 'gmapsupp.img')
        if os.path.isfile(gmapsupp) and os.path.getmtime(gmapsupp) >= started_at - 1:
            return gmapsupp

        if output_filename:
            named = os.path.join(output_folder, output_filename + '.img')
            if os.path.isfile(named) and os.path.getmtime(named) >= started_at - 1:
                return named

        candidates = []
        try:
            for file_name in os.listdir(output_folder):
                if file_name.lower().endswith('.img'):
                    file_path = os.path.join(output_folder, file_name)
                    mtime = os.path.getmtime(file_path)
                    if mtime >= started_at - 1:
                        candidates.append((mtime, file_path))
        except OSError:
            return None

        if candidates:
            candidates.sort(reverse=True)
            return candidates[0][1]

        return None

    def stop_compilation(self):
        """Остановка компиляции"""
        self.is_cancelled = True

        if self.process and self.process.poll() is None:
            try:
                self.process.terminate()
                for _ in range(50):
                    if self.process.poll() is not None:
                        break
                    time.sleep(0.1)
                if self.process.poll() is None:
                    self.process.kill()
            except OSError:
                pass
