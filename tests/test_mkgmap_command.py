# -*- coding: utf-8 -*-
"""Тесты построителя командной строки mkgmap."""

import unittest

from _bootstrap import PACKAGE  # noqa: F401
from garmin_export.core import mkgmap_command


class BuildCommandTest(unittest.TestCase):

    def _build(self, options=None, inputs=None):
        return mkgmap_command.build_command(
            'java', '/path/mkgmap.jar',
            options or {}, inputs or ['map.mp'])

    def test_java_options_before_jar(self):
        cmd = self._build({'java_xmx': '4g'}, ['map.mp'])
        jar_index = cmd.index('-jar')
        xmx_index = cmd.index('-Xmx4g')
        self.assertLess(xmx_index, jar_index)

    def test_jar_path_present(self):
        cmd = self._build()
        self.assertEqual(cmd[cmd.index('-jar') + 1], '/path/mkgmap.jar')

    def test_input_file_is_last(self):
        cmd = self._build(inputs=['map.mp'])
        self.assertEqual(cmd[-1], 'map.mp')

    def test_typ_after_mp(self):
        cmd = self._build(inputs=['map.mp', 'style.txt'])
        self.assertEqual(cmd[-2], 'map.mp')
        self.assertEqual(cmd[-1], 'style.txt')

    def test_gmapsupp_default(self):
        cmd = self._build()
        self.assertIn('--gmapsupp', cmd)

    def test_family_id(self):
        cmd = self._build({'family_id': 5555})
        self.assertIn('--family-id=5555', cmd)

    def test_unicode_code_page(self):
        cmd = self._build({'code_page': '65001'})
        self.assertIn('--unicode', cmd)
        self.assertFalse(any(a.startswith('--code-page') for a in cmd))

    def test_code_page_1251(self):
        cmd = self._build({'code_page': '1251'})
        self.assertIn('--code-page=1251', cmd)

    def test_route_option(self):
        cmd = self._build({'route': True})
        self.assertIn('--route', cmd)
        self.assertNotIn('--net', cmd)

    def test_net_without_route(self):
        cmd = self._build({'route': False, 'net': True})
        self.assertIn('--net', cmd)

    def test_transparent(self):
        cmd = self._build({'transparent': True})
        self.assertIn('--transparent', cmd)

    def test_draw_priority_only_when_non_default(self):
        self.assertNotIn('--draw-priority=25', self._build({'draw_priority': 25}))
        self.assertIn('--draw-priority=50', self._build({'draw_priority': 50}))

    def test_max_jobs(self):
        self.assertIn('--max-jobs=4', self._build({'max_jobs': 4}))
        self.assertFalse(any(a.startswith('--max-jobs') for a in self._build({'max_jobs': 0})))

    def test_extra_args_split(self):
        cmd = self._build({'extra_args': '--generate-sea --housenumbers'})
        self.assertIn('--generate-sea', cmd)
        self.assertIn('--housenumbers', cmd)

    def test_output_dir(self):
        cmd = self._build({'output_dir': '/out'})
        self.assertIn('--output-dir=/out', cmd)

    def test_options_before_inputs(self):
        cmd = self._build({'family_id': 1234}, ['map.mp'])
        self.assertLess(cmd.index('--family-id=1234'), cmd.index('map.mp'))


class LoggingConfigTest(unittest.TestCase):

    def test_file_handler_pattern_forward_slashes(self):
        cfg = mkgmap_command.build_logging_config('C:\\out\\mkgmap.log')
        self.assertIn('java.util.logging.FileHandler.pattern=C:/out/mkgmap.log', cfg)

    def test_verbose_info_level(self):
        cfg = mkgmap_command.build_logging_config('/tmp/m.log', verbose=True)
        self.assertIn('uk.me.parabola.mkgmap.build.level=INFO', cfg)

    def test_non_verbose_warning_level(self):
        cfg = mkgmap_command.build_logging_config('/tmp/m.log', verbose=False)
        self.assertIn('uk.me.parabola.mkgmap.build.level=WARNING', cfg)

    def test_handlers_line(self):
        cfg = mkgmap_command.build_logging_config('/tmp/m.log')
        self.assertIn('handlers:', cfg)
        self.assertIn('FileHandler', cfg)


if __name__ == '__main__':
    unittest.main()
