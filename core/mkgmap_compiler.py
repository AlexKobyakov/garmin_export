# -*- coding: utf-8 -*-
"""
Mkgmap Compiler for Garmin Export Plugin
Компилятор mkgmap для плагина экспорта в Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

import os
import subprocess
import threading
import time
from qgis.PyQt.QtCore import QObject


class MkgmapCompiler(QObject):
    """Компилятор для преобразования MP файлов в IMG через mkgmap"""
    
    def __init__(self):
        super().__init__()
        self.process = None
        self.is_cancelled = False
    
    def validate_mkgmap(self, mkgmap_path):
        """Проверка корректности пути к mkgmap.jar"""
        if not mkgmap_path or not os.path.exists(mkgmap_path):
            return False
        
        if not mkgmap_path.lower().endswith('.jar'):
            return False
        
        # Проверяем, что это действительно mkgmap
        try:
            result = subprocess.run([
                'java', '-jar', mkgmap_path, '--help'
            ], capture_output=True, text=True, timeout=10)
            
            return 'mkgmap' in result.stdout.lower() or 'mkgmap' in result.stderr.lower()
            
        except (subprocess.TimeoutExpired, subprocess.SubprocessError, FileNotFoundError):
            return False
    
    def compile_to_img(self, settings, progress_callback=None):
        """Компиляция MP файла в IMG"""
        mkgmap_path = settings['mkgmap_path']
        input_file = settings['input_file']
        output_folder = settings['output_folder']
        output_filename = settings['output_filename']
        family_id = settings['family_id']
        map_name = settings['map_name']
        
        # Проверяем входные данные
        if not os.path.exists(input_file):
            raise Exception(f"MP файл не найден: {input_file}")
        
        if not os.path.exists(output_folder):
            raise Exception(f"Выходная папка не найдена: {output_folder}")
        
        # Формируем команду mkgmap
        cmd = self._build_mkgmap_command(
            mkgmap_path, input_file, output_folder, 
            output_filename, family_id, map_name
        )
        
        # Запускаем компиляцию
        try:
            self.is_cancelled = False
            output_file = self._execute_mkgmap(cmd, output_folder, output_filename, progress_callback)
            return output_file
            
        except Exception as e:
            if self.is_cancelled:
                raise Exception("Компиляция отменена пользователем")
            else:
                raise Exception(f"Ошибка компиляции mkgmap: {str(e)}")
    
    def _build_mkgmap_command(self, mkgmap_path, input_file, output_folder, 
                             output_filename, family_id, map_name):
        """Построение команды mkgmap"""
        cmd = [
            'java', '-jar', mkgmap_path,
            '--gmapsupp',  # Создаём gmapsupp.img
            f'--family-id={family_id}',
            f'--description={map_name}',
            f'--family-name={map_name}',
            '--index',  # Включаем индексацию для поиска
            '--route',  # Поддержка маршрутизации
            '--generate-sea=extend-sea-sectors',  # Генерация морей
            '--draw-priority=100',  # Приоритет отрисовки
            '--add-pois-to-areas',  # Добавление POI к областям
            '--link-pois-to-ways',  # Связывание POI с дорогами
            '--remove-short-arcs',  # Удаление коротких дуг
            '--merge-lines',  # Объединение линий
            '--reduce-point-density=5.4',  # Упрощение геометрии
            '--reduce-point-density-polygon=8',  # Упрощение полигонов
            input_file
        ]
        
        return cmd
    
    def _execute_mkgmap(self, cmd, output_folder, output_filename, progress_callback):
        """Выполнение команды mkgmap"""
        if progress_callback:
            progress_callback("Запуск компиляции mkgmap...")
        
        # Запускаем процесс
        self.process = subprocess.Popen(
            cmd,
            cwd=output_folder,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            universal_newlines=True
        )
        
        # Читаем вывод
        output_lines = []
        
        while True:
            if self.is_cancelled:
                self.process.terminate()
                time.sleep(1)
                if self.process.poll() is None:
                    self.process.kill()
                raise Exception("Компиляция отменена")
            
            line = self.process.stdout.readline()
            
            if line:
                line = line.strip()
                output_lines.append(line)
                
                if progress_callback:
                    progress_callback(line)
                
                # Парсим прогресс
                self._parse_mkgmap_progress(line, progress_callback)
            
            # Проверяем завершение процесса
            if self.process.poll() is not None:
                break
        
        # Ждём завершения
        return_code = self.process.wait()
        
        if return_code != 0:
            error_output = "\n".join(output_lines[-10:])  # Последние 10 строк
            raise Exception(f"mkgmap завершился с ошибкой (код {return_code}):\n{error_output}")
        
        # Ищем созданный файл
        output_file = self._find_output_file(output_folder, output_filename)
        
        if not output_file:
            raise Exception("Не удалось найти созданный IMG файл")
        
        return output_file
    
    def _parse_mkgmap_progress(self, line, progress_callback):
        """Парсинг прогресса mkgmap"""
        if not progress_callback:
            return
        
        # Ключевые фразы для определения этапов
        progress_phrases = [
            ("Reading input file", "Чтение входного файла"),
            ("Processing", "Обработка"),
            ("Writing", "Запись"),
            ("Building", "Построение"),
            ("Generating", "Генерация"),
            ("Creating", "Создание"),
            ("Indexing", "Индексация"),
            ("Finishing", "Завершение")
        ]
        
        line_lower = line.lower()
        
        for english_phrase, russian_phrase in progress_phrases:
            if english_phrase.lower() in line_lower:
                progress_callback(f"{russian_phrase}...")
                break
    
    def _find_output_file(self, output_folder, output_filename):
        """Поиск созданного IMG файла"""
        # Возможные имена файлов
        possible_names = [
            f"{output_filename}.img",
            "gmapsupp.img",
            "map.img"
        ]
        
        for filename in possible_names:
            file_path = os.path.join(output_folder, filename)
            if os.path.exists(file_path):
                return file_path
        
        # Ищем любой IMG файл в папке
        try:
            for file in os.listdir(output_folder):
                if file.lower().endswith('.img'):
                    return os.path.join(output_folder, file)
        except OSError:
            pass
        
        return None
    
    def stop_compilation(self):
        """Остановка компиляции"""
        self.is_cancelled = True
        
        if self.process and self.process.poll() is None:
            try:
                self.process.terminate()
                
                # Ждём до 5 секунд
                for _ in range(50):
                    if self.process.poll() is not None:
                        break
                    time.sleep(0.1)
                
                # Если не завершился - принудительно убиваем
                if self.process.poll() is None:
                    self.process.kill()
                    
            except Exception:
                pass  # Игнорируем ошибки при остановке
    
    def get_java_version(self):
        """Получение версии Java"""
        try:
            result = subprocess.run(
                ['java', '-version'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            # Java выводит версию в stderr
            version_output = result.stderr
            
            if 'version' in version_output:
                return version_output.split('\n')[0]
            
        except Exception:
            pass
        
        return None
    
    def check_java_available(self):
        """Проверка доступности Java"""
        try:
            result = subprocess.run(
                ['java', '-version'],
                capture_output=True,
                timeout=5
            )
            return result.returncode == 0
            
        except Exception:
            return False
