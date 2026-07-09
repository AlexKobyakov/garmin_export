# -*- coding: utf-8 -*-
"""
Russian translations for Garmin Export Plugin
Русские переводы для плагина экспорта в Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""

translations = {
    # Main interface
    'window_title': 'Экспорт в Garmin IMG - Конвертер векторных данных',
    'no_vector_layers': 'В проекте нет векторных слоёв для экспорта.\n\n'
                        'Добавьте векторные слои в проект и повторите попытку.',

    # Tabs
    'tab_layers': 'Слои',
    'tab_export': 'Экспорт',
    'tab_tools': 'Инструменты',
    'tab_styles': 'Стили',
    'tab_typ': 'TYP',
    'tab_levels': 'Уровни',
    'tab_tuning': 'Тюнинг',

    # Layer selection
    'select_layers': 'Выбор слоёв для экспорта',
    'select_all_layers': 'Выбрать все слои',
    'deselect_all_layers': 'Снять выделение',
    'refresh': 'Обновить',
    'layers_list': 'Список слоёв проекта:',

    # Export settings
    'output_files': 'Выходные файлы',
    'output_folder': 'Выходная папка:',
    'output_file_name': 'Имя файла карты:',
    'browse': 'Обзор...',
    'map_settings': 'Настройки карты',
    'family_id': 'Family ID:',
    'map_id': 'Map ID:',
    'map_name': 'Название карты:',
    'map_description': 'Описание:',
    'transparent': 'Прозрачная карта',
    'routing': 'Поддержка маршрутизации',

    # Tools (mkgmap / splitter / java)
    'tools_mkgmap': 'Инструменты mkgmap',
    'add_mkgmap': 'Добавить mkgmap',
    'download_mkgmap': 'Скачать mkgmap',
    'add_splitter': 'Добавить splitter',
    'download_splitter': 'Скачать splitter',
    'detect_java': 'Найти автоматически',
    'select_mkgmap': 'Выберите файл mkgmap.jar',
    'select_splitter': 'Выберите файл splitter.jar',
    'select_java': 'Выберите исполняемый файл java',
    'jar_valid': 'файл корректен',
    'jar_invalid': 'Файл не является корректным mkgmap.jar',
    'java_not_found': 'Java не найдена. Установите Java (JRE 8+).',
    'downloading': 'Скачивание...',
    'download_in_progress': 'Скачивание уже выполняется.',
    'download_failed': 'Не удалось скачать файл',
    'download_complete': 'Скачивание завершено',

    # Style mapping
    'style_mapping': 'JSON-сопоставление стилей',
    'load_mapping': 'Загрузить',
    'save_mapping': 'Сохранить',
    'edit_mapping': 'Редактировать',
    'default_mapping': 'По умолчанию',
    'mapping_title': 'Редактор JSON-сопоставления стилей',
    'mapping_description': 'Настройте соответствие между слоями QGIS и типами объектов Garmin',
    'validate_json': 'Проверить JSON',
    'json_valid': 'JSON синтаксически корректен!',
    'select_mapping_file': 'Выберите файл JSON-сопоставления',
    'save_mapping_file': 'Сохранить файл JSON-сопоставления',

    # TYP styling
    'typ_styling': 'Стилизация карты (TYP)',
    'select_typ_file': 'Выберите файл TYP',

    # Levels
    'export_levels': 'Уровни отображения карты',
    'level_0': 'Уровень 0 (детальный)',
    'level_1': 'Уровень 1 (основной)',
    'level_2': 'Уровень 2 (средний)',
    'level_3': 'Уровень 3 (обзорный)',

    # Control buttons
    'compile_map': 'Скомпилировать карту',
    'compiling': 'Компиляция...',
    'cancel': 'Отмена',
    'clear_logs': 'Очистить логи',
    'save': 'Сохранить',
    'close': 'Закрыть',
    'details': 'Подробности',

    # Progress / results
    'progress': 'Прогресс',
    'logs': 'Логи',
    'results': 'Результаты',
    'layer': 'Слой',
    'status': 'Статус',
    'message': 'Сообщение',
    'geometry_type': 'Тип геометрии',
    'garmin_type': 'Тип Garmin',
    'label_field': 'Поле подписи',

    # Common
    'success': 'Успешно',
    'error': 'Ошибка',
    'warning': 'Предупреждение',
    'info': 'Информация',
    'confirmation': 'Подтверждение',
    'critical_error': 'Критическая ошибка',
    'select_output_folder': 'Выберите папку для сохранения IMG файла',

    # Errors
    'error_no_layers': 'Выберите хотя бы один слой для экспорта',
    'error_no_output_folder': 'Укажите выходную папку',
    'error_output_folder_missing': 'Выходная папка не существует',
    'error_no_mkgmap': 'Укажите путь к файлу mkgmap.jar или скачайте его '
                       'кнопкой «Скачать mkgmap»',
    'error_invalid_mkgmap': 'Указанный файл не является корректным mkgmap.jar',
    'error_java_not_found': 'Java не найдена в системе. Установите Java (JRE 8+) '
                            'и укажите путь на вкладке «Инструменты».',
    'error_typ_not_found': 'Указанный файл TYP не найден',
    'error_invalid_json': 'Неверный формат JSON-сопоставления',
    'error_mkgmap_execution': 'Ошибка выполнения mkgmap: {error}',
    'confirm_close': 'Компиляция в процессе. Остановить и закрыть?',

    # Author dialog
    'about_author': 'Об авторе',
    'header_support': 'Поддержка',
    'header_about_author': 'Об авторе',
    'version': 'Версия',
    'author': 'Автор',
    'contact': 'Контакт',
    'year': 'Год',
    'organization': 'Организация',
    'plugin_description': 'Профессиональный инструмент экспорта данных QGIS '
                          'в формат карт Garmin IMG через mkgmap',
    'multilingual_support': 'Стилизация из QGIS, генерация TYP, тонкая '
                            'настройка mkgmap, многоязычный интерфейс',

    # Donation dialog
    'donation_title': '☕ Поддержка разработки',
    'donation_window_title': '☕ Поддержите разработку плагина',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 Garmin Export Plugin</b></p>
            <p>этот плагин разрабатывается и поддерживается <b>бесплатно</b>!</p>
            <p>Ваша поддержка помогает обновлять и улучшать плагин.</p>
            <p style="color: #7f8c8d; font-size: 13px;">Каждый кофе имеет значение! ❤️</p>
        </div>''',
    'donation_kofi': '☕ Купить кофе на Ko-fi',
    'donation_tbank': '💳 Пожертвовать через Т Банк',
    'donation_github': '💖 Спонсировать на GitHub',
    'donation_maybe_later': '✅ Может быть позже',

    # Success messages
    'success_export_complete': 'Карта успешно скомпилирована! Файл сохранён:',
    'success_mapping_saved': 'Сопоставление сохранено успешно',
    'success_mapping_loaded': 'Сопоставление загружено успешно',

    # Tools tab (labels, placeholders, info)
    'mkgmap_path_label': 'Путь к mkgmap.jar:',
    'mkgmap_path_placeholder': 'Выберите или скачайте mkgmap.jar',
    'splitter_path_label': 'Путь к splitter.jar (необязательно):',
    'splitter_path_placeholder': 'splitter нужен для нарезки больших карт (необязательно)',
    'java_path_label': 'Путь к Java:',
    'java_path_placeholder': 'Пусто = java из PATH; кнопка справа найдёт автоматически',
    'tools_info': 'Правила QGIS запрещают включать mkgmap.jar в состав плагина. '
                  'Нажмите «Скачать mkgmap» — плагин получит последнюю версию с '
                  'mkgmap.org.uk (или с резервного Яндекс.Диска), либо укажите '
                  'свой файл кнопкой «Добавить mkgmap».',
    'support_tip': 'Поддержите разработку плагина!',
    'author_tip': 'Информация об авторе плагина',

    # Tuning tab - group titles
    'map_params_group': 'Параметры карты (mkgmap)',
    'generalization_group': 'Генерализация',
    'performance_group': 'Производительность (тюнинг)',
    'logging_group': 'Логирование и отладка',

    # Tuning tab - options
    'code_page_label': 'Кодовая страница подписей:',
    'draw_priority_label': 'Приоритет отрисовки (--draw-priority):',
    'draw_priority_tip': '25 - стандарт. Больше = карта рисуется поверх других. '
                         'Для прозрачных карт-надстроек ставьте больше 25.',
    'opt_index': 'Адресный индекс для поиска (--index)',
    'opt_add_pois': 'Создавать POI из полигонов (--add-pois-to-areas)',
    'opt_lower_case': 'Разрешить строчные буквы в подписях (--lower-case)',
    'opt_order_area': 'Мелкие полигоны поверх крупных (--order-by-decreasing-area)',
    'reduce_density_label': 'Упрощение линий, м (--reduce-point-density):',
    'reduce_density_polygon_label': 'Упрощение полигонов, м (--reduce-point-density-polygon):',
    'min_polygon_label': 'Мин. размер полигона (--min-size-polygon):',
    'min_polygon_tip': 'Полигоны меньше этого размера удаляются. 8-15 рекомендовано.',
    'java_heap_label': 'Память Java, ГБ (-Xmx):',
    'java_heap_tip': 'mkgmap требует ~500 МБ на поток. Для 8 ядер задайте 4 ГБ.',
    'max_jobs_label': 'Потоки (--max-jobs):',
    'max_jobs_tip': '0 = mkgmap определит по количеству ядер и памяти.',
    'opt_mkgmap_log': 'Вести файл журнала mkgmap.log в выходной папке',
    'opt_verbose': 'Подробный журнал (уровень INFO)',
    'opt_keep_temp': 'Сохранять промежуточные файлы (MP, TYP) в выходной папке',
    'extra_args_label': 'Доп. аргументы mkgmap:',
    'extra_args_placeholder': 'например: --precomp-sea=C:/sea.zip --generate-sea',
    'value_auto': 'авто',
    'value_auto_default': 'авто (2.6)',

    # Code pages
    'cp_1251': 'CP1251 (кириллица)',
    'cp_1252': 'CP1252 (Latin-1, Западная Европа)',
    'cp_1250': 'CP1250 (Центральная Европа)',
    'cp_1253': 'CP1253 (греческий)',
    'cp_1254': 'CP1254 (турецкий)',
    'cp_1257': 'CP1257 (балтийский)',
    'cp_65001': 'UTF-8 / Unicode (все языки)',
    'cp_1255': 'CP1255 (иврит)',
    'cp_1256': 'CP1256 (арабский)',
    'cp_1258': 'CP1258 (вьетнамский)',
    'cp_874': 'CP874 (тайский)',
    'cp_932': 'CP932 (японский, Shift-JIS)',
    'cp_936': 'CP936 (упрощённый китайский, GBK)',
    'cp_949': 'CP949 (корейский)',
    'cp_950': 'CP950 (традиционный китайский, Big5)',
    'cp_866': 'CP866 (кириллица, DOS)',
    'cp_850': 'CP850 (Западная Европа, DOS)',
    'cp_852': 'CP852 (Центральная Европа, DOS)',
    # TYP tab
    'typ_info': 'TYP-файл задаёт внешний вид объектов на устройстве Garmin: '
                'цвета полигонов, толщину линий, иконки точек. Плагин может '
                'сгенерировать TYP автоматически из текущей символики слоёв QGIS '
                '— карта на навигаторе будет выглядеть как в QGIS.',
    'typ_none': 'Стандартный стиль Garmin (без TYP)',
    'typ_generate': 'Сгенерировать TYP из стилей QGIS (рекомендуется)',
    'typ_file': 'Использовать готовый файл TYP / typ.txt:',
    'typ_file_placeholder': 'Путь к файлу .typ или .txt',

    # Layers tab
    'layers_info': 'Выберите слои проекта для экспорта в формат Garmin IMG',

    # Export tab (placeholders, tooltips)
    'output_folder_placeholder': 'Выберите папку для сохранения IMG файла',
    'map_description_placeholder': 'Карта создана плагином QGIS Garmin Export',
    'family_id_tip': 'Идентификатор семейства карт. Должен быть уникален среди '
                     'карт на устройстве.',
    'map_id_tip': '8-значный номер тайла карты. Должен быть уникален.',
    'transparent_tip': 'Прозрачная карта отображается поверх других карт '
                       '(например, поверх базовой карты).',
    'routing_tip': 'Записать данные NET/NOD (--route). Работает, если данные '
                   'содержат дорожную сеть.',

    # Styles tab
    'mapping_info': 'Настройте соответствие между слоями QGIS и типами объектов Garmin',
    'mapping_placeholder': 'JSON-сопоставление стилей будет загружено автоматически...',

    # Levels tab
    'levels_info': 'Уровни определяют, при каких масштабах объекты видны на '
                   'устройстве. Уровень 0 (разрешение 24) - самый детальный, '
                   'уровень 3 (разрешение 18) - обзорный. В сопоставлении стилей '
                   'параметр "level" задаёт, до какого уровня виден объект.',

    # Log widget
    'log_ready': 'Garmin Export Plugin загружен и готов к работе',
    'log_hint': 'Логи операций будут отображаться здесь...',
    'extracting': 'Распаковка...',
}
