# -*- coding: utf-8 -*-
"""Офлайн-тесты жизненного цикла экспорта и run-manifest."""

import json
import os
import tempfile
import unittest

from _bootstrap import PACKAGE  # noqa: F401
from garmin_export.core.export_service import (
    ExportService, STATUS_CANCELLED, STATUS_FAILED, STATUS_SUCCESS,
)


class ExportServiceTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix='export_service_')
        self.settings = {
            'output_folder': self.tmp,
            'mkgmap_path': 'mkgmap-r4924/mkgmap.jar',
            'splitter_path': 'splitter-r654/splitter.jar',
            'java_path': 'java.exe',
            'token': 'must-not-be-written',
        }

    def test_success_manifest_has_output_and_no_raw_settings(self):
        output = os.path.join(self.tmp, 'map.img')
        with open(output, 'wb') as stream:
            stream.write(b'img')
        service = ExportService([{'id': 'layer-1', 'name': 'Roads'}],
                                self.settings)
        self.assertTrue(service.finish_success(output))
        path = service.write_manifest()
        with open(path, encoding='utf-8') as stream:
            manifest = json.load(stream)
        self.assertEqual(manifest['status'], STATUS_SUCCESS)
        self.assertEqual(manifest['output']['size'], 3)
        self.assertEqual(manifest['tool_versions']['mkgmap'], 'r4924')
        self.assertNotIn('token', json.dumps(manifest))

    def test_cancel_never_claims_output(self):
        service = ExportService([], self.settings)
        service.request_cancel()
        self.assertFalse(service.finish_success('map.img'))
        path = service.write_manifest()
        with open(path, encoding='utf-8') as stream:
            manifest = json.load(stream)
        self.assertEqual(manifest['status'], STATUS_CANCELLED)
        self.assertIsNone(manifest['output'])

    def test_failure_records_error_class(self):
        service = ExportService([], self.settings)
        service.finish_failure(ValueError('bad input'))
        manifest_path = os.path.join(self.tmp, 'manifest.json')
        service.write_manifest(manifest_path)
        with open(manifest_path, encoding='utf-8') as stream:
            manifest = json.load(stream)
        self.assertEqual(manifest['status'], STATUS_FAILED)
        self.assertEqual(manifest['error_class'], 'ValueError')

    def test_manifest_write_failure_is_non_fatal(self):
        service = ExportService([], self.settings)
        service.finish_failure(RuntimeError('x'))
        self.assertIsNone(service.write_manifest(self.tmp))
        self.assertIn(service.manifest_error,
                      ('IsADirectoryError', 'PermissionError'))


if __name__ == '__main__':
    unittest.main()
