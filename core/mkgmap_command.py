# -*- coding: utf-8 -*-
"""
mkgmap Command Builder for Garmin Export Plugin
Построитель командной строки mkgmap (чистая логика, без QGIS)

Формирует команду в соответствии с документацией mkgmap:
  java [java-options] -jar mkgmap.jar [mkgmap-options] input-files...

Ключевые правила из документации:
  - Java-опции (-Xmx, -Dlog.config) указываются ДО -jar;
  - опции mkgmap действуют на последующие входные файлы,
    поэтому все опции ставятся перед входными файлами;
  - TYP файл (typ.txt) не должен быть первым входным файлом
    при автоматическом определении --max-jobs;
  - --remove-short-arcs устарела и игнорируется (не используется);
  - --generate-sea нужна только при наличии береговой линии.

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

import shlex


# Значения по умолчанию согласуются с документацией mkgmap
DEFAULT_OPTIONS = {
    'family_id': 1234,
    'product_id': 1,
    'family_name': 'QGIS Map',
    'series_name': '',
    'description': '',
    'mapname': '',            # 8-значный номер тайла (пусто = из MP файла)
    'code_page': '1251',
    'gmapsupp': True,
    'index': False,           # адресный индекс: имеет смысл при поиске
    'route': False,           # NET+NOD для маршрутизации
    'net': False,             # только NET (адресный поиск без роутинга)
    'transparent': False,
    'draw_priority': 25,      # 25 - значение по умолчанию mkgmap
    'lower_case': False,
    'keep_going': True,
    'add_pois_to_areas': False,
    'poi_address': True,
    'merge_lines': True,
    'reduce_point_density': None,          # None = значение mkgmap (2.6)
    'reduce_point_density_polygon': None,
    'min_size_polygon': None,
    'order_by_decreasing_area': False,
    'max_jobs': 0,            # 0 = авто
    'java_xmx': '',           # например '2g'
    'log_config': '',         # путь к logging.properties (-Dlog.config=)
    'output_dir': '',
    'extra_args': '',         # дополнительные аргументы опытного пользователя
}


def normalize_options(options):
    """Дополняет словарь опций значениями по умолчанию"""
    result = dict(DEFAULT_OPTIONS)
    if options:
        for key, value in options.items():
            result[key] = value
    return result


def build_java_options(options):
    """Java-опции: указываются до -jar"""
    java_opts = []
    xmx = str(options.get('java_xmx') or '').strip()
    if xmx:
        java_opts.append('-Xmx{0}'.format(xmx))
    log_config = str(options.get('log_config') or '').strip()
    if log_config:
        java_opts.append('-Dlog.config={0}'.format(log_config))
    return java_opts


def build_mkgmap_options(options):
    """Опции mkgmap: указываются после -jar и до входных файлов"""
    args = []

    output_dir = str(options.get('output_dir') or '').strip()
    if output_dir:
        args.append('--output-dir={0}'.format(output_dir))

    # Идентификация продукта
    args.append('--family-id={0}'.format(int(options['family_id'])))
    args.append('--product-id={0}'.format(int(options.get('product_id', 1))))

    family_name = str(options.get('family_name') or '').strip()
    if family_name:
        args.append('--family-name={0}'.format(family_name))

    series_name = str(options.get('series_name') or '').strip()
    if series_name:
        args.append('--series-name={0}'.format(series_name))

    description = str(options.get('description') or '').strip()
    if description:
        args.append('--description={0}'.format(description))

    mapname = str(options.get('mapname') or '').strip()
    if mapname:
        args.append('--mapname={0}'.format(mapname))

    # Кодировка подписей
    code_page = str(options.get('code_page') or '').strip()
    if code_page == '65001':
        args.append('--unicode')
    elif code_page:
        args.append('--code-page={0}'.format(code_page))

    if options.get('lower_case'):
        args.append('--lower-case')

    # Маршрутизация и индексы
    if options.get('route'):
        args.append('--route')
    elif options.get('net'):
        args.append('--net')

    if options.get('index'):
        args.append('--index')

    # Отображение
    if options.get('transparent'):
        args.append('--transparent')

    draw_priority = options.get('draw_priority')
    if draw_priority is not None and int(draw_priority) != 25:
        args.append('--draw-priority={0}'.format(int(draw_priority)))

    if options.get('order_by_decreasing_area'):
        args.append('--order-by-decreasing-area')

    # POI
    if options.get('add_pois_to_areas'):
        args.append('--add-pois-to-areas')
    if not options.get('poi_address', True):
        args.append('--no-poi-address')

    # Генерализация
    if not options.get('merge_lines', True):
        args.append('--no-merge-lines')

    rpd = options.get('reduce_point_density')
    if rpd:
        args.append('--reduce-point-density={0}'.format(rpd))

    rpdp = options.get('reduce_point_density_polygon')
    if rpdp:
        args.append('--reduce-point-density-polygon={0}'.format(rpdp))

    msp = options.get('min_size_polygon')
    if msp is not None and str(msp) != '' and int(msp) != 8:
        args.append('--min-size-polygon={0}'.format(int(msp)))

    # Надёжность и производительность
    if options.get('keep_going', True):
        args.append('--keep-going')

    max_jobs = int(options.get('max_jobs') or 0)
    if max_jobs > 0:
        args.append('--max-jobs={0}'.format(max_jobs))

    # Выходной формат
    if options.get('gmapsupp', True):
        args.append('--gmapsupp')

    # Дополнительные аргументы опытного пользователя
    extra = str(options.get('extra_args') or '').strip()
    if extra:
        args.extend(shlex.split(extra))

    return args


def build_command(java_path, jar_path, options, input_files):
    """Полная команда запуска mkgmap.

    Args:
        java_path: путь к java (или просто 'java')
        jar_path: путь к mkgmap.jar
        options: словарь опций (см. DEFAULT_OPTIONS)
        input_files: список входных файлов; MP файл должен быть первым,
            TYP файл (если есть) - последним
    Returns:
        список аргументов для subprocess
    """
    opts = normalize_options(options)

    cmd = [java_path or 'java']
    cmd.extend(build_java_options(opts))
    cmd.extend(['-jar', jar_path])
    cmd.extend(build_mkgmap_options(opts))
    cmd.extend(input_files)

    return cmd


def build_logging_config(log_file_path, verbose=False):
    """Содержимое конфигурационного файла логирования mkgmap.

    Формат соответствует разделу Logging документации mkgmap
    (java.util.logging). Файл передаётся через -Dlog.config=<файл>.

    Args:
        log_file_path: путь к файлу журнала mkgmap (mkgmap.log)
        verbose: True = уровень INFO для ключевых пакетов, иначе WARNING
    """
    level = 'INFO' if verbose else 'WARNING'
    # java.util.logging требует прямые слэши или экранированные обратные
    log_path = log_file_path.replace('\\', '/')

    lines = [
        '# Generated by Garmin Export Plugin for QGIS',
        '.level=SEVERE',
        'handlers: java.util.logging.FileHandler java.util.logging.ConsoleHandler',
        'uk.me.parabola.imgfmt.level={0}'.format(level),
        'uk.me.parabola.mkgmap.build.level={0}'.format(level),
        'uk.me.parabola.mkgmap.main.level={0}'.format(level),
        'uk.me.parabola.mkgmap.general.level={0}'.format(level),
        'uk.me.parabola.mkgmap.reader.level={0}'.format(level),
        'java.util.logging.ConsoleHandler.level=WARNING',
        'java.util.logging.ConsoleHandler.formatter=uk.me.parabola.log.UsefulFormatter',
        'java.util.logging.FileHandler.level={0}'.format(level),
        'java.util.logging.FileHandler.encoding=UTF-8',
        'java.util.logging.FileHandler.formatter=uk.me.parabola.log.UsefulFormatter',
        'java.util.logging.FileHandler.limit=20000000',
        'java.util.logging.FileHandler.count=2',
        'java.util.logging.FileHandler.pattern={0}'.format(log_path),
        'java.util.logging.FileHandler.append=false',
        '',
    ]
    return '\n'.join(lines)
