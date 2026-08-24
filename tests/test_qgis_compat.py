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

    def test_ci_uses_report_and_checker_without_diff_gate(self):
        workflow = _source('.github/workflows/ci.yml')
        self.assertIn('pyqt5_to_pyqt6.py --dry_run', workflow)
        self.assertIn('pyqt5_to_pyqt6.py .', workflow)
        self.assertNotIn('git diff --exit-code', workflow)

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

    def test_qt5_language_signal_uses_canonical_codes(self):
        header = _source('gui/widget_header.py')
        main = _source('gui/gui_main.py')
        handler = _source('gui/handler_ui.py')
        self.assertIn('self._language_codes', header)
        self.assertIn('def language_code_at', header)
        self.assertIn('language_signal[int]', main)
        self.assertIn('language_code_at(index)', handler)
        self.assertIn('QSignalBlocker', _source('gui/gui_mkgmap_widgets.py'))

    def test_language_selector_uses_packaged_svg_flags(self):
        manager = _source('translation_manager.py')
        header = _source('gui/widget_header.py')
        self.assertIn('LANGUAGE_FLAG_FILES', manager)
        self.assertIn('get_language_flag_path', manager)
        self.assertIn('QIcon(flag)', header)
        self.assertIn('refreshLanguageSelector', header)
        self.assertNotIn('🇷🇺', manager)

    def test_g3_rtl_and_language_persistence_contract(self):
        main = _source('gui/gui_main.py')
        handler = _source('gui/handler_ui.py')
        settings = _source('core/settings_manager.py')
        self.assertIn('_applySavedLanguage', main)
        self.assertIn('_applyLayoutDirection', main)
        self.assertIn("self.settings_manager.set('language', code)", handler)
        self.assertIn("'language': ''", settings)
        self.assertIn("translations.is_rtl()", main)

    def test_qt6_checkbox_has_explicit_checkmark_asset(self):
        styles = _source('gui/gui_components.py')
        self.assertIn('checkmark.svg', styles)
        self.assertIn('radio_dot.svg', styles)
        self.assertIn('QComboBox QAbstractItemView::item:hover', styles)
        self.assertIn('class ComboPopupDelegate', styles)
        self.assertIn('class StyledComboBox', styles)
        self.assertIn('def showPopup(self)', styles)
        self.assertIn('QSpinBox::up-button', styles)
        self.assertIn('QDoubleSpinBox::down-arrow', styles)
        self.assertIn('spin_up.svg', styles)
        self.assertIn('spin_down.svg', styles)
        self.assertIn('HighlightedText', styles)
        self.assertIn('url("__CHECKMARK__")', styles)
        self.assertIn('url("__RADIO_DOT__")', styles)
        self.assertTrue(os.path.isfile(os.path.join(
            ROOT, 'resources', 'checkmark.svg')))
        self.assertTrue(os.path.isfile(os.path.join(
            ROOT, 'resources', 'radio_dot.svg')))
        self.assertTrue(os.path.isfile(os.path.join(
            ROOT, 'resources', 'spin_up.svg')))
        self.assertTrue(os.path.isfile(os.path.join(
            ROOT, 'resources', 'spin_down.svg')))

    def test_support_title_is_wrap_safe(self):
        source = _source('gui/simple_donation.py')
        self.assertIn('self.title_label.setWordWrap(True)', source)
        self.assertIn('self.setMinimumSize(560, 420)', source)

    def test_code_page_popup_forces_item_foreground(self):
        source = _source('gui/gui_mkgmap_widgets.py')
        self.assertIn('ForegroundRole', source)
        self.assertIn('self.code_page_combo = StyledComboBox()', source)

    def test_scoped_gui_has_no_untranslated_cyrillic_literals(self):
        paths = ('gui/gui_handlers.py', 'gui/gui_main.py',
                 'gui/gui_widgets.py', 'gui/gui_mkgmap_widgets.py',
                 'gui/simple_donation.py', 'gui/widget_i18n.py',
                 'gui/widget_header.py', 'gui/widget_selection.py',
                 'gui/widget_results.py', 'gui/handler_ui.py',
                 'gui/handler_download.py', 'gui/handler_mapping.py',
                 'gui/handler_compile.py', 'gui/handler_settings.py',
                 'core/export_worker.py')
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
