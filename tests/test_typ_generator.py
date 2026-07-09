# -*- coding: utf-8 -*-
"""Тесты генератора TYP-файлов."""

import unittest

from _bootstrap import PACKAGE  # noqa: F401
from garmin_export.core.typ_generator import TypFileBuilder


class FormatTypeTest(unittest.TestCase):

    def test_short_type(self):
        self.assertEqual(TypFileBuilder._format_type(0x16), '0x16')

    def test_type_subtype(self):
        self.assertEqual(TypFileBuilder._format_type(0x2f00), '0x2f00')

    def test_extended_type(self):
        self.assertEqual(TypFileBuilder._format_type(0x10208), '0x10208')


class BuilderTest(unittest.TestCase):

    def test_id_section(self):
        b = TypFileBuilder(1234, 1, '1251')
        text = b.build()
        self.assertIn('[_id]', text)
        self.assertIn('FID=1234', text)
        self.assertIn('ProductCode=1', text)
        self.assertIn('CodePage=1251', text)
        self.assertIn('[end]', text)

    def test_polygon_and_draworder(self):
        b = TypFileBuilder(1234)
        b.add_polygon(0x16, '#00ff00', draw_order=3, label='Forest')
        text = b.build()
        self.assertIn('[_drawOrder]', text)
        self.assertIn('Type=0x16,3', text)
        self.assertIn('[_polygon]', text)
        self.assertIn('"a c #00ff00"', text)
        self.assertIn('String=Forest', text)

    def test_line_with_width(self):
        b = TypFileBuilder(1234)
        b.add_line(0x06, '#ff0000', width=3)
        text = b.build()
        self.assertIn('[_line]', text)
        self.assertIn('LineWidth=3', text)
        self.assertIn('"a c #ff0000"', text)

    def test_line_with_border(self):
        b = TypFileBuilder(1234)
        b.add_line(0x06, '#ff0000', width=2, border_color='#000000', border_width=1)
        text = b.build()
        self.assertIn('BorderWidth=1', text)
        self.assertIn('"b c #000000"', text)

    def test_line_width_clamped(self):
        b = TypFileBuilder(1234)
        b.add_line(0x06, '#ff0000', width=999)
        self.assertEqual(b.lines[0][2], 15)  # width clamped to 15

    def test_point_xpm(self):
        b = TypFileBuilder(1234)
        pixels = [
            ['#ff0000', None],
            [None, '#00ff00'],
        ]
        b.add_point(0x2f00, pixels, label='POI')
        text = b.build()
        self.assertIn('[_point]', text)
        self.assertIn('DayXpm="2 2 ', text)
        self.assertIn('String=POI', text)
        self.assertIn('c none', text)

    def test_color_normalization_short_hex(self):
        b = TypFileBuilder(1234)
        b.add_polygon(0x16, '#0f0')
        self.assertEqual(b.polygons[0][1], '#00ff00')

    def test_empty_point_ignored(self):
        b = TypFileBuilder(1234)
        b.add_point(0x2f00, [])
        self.assertEqual(len(b.points), 0)


class XpmPaletteTest(unittest.TestCase):

    def test_none_becomes_none(self):
        pixels = [['#112233', None]]
        palette, rows = TypFileBuilder._build_xpm_palette(pixels)
        colors = [c for _, c in palette]
        self.assertIn('none', colors)
        self.assertIn('#112233', colors)
        self.assertEqual(len(rows), 1)
        self.assertEqual(len(rows[0]), 2)


if __name__ == '__main__':
    unittest.main()
