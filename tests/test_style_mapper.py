# -*- coding: utf-8 -*-
"""Тесты сопоставления стилей QGIS -> Garmin."""

import unittest

from _bootstrap import PACKAGE  # noqa: F401
from garmin_export.core.style_mapper import StyleMapper


class StyleMapperTest(unittest.TestCase):

    def setUp(self):
        self.mapper = StyleMapper()
        self.mapper.load_mapping(self.mapper._get_default_mapping())

    def test_default_mapping_has_layers(self):
        self.assertIn('layers', self.mapper.mapping_data)
        self.assertIn('roads', self.mapper.mapping_data['layers'])

    def test_exact_name_match(self):
        mapping = self.mapper.get_layer_mapping('roads', 'LineString')
        self.assertEqual(mapping['type'], '0x06')

    def test_partial_name_match(self):
        mapping = self.mapper.get_layer_mapping('my_roads_layer', 'LineString')
        self.assertEqual(mapping['type'], '0x06')

    def test_geometry_default_fallback(self):
        mapping = self.mapper.get_layer_mapping('unknown_xyz', 'Polygon')
        self.assertIn('type', mapping)

    def test_suggest_forest(self):
        self.assertEqual(
            self.mapper.suggest_garmin_type('forest_areas', 'Polygon'), '0x16')

    def test_suggest_default_for_point(self):
        self.assertEqual(
            self.mapper.suggest_garmin_type('mystery', 'Point'), '0x2F00')


if __name__ == '__main__':
    unittest.main()
