# -*- coding: utf-8 -*-
"""
Style Mapper for Garmin Export Plugin
Картограф стилей для плагина экспорта в Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""

import json


class StyleMapper:
    """Класс для сопоставления стилей QGIS с типами Garmin"""

    def __init__(self):
        self.mapping_data = {}
        self.default_mapping = self._get_default_mapping()

    def load_mapping(self, mapping_data):
        """Загрузка данных сопоставления"""
        if isinstance(mapping_data, dict):
            self.mapping_data = mapping_data
        else:
            raise ValueError("Неверный формат данных сопоставления")

    def get_layer_mapping(self, layer_name, geometry_type):
        """Получение сопоставления для слоя"""
        # Сначала ищем точное совпадение по имени
        layers_mapping = self.mapping_data.get('layers', {})

        # Точное совпадение имени
        if layer_name in layers_mapping:
            mapping = layers_mapping[layer_name]
            if self._validate_mapping(mapping, geometry_type):
                return mapping

        # Поиск по частичному совпадению имени (нижний регистр)
        layer_name_lower = layer_name.lower()
        for key, mapping in layers_mapping.items():
            if key.lower() in layer_name_lower or layer_name_lower in key.lower():
                if self._validate_mapping(mapping, geometry_type):
                    return mapping

        # Поиск по типу геометрии
        geometry_mapping = self._find_by_geometry_type(geometry_type)
        if geometry_mapping:
            return geometry_mapping

        # Возвращаем сопоставление по умолчанию
        return self._get_default_for_geometry(geometry_type)

    def _validate_mapping(self, mapping, geometry_type):
        """Проверка корректности сопоставления"""
        if not isinstance(mapping, dict):
            return False

        # Проверяем соответствие типа геометрии
        mapping_geometry = mapping.get('geometry', '')

        geometry_aliases = {
            'Point': ['Point', 'POI', 'point'],
            'LineString': ['LineString', 'Line', 'Polyline', 'line'],
            'Polygon': ['Polygon', 'Area', 'polygon', 'area']
        }

        valid_geometries = geometry_aliases.get(geometry_type, [])

        return mapping_geometry in valid_geometries

    def _find_by_geometry_type(self, geometry_type):
        """Поиск сопоставления по типу геометрии"""
        layers_mapping = self.mapping_data.get('layers', {})

        for key, mapping in layers_mapping.items():
            if self._validate_mapping(mapping, geometry_type):
                return mapping

        return None

    def _get_default_for_geometry(self, geometry_type):
        """Получение сопоставления по умолчанию для типа геометрии"""
        defaults = {
            'Point': {
                'geometry': 'Point',
                'type': '0x2f00',  # Generic POI
                'label_field': 'name',
                'level': 1
            },
            'LineString': {
                'geometry': 'LineString',
                'type': '0x06',  # Major road
                'label_field': 'name',
                'level': 1
            },
            'Polygon': {
                'geometry': 'Polygon',
                'type': '0x16',  # Forest
                'label_field': 'name',
                'level': 2
            }
        }

        return defaults.get(geometry_type, defaults['Point'])

    def _get_default_mapping(self):
        """Получение сопоставления по умолчанию"""
        return {
            "layers": {
                "roads": {
                    "geometry": "LineString",
                    "type": "0x06",
                    "label_field": "name",
                    "style": {
                        "color": "#FF0000",
                        "width": 2
                    },
                    "level": 1
                },
                "highways": {
                    "geometry": "LineString",
                    "type": "0x01",
                    "label_field": "name",
                    "style": {
                        "color": "#FF8000",
                        "width": 3
                    },
                    "level": 0
                },
                "rivers": {
                    "geometry": "LineString",
                    "type": "0x1F",
                    "label_field": "name",
                    "style": {
                        "color": "#0000FF",
                        "width": 1
                    },
                    "level": 2
                },
                "railways": {
                    "geometry": "LineString",
                    "type": "0x14",
                    "label_field": "name",
                    "style": {
                        "color": "#808080",
                        "width": 1
                    },
                    "level": 2
                },
                "forests": {
                    "geometry": "Polygon",
                    "type": "0x16",
                    "label_field": "name",
                    "style": {
                        "fill_color": "#00FF00"
                    },
                    "level": 3
                },
                "water": {
                    "geometry": "Polygon",
                    "type": "0x3C",
                    "label_field": "name",
                    "style": {
                        "fill_color": "#0080FF"
                    },
                    "level": 2
                },
                "buildings": {
                    "geometry": "Polygon",
                    "type": "0x13",
                    "label_field": "name",
                    "style": {
                        "fill_color": "#C0C0C0"
                    },
                    "level": 1
                },
                "poi": {
                    "geometry": "Point",
                    "type": "0x2f00",
                    "label_field": "name",
                    "icon": "tree",
                    "level": 1
                },
                "cities": {
                    "geometry": "Point",
                    "type": "0x0100",
                    "label_field": "name",
                    "icon": "city",
                    "level": 0
                },
                "villages": {
                    "geometry": "Point",
                    "type": "0x0800",
                    "label_field": "name",
                    "icon": "village",
                    "level": 1
                }
            }
        }

    def get_garmin_types_by_category(self):
        """Получение типов Garmin по категориям"""
        return {
            "roads": {
                "0x01": "Автомагистраль",
                "0x02": "Главная дорога",
                "0x03": "Второстепенная дорога",
                "0x04": "Артериальная дорога",
                "0x05": "Коллекторная дорога",
                "0x06": "Жилая дорога",
                "0x07": "Переулок",
                "0x08": "Пешеходная дорога",
                "0x09": "Неклассифицированная дорога",
                "0x0a": "Паром",
                "0x0b": "Мост",
                "0x0c": "Туннель",
                "0x14": "Железная дорога",
                "0x16": "Тропа",
                "0x18": "Линия электропередач"
            },
            "water": {
                "0x1F": "Река/ручей",
                "0x26": "Морское побережье",
                "0x3C": "Озеро",
                "0x3D": "Пруд",
                "0x3E": "Водохранилище",
                "0x3F": "Залив",
                "0x40": "Море",
                "0x41": "Океан",
                "0x46": "Болото"
            },
            "areas": {
                "0x13": "Здание",
                "0x14": "Кладбище",
                "0x15": "Пустыня",
                "0x16": "Лес",
                "0x17": "Гольф-поле",
                "0x18": "Больница",
                "0x19": "Промышленная зона",
                "0x1A": "Парк",
                "0x1B": "Парковка",
                "0x1C": "Заповедник",
                "0x1D": "Аэропорт",
                "0x1E": "Торговый центр",
                "0x1F": "Военная база",
                "0x20": "Университет"
            },
            "poi": {
                "0x0100": "Город (большой)",
                "0x0200": "Город (средний)",
                "0x0300": "Город (малый)",
                "0x0400": "Поселок",
                "0x0500": "Деревня",
                "0x0600": "Населенный пункт",
                "0x0700": "Округ",
                "0x0800": "Край/область",
                "0x1100": "Выход",
                "0x2A00": "Больница",
                "0x2B00": "Заправка",
                "0x2C00": "Автомойка",
                "0x2D00": "Ремонт авто",
                "0x2E00": "Дилер авто",
                "0x2F00": "Общая точка интереса",
                "0x3000": "Еда быстрого приготовления",
                "0x4000": "Гостиница",
                "0x4100": "Ресторан",
                "0x5000": "Магазин",
                "0x6000": "Развлечения"
            }
        }

    def suggest_garmin_type(self, layer_name, geometry_type):
        """Предложение типа Garmin на основе имени слоя"""
        layer_name_lower = layer_name.lower()

        # Словарь ключевых слов для автоматического определения
        keyword_mapping = {
            # Дороги
            'road': '0x06', 'дорога': '0x06', 'street': '0x06', 'улица': '0x06',
            'highway': '0x01', 'автомагистраль': '0x01', 'трасса': '0x01',
            'railway': '0x14', 'железная': '0x14', 'жд': '0x14',

            # Водные объекты
            'river': '0x1F', 'река': '0x1F', 'stream': '0x1F', 'ручей': '0x1F',
            'lake': '0x3C', 'озеро': '0x3C', 'pond': '0x3C', 'пруд': '0x3C',
            'water': '0x3C', 'вода': '0x3C',

            # Области
            'forest': '0x16', 'лес': '0x16', 'woods': '0x16',
            'building': '0x13', 'здание': '0x13', 'дом': '0x13',
            'park': '0x1A', 'парк': '0x1A',

            # POI
            'city': '0x0100', 'город': '0x0100',
            'village': '0x0800', 'деревня': '0x0800', 'село': '0x0800',
            'poi': '0x2F00', 'point': '0x2F00'
        }

        # Ищем ключевые слова в имени слоя
        for keyword, garmin_type in keyword_mapping.items():
            if keyword in layer_name_lower:
                return garmin_type

        # Возвращаем тип по умолчанию для геометрии
        default_types = {
            'Point': '0x2F00',
            'LineString': '0x06',
            'Polygon': '0x16'
        }

        return default_types.get(geometry_type, '0x2F00')

    def export_mapping_to_json(self, file_path):
        """Экспорт сопоставления в JSON файл"""
        try:
            data = self.mapping_data or self.default_mapping
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception:
            return False

    def import_mapping_from_json(self, file_path):
        """Импорт сопоставления из JSON файла"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.load_mapping(data)
            return True
        except Exception:
            return False
