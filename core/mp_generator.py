# -*- coding: utf-8 -*-
"""
MP Generator for Garmin Export Plugin
Генератор файлов Polish format (MP) для плагина экспорта в Garmin

Формат соответствует спецификации cGPSmapper Polish format и требованиям
парсера mkgmap (PolishMapDataSource):
  - заголовок [IMG ID] завершается строкой [END-IMG ID];
  - секции данных [POI]/[POLYLINE]/[POLYGON] завершаются строкой [END];
  - Data<N> задаёт геометрию для уровня N (не используется для "продолжения"
    длинных списков координат — mkgmap не имеет ограничения в 255 точек);
  - файл записывается в кодировке, соответствующей объявленному CodePage.

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""


# Соответствие CodePage -> кодировка Python.
# Покрывает все языки интерфейса плагина и распространённые кодовые страницы.
# Все перечисленные кодеки входят в стандартную библиотеку Python.
CODEPAGE_ENCODINGS = {
    # DOS / OEM
    '437': 'cp437',      # Latin US
    '850': 'cp850',      # Западная Европа
    '852': 'cp852',      # Центральная Европа
    '855': 'cp855',      # Кириллица
    '866': 'cp866',      # Кириллица (русская DOS)
    '874': 'cp874',      # Тайский
    # CJK
    '932': 'cp932',      # Японский (Shift-JIS)
    '936': 'cp936',      # Упрощённый китайский (GBK)
    '949': 'cp949',      # Корейский
    '950': 'cp950',      # Традиционный китайский (Big5)
    # Windows single-byte
    '1250': 'cp1250',    # Центральная Европа
    '1251': 'cp1251',    # Кириллица
    '1252': 'cp1252',    # Западная Европа (Latin-1)
    '1253': 'cp1253',    # Греческий
    '1254': 'cp1254',    # Турецкий
    '1255': 'cp1255',    # Иврит
    '1256': 'cp1256',    # Арабский
    '1257': 'cp1257',    # Балтийский
    '1258': 'cp1258',    # Вьетнамский
    # Unicode
    '65001': 'utf-8',
}

# Разрешения по умолчанию для уровней 0..3 (см. документацию mkgmap --levels)
DEFAULT_LEVEL_RESOLUTIONS = [24, 22, 20, 18]

MAX_LEVELS = 4


def sanitize_label(value):
    """Очистка подписи для безопасной записи в MP файл.

    Убирает переводы строк и управляющие символы, ограничивает длину
    (лейблы Garmin ограничены, длинные строки не имеют смысла).
    """
    if value is None:
        return ''
    text = str(value)
    # Переводы строк и табуляция ломают формат "ключ=значение"
    for bad in ('\r', '\n', '\t'):
        text = text.replace(bad, ' ')
    # Управляющие символы
    text = ''.join(ch for ch in text if ord(ch) >= 32)
    text = text.strip()
    # Разумное ограничение длины подписи
    if len(text) > 80:
        text = text[:80].rstrip()
    return text


def format_coord_pair(lon, lat):
    """Форматирование пары координат в нотацию MP: (lat,lon)"""
    return '({0:.6f},{1:.6f})'.format(lat, lon)


class MPGenerator:
    """Генератор файлов формата Polish (MP) для Garmin"""

    def __init__(self):
        self.reset()

    def reset(self):
        """Сброс состояния генератора"""
        self.header_lines = []
        self.data_sections = []
        self.poi_count = 0
        self.polyline_count = 0
        self.polygon_count = 0
        self.skipped_count = 0
        self.levels_count = MAX_LEVELS
        self.encoding = 'cp1251'

    # ------------------------------------------------------------------
    # Публичный API
    # ------------------------------------------------------------------

    def generate_mp_file(self, processed_data, output_path, settings):
        """Генерация MP файла из обработанных данных.

        Args:
            processed_data: список словарей layer_data (см. LayerProcessor)
            output_path: путь к результирующему .mp файлу
            settings: словарь настроек карты (map_id, map_name, code_page,
                enabled_levels, transparent, routing, ...)
        """
        self.reset()

        code_page = str(settings.get('code_page', '1251'))
        self.encoding = CODEPAGE_ENCODINGS.get(code_page, 'cp1251')

        self._generate_header(settings, code_page)

        for layer_data in processed_data:
            self._generate_layer_sections(layer_data)

        self._write_mp_file(output_path)

    # ------------------------------------------------------------------
    # Заголовок
    # ------------------------------------------------------------------

    def _resolve_levels(self, settings):
        """Определение количества уровней и их разрешений.

        enabled_levels - список включённых уровней GUI (подмножество 0..3).
        Количество уровней в карте = количеству включённых уровней,
        разрешения назначаются по убыванию начиная с 24.
        """
        enabled = settings.get('enabled_levels') or [0, 1, 2, 3]
        count = max(1, min(MAX_LEVELS, len(enabled)))
        resolutions = DEFAULT_LEVEL_RESOLUTIONS[:count]
        return count, resolutions

    def _generate_header(self, settings, code_page):
        """Генерация заголовочной секции [IMG ID]"""
        count, resolutions = self._resolve_levels(settings)
        self.levels_count = count

        map_name = sanitize_label(settings.get('map_name', 'QGIS Map')) or 'QGIS Map'

        lines = [
            '; Generated by Garmin Export Plugin for QGIS',
            '; https://github.com/AlexKobyakov/garmin_export',
        ]
        description = sanitize_label(settings.get('map_description', ''))
        if description:
            lines.append('; Description: {0}'.format(description))

        lines += [
            '',
            '[IMG ID]',
            'ID={0}'.format(settings.get('map_id', 12340001)),
            'Name={0}'.format(map_name),
            'CodePage={0}'.format(code_page),
            'LblCoding=9',
            'Elevation=M',
            'Preprocess=F',
            'TreSize=2048',
            'RgnLimit=1024',
            'POIIndex=Y',
        ]

        if settings.get('transparent'):
            lines.append('Transparent=Y')
        else:
            lines.append('Transparent=N')

        if settings.get('routing'):
            lines.append('Routing=Y')

        lines.append('Levels={0}'.format(count))
        for i, resolution in enumerate(resolutions):
            lines.append('Level{0}={1}'.format(i, resolution))
        for i in range(count):
            lines.append('Zoom{0}={1}'.format(i, i))

        lines.append('[END-IMG ID]')

        self.header_lines = lines

    # ------------------------------------------------------------------
    # Секции данных
    # ------------------------------------------------------------------

    def _generate_layer_sections(self, layer_data):
        """Генерация секций для слоя"""
        geometry_type = layer_data.get('geometry_type')
        features = layer_data.get('features', [])
        garmin_type = layer_data.get('garmin_type', '0x01')
        label_field = layer_data.get('label_field')
        level = layer_data.get('level', 1)

        # EndLevel не может превышать количество уровней карты - 1
        end_level = max(0, min(int(level), self.levels_count - 1))

        for feature in features:
            if geometry_type == 'Point':
                self._generate_poi_section(feature, garmin_type, label_field, end_level)
            elif geometry_type == 'LineString':
                self._generate_polyline_section(feature, garmin_type, label_field, end_level)
            elif geometry_type == 'Polygon':
                self._generate_polygon_section(feature, garmin_type, label_field, end_level)
            else:
                self.skipped_count += 1

    def _get_label(self, feature, label_field):
        """Получение подписи объекта из атрибутов"""
        attributes = feature.get('attributes', {})
        if label_field and label_field in attributes:
            return sanitize_label(attributes[label_field])
        return ''

    def _common_section_lines(self, section_name, garmin_type, label, end_level):
        """Общие строки для любой секции данных"""
        lines = [
            '[{0}]'.format(section_name),
            'Type={0}'.format(garmin_type),
        ]
        if label:
            lines.append('Label={0}'.format(label))
        if end_level > 0:
            lines.append('EndLevel={0}'.format(end_level))
        return lines

    def _generate_poi_section(self, feature, garmin_type, label_field, end_level):
        """Генерация секции [POI] (точка)"""
        geometry = feature.get('geometry') or {}
        coords = geometry.get('coordinates')
        if not coords or len(coords) < 2:
            self.skipped_count += 1
            return

        label = self._get_label(feature, label_field)
        lines = self._common_section_lines('POI', garmin_type, label, end_level)
        lines.append('Data0={0}'.format(format_coord_pair(coords[0], coords[1])))
        lines.append('[END]')

        self.data_sections.append('\n'.join(lines))
        self.poi_count += 1

    def _generate_polyline_section(self, feature, garmin_type, label_field, end_level):
        """Генерация секции [POLYLINE] (линия).

        Каждая часть мультилинии записывается отдельной секцией.
        """
        geometry = feature.get('geometry') or {}
        parts = geometry.get('parts')
        if parts is None:
            coords = geometry.get('coordinates')
            parts = [coords] if coords else []

        label = self._get_label(feature, label_field)

        for part in parts:
            if not part or len(part) < 2:
                self.skipped_count += 1
                continue

            coord_pairs = [
                format_coord_pair(c[0], c[1]) for c in part if len(c) >= 2
            ]
            if len(coord_pairs) < 2:
                self.skipped_count += 1
                continue

            lines = self._common_section_lines('POLYLINE', garmin_type, label, end_level)
            lines.append('Data0={0}'.format(','.join(coord_pairs)))
            lines.append('[END]')

            self.data_sections.append('\n'.join(lines))
            self.polyline_count += 1

    def _generate_polygon_section(self, feature, garmin_type, label_field, end_level):
        """Генерация секции [POLYGON] (полигон).

        Каждая часть мультиполигона записывается отдельной секцией.
        Используется только внешнее кольцо: формат MP не поддерживает
        отверстия в полигонах.
        """
        geometry = feature.get('geometry') or {}
        parts = geometry.get('parts')
        if parts is None:
            coords = geometry.get('coordinates')
            parts = [coords] if coords else []

        label = self._get_label(feature, label_field)

        for rings in parts:
            if not rings or not rings[0]:
                self.skipped_count += 1
                continue

            outer_ring = rings[0]
            coord_pairs = [
                format_coord_pair(c[0], c[1]) for c in outer_ring if len(c) >= 2
            ]
            if len(coord_pairs) < 3:
                self.skipped_count += 1
                continue

            lines = self._common_section_lines('POLYGON', garmin_type, label, end_level)
            lines.append('Data0={0}'.format(','.join(coord_pairs)))
            lines.append('[END]')

            self.data_sections.append('\n'.join(lines))
            self.polygon_count += 1

    # ------------------------------------------------------------------
    # Запись
    # ------------------------------------------------------------------

    def _write_mp_file(self, output_path):
        """Запись MP файла в кодировке, соответствующей CodePage"""
        try:
            with open(output_path, 'w', encoding=self.encoding, errors='replace',
                      newline='\r\n') as f:
                f.write('\n'.join(self.header_lines))
                f.write('\n\n')
                for section in self.data_sections:
                    f.write(section)
                    f.write('\n\n')
        except (OSError, ValueError) as e:
            raise Exception('Ошибка записи MP файла: {0}'.format(str(e)))

    def get_statistics(self):
        """Получение статистики генерации"""
        return {
            'total_sections': len(self.data_sections),
            'poi_count': self.poi_count,
            'polyline_count': self.polyline_count,
            'polygon_count': self.polygon_count,
            'skipped_count': self.skipped_count,
        }
