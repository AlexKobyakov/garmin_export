# -*- coding: utf-8 -*-
"""Тесты валидации jar-файлов и поиска Java."""

import os
import shutil
import tempfile
import unittest
import zipfile
from unittest.mock import patch

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

    def test_tool_installation_requires_lib_directory(self):
        path = _make_jar(['uk/me/parabola/splitter/Main.class'])
        lib_dir = os.path.join(os.path.dirname(path), 'lib')
        if os.path.isdir(lib_dir):
            shutil.rmtree(lib_dir)
        try:
            self.assertFalse(mkgmap_compiler.validate_tool_installation(
                path, 'splitter'))
            os.makedirs(lib_dir)
            self.assertTrue(mkgmap_compiler.validate_tool_installation(
                path, 'splitter'))
        finally:
            os.remove(path)
            if os.path.isdir(lib_dir):
                shutil.rmtree(lib_dir)

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

    def test_java_diagnostics_reports_missing_executable(self):
        result = mkgmap_compiler.java_diagnostics('C:/does/not/exist/java.exe')
        self.assertFalse(result['ok'])
        self.assertIn(result['code'], ('unreadable', 'not_found'))

    def test_java_heap_validation(self):
        self.assertTrue(mkgmap_compiler.validate_java_heap(0, 1))
        self.assertTrue(mkgmap_compiler.validate_java_heap(1, 2))
        self.assertFalse(mkgmap_compiler.validate_java_heap(3, 2))
        self.assertFalse(mkgmap_compiler.validate_java_heap(-1))

    def test_java_diagnostics_rejects_incompatible_major(self):
        with patch.object(mkgmap_compiler, 'find_java',
                          return_value='java.exe') as find_java_patch:
            with patch.object(
                    mkgmap_compiler, 'get_java_version',
                    return_value='java version "7.0.401"'):
                result = mkgmap_compiler.java_diagnostics()
        self.assertTrue(find_java_patch.called)
        self.assertFalse(result['ok'])
        self.assertEqual(result['code'], 'incompatible')
        self.assertEqual(result['major'], 7)


if __name__ == '__main__':
    unittest.main()
