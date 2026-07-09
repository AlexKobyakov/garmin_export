# -*- coding: utf-8 -*-
"""Тесты логики скачивания и распаковки zip-архивов mkgmap/splitter."""

import io
import os
import tempfile
import unittest
import zipfile

from _bootstrap import PACKAGE  # noqa: F401
from garmin_export.core import downloader


def _make_inner_jar(class_prefix):
    """Синтетический jar (zip) с классом нужного пакета"""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w') as z:
        z.writestr('META-INF/MANIFEST.MF', 'Manifest-Version: 1.0\n')
        z.writestr(class_prefix + '/main/Main.class', b'\xca\xfe\xba\xbe')
    return buf.getvalue()


def _make_archive(tool='mkgmap', version='9999'):
    """Синтетический дистрибутив: <name>/main.jar + <name>/lib/dep.jar"""
    config = downloader.TOOLS[tool]
    main = config['main_jar_name']
    prefix = config['jar_class_prefix']
    root = '{0}-r{1}'.format(tool, version)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w') as z:
        z.writestr(root + '/', b'')
        z.writestr(root + '/' + main, _make_inner_jar(prefix))
        z.writestr(root + '/lib/', b'')
        z.writestr(root + '/lib/osmpbf-1.3.3.jar', _make_inner_jar('crosby/binary'))
        z.writestr(root + '/README', b'readme')
    return buf.getvalue(), root


class _FakeResponse:
    def __init__(self, data):
        self._buf = io.BytesIO(data)
        self.headers = {'Content-Length': str(len(data))}

    def read(self, size=-1):
        return self._buf.read() if size < 0 else self._buf.read(size)

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


class ParseVersionTest(unittest.TestCase):

    def test_parse_latest_mkgmap(self):
        html = 'mkgmap-r4920.zip mkgmap-r4924.zip mkgmap-r4919.jar'
        self.assertEqual(downloader.parse_latest_version(html, 'mkgmap'), 4924)

    def test_parse_latest_splitter(self):
        html = 'splitter-r650.zip splitter-r654.zip'
        self.assertEqual(downloader.parse_latest_version(html, 'splitter'), 654)

    def test_no_version(self):
        self.assertIsNone(downloader.parse_latest_version('nothing', 'mkgmap'))

    def test_latest_archive_url(self):
        html = 'mkgmap-r4924.zip'
        self.assertEqual(
            downloader.latest_archive_url(html, 'mkgmap'),
            'https://www.mkgmap.org.uk/download/mkgmap-r4924.zip')


class FilenameTest(unittest.TestCase):

    def test_zip_from_path(self):
        self.assertEqual(
            downloader.filename_from_url(
                'https://x/download/mkgmap-r4924.zip', 'def.zip'),
            'mkgmap-r4924.zip')

    def test_zip_from_query(self):
        url = 'https://downloader.disk.yandex.ru/disk/abc?filename=mkgmap-r4924.zip&x=1'
        self.assertEqual(
            downloader.filename_from_url(url, 'def.zip'),
            'mkgmap-r4924.zip')

    def test_jar_still_accepted(self):
        self.assertEqual(
            downloader.filename_from_url('https://x/mkgmap.jar', 'd.zip'),
            'mkgmap.jar')

    def test_fallback(self):
        self.assertEqual(
            downloader.filename_from_url('https://x/download/', 'def.zip'),
            'def.zip')


class CandidatesTest(unittest.TestCase):

    def test_first_candidate_uses_page_zip(self):
        def fake_opener(url, timeout=30):
            self.assertIn('mkgmap.html', url)
            return _FakeResponse(b'mkgmap-r4930.zip')

        candidates = downloader.build_download_candidates('mkgmap', fake_opener)
        url, filename = candidates[0]()
        self.assertEqual(
            url, 'https://www.mkgmap.org.uk/download/mkgmap-r4930.zip')
        self.assertEqual(filename, 'mkgmap-r4930.zip')

    def test_fallback_candidate_zip(self):
        candidates = downloader.build_download_candidates('splitter')
        url, filename = candidates[1]()
        self.assertTrue(url.endswith('splitter-r654.zip'))
        self.assertEqual(filename, 'splitter-r654.zip')

    def test_three_candidates(self):
        self.assertEqual(
            len(downloader.build_download_candidates('mkgmap')), 3)

    def test_yandex_url_is_zip_link(self):
        # Ссылки Яндекс.Диска обновлены на zip-архивы
        self.assertEqual(downloader.TOOLS['mkgmap']['yandex_public_url'],
                         'https://disk.yandex.ru/d/H39zRcOscXvDiw')
        self.assertEqual(downloader.TOOLS['splitter']['yandex_public_url'],
                         'https://disk.yandex.ru/d/h5kqHSN7CqYzLw')


class ArchiveValidationTest(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix='arc_test_')

    def _save(self, data, name='a.zip'):
        path = os.path.join(self.tmp, name)
        with open(path, 'wb') as f:
            f.write(data)
        return path

    def test_valid_archive(self):
        data, _ = _make_archive('mkgmap')
        path = self._save(data)
        self.assertTrue(downloader.validate_archive(
            path, 'mkgmap.jar', 'uk/me/parabola/mkgmap'))

    def test_archive_wrong_tool_rejected(self):
        data, _ = _make_archive('mkgmap')
        path = self._save(data)
        # splitter-проверка не должна принять mkgmap-архив
        self.assertFalse(downloader.validate_archive(
            path, 'splitter.jar', 'uk/me/parabola/splitter'))

    def test_not_a_zip(self):
        path = self._save(b'not a zip at all')
        self.assertFalse(downloader.validate_archive(
            path, 'mkgmap.jar', 'uk/me/parabola/mkgmap'))

    def test_find_main_jar_ignores_lib(self):
        names = ['mkgmap-r1/mkgmap.jar', 'mkgmap-r1/lib/osmpbf.jar',
                 'mkgmap-r1/lib/mkgmap.jar']
        member = downloader.find_main_jar_member(names, 'mkgmap.jar')
        self.assertEqual(member, 'mkgmap-r1/mkgmap.jar')


class ExtractArchiveTest(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix='ext_test_')

    def test_extract_returns_main_jar_with_lib(self):
        data, root = _make_archive('mkgmap', '9999')
        arc = os.path.join(self.tmp, 'mkgmap.zip')
        with open(arc, 'wb') as f:
            f.write(data)

        jar_path = downloader.extract_archive(arc, self.tmp, 'mkgmap.jar')
        self.assertTrue(os.path.isfile(jar_path))
        self.assertTrue(jar_path.endswith('mkgmap.jar'))
        # рядом с jar должна лежать папка lib/ с зависимостями
        lib_dir = os.path.join(os.path.dirname(jar_path), 'lib')
        self.assertTrue(os.path.isdir(lib_dir))
        self.assertTrue(os.path.isfile(
            os.path.join(lib_dir, 'osmpbf-1.3.3.jar')))

    def test_zip_slip_blocked(self):
        # архив с путём выхода за пределы каталога должен быть отклонён
        arc = os.path.join(self.tmp, 'evil.zip')
        with zipfile.ZipFile(arc, 'w') as z:
            z.writestr('mkgmap-r1/mkgmap.jar', _make_inner_jar('uk/me/parabola/mkgmap'))
            z.writestr('../evil.txt', b'pwned')
        with self.assertRaises(ValueError):
            downloader.extract_archive(arc, self.tmp, 'mkgmap.jar')


class DownloadToolEndToEndTest(unittest.TestCase):
    """Полный сценарий: страница -> скачивание zip -> распаковка -> путь к jar"""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix='dl_e2e_')

    def test_download_and_extract(self):
        data, root = _make_archive('mkgmap', '4924')

        def fake_opener(url, timeout=30):
            if url.endswith('.html'):
                return _FakeResponse(b'mkgmap-r4924.zip')
            if url.endswith('.zip'):
                return _FakeResponse(data)
            raise AssertionError('unexpected url ' + url)

        statuses = []
        jar = downloader.download_tool(
            'mkgmap', self.tmp,
            progress_callback=lambda r, t, s: statuses.append(s) if s else None,
            opener=fake_opener)

        self.assertTrue(os.path.isfile(jar))
        self.assertTrue(jar.endswith('mkgmap.jar'))
        self.assertIn(downloader.STATUS_EXTRACT, statuses)
        # архив тоже сохранён в каталоге
        self.assertTrue(os.path.isfile(os.path.join(self.tmp, 'mkgmap-r4924.zip')))


if __name__ == '__main__':
    unittest.main()
