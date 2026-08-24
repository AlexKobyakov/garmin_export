# -*- coding: utf-8 -*-
"""Offline contract guards for the G6 Processing provider boundary."""

import ast
import os


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _source(relative):
    with open(os.path.join(ROOT, relative), encoding='utf-8') as handle:
        return handle.read()


def test_provider_registers_exactly_three_stable_algorithms():
    source = _source('processing_provider/provider.py')
    assert source.count('self.addAlgorithm(') == 3
    algorithms = _source('processing_provider/algorithms.py')
    for algorithm_id in (
            'validate_environment', 'build_typ_mapping',
            'export_selected_layers'):
        assert "return '{0}'".format(algorithm_id) in algorithms


def test_processing_boundary_has_no_gui_side_effect_imports():
    for relative in ('processing_provider/provider.py',
                     'processing_provider/algorithms.py'):
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
                  'QgsProcessingException', 'LAYERS', 'MKGMP', 'OUTPUT'):
        assert token in source


def test_processing_provider_registration_is_duplicate_safe():
    source = _source('garmin_exporter.py')
    assert "providerById('garmin_export')" in source
    assert 'registry.addProvider(provider)' in source
    assert 'registry.removeProvider(provider.id())' in source


def test_g6_production_files_stay_within_size_rule():
    for relative in ('processing_provider/__init__.py',
                     'processing_provider/provider.py',
                     'processing_provider/algorithms.py'):
        assert len(_source(relative).splitlines()) <= 500


def test_processing_provider_is_declared_in_metadata():
    assert 'hasProcessingProvider=yes' in _source('metadata.txt')
