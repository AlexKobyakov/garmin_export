# -*- coding: utf-8 -*-
"""
Downloader logic for Garmin Export Plugin
Логика скачивания mkgmap/splitter (чистая часть, без Qt)

Скачиваются ПОЛНЫЕ zip-архивы дистрибутивов, а не одиночные jar, потому что
mkgmap.jar/splitter.jar зависят от библиотек в подпапке lib/ (osmpbf, protobuf,
fastutil и др.). Манифест jar ссылается на них через Class-Path=lib/..., поэтому
достаточно распаковать архив с сохранением структуры и указать путь на
извлечённый mkgmap.jar (рядом окажется папка lib/).

Порядок получения инструмента:
  1. "Переменная" ссылка: страница загрузок mkgmap.org.uk разбирается
     регулярным выражением, определяется последняя версия -> zip-архив;
  2. Постоянная прямая ссылка на известный zip с mkgmap.org.uk;
  3. Постоянная ссылка на Яндекс.Диске (через публичный API получается
     прямой href для скачивания zip).

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""

import io
import json
import os
import re
import urllib.parse
import urllib.request
import zipfile


USER_AGENT = 'QGIS-GarminExportPlugin/1.1 (+https://github.com/AlexKobyakov/garmin_export)'

# Сигнальная строка статуса для фазы распаковки (переводится в UI-обёртке)
STATUS_EXTRACT = 'extract'

TOOLS = {
    'mkgmap': {
        'page_url': 'https://www.mkgmap.org.uk/download/mkgmap.html',
        'version_pattern': r'mkgmap-r(\d+)',
        'archive_url_template': 'https://www.mkgmap.org.uk/download/mkgmap-r{0}.zip',
        'fallback_archive_url': 'https://www.mkgmap.org.uk/download/mkgmap-r4924.zip',
        'fallback_filename': 'mkgmap-r4924.zip',
        'yandex_public_url': 'https://disk.yandex.ru/d/H39zRcOscXvDiw',
        'jar_class_prefix': 'uk/me/parabola/mkgmap',
        'main_jar_name': 'mkgmap.jar',
    },
    'splitter': {
        'page_url': 'https://www.mkgmap.org.uk/download/splitter.html',
        'version_pattern': r'splitter-r(\d+)',
        'archive_url_template': 'https://www.mkgmap.org.uk/download/splitter-r{0}.zip',
        'fallback_archive_url': 'https://www.mkgmap.org.uk/download/splitter-r654.zip',
        'fallback_filename': 'splitter-r654.zip',
        'yandex_public_url': 'https://disk.yandex.ru/d/h5kqHSN7CqYzLw',
        'jar_class_prefix': 'uk/me/parabola/splitter',
        'main_jar_name': 'splitter.jar',
    },
}

YANDEX_API_TEMPLATE = (
    'https://cloud-api.yandex.net/v1/disk/public/resources/download'
    '?public_key={0}'
)


# Разрешённые схемы URL. Открытие file:/ftp:/data: и прочих схем недопустимо
# (безопасность: CWE-22). Скачиваются только ресурсы по http/https.
ALLOWED_SCHEMES = ('http', 'https')


def _build_web_opener():
    """OpenerDirector только с обработчиками http/https.

    Намеренно НЕ регистрируем FileHandler/FTPHandler/DataHandler, поэтому
    схемы file:, ftp:, data: не могут быть открыты даже при редиректах.
    Системный прокси сохраняется через ProxyHandler.
    """
    opener = urllib.request.OpenerDirector()
    for handler in (
        urllib.request.ProxyHandler(),
        urllib.request.HTTPHandler(),
        urllib.request.HTTPSHandler(),
        urllib.request.HTTPDefaultErrorHandler(),
        urllib.request.HTTPRedirectHandler(),
        urllib.request.HTTPErrorProcessor(),
    ):
        opener.add_handler(handler)
    return opener


_WEB_OPENER = _build_web_opener()


def _open_url(url, timeout=30):
    """Открытие URL только по http/https (прокси берётся из системы).

    Схема проверяется явно (защита от file:/ и нестандартных схем), а
    используемый opener не содержит обработчиков не-web схем.
    """
    scheme = urllib.parse.urlparse(url).scheme.lower()
    if scheme not in ALLOWED_SCHEMES:
        raise ValueError('Недопустимая схема URL: {0}'.format(scheme or '(пусто)'))
    request = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    return _WEB_OPENER.open(request, timeout=timeout)


def parse_latest_version(html, tool):
    """Определение номера последней версии из HTML страницы загрузок.

    Returns:
        int (номер ревизии) или None
    """
    pattern = TOOLS[tool]['version_pattern']
    versions = [int(m) for m in re.findall(pattern, html or '')]
    return max(versions) if versions else None


def latest_archive_url(html, tool):
    """URL zip-архива последней версии по содержимому страницы загрузок"""
    version = parse_latest_version(html, tool)
    if version is None:
        return None
    return TOOLS[tool]['archive_url_template'].format(version)


def filename_from_url(url, default_name):
    """Имя файла из URL (учитывает параметр filename= у Яндекс.Диска)"""
    try:
        parsed = urllib.parse.urlparse(url)
        query = urllib.parse.parse_qs(parsed.query)
        if 'filename' in query and query['filename']:
            return os.path.basename(query['filename'][0])
        name = os.path.basename(parsed.path)
        if name.lower().endswith(('.zip', '.jar')):
            return name
    except ValueError:
        pass
    return default_name


def resolve_yandex_direct_url(public_url, opener=_open_url):
    """Прямой href для скачивания по публичной ссылке Яндекс.Диска"""
    api_url = YANDEX_API_TEMPLATE.format(urllib.parse.quote(public_url, safe=''))
    with opener(api_url) as response:
        payload = json.loads(response.read().decode('utf-8'))
    return payload.get('href')


def build_download_candidates(tool, opener=_open_url):
    """Список кандидатов на скачивание zip-архива в порядке приоритета.

    Каждый кандидат - функция без аргументов, возвращающая
    (url, имя_файла). Исключения кандидата означают переход к следующему.
    """
    config = TOOLS[tool]

    def from_download_page():
        with opener(config['page_url']) as response:
            html = response.read().decode('utf-8', errors='replace')
        url = latest_archive_url(html, tool)
        if not url:
            raise ValueError('Не удалось определить версию на странице загрузок')
        return url, filename_from_url(url, config['fallback_filename'])

    def from_fallback():
        return (config['fallback_archive_url'],
                filename_from_url(config['fallback_archive_url'],
                                  config['fallback_filename']))

    def from_yandex():
        href = resolve_yandex_direct_url(config['yandex_public_url'], opener)
        if not href:
            raise ValueError('Яндекс.Диск не вернул ссылку для скачивания')
        return href, filename_from_url(href, config['fallback_filename'])

    return [from_download_page, from_fallback, from_yandex]


def find_main_jar_member(archive_names, main_jar_name):
    """Имя элемента архива, соответствующего главному jar (не из lib/).

    Возвращает имя элемента (например 'mkgmap-r4924/mkgmap.jar') или None.
    """
    candidates = []
    for name in archive_names:
        base = name.rsplit('/', 1)[-1]
        if base != main_jar_name:
            continue
        parent = name.rsplit('/', 2)[-2] if '/' in name.strip('/') else ''
        if parent == 'lib':          # jar из папки зависимостей - не главный
            continue
        candidates.append(name)
    if not candidates:
        return None
    # Предпочитаем наименее вложенный путь
    candidates.sort(key=lambda n: n.count('/'))
    return candidates[0]


def validate_archive(archive_path, main_jar_name, class_prefix):
    """Проверка, что zip содержит корректный главный jar с нужными классами"""
    if not archive_path or not os.path.isfile(archive_path):
        return False
    try:
        with zipfile.ZipFile(archive_path) as zf:
            member = find_main_jar_member(zf.namelist(), main_jar_name)
            if not member:
                return False
            jar_bytes = zf.read(member)
        with zipfile.ZipFile(io.BytesIO(jar_bytes)) as jar:
            for entry in jar.namelist():
                if entry.startswith(class_prefix):
                    return True
    except (zipfile.BadZipFile, OSError, KeyError):
        return False
    return False


def _is_within(base_dir, target_path):
    """Защита от zip-slip: target_path должен быть внутри base_dir"""
    base = os.path.abspath(base_dir)
    target = os.path.abspath(target_path)
    return target == base or target.startswith(base + os.sep)


def extract_archive(archive_path, dest_dir, main_jar_name):
    """Безопасная распаковка zip и поиск главного jar.

    Returns:
        абсолютный путь к извлечённому главному jar
    Raises:
        ValueError при небезопасных путях или отсутствии главного jar
    """
    os.makedirs(dest_dir, exist_ok=True)
    with zipfile.ZipFile(archive_path) as zf:
        names = zf.namelist()
        member = find_main_jar_member(names, main_jar_name)
        if not member:
            raise ValueError(
                'В архиве не найден {0}'.format(main_jar_name))
        # Защита от path traversal
        for name in names:
            out_path = os.path.join(dest_dir, name)
            if not _is_within(dest_dir, out_path):
                raise ValueError('Небезопасный путь в архиве: {0}'.format(name))
        zf.extractall(dest_dir)

    jar_path = os.path.join(dest_dir, member.replace('/', os.sep))
    if not os.path.isfile(jar_path):
        raise ValueError('Извлечённый {0} не найден'.format(main_jar_name))
    return jar_path


def download_tool(tool, dest_dir, progress_callback=None,
                  cancelled_callback=None, opener=_open_url):
    """Скачивание и установка инструмента (zip-архив + распаковка).

    Args:
        tool: 'mkgmap' или 'splitter'
        dest_dir: каталог для распаковки дистрибутива
        progress_callback: функция (получено_байт, всего_байт, статус) -> None
        cancelled_callback: функция () -> bool; True = отменить
        opener: функция открытия URL (для тестов)
    Returns:
        путь к извлечённому главному jar (рядом лежит папка lib/)
    Raises:
        Exception при неудаче всех источников или отмене
    """
    os.makedirs(dest_dir, exist_ok=True)
    config = TOOLS[tool]

    errors = []
    for candidate in build_download_candidates(tool, opener):
        try:
            url, filename = candidate()
            if progress_callback:
                progress_callback(0, 0, urllib.parse.urlparse(url).netloc)

            archive_path = os.path.join(dest_dir, filename)
            temp_path = archive_path + '.part'

            _download_file(url, temp_path, progress_callback,
                           cancelled_callback, opener)

            # Проверяем содержимое архива (главный jar с нужными классами)
            if not validate_archive(temp_path, config['main_jar_name'],
                                    config['jar_class_prefix']):
                os.remove(temp_path)
                raise ValueError(
                    'Скачанный архив не содержит корректный {0}'.format(
                        config['main_jar_name']))

            if os.path.exists(archive_path):
                os.remove(archive_path)
            os.replace(temp_path, archive_path)

            # Распаковка со всеми зависимостями (lib/)
            if progress_callback:
                progress_callback(0, 0, STATUS_EXTRACT)
            jar_path = extract_archive(archive_path, dest_dir,
                                       config['main_jar_name'])
            return jar_path

        except InterruptedError:
            raise Exception('Скачивание отменено пользователем')
        except Exception as e:
            errors.append(str(e))
            continue

    raise Exception(
        'Не удалось скачать {0} ни из одного источника:\n{1}'.format(
            tool, '\n'.join('- ' + err for err in errors)))


def _download_file(url, dest_path, progress_callback, cancelled_callback,
                   opener):
    """Скачивание одного файла с прогрессом и возможностью отмены"""
    with opener(url, timeout=120) as response:
        total = 0
        try:
            total = int(response.headers.get('Content-Length') or 0)
        except (TypeError, ValueError, AttributeError):
            total = 0

        received = 0
        try:
            with open(dest_path, 'wb') as out:
                while True:
                    if cancelled_callback and cancelled_callback():
                        raise InterruptedError()
                    chunk = response.read(65536)
                    if not chunk:
                        break
                    out.write(chunk)
                    received += len(chunk)
                    if progress_callback:
                        progress_callback(received, total, '')
        except InterruptedError:
            try:
                os.remove(dest_path)
            except OSError:
                pass
            raise
