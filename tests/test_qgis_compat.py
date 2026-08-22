# -*- coding: utf-8 -*-
"""Static guards for the QGIS 3/4 and Qt5/Qt6 compatibility boundary."""

import os
import re
import unittest

from _bootstrap import PACKAGE  # noqa: F401


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEGACY_OVERSIZED = {
    # These files predate G1 and are bounded G2 decomposition debt.
    'gui/gui_handlers.py': 717,
    'gui/gui_widgets.py': 633,
}


def _python_files():
    for folder, _dirs, names in os.walk(ROOT):
        if os.path.basename(folder) in ('.git', '__pycache__'):
            continue
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
                    lines, 500, '{0} exceeds the 500-line module limit'.format(path))

    def test_legacy_oversized_files_are_explicit_decomposition_debt(self):
        actual = {_key(path) for path in _python_files()
                  if len(_source(path).splitlines()) > 500}
        self.assertEqual(actual, set(LEGACY_OVERSIZED))


if __name__ == '__main__':
    unittest.main()
