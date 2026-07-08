# -*- coding: utf-8 -*-
"""Тесты поддержки кодовых страниц (code pages) для генерации MP и команды."""

import codecs
import os
import tempfile
import unittest

from _bootstrap import PACKAGE  # noqa: F401
from garmin_export.core import mp_generator, mkgmap_command
from garmin_export.core.codepages import CODE_PAGES, CODE_PAGE_CODES


class CodepageCatalogueTest(unittest.TestCase):

    def test_utf8_first(self):
        # UTF-8/Unicode должен быть первым (универсальный вариант)
        self.assertEqual(CODE_PAGES[0][0], '65001')

    def test_no_duplicate_codes(self):
        self.assertEqual(len(CODE_PAGE_CODES), len(set(CODE_PAGE_CODES)))

    def test_every_ui_code_has_encoding(self):
        # каждая кодовая страница из UI имеет отображение на кодек Python
        for code in CODE_PAGE_CODES:
            self.assertIn(code, mp_generator.CODEPAGE_ENCODINGS,
                          'no encoding for code page {0}'.format(code))

    def test_all_encodings_are_valid_codecs(self):
        for code, enc in mp_generator.CODEPAGE_ENCODINGS.items():
            try:
                codecs.lookup(enc)
            except LookupError:
                self.fail('invalid codec {0} for code page {1}'.format(enc, code))

    def test_covers_key_languages(self):
        # ключевые языки интерфейса покрыты соответствующими кодировками
        needed = {'1251', '1250', '1252', '1253', '1254', '1255', '1256',
                  '1257', '1258', '874', '932', '936', '949', '950', '65001'}
        self.assertTrue(needed.issubset(set(CODE_PAGE_CODES)))


class MkgmapCodePageOptionTest(unittest.TestCase):

    def _cmd(self, code_page):
        return mkgmap_command.build_command(
            'java', 'm.jar', {'code_page': code_page}, ['map.mp'])

    def test_unicode_for_65001(self):
        cmd = self._cmd('65001')
        self.assertIn('--unicode', cmd)
        self.assertFalse(any(a.startswith('--code-page') for a in cmd))

    def test_code_page_option_for_others(self):
        for code in CODE_PAGE_CODES:
            if code == '65001':
                continue
            cmd = self._cmd(code)
            self.assertIn('--code-page={0}'.format(code), cmd,
                          'missing --code-page for {0}'.format(code))


class MpEncodingRoundTripTest(unittest.TestCase):
    """Подпись, записанная в MP, читается обратно в объявленной кодировке."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix='enc_test_')

    def _write_and_read(self, code_page, label):
        gen = mp_generator.MPGenerator()
        data = [{
            'geometry_type': 'Point',
            'garmin_type': '0x2f00',
            'label_field': 'name',
            'level': 1,
            'features': [{
                'geometry': {'type': 'Point', 'coordinates': [37.6, 55.7]},
                'attributes': {'name': label},
            }],
        }]
        settings = {
            'map_id': 12340001, 'map_name': 'Test',
            'enabled_levels': [0, 1, 2, 3], 'code_page': code_page,
        }
        path = os.path.join(self.tmp, 'cp{0}.mp'.format(code_page))
        gen.generate_mp_file(data, path, settings)
        enc = mp_generator.CODEPAGE_ENCODINGS[code_page]
        with open(path, 'r', encoding=enc) as f:
            return f.read()

    def test_cyrillic_cp1251(self):
        text = self._write_and_read('1251', 'Река Волга')
        self.assertIn('Label=Река Волга', text)
        self.assertIn('CodePage=1251', text)

    def test_cyrillic_cp866(self):
        text = self._write_and_read('866', 'Река')
        self.assertIn('Label=Река', text)

    def test_latin_cp1252(self):
        text = self._write_and_read('1252', 'Zürich Straße')
        self.assertIn('Label=Zürich Straße', text)

    def test_central_europe_cp1250(self):
        text = self._write_and_read('1250', 'Kraków')
        self.assertIn('Label=Kraków', text)

    def test_greek_cp1253(self):
        text = self._write_and_read('1253', 'Αθήνα')
        self.assertIn('Label=Αθήνα', text)

    def test_hebrew_cp1255(self):
        text = self._write_and_read('1255', 'שלום')
        self.assertIn('Label=שלום', text)

    def test_arabic_cp1256(self):
        text = self._write_and_read('1256', 'القاهرة')
        self.assertIn('Label=القاهرة', text)

    def test_thai_cp874(self):
        text = self._write_and_read('874', 'แม่น้ำเจ้าพระยา')
        self.assertIn('Label=แม่น้ำเจ้าพระยา', text)

    def test_japanese_cp932(self):
        text = self._write_and_read('932', '東京')
        self.assertIn('Label=東京', text)

    def test_simplified_chinese_cp936(self):
        text = self._write_and_read('936', '北京')
        self.assertIn('Label=北京', text)

    def test_korean_cp949(self):
        text = self._write_and_read('949', '서울')
        self.assertIn('Label=서울', text)

    def test_traditional_chinese_cp950(self):
        text = self._write_and_read('950', '臺北')
        self.assertIn('Label=臺北', text)

    def test_utf8_multilingual(self):
        # UTF-8 покрывает всё сразу: китайский, хинди, кириллица, вьетнамский
        text = self._write_and_read('65001', '长江 गंगा Волга Sông Hồng')
        self.assertIn('Label=长江 गंगा Волга Sông Hồng', text)
        self.assertIn('CodePage=65001', text)

    def test_vietnamese_via_utf8(self):
        # вьетнамский с тоновыми знаками надёжно работает через UTF-8
        text = self._write_and_read('65001', 'Sông Hồng, Hà Nội')
        self.assertIn('Label=Sông Hồng, Hà Nội', text)


class MpEncodingSelectionTest(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix='encsel_test_')

    def _encoding_for(self, code_page):
        gen = mp_generator.MPGenerator()
        gen.generate_mp_file(
            [], os.path.join(self.tmp, 'x.mp'),
            {'map_id': 1, 'map_name': 'x', 'code_page': code_page,
             'enabled_levels': [0]})
        return gen.encoding

    def test_utf8_selected(self):
        self.assertEqual(self._encoding_for('65001'), 'utf-8')

    def test_cp1251_selected(self):
        self.assertEqual(self._encoding_for('1251'), 'cp1251')

    def test_cp1258_selected(self):
        self.assertEqual(self._encoding_for('1258'), 'cp1258')

    def test_unknown_falls_back_to_cp1251(self):
        self.assertEqual(self._encoding_for('99999'), 'cp1251')


if __name__ == '__main__':
    unittest.main()
