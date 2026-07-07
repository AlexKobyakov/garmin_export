# -*- coding: utf-8 -*-
"""
Settings Manager for Garmin Export Plugin
Сохранение настроек плагина между сеансами (QSettings)

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

from qgis.PyQt.QtCore import QSettings

GROUP = 'garmin_export'

# Ключ: значение по умолчанию
DEFAULTS = {
    'mkgmap_path': '',
    'splitter_path': '',
    'java_path': '',
    'output_folder': '',
    'output_filename': 'map',
    'family_id': 1234,
    'map_id': 12340001,
    'map_name': 'QGIS Map',
    'map_description': '',
    'code_page': '1251',
    'transparent': False,
    'routing': False,
    'index': False,
    'add_pois_to_areas': False,
    'draw_priority': 25,
    'lower_case': False,
    'order_by_decreasing_area': False,
    'reduce_point_density': '',
    'reduce_point_density_polygon': '',
    'min_size_polygon': 8,
    'java_xmx_gb': 0,
    'max_jobs': 0,
    'mkgmap_logging': False,
    'mkgmap_verbose': False,
    'keep_temp_files': False,
    'extra_args': '',
    'typ_mode': 'none',      # none | generate | file
    'typ_file_path': '',
}

_BOOL_KEYS = {
    'transparent', 'routing', 'index', 'add_pois_to_areas', 'lower_case',
    'order_by_decreasing_area', 'mkgmap_logging', 'mkgmap_verbose',
    'keep_temp_files',
}

_INT_KEYS = {
    'family_id', 'map_id', 'draw_priority', 'min_size_polygon',
    'java_xmx_gb', 'max_jobs',
}


class SettingsManager:
    """Чтение и запись настроек плагина"""

    def __init__(self):
        self._settings = QSettings()

    def _key(self, name):
        return '{0}/{1}'.format(GROUP, name)

    def get(self, name):
        """Значение настройки с приведением типа"""
        default = DEFAULTS.get(name, '')
        value = self._settings.value(self._key(name), default)

        if name in _BOOL_KEYS:
            if isinstance(value, bool):
                return value
            return str(value).lower() in ('true', '1', 'yes')

        if name in _INT_KEYS:
            try:
                return int(value)
            except (TypeError, ValueError):
                return int(default)

        return '' if value is None else str(value)

    def set(self, name, value):
        """Сохранение настройки"""
        self._settings.setValue(self._key(name), value)

    def get_all(self):
        """Все настройки одним словарём"""
        return {name: self.get(name) for name in DEFAULTS}

    def set_many(self, values):
        """Сохранение набора настроек"""
        for name, value in values.items():
            if name in DEFAULTS:
                self.set(name, value)
