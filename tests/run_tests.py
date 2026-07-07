# -*- coding: utf-8 -*-
"""
Запуск всех офлайн-тестов ядра плагина (без QGIS/Qt).

Использование:
    python tests/run_tests.py
или из каталога tests:
    python run_tests.py
"""

import os
import sys
import unittest

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
if TESTS_DIR not in sys.path:
    sys.path.insert(0, TESTS_DIR)


def main():
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=TESTS_DIR, pattern='test_*.py')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(main())
