# -*- coding: utf-8 -*-
"""Тесты системы переводов и языков интерфейса (без QGIS/Qt)."""

import importlib
import os
import unittest

from _bootstrap import PACKAGE  # noqa: F401
from garmin_export import translation_manager as tmmod
from garmin_export.translation_manager import TranslationManager

# Ожидаемый набор языков (соответствует LANGUAGE_LABELS)
EXPECTED_LANGUAGES = ['ru', 'en', 'zh', 'hi', 'es', 'ar', 'fr', 'pt', 'de',
                      'id', 'th', 'vi']

TRANSLATIONS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'translations')


def _load(lang):
    return importlib.import_module(
        'garmin_export.translations.{0}'.format(lang)).translations


class LanguageRegistryTest(unittest.TestCase):

    def setUp(self):
        self.tm = TranslationManager()

    def test_supported_languages(self):
        self.assertEqual(set(self.tm.get_supported_languages()),
                         set(EXPECTED_LANGUAGES))

    def test_twelve_languages(self):
        self.assertEqual(len(self.tm.get_supported_languages()), 12)

    def test_labels_match_supported(self):
        labels = self.tm.get_language_labels()
        self.assertEqual(len(labels), 12)
        codes = [code for code, _ in labels]
        self.assertEqual(set(codes), set(EXPECTED_LANGUAGES))
        # У каждого языка непустое отображаемое имя
        for code, label in labels:
            self.assertTrue(label.strip(), 'empty label for {0}'.format(code))

    def test_every_language_has_a_file(self):
        for lang in EXPECTED_LANGUAGES:
            path = os.path.join(TRANSLATIONS_DIR, '{0}.py'.format(lang))
            self.assertTrue(os.path.isfile(path),
                            'missing translation file: {0}'.format(path))

    def test_all_languages_load(self):
        for lang in EXPECTED_LANGUAGES:
            self.assertTrue(self.tm.set_language(lang),
                            'failed to load {0}'.format(lang))


class KeyConsistencyTest(unittest.TestCase):
    """Все языки имеют одинаковый набор ключей, без пустых значений."""

    def setUp(self):
        self.base = set(_load('en').keys())

    def test_base_nonempty(self):
        self.assertGreater(len(self.base), 150)

    def test_same_keys_all_languages(self):
        for lang in EXPECTED_LANGUAGES:
            keys = set(_load(lang).keys())
            missing = self.base - keys
            extra = keys - self.base
            self.assertFalse(missing, '{0} missing: {1}'.format(lang, sorted(missing)))
            self.assertFalse(extra, '{0} extra: {1}'.format(lang, sorted(extra)))

    def test_no_empty_values(self):
        for lang in EXPECTED_LANGUAGES:
            for key, value in _load(lang).items():
                self.assertTrue(str(value).strip(),
                                'empty value {0}/{1}'.format(lang, key))

    def test_format_placeholder_preserved(self):
        # ключ с подстановкой {error} должен сохранять плейсхолдер
        for lang in EXPECTED_LANGUAGES:
            self.assertIn('{error}', _load(lang)['error_mkgmap_execution'],
                          '{0} lost {{error}} placeholder'.format(lang))


class CodePageKeysTest(unittest.TestCase):
    """Названия всех кодовых страниц переведены во всех языках."""

    def test_codepage_keys_present(self):
        from garmin_export.core.codepages import CODE_PAGE_KEYS
        for lang in EXPECTED_LANGUAGES:
            d = _load(lang)
            for key in CODE_PAGE_KEYS:
                self.assertIn(key, d, '{0} missing {1}'.format(lang, key))
                self.assertTrue(str(d[key]).strip())


class TranslationLookupTest(unittest.TestCase):

    def setUp(self):
        self.tm = TranslationManager()

    def test_get_text_translated(self):
        # один и тот же ключ на разных языках даёт непустой перевод
        for lang in EXPECTED_LANGUAGES:
            self.tm.set_language(lang)
            text = self.tm.get_text('compile_map')
            self.assertTrue(text.strip())
            self.assertNotEqual(text, 'compile_map')

    def test_missing_key_returns_key(self):
        self.tm.set_language('en')
        self.assertEqual(self.tm.get_text('__no_such_key__'), '__no_such_key__')

    def test_fallback_to_english(self):
        # неизвестный язык не ломает выдачу
        self.assertFalse(self.tm.set_language('xx'))

    def test_rtl_only_arabic(self):
        self.assertTrue(self.tm.is_rtl('ar'))
        for lang in EXPECTED_LANGUAGES:
            if lang != 'ar':
                self.assertFalse(self.tm.is_rtl(lang),
                                 '{0} should not be RTL'.format(lang))


if __name__ == '__main__':
    unittest.main()
