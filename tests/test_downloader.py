# -*- coding: utf-8 -*-
"""Тесты логики скачивания mkgmap/splitter."""

import io
import unittest

from _bootstrap import PACKAGE  # noqa: F401
from garmin_export.core import downloader


class ParseVersionTest(unittest.TestCase):

    def test_parse_latest_mkgmap(self):
        html = 'mkgmap-r4920.zip mkgmap-r4924.jar mkgmap-r4919.jar'
        self.assertEqual(downloader.parse_latest_version(html, 'mkgmap'), 4924)

    def test_parse_latest_splitter(self):
        html = 'splitter-r650.zip splitter-r654.jar'
        self.assertEqual(downloader.parse_latest_version(html, 'splitter'), 654)

    def test_no_version(self):
        self.assertIsNone(downloader.parse_latest_version('nothing here', 'mkgmap'))

    def test_latest_jar_url(self):
        html = 'mkgmap-r4924.jar'
        self.assertEqual(
            downloader.latest_jar_url(html, 'mkgmap'),
            'https://www.mkgmap.org.uk/download/mkgmap-r4924.jar')


class FilenameTest(unittest.TestCase):

    def test_from_path(self):
        self.assertEqual(
            downloader.filename_from_url(
                'https://x/download/mkgmap-r4924.jar', 'def.jar'),
            'mkgmap-r4924.jar')

    def test_from_query(self):
        url = 'https://downloader.disk.yandex.ru/disk/abc?filename=mkgmap-r4924.jar&x=1'
        self.assertEqual(
            downloader.filename_from_url(url, 'def.jar'),
            'mkgmap-r4924.jar')

    def test_fallback(self):
        self.assertEqual(
            downloader.filename_from_url('https://x/download/', 'def.jar'),
            'def.jar')


class CandidatesTest(unittest.TestCase):

    def test_first_candidate_uses_page(self):
        def fake_opener(url, timeout=30):
            self.assertIn('mkgmap.html', url)
            return io.BytesIO(b'mkgmap-r4930.jar')

        candidates = downloader.build_download_candidates('mkgmap', fake_opener)
        url, filename = candidates[0]()
        self.assertEqual(
            url, 'https://www.mkgmap.org.uk/download/mkgmap-r4930.jar')
        self.assertEqual(filename, 'mkgmap-r4930.jar')

    def test_fallback_candidate(self):
        candidates = downloader.build_download_candidates('splitter')
        url, filename = candidates[1]()
        self.assertIn('splitter-r654.jar', url)
        self.assertEqual(filename, 'splitter-r654.jar')

    def test_three_candidates(self):
        self.assertEqual(
            len(downloader.build_download_candidates('mkgmap')), 3)


if __name__ == '__main__':
    unittest.main()
