# -*- coding: utf-8 -*-
"""Stable Garmin Export Processing algorithms.

The provider is deliberately independent from the dialog.  Processing owns
parameters, feedback, cancellation and output paths; the existing export
worker remains the single implementation of the full IMG workflow.
"""

import os

from qgis.core import (
    QgsProcessing, QgsProcessingAlgorithm, QgsProcessingException,
    QgsProcessingParameterBoolean, QgsProcessingParameterFile,
    QgsProcessingParameterFileDestination, QgsProcessingParameterMultipleLayers,
    QgsProcessingParameterNumber, QgsProcessingParameterString,
    QgsProcessingOutputString,
)

from ..core.export_worker import ExportWorker
from ..core.layer_manager import LayerManager
from ..core.mkgmap_compiler import MkgmapCompiler, java_diagnostics
from ..core.style_mapper import StyleMapper
from ..core import typ_generator
from ..qgis_compat import qgis_enum


def _number(owner, name, description, default, minimum=0):
    kind = qgis_enum('ProcessingNumberParameterType', 'Integer', owner)
    return QgsProcessingParameterNumber(
        name, description, kind, defaultValue=default, minValue=minimum)


def _optional_file(name, description):
    parameter = QgsProcessingParameterFile(name, description)
    parameter.setIsDynamic(False)
    parameter.setOptional(True)
    return parameter


def _vector_type():
    return qgis_enum(
        'ProcessingSourceType', 'VectorAnyGeometry',
        QgsProcessing, 'TypeVectorAnyGeometry')


class _BaseAlgorithm(QgsProcessingAlgorithm):
    """Shared labels and machine-stable Processing group."""

    def group(self):
        return 'Garmin Export'

    def groupId(self):
        return 'garmin_export'

    def shortHelpString(self):
        return 'Garmin Export Processing workflow; paths and IDs are stable.'


class ValidateEnvironmentAlgorithm(_BaseAlgorithm):
    """Validate Java and the complete mkgmap/splitter distributions."""

    def name(self):
        return 'validate_environment'

    def displayName(self):
        return 'Validate Garmin environment'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterFile(
            'MKGMP', 'mkgmap.jar (with adjacent lib directory)'))
        self.addParameter(_optional_file('SPLITTER',
                                         'splitter.jar (with adjacent lib)'))
        self.addParameter(_optional_file('JAVA', 'Java executable'))
        self.addParameter(QgsProcessingParameterString(
            'MIN_JAVA', 'Minimum Java major version', defaultValue='8'))
        self.addOutput(QgsProcessingOutputString('STATUS', 'Validation status'))

    def processAlgorithm(self, parameters, context, feedback):
        mkgmap = self.parameterAsFile(parameters, 'MKGMP', context)
        splitter = self.parameterAsFile(parameters, 'SPLITTER', context)
        java = self.parameterAsFile(parameters, 'JAVA', context)
        if not mkgmap or not MkgmapCompiler().validate_tool_installation(
                mkgmap, 'mkgmap'):
            raise QgsProcessingException('mkgmap_invalid')
        if splitter and not MkgmapCompiler().validate_tool_installation(
                splitter, 'splitter'):
            raise QgsProcessingException('splitter_invalid')
        try:
            minimum = int(self.parameterAsString(parameters, 'MIN_JAVA', context) or 8)
        except ValueError:
            raise QgsProcessingException('java_minimum_invalid')
        diagnostics = java_diagnostics(java or None, min_major=minimum)
        if not diagnostics.get('ok'):
            raise QgsProcessingException('java_{0}'.format(diagnostics.get('code')))
        feedback.pushInfo('mkgmap, splitter and Java environment are valid')
        feedback.setProgress(100)
        return {'STATUS': 'ok'}

    def createInstance(self):
        return ValidateEnvironmentAlgorithm()


class BuildTypMappingAlgorithm(_BaseAlgorithm):
    """Create a TYP file from selected layer symbology."""

    def name(self):
        return 'build_typ_mapping'

    def displayName(self):
        return 'Build TYP mapping from layers'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterMultipleLayers(
            'LAYERS', 'Vector layers', _vector_type()))
        self.addParameter(_number(QgsProcessingParameterNumber, 'FID',
                                  'Family ID', 1234, 1))
        self.addParameter(_number(QgsProcessingParameterNumber, 'PRODUCT_ID',
                                  'Product ID', 1, 1))
        self.addParameter(QgsProcessingParameterString(
            'CODE_PAGE', 'Code page', defaultValue='1252'))
        self.addParameter(QgsProcessingParameterFileDestination(
            'OUTPUT', 'TYP output', 'Text files (*.txt);;All files (*.*)'))

    def processAlgorithm(self, parameters, context, feedback):
        layers = self.parameterAsLayerList(parameters, 'LAYERS', context)
        if not layers:
            raise QgsProcessingException('layers_empty')
        mapper = StyleMapper()
        entries = []
        for index, layer in enumerate(layers):
            if feedback.isCanceled():
                raise QgsProcessingException('cancelled')
            geometry = LayerManager.get_geometry_type(layer)
            if geometry == 'Unknown':
                raise QgsProcessingException('geometry_unsupported')
            mapping = mapper.get_layer_mapping(layer.name(), geometry)
            entries.append({
                'layer': layer,
                'name': layer.name(),
                'geometry_type': geometry,
                'garmin_type': mapping.get('type', '0x01'),
            })
            feedback.setProgress((index + 1) * 80.0 / len(layers))
        text = typ_generator.build_typ_from_layers(
            entries,
            self.parameterAsInt(parameters, 'FID', context),
            self.parameterAsInt(parameters, 'PRODUCT_ID', context),
            self.parameterAsString(parameters, 'CODE_PAGE', context) or '1252')
        output = self.parameterAsFileOutput(parameters, 'OUTPUT', context)
        if not output:
            raise QgsProcessingException('output_missing')
        try:
            with open(output, 'w', encoding='utf-8') as handle:
                handle.write(text)
        except OSError as exc:
            raise QgsProcessingException('output_write_failed: {0}'.format(exc))
        feedback.setProgress(100)
        return {'OUTPUT': output}

    def createInstance(self):
        return BuildTypMappingAlgorithm()


class ExportSelectedLayersAlgorithm(_BaseAlgorithm):
    """Run the existing export worker synchronously through Processing feedback."""

    def name(self):
        return 'export_selected_layers'

    def displayName(self):
        return 'Export selected layers to Garmin IMG'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterMultipleLayers(
            'LAYERS', 'Vector layers', _vector_type()))
        self.addParameter(QgsProcessingParameterFile(
            'MKGMP', 'mkgmap.jar (with adjacent lib directory)'))
        self.addParameter(_optional_file('JAVA', 'Java executable'))
        self.addParameter(_number(QgsProcessingParameterNumber, 'FID',
                                  'Family ID', 1234, 1))
        self.addParameter(_number(QgsProcessingParameterNumber, 'MAP_ID',
                                  'Map ID', 1, 1))
        for name, label, default in (
                ('MAP_NAME', 'Map name', 'Garmin Map'),
                ('MAP_DESCRIPTION', 'Map description', ''),
                ('CODE_PAGE', 'Code page', '1252')):
            self.addParameter(QgsProcessingParameterString(
                name, label, defaultValue=default))
        self.addParameter(QgsProcessingParameterBoolean(
            'TRANSPARENT', 'Transparent map', defaultValue=False))
        self.addParameter(QgsProcessingParameterBoolean(
            'ROUTING', 'Enable routing', defaultValue=False))
        self.addParameter(QgsProcessingParameterFileDestination(
            'OUTPUT', 'IMG output', 'Garmin IMG (*.img);;All files (*.*)'))

    def processAlgorithm(self, parameters, context, feedback):
        layers = self.parameterAsLayerList(parameters, 'LAYERS', context)
        output = self.parameterAsFileOutput(parameters, 'OUTPUT', context)
        mkgmap = self.parameterAsFile(parameters, 'MKGMP', context)
        if not layers:
            raise QgsProcessingException('layers_empty')
        if not output:
            raise QgsProcessingException('output_missing')
        if not mkgmap:
            raise QgsProcessingException('mkgmap_missing')
        folder = os.path.dirname(output) or os.getcwd()
        os.makedirs(folder, exist_ok=True)
        selected = [{'id': layer.id(), 'name': layer.name()} for layer in layers]
        filename = os.path.splitext(os.path.basename(output))[0]
        settings = {
            'output_folder': folder,
            'output_filename': filename,
            'mkgmap_path': mkgmap,
            'java_path': self.parameterAsFile(parameters, 'JAVA', context),
            'family_id': self.parameterAsInt(parameters, 'FID', context),
            'map_id': self.parameterAsInt(parameters, 'MAP_ID', context),
            'map_name': self.parameterAsString(parameters, 'MAP_NAME', context),
            'map_description': self.parameterAsString(
                parameters, 'MAP_DESCRIPTION', context),
            'code_page': self.parameterAsString(parameters, 'CODE_PAGE', context),
            'transparent': self.parameterAsBool(parameters, 'TRANSPARENT', context),
            'routing': self.parameterAsBool(parameters, 'ROUTING', context),
            'enabled_levels': [0, 1, 2, 3],
            'typ_mode': 'generate',
        }
        worker = ExportWorker(selected, settings)
        result = {'success': False, 'path': '', 'error': ''}

        def progress(value, message):
            feedback.setProgress(value)
            feedback.pushInfo(str(message))
            if feedback.isCanceled():
                worker.stop()

        def log(message):
            feedback.pushInfo(str(message))
            if feedback.isCanceled():
                worker.stop()

        def finished(success, path):
            result.update(success=bool(success), path=path or '')

        def failed(message):
            result['error'] = str(message)

        worker.progress.connect(progress)
        worker.log_message.connect(log)
        worker.finished.connect(finished)
        worker.error.connect(failed)
        worker.run()
        if feedback.isCanceled() or not result['success']:
            raise QgsProcessingException(
                'cancelled' if feedback.isCanceled() else
                'export_failed: {0}'.format(result['error'] or 'unknown'))
        feedback.setProgress(100)
        return {'OUTPUT': result['path']}

    def createInstance(self):
        return ExportSelectedLayersAlgorithm()
