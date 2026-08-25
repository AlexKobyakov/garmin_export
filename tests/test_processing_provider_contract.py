# -*- coding: utf-8 -*-
"""Offline contract guards for the G6 Processing provider boundary."""

import ast
import os


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _source(relative):
    with open(os.path.join(ROOT, relative), encoding='utf-8') as handle:
        return handle.read()


def test_provider_registers_exactly_seven_stable_algorithms():
    source = _source('processing_provider/provider.py')
    assert source.count('self.addAlgorithm(') == 7
    algorithms = (_source('processing_provider/algorithms.py') +
                  _source('processing_provider/extra_algorithms.py'))
    for algorithm_id in (
            'validate_environment', 'build_typ_mapping',
            'export_selected_layers', 'validate_typ_code_page',
            'generate_mp_preview', 'validate_mapping_json',
            'dependency_diagnostics_download'):
        assert "return '{0}'".format(algorithm_id) in algorithms


def test_processing_boundary_has_no_gui_side_effect_imports():
    for relative in ('processing_provider/provider.py',
                     'processing_provider/algorithms.py',
                     'processing_provider/runtime.py',
                     'processing_provider/extra_algorithms.py'):
        tree = ast.parse(_source(relative))
        imported = [node for node in ast.walk(tree)
                    if isinstance(node, (ast.Import, ast.ImportFrom))]
        imported_names = ' '.join(ast.unparse(node) for node in imported)
        assert 'QMessageBox' not in imported_names
        assert 'QWidget' not in imported_names
        assert 'qgis.PyQt.QtWidgets' not in imported_names


def test_processing_algorithms_use_feedback_and_stable_parameter_keys():
    source = _source('processing_provider/algorithms.py')
    for token in ('feedback.isCanceled', 'feedback.setProgress',
                  'QgsProcessingException', 'LAYERS', 'MKGMP', 'OUTPUT',
                  'AUTO_DOWNLOAD', 'ensure_tool', 'TYP_MODE', 'TYP_FILE',
                  'ENABLED_LEVELS', 'typ_file_path', 'DRAW_PRIORITY',
                  'MKGMAP_LOGGING', 'EXTRA_ARGS', 'MANIFEST'):
        assert token in source


def test_processing_provider_registration_is_duplicate_safe():
    source = _source('garmin_exporter.py')
    assert "providerById('garmin_export')" in source
    assert 'registry.addProvider(provider)' in source
    assert 'registry.removeProvider(provider.id())' in source


def test_g6_production_files_stay_within_size_rule():
    for relative in ('processing_provider/__init__.py',
                     'processing_provider/provider.py',
                     'processing_provider/algorithms.py',
                     'processing_provider/runtime.py',
                     'processing_provider/extra_algorithms.py'):
        assert len(_source(relative).splitlines()) <= 500


def test_processing_provider_is_declared_in_metadata():
    assert 'hasProcessingProvider=yes' in _source('metadata.txt')


def test_runtime_reuses_the_ui_downloader_contract():
    source = _source('processing_provider/runtime.py')
    assert 'discover_tool' in source
    assert 'downloader.download_tool' in source
    assert 'validate_tool_installation' in source
    assert 'cancelled_callback=feedback.isCanceled' in source
    assert 'translations.get_current_language()' in source


def test_processing_export_exposes_styling_and_level_controls():
    source = _source('processing_provider/algorithms.py')
    for token in ('QgsProcessingParameterEnum',
                  'Generate from layer styles',
                  'Use existing TYP/TXT file',
                  'Garmin default (no TYP)',
                  'levels_invalid'):
        assert token in source


def test_author_dialog_refreshes_metadata_from_metadata_file():
    dialog = _source('gui/gui_dialogs.py')
    exporter = _source('garmin_exporter.py')
    for token in ('metadata_label', 'get_plugin_info()', 'metadata_details',
                  'QFileSystemWatcher', '_metadata_changed', 'changelog'):
        assert token in dialog
    for token in ('qgis_minimum', 'qgis_maximum', 'has_processing_provider',
                  'repository', 'tags', 'changelog'):
        assert token in exporter


def test_processing_optional_flags_support_qgis3_and_qgis4():
    source = _source('processing_provider/algorithms.py')
    assert 'ProcessingParameterFlag' in source
    assert 'FlagOptional' in source
    assert 'setOptional' not in source


def test_processing_follow_up_algorithms_have_stable_contracts():
    source = _source('processing_provider/extra_algorithms.py')
    for token in ('validate_typ_code_page', 'generate_mp_preview',
                  'CODE_PAGE_STATUS', 'TYP_STATUS', 'MPGenerator',
                  'validate_mapping_json', 'dependency_diagnostics_download',
                  'AUTO_DOWNLOAD', 'tool_manifest', 'feedback.isCanceled'):
        assert token in source
