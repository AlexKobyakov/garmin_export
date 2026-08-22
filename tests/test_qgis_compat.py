# -*- coding: utf-8 -*-
"""Static guards for the QGIS 3/4 and Qt5/Qt6 compatibility boundary."""

import os
import re
import io
import tokenize
import unittest

from _bootstrap import PACKAGE  # noqa: F401


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEGACY_OVERSIZED = {}


def _python_files():
    for folder, dirs, names in os.walk(ROOT):
        dirs[:] = [name for name in dirs
                   if name not in ('.git', '__pycache__', 'build', 'dist')]
        for name in names:
            if name.endswith('.py') and not name.startswith('test_'):
                yield os.path.relpath(os.path.join(folder, name), ROOT)


def _source(path):
    with open(os.path.join(ROOT, path), encoding='utf-8') as handle:
        return handle.read()


def _key(path):
    """Use repository-style separators on Windows and POSIX."""
    return path.replace(os.sep, '/')


class CompatibilityBoundaryTest(unittest.TestCase):

    def test_no_direct_pyqt_major_imports(self):
        for path in _python_files():
            source = _source(path)
            self.assertNotIn('PyQt5', source, path)
            self.assertNotIn('PyQt6', source, path)

    def test_qt6_sensitive_spellings_are_shimmed(self):
        forbidden = (
            r'\.exec_\(', r'QAction.*QtWidgets',
            r'QVariant\.(Int|Double|String)',
            r'QgsTask\.CanCancel',
            r'QgsWkbTypes\.(Point|Line|Polygon)Geometry',
            r'\bQt\.',
            r'QFont\.(Thin|ExtraLight|Light|Normal|Medium|DemiBold|Bold|'
            r'ExtraBold|Black)',
            r'QHeaderView\.(Stretch|ResizeToContents|Interactive|Fixed)',
            r'QTableWidget\.(NoEditTriggers|SelectRows)',
            r'QAbstractItemView\.(NoEditTriggers|SelectRows)',
            r'QPainter\.Antialiasing', r'QFrame\.(NoFrame|HLine|Sunken)',
            r'\b(?:cursor|QTextCursor)\.End\b',
        )
        for path in _python_files():
            if path == 'qgis_compat.py':
                continue
            source = _source(path)
            for pattern in forbidden:
                self.assertIsNone(
                    re.search(pattern, source),
                    '{0}: forbidden {1}'.format(path, pattern))

    def test_compat_imports_are_package_relative(self):
        for path in _python_files():
            if path == 'qgis_compat.py':
                continue
            self.assertNotIn('from qgis_compat import', _source(path), path)

    def test_new_files_respect_500_line_limit(self):
        for path in _python_files():
            lines = len(_source(path).splitlines())
            if _key(path) in LEGACY_OVERSIZED:
                self.assertLessEqual(
                    lines, LEGACY_OVERSIZED[_key(path)],
                    '{0} grew beyond its G1 baseline'.format(path))
            else:
                self.assertLessEqual(
                    lines, 500,
                    '{0} exceeds the 500-line module limit'.format(path))

    def test_legacy_oversized_files_are_explicit_decomposition_debt(self):
        actual = {_key(path) for path in _python_files()
                  if len(_source(path).splitlines()) > 500}
        self.assertEqual(actual, set(LEGACY_OVERSIZED))

    def test_reference_author_and_support_dialog_contract(self):
        author = _source('gui/gui_dialogs.py')
        support = _source('gui/simple_donation.py')
        self.assertIn('class AuthorInfoDialog(QDialog):', author)
        self.assertIn('def retranslateUi(self):', author)
        for name in ('title_label', 'subtitle_label', 'version_label',
                     'about_label', 'contact_label', 'close_button'):
            self.assertIn('self.{0}'.format(name), author)
        self.assertIn('class SimpleDonationDialog(QDialog):', support)
        self.assertIn('def retranslateUi(self):', support)
        for name in ('title_label', 'description_label', 'kofi_button',
                     'tbank_button', 'github_button'):
            self.assertIn('self.{0}'.format(name), support)

    def test_dialogs_expose_retranslate_contract(self):
        source = _source('gui/gui_dialogs.py')
        for class_name in ('MappingEditorDialog', 'DownloadProgressDialog',
                           'ErrorDialog'):
            block = source.split('class {0}'.format(class_name), 1)[1]
            self.assertIn('def retranslateUi(self):', block, class_name)

    def test_legacy_gui_facades_keep_public_exports(self):
        widgets = _source('gui/gui_widgets.py')
        handlers = _source('gui/gui_handlers.py')
        for name in ('HeaderWidget', 'LayerSelectionWidget',
                     'ExportSettingsWidget', 'StyleMappingWidget',
                     'ControlButtonsWidget', 'LogTextWidget',
                     'ResultsTableWidget', 'LevelSettingsWidget'):
            self.assertIn(name, widgets)
        self.assertIn('class GuiEventHandlers(', handlers)
        for name in ('UiHandlers', 'DownloadHandlers', 'MappingHandlers',
                     'CompilationHandlers', 'SettingsHandlers'):
            self.assertIn(name, handlers)

    def test_scoped_gui_has_no_untranslated_cyrillic_literals(self):
        paths = ('gui/gui_handlers.py', 'gui/gui_main.py',
                 'gui/gui_widgets.py', 'gui/gui_mkgmap_widgets.py',
                 'gui/simple_donation.py', 'gui/widget_i18n.py',
                 'gui/widget_header.py', 'gui/widget_selection.py',
                 'gui/widget_results.py', 'gui/handler_ui.py',
                 'gui/handler_download.py', 'gui/handler_mapping.py',
                 'gui/handler_compile.py', 'gui/handler_settings.py')
        for path in paths:
            tokens = tokenize.generate_tokens(
                io.StringIO(_source(path)).readline)
            for token in tokens:
                if token.type != tokenize.STRING:
                    continue
                if token.string.startswith(('"""', "'''")):
                    continue
                alphabet = ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
                            'абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
                if any(char in token.string for char in alphabet):
                    self.fail('{0}:{1} has an untranslated string'.format(
                        path, token.start[0]))


if __name__ == '__main__':
    unittest.main()
