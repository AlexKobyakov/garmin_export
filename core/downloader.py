# -*- coding: utf-8 -*-
"""
Downloader logic for Garmin Export Plugin
Логика скачивания mkgmap/splitter (чистая часть, без Qt)

Порядок получения инструмента:
  1. "Переменная" ссылка: страница загрузок mkgmap.org.uk разбирается
     регулярным выражением, определяется последняя версия
     (mkgmap-rXXXX.jar / splitter-rXXX.jar);
  2. Постоянная прямая ссылка на известную версию с mkgmap.org.uk;
  3. Постоянная ссылка на Яндекс.Диске (через публичный API получается
     прямой href для скачивания).

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""

import json
import os
import re
import urllib.parse
import urllib.request


USER_AGENT = 'QGIS-GarminExportPlugin/1.1 (+https://github.com/AlexKobyakov/garmin_export)'

TOOLS = {
    'mkgmap': {
        'page_url': 'https://www.mkgmap.org.uk/download/mkgmap.html',
        'jar_pattern': r'mkgmap-r(\d+)',
        'jar_url_template': 'https://www.mkgmap.org.uk/download/mkgmap-r{0}.jar',
        'fallback_jar_url': 'https://www.mkgmap.org.uk/download/mkgmap-r4924.jar',
        'fallback_filename': 'mkgmap-r4924.jar',
        'yandex_public_url': 'https://disk.yandex.ru/d/_tTYvNky5xm6bQ',
        'jar_class_prefix': 'uk/me/parabola/mkgmap',
    },
    'splitter': {
        'page_url': 'https://www.mkgmap.org.uk/download/splitter.html',
        'jar_pattern': r'splitter-r(\d+)',
        'jar_url_template': 'https://www.mkgmap.org.uk/download/splitter-r{0}.jar',
        'fallback_jar_url': 'https://www.mkgmap.org.uk/download/splitter-r654.jar',
        'fallback_filename': 'splitter-r654.jar',
        'yandex_public_url': 'https://disk.yandex.ru/d/6NgiciVPdvpZUg',
        'jar_class_prefix': 'uk/me/parabola/splitter',
    },
}

YANDEX_API_TEMPLATE = (
    'https://cloud-api.yandex.net/v1/disk/public/resources/download'
    '?public_key={0}'
)


def _open_url(url, timeout=30):
    """Открытие URL с корректным User-Agent (прокси берётся из системы)"""
    request = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    return urllib.request.urlopen(request, timeout=timeout)


def parse_latest_version(html, tool):
    """Определение номера последней версии из HTML страницы загрузок.

    Returns:
        int (номер ревизии) или None
    """
    pattern = TOOLS[tool]['jar_pattern']
    versions = [int(m) for m in re.findall(pattern, html or '')]
    return max(versions) if versions else None


def latest_jar_url(html, tool):
    """URL jar-файла последней версии по содержимому страницы загрузок"""
    version = parse_latest_version(html, tool)
    if version is None:
        return None
    return TOOLS[tool]['jar_url_template'].format(version)


def filename_from_url(url, default_name):
    """Имя файла из URL (учитывает параметр filename= у Яндекс.Диска)"""
    try:
        parsed = urllib.parse.urlparse(url)
        query = urllib.parse.parse_qs(parsed.query)
        if 'filename' in query and query['filename']:
            return os.path.basename(query['filename'][0])
        name = os.path.basename(parsed.path)
        if name.lower().endswith('.jar'):
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
    """Список кандидатов на скачивание в порядке приоритета.

    Каждый кандидат - функция без аргументов, возвращающая
    (url, имя_файла). Исключения кандидата означают переход к следующему.
    """
    config = TOOLS[tool]

    def from_download_page():
        with opener(config['page_url']) as response:
            html = response.read().decode('utf-8', errors='replace')
        url = latest_jar_url(html, tool)
        if not url:
            raise ValueError('Не удалось определить версию на странице загрузок')
        return url, filename_from_url(url, config['fallback_filename'])

    def from_fallback():
        return (config['fallback_jar_url'],
                filename_from_url(config['fallback_jar_url'],
                                  config['fallback_filename']))

    def from_yandex():
        href = resolve_yandex_direct_url(config['yandex_public_url'], opener)
        if not href:
            raise ValueError('Яндекс.Диск не вернул ссылку для скачивания')
        return href, filename_from_url(href, config['fallback_filename'])

    return [from_download_page, from_fallback, from_yandex]


def download_tool(tool, dest_dir, progress_callback=None,
                  cancelled_callback=None, opener=_open_url):
    """Скачивание инструмента с перебором источников.

    Args:
        tool: 'mkgmap' или 'splitter'
        dest_dir: каталог для сохранения jar
        progress_callback: функция (получено_байт, всего_байт, статус) -> None
        cancelled_callback: функция () -> bool; True = отменить
        opener: функция открытия URL (для тестов)
    Returns:
        путь к скачанному jar файлу
    Raises:
        Exception при неудаче всех источников или отмене
    """
    from .mkgmap_compiler import validate_jar

    os.makedirs(dest_dir, exist_ok=True)
    config = TOOLS[tool]

    errors = []
    for candidate in build_download_candidates(tool, opener):
        try:
            url, filename = candidate()
            if progress_callback:
                progress_callback(0, 0, 'Источник: {0}'.format(
                    urllib.parse.urlparse(url).netloc))

            dest_path = os.path.join(dest_dir, filename)
            temp_path = dest_path + '.part'

            _download_file(url, temp_path, progress_callback,
                           cancelled_callback, opener)

            # temp_path заканчивается на .part, поэтому проверку расширения
            # отключаем — валидируем только содержимое архива
            if not validate_jar(temp_path, config['jar_class_prefix'],
                                 check_extension=False):
                os.remove(temp_path)
                raise ValueError(
                    'Скачанный файл не является корректным {0}.jar'.format(tool))

            if os.path.exists(dest_path):
                os.remove(dest_path)
            os.replace(temp_path, dest_path)
            return dest_path

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
    with opener(url, timeout=60) as response:
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
