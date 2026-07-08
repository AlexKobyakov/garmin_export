# -*- coding: utf-8 -*-
"""Тесты валидации jar-файлов и поиска Java."""

import io
import os
import tempfile
import unittest
import zipfile

from _bootstrap import PACKAGE  # noqa: F401
from garmin_export.core import mkgmap_compiler


def _make_jar(entries):
    """Создаёт временный jar (zip) с указанными путями внутри"""
    fd, path = tempfile.mkstemp(suffix='.jar')
    os.close(fd)
    with zipfile.ZipFile(path, 'w') as z:
        for name in entries:
            z.writestr(name, b'x')
    return path


class ValidateJarTest(unittest.TestCase):

    def test_valid_mkgmap(self):
        path = _make_jar(['uk/me/parabola/mkgmap/main/Main.class'])
        try:
            self.assertTrue(mkgmap_compiler.validate_mkgmap_jar(path))
        finally:
            os.remove(path)

    def test_valid_splitter(self):
        path = _make_jar(['uk/me/parabola/splitter/Main.class'])
        try:
            self.assertTrue(mkgmap_compiler.validate_splitter_jar(path))
        finally:
            os.remove(path)

    def test_mkgmap_rejects_splitter(self):
        path = _make_jar(['uk/me/parabola/splitter/Main.class'])
        try:
            self.assertFalse(mkgmap_compiler.validate_mkgmap_jar(path))
        finally:
            os.remove(path)

    def test_not_a_jar_extension(self):
        fd, path = tempfile.mkstemp(suffix='.txt')
        os.close(fd)
        try:
            self.assertFalse(mkgmap_compiler.validate_mkgmap_jar(path))
        finally:
            os.remove(path)

    def test_part_file_valid_without_extension_check(self):
        # Промежуточный файл загрузки *.jar.part должен проходить проверку
        # содержимого при check_extension=False (регрессия: скачивание)
        path = _make_jar(['uk/me/parabola/mkgmap/main/Main.class'])
        part_path = path + '.part'
        os.rename(path, part_path)
        try:
            self.assertFalse(
                mkgmap_compiler.validate_jar(
                    part_path, 'uk/me/parabola/mkgmap'))
            self.assertTrue(
                mkgmap_compiler.validate_jar(
                    part_path, 'uk/me/parabola/mkgmap', check_extension=False))
        finally:
            os.remove(part_path)

    def test_missing_file(self):
        self.assertFalse(mkgmap_compiler.validate_mkgmap_jar('/no/such/file.jar'))

    def test_corrupt_zip(self):
        fd, path = tempfile.mkstemp(suffix='.jar')
        os.write(fd, b'not a zip file')
        os.close(fd)
        try:
            self.assertFalse(mkgmap_compiler.validate_mkgmap_jar(path))
        finally:
            os.remove(path)


class FindJavaTest(unittest.TestCase):

    def test_find_java_returns_str_or_none(self):
        # На тестовой машине Java может быть или не быть - проверяем тип
        result = mkgmap_compiler.find_java()
        self.assertTrue(result is None or isinstance(result, str))


if __name__ == '__main__':
    unittest.main()
