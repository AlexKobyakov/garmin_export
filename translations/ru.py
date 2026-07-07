# -*- coding: utf-8 -*-
"""
Russian translations for Garmin Export Plugin
Русские переводы для плагина экспорта в Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
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
}
