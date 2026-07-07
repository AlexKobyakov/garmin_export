# -*- coding: utf-8 -*-
"""
Russian translations for Garmin Export Plugin
Русские переводы для плагина экспорта в Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

translations = {
    # Main interface translations
    'window_title': 'Экспорт в Garmin IMG - Конвертер векторных данных',
    'select_layers': 'Выбор слоёв для экспорта',
    'layer_mapping': 'Сопоставление стилей',
    'export_settings': 'Настройки экспорта',
    'mkgmap_settings': 'Настройки mkgmap',
    'select_all_layers': 'Выбрать все слои',
    'deselect_all_layers': 'Снять выделение',
    'layers_list': 'Список слоёв проекта:',
    'output_folder': 'Выходная папка:',
    'output_file_name': 'Имя файла карты:',
    'browse': 'Обзор...',
    'map_settings': 'Настройки карты',
    'family_id': 'Family ID:',
    'map_id': 'Map ID:',
    'map_name': 'Название карты:',
    'map_description': 'Описание карты:',
    'transparent': 'Прозрачная карта',
    'routing': 'Поддержка маршрутизации',
    'mkgmap_path': 'Путь к mkgmap.jar:',
    'style_mapping': 'JSON-сопоставление стилей:',
    'edit_mapping': 'Редактировать сопоставление',
    'load_mapping': 'Загрузить сопоставление',
    'save_mapping': 'Сохранить сопоставление',
    'compile_map': 'Скомпилировать карту',
    'cancel': 'Отмена',
    'progress': 'Прогресс:',
    'logs': 'Логи',
    'results': 'Результаты',
    'clear_logs': 'Очистить логи',
    'compiling': 'Компиляция...',
    'language': 'Язык:',
    'layer': 'Слой',
    'geometry_type': 'Тип геометрии',
    'garmin_type': 'Тип Garmin',
    'label_field': 'Поле подписи',
    'export_levels': 'Уровни экспорта',
    'level_0': 'Уровень 0 (детальный)',
    'level_1': 'Уровень 1 (основной)',
    'level_2': 'Уровень 2 (средний)',
    'level_3': 'Уровень 3 (обзорный)',
    'success': 'Успешно',
    'error': 'Ошибка',
    'warning': 'Предупреждение',
    'info': 'Информация',
    'select_output_folder': 'Выберите выходную папку',
    'select_mkgmap': 'Выберите файл mkgmap.jar',
    'select_mapping_file': 'Выберите файл JSON-сопоставления',
    'save_mapping_file': 'Сохранить файл JSON-сопоставления',
    'error_no_layers': 'Выберите хотя бы один слой для экспорта',
    'error_no_output_folder': 'Укажите выходную папку',
    'error_no_mkgmap': 'Укажите путь к файлу mkgmap.jar',
    'error_invalid_mkgmap': 'Неверный путь к mkgmap.jar',
    'error_java_not_found': 'Java не найдена в системе',
    'compilation_cancelled': 'Отмена компиляции...',
    'confirm_close': 'Компиляция в процессе. Остановить и закрыть?',
    'confirmation': 'Подтверждение',
    'critical_error': 'Критическая ошибка',
    'author_info': 'Автор: Кобяков Александр Викторович (Alex Kobyakov)\\nEmail: kobyakov@lesburo.ru\\nГод создания: 2025',
    'about_author': 'Об авторе',
    'settings': 'Настройки',
    'layer_selection': 'Выбор слоёв',
    'export_options': 'Параметры экспорта',
    
    # Style mapping translations
    'mapping_title': 'Редактор JSON-сопоставления стилей',
    'mapping_description': 'Настройте соответствие между слоями QGIS и типами объектов Garmin',
    'default_mapping': 'Сопоставление по умолчанию',
    'custom_mapping': 'Пользовательское сопоставление',
    'geometry_point': 'Точка',
    'geometry_line': 'Линия',
    'geometry_polygon': 'Полигон',
    'garmin_types_poi': 'POI (Точки интереса)',
    'garmin_types_roads': 'Дороги',
    'garmin_types_areas': 'Области',
    'garmin_types_other': 'Прочее',
    
    # Donation dialog translations
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
    'donation_support_development': '☕ Поддержите разработку плагина',
    'donation_plugin_info': 'этот плагин разрабатывается и поддерживается бесплатно!',
    'donation_help_improve': 'Ваша поддержка помогает обновлять и улучшать плагин.',
    'donation_every_coffee': 'Каждый кофе имеет значение! ❤️',
    
    # Header buttons translations
    'header_support': 'Поддержка',
    'header_about_author': 'Об авторе',
    
    # Author dialog translations
    'version': 'Версия',
    'author': 'Автор',
    'contact': 'Контакт',
    'year': 'Год',
    'organization': 'Организация',
    'plugin_description': 'Профессиональный инструмент экспорта ГИС данных в формат Garmin',
    'multilingual_support': 'Поддерживает множество языков и форматов',
    
    # Processing messages
    'processing_start': 'Начало обработки слоёв...',
    'processing_layer': 'Обработка слоя: {layer_name}',
    'processing_complete': 'Обработка завершена успешно!',
    'mp_generation_start': 'Генерация MP файла...',
    'mp_generation_complete': 'MP файл создан: {file_path}',
    'mkgmap_compilation_start': 'Запуск компиляции mkgmap...',
    'mkgmap_compilation_complete': 'Компиляция завершена: {file_path}',
    'export_statistics': 'Статистика экспорта: {count} объектов обработано',
    
    # File operations
    'creating_folder': 'Создание папки: {folder_path}',
    'writing_file': 'Запись файла: {file_path}',
    'reading_mapping': 'Чтение сопоставления из: {file_path}',
    'saving_mapping': 'Сохранение сопоставления в: {file_path}',
    
    # Error messages
    'error_layer_processing': 'Ошибка обработки слоя {layer_name}: {error}',
    'error_mp_generation': 'Ошибка генерации MP файла: {error}',
    'error_mkgmap_execution': 'Ошибка выполнения mkgmap: {error}',
    'error_file_not_found': 'Файл не найден: {file_path}',
    'error_permission_denied': 'Отказано в доступе: {file_path}',
    'error_invalid_json': 'Неверный формат JSON в файле сопоставления',
    'error_unsupported_geometry': 'Неподдерживаемый тип геометрии: {geometry_type}',
    
    # Success messages
    'success_export_complete': 'Экспорт успешно завершён!',
    'success_mapping_saved': 'Сопоставление сохранено успешно',
    'success_mapping_loaded': 'Сопоставление загружено успешно',
    'success_layer_processed': 'Слой {layer_name} обработан успешно',
}
