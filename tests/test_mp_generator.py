# -*- coding: utf-8 -*-
"""Тесты генератора Polish MP формата."""

import os
import tempfile
import unittest

from _bootstrap import PACKAGE  # noqa: F401
from garmin_export.core import mp_generator


class SanitizeLabelTest(unittest.TestCase):

    def test_removes_newlines_and_tabs(self):
        self.assertEqual(mp_generator.sanitize_label('a\nb\tc\r'), 'a b c')

    def test_strips(self):
        self.assertEqual(mp_generator.sanitize_label('  hello  '), 'hello')

    def test_none(self):
        self.assertEqual(mp_generator.sanitize_label(None), '')

    def test_length_limit(self):
        long = 'x' * 200
        self.assertLessEqual(len(mp_generator.sanitize_label(long)), 80)

    def test_removes_control_chars(self):
        self.assertEqual(mp_generator.sanitize_label('a\x00\x01b'), 'ab')


class FormatCoordTest(unittest.TestCase):

    def test_lat_lon_order(self):
        # Вход: (lon, lat) -> вывод (lat,lon)
        self.assertEqual(
            mp_generator.format_coord_pair(37.6173, 55.7558),
            '(55.755800,37.617300)')


class GenerateMpTest(unittest.TestCase):

    def setUp(self):
        self.gen = mp_generator.MPGenerator()
        self.tmp = tempfile.mkdtemp(prefix='mp_test_')

    def _write(self, data, settings):
        path = os.path.join(self.tmp, 'out.mp')
        self.gen.generate_mp_file(data, path, settings)
        with open(path, 'r', encoding=self.gen.encoding, errors='replace') as f:
            return f.read()

    def _base_settings(self, **kw):
        s = {
            'map_id': 12340001,
            'map_name': 'Test Map',
            'map_description': 'desc',
            'enabled_levels': [0, 1, 2, 3],
            'code_page': '1251',
        }
        s.update(kw)
        return s

    def test_header_markers(self):
        text = self._write([], self._base_settings())
        self.assertIn('[IMG ID]', text)
        self.assertIn('[END-IMG ID]', text)
        self.assertIn('CodePage=1251', text)
        self.assertIn('Levels=4', text)
        self.assertIn('Level0=24', text)

    def test_poi_section(self):
        data = [{
            'geometry_type': 'Point',
            'garmin_type': '0x2f00',
            'label_field': 'name',
            'level': 1,
            'features': [{
                'geometry': {'type': 'Point', 'coordinates': [37.6, 55.7]},
                'attributes': {'name': 'Point A'},
            }],
        }]
        text = self._write(data, self._base_settings())
        self.assertIn('[POI]', text)
        self.assertIn('Type=0x2f00', text)
        self.assertIn('Label=Point A', text)
        self.assertIn('Data0=(55.700000,37.600000)', text)
        self.assertIn('[END]', text)

    def test_polyline_multipart_creates_two_sections(self):
        data = [{
            'geometry_type': 'LineString',
            'garmin_type': '0x06',
            'label_field': 'name',
            'level': 1,
            'features': [{
                'geometry': {'type': 'LineString', 'parts': [
                    [[37.0, 55.0], [37.1, 55.1]],
                    [[38.0, 56.0], [38.1, 56.1]],
                ]},
                'attributes': {'name': 'Road'},
            }],
        }]
        text = self._write(data, self._base_settings())
        self.assertEqual(text.count('[POLYLINE]'), 2)
        stats = self.gen.get_statistics()
        self.assertEqual(stats['polyline_count'], 2)

    def test_polygon_requires_three_points(self):
        data = [{
            'geometry_type': 'Polygon',
            'garmin_type': '0x16',
            'label_field': 'name',
            'level': 2,
            'features': [
                {  # валидный полигон
                    'geometry': {'type': 'Polygon', 'parts': [
                        [[[37.0, 55.0], [37.1, 55.0], [37.1, 55.1], [37.0, 55.0]]],
                    ]},
                    'attributes': {'name': 'Forest'},
                },
                {  # вырожденный - должен быть пропущен
                    'geometry': {'type': 'Polygon', 'parts': [
                        [[[37.0, 55.0], [37.1, 55.0]]],
                    ]},
                    'attributes': {'name': 'Bad'},
                },
            ],
        }]
        text = self._write(data, self._base_settings())
        self.assertEqual(text.count('[POLYGON]'), 1)
        self.assertIn('Type=0x16', text)
        self.assertGreaterEqual(self.gen.get_statistics()['skipped_count'], 1)

    def test_cyrillic_label_cp1251(self):
        data = [{
            'geometry_type': 'Point',
            'garmin_type': '0x2f00',
            'label_field': 'name',
            'level': 1,
            'features': [{
                'geometry': {'type': 'Point', 'coordinates': [37.6, 55.7]},
                'attributes': {'name': 'Река'},
            }],
        }]
        path = os.path.join(self.tmp, 'cyr.mp')
        self.gen.generate_mp_file(data, path, self._base_settings())
        # Файл должен читаться в cp1251 и содержать кириллицу
        with open(path, 'r', encoding='cp1251') as f:
            text = f.read()
        self.assertIn('Label=Река', text)

    def test_endlevel_clamped_to_level_count(self):
        # Только 1 уровень включён -> EndLevel не может быть 3
        data = [{
            'geometry_type': 'Point',
            'garmin_type': '0x2f00',
            'label_field': 'name',
            'level': 3,
            'features': [{
                'geometry': {'type': 'Point', 'coordinates': [37.6, 55.7]},
                'attributes': {'name': 'P'},
            }],
        }]
        text = self._write(data, self._base_settings(enabled_levels=[0]))
        # При одном уровне EndLevel=0 -> строка EndLevel не пишется
        self.assertNotIn('EndLevel=3', text)


if __name__ == '__main__':
    unittest.main()
