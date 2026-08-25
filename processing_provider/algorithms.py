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
    QgsProcessingParameterDefinition,
    QgsProcessingParameterFileDestination, QgsProcessingParameterMultipleLayers,
    QgsProcessingParameterNumber, QgsProcessingParameterString,
    QgsProcessingParameterEnum,
    QgsProcessingOutputString,
)

from ..core.export_worker import ExportWorker
from ..core.layer_manager import LayerManager
from ..core.mkgmap_compiler import java_diagnostics
from ..core.style_mapper import StyleMapper
from ..core.codepages import CODE_PAGE_CODES
from ..core import typ_generator
from ..qgis_compat import qgis_enum
from .runtime import ensure_tool


def _number(owner, name, description, default, minimum=0, integer=True):
    kind = qgis_enum(
        'ProcessingNumberParameterType', 'Integer' if integer else 'Double',
        owner)
    return QgsProcessingParameterNumber(
        name, description, kind, defaultValue=default, minValue=minimum)


def _optional(parameter):
    flag = qgis_enum(
        'ProcessingParameterFlag', 'Optional',
        QgsProcessingParameterDefinition, 'FlagOptional')
    parameter.setFlags(parameter.flags() | flag)
    return parameter


def _optional_file(name, description):
    parameter = QgsProcessingParameterFile(name, description)
    parameter.setIsDynamic(False)
    return _optional(parameter)


def _vector_type():
    return qgis_enum(
        'ProcessingSourceType', 'VectorAnyGeometry',
        QgsProcessing, 'TypeVectorAnyGeometry')


def _parse_levels(value):
    try:
        levels = sorted({
            int(item.strip()) for item in str(value or '').split(',')
            if item.strip()})
    except (TypeError, ValueError):
        raise QgsProcessingException('levels_invalid')
    if not levels or any(level < 0 or level > 7 for level in levels):
        raise QgsProcessingException('levels_invalid')
    return levels


def _validate_code_page(value):
    code_page = str(value or '').strip()
    if code_page not in CODE_PAGE_CODES:
        raise QgsProcessingException('code_page_invalid')
    return code_page


def _project_layers():
    return [entry['layer'] for entry in LayerManager.get_project_layers()
            if entry.get('layer') is not None]


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
        mkgmap = QgsProcessingParameterFile(
            'MKGMP', 'mkgmap.jar (with adjacent lib directory)')
        self.addParameter(_optional(mkgmap))
        self.addParameter(_optional_file('SPLITTER',
                                         'splitter.jar (with adjacent lib)'))
        self.addParameter(_optional_file('JAVA', 'Java executable'))
        self.addParameter(QgsProcessingParameterBoolean(
            'AUTO_DOWNLOAD', 'Download mkgmap when missing', defaultValue=False))
        self.addParameter(QgsProcessingParameterString(
            'MIN_JAVA', 'Minimum Java major version', defaultValue='8'))
        self.addOutput(QgsProcessingOutputString('STATUS', 'Validation status'))
        self.addOutput(QgsProcessingOutputString('MKGMP_PATH', 'mkgmap path'))
        self.addOutput(QgsProcessingOutputString('SPLITTER_PATH', 'splitter path'))
        self.addOutput(QgsProcessingOutputString('JAVA_PATH', 'Java path'))
        self.addOutput(QgsProcessingOutputString(
            'MKGMP_STATUS', 'mkgmap status'))
        self.addOutput(QgsProcessingOutputString(
            'SPLITTER_STATUS', 'splitter status'))
        self.addOutput(QgsProcessingOutputString('JAVA_STATUS', 'Java status'))

    def processAlgorithm(self, parameters, context, feedback):
        mkgmap = self.parameterAsFile(parameters, 'MKGMP', context)
        splitter = self.parameterAsFile(parameters, 'SPLITTER', context)
        java = self.parameterAsFile(parameters, 'JAVA', context)
        auto_download = self.parameterAsBool(
            parameters, 'AUTO_DOWNLOAD', context)
        try:
            mkgmap = ensure_tool(
                'mkgmap', mkgmap, auto_download, feedback, start=0, span=45)
            if splitter:
                splitter = ensure_tool(
                    'splitter', splitter, auto_download, feedback,
                    start=45, span=25)
        except ValueError as exc:
            raise QgsProcessingException(str(exc))
        try:
            minimum = int(self.parameterAsString(parameters, 'MIN_JAVA', context) or 8)
        except ValueError:
            raise QgsProcessingException('java_minimum_invalid')
        diagnostics = java_diagnostics(java or None, min_major=minimum)
        if not diagnostics.get('ok'):
            raise QgsProcessingException('java_{0}'.format(diagnostics.get('code')))
        splitter_status = 'not_requested'
        if splitter:
            splitter_status = 'valid'
        feedback.pushInfo('mkgmap, splitter and Java environment are valid')
        feedback.setProgress(100)
        return {
            'STATUS': 'ok',
            'MKGMP_PATH': mkgmap,
            'SPLITTER_PATH': splitter or '',
            'JAVA_PATH': diagnostics.get('path') or '',
            'MKGMP_STATUS': 'valid',
            'SPLITTER_STATUS': splitter_status,
            'JAVA_STATUS': 'valid',
        }

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
        code_page = _validate_code_page(
            self.parameterAsString(parameters, 'CODE_PAGE', context) or '1252')
        text = typ_generator.build_typ_from_layers(
            entries,
            self.parameterAsInt(parameters, 'FID', context),
            self.parameterAsInt(parameters, 'PRODUCT_ID', context),
            code_page)
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
        layers_parameter = QgsProcessingParameterMultipleLayers(
            'LAYERS', 'Vector layers', _vector_type())
        self.addParameter(_optional(layers_parameter))
        self.addParameter(QgsProcessingParameterBoolean(
            'USE_PROJECT_LAYERS', 'Use all valid project vector layers',
            defaultValue=False))
        mkgmap = QgsProcessingParameterFile(
            'MKGMP', 'mkgmap.jar (with adjacent lib directory)')
        self.addParameter(_optional(mkgmap))
        self.addParameter(_optional_file('JAVA', 'Java executable'))
        self.addParameter(QgsProcessingParameterBoolean(
            'AUTO_DOWNLOAD', 'Download mkgmap when missing', defaultValue=False))
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
        for name, label, default in (
                ('INDEX', 'Enable address index', False),
                ('ADD_POIS_TO_AREAS', 'Add POIs to areas', False),
                ('ORDER_BY_DECREASING_AREA', 'Order polygons by area', False),
                ('LOWER_CASE', 'Use lower-case labels', False),
                ('MKGMAP_LOGGING', 'Write mkgmap log', False),
                ('MKGMAP_VERBOSE', 'Verbose mkgmap log', False),
                ('KEEP_TEMP_FILES', 'Keep intermediate files', False)):
            self.addParameter(QgsProcessingParameterBoolean(
                name, label, defaultValue=default))
        self.addParameter(_number(
            QgsProcessingParameterNumber, 'DRAW_PRIORITY',
            'Draw priority', 25, 0))
        self.addParameter(_number(
            QgsProcessingParameterNumber, 'MIN_SIZE_POLYGON',
            'Minimum polygon size', 8, 0))
        self.addParameter(_number(
            QgsProcessingParameterNumber, 'MAX_JOBS',
            'Maximum mkgmap jobs (0=auto)', 0, 0))
        for name, label in (
                ('REDUCE_POINT_DENSITY', 'Reduce point density'),
                ('REDUCE_POINT_DENSITY_POLYGON',
                 'Reduce polygon point density')):
            self.addParameter(_number(
                QgsProcessingParameterNumber, name, label, 0.0, 0.0,
                integer=False))
        self.addParameter(_number(
            QgsProcessingParameterNumber, 'JAVA_HEAP_GB',
            'Java heap limit in GB (0=auto)', 0.0, 0.0, integer=False))
        self.addParameter(QgsProcessingParameterString(
            'EXTRA_ARGS', 'Additional mkgmap arguments', defaultValue=''))
        self.addParameter(QgsProcessingParameterEnum(
            'TYP_MODE', 'TYP styling',
            options=['Generate from layer styles',
                     'Use existing TYP/TXT file',
                     'Garmin default (no TYP)'],
            defaultValue=0))
        self.addParameter(_optional_file(
            'TYP_FILE', 'Existing TYP/TXT file (for TYP_MODE=1)'))
        self.addParameter(QgsProcessingParameterString(
            'ENABLED_LEVELS', 'Enabled levels (comma-separated)',
            defaultValue='0,1,2,3'))
        self.addParameter(QgsProcessingParameterFileDestination(
            'OUTPUT', 'IMG output', 'Garmin IMG (*.img);;All files (*.*)'))
        self.addOutput(QgsProcessingOutputString(
            'MANIFEST', 'Redacted run manifest path'))

    def processAlgorithm(self, parameters, context, feedback):
        layers = self.parameterAsLayerList(parameters, 'LAYERS', context)
        if self.parameterAsBool(parameters, 'USE_PROJECT_LAYERS', context):
            layers = _project_layers()
        output = self.parameterAsFileOutput(parameters, 'OUTPUT', context)
        mkgmap = self.parameterAsFile(parameters, 'MKGMP', context)
        if not layers:
            raise QgsProcessingException('layers_empty')
        if not output:
            raise QgsProcessingException('output_missing')
        auto_download = self.parameterAsBool(
            parameters, 'AUTO_DOWNLOAD', context)
        try:
            mkgmap = ensure_tool(
                'mkgmap', mkgmap, auto_download, feedback, start=0, span=25)
        except ValueError as exc:
            raise QgsProcessingException(str(exc))
        typ_mode_index = self.parameterAsInt(parameters, 'TYP_MODE', context)
        typ_modes = ('generate', 'file', 'none')
        if typ_mode_index not in range(len(typ_modes)):
            raise QgsProcessingException('typ_mode_invalid')
        typ_file = self.parameterAsFile(parameters, 'TYP_FILE', context)
        if typ_modes[typ_mode_index] == 'file' and (
                not typ_file or not os.path.isfile(typ_file)):
            raise QgsProcessingException('typ_file_missing')
        code_page = _validate_code_page(
            self.parameterAsString(parameters, 'CODE_PAGE', context) or '1252')
        enabled_levels = _parse_levels(
            self.parameterAsString(parameters, 'ENABLED_LEVELS', context)
            or '0,1,2,3')
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
            'code_page': code_page,
            'transparent': self.parameterAsBool(parameters, 'TRANSPARENT', context),
            'routing': self.parameterAsBool(parameters, 'ROUTING', context),
            'mkgmap_logging': self.parameterAsBool(
                parameters, 'MKGMAP_LOGGING', context),
            'mkgmap_verbose': self.parameterAsBool(
                parameters, 'MKGMAP_VERBOSE', context),
            'keep_temp_files': self.parameterAsBool(
                parameters, 'KEEP_TEMP_FILES', context),
            'enabled_levels': enabled_levels,
            'typ_mode': typ_modes[typ_mode_index],
            'typ_file_path': typ_file or '',
            'mkgmap_options': {
                'index': self.parameterAsBool(parameters, 'INDEX', context),
                'add_pois_to_areas': self.parameterAsBool(
                    parameters, 'ADD_POIS_TO_AREAS', context),
                'order_by_decreasing_area': self.parameterAsBool(
                    parameters, 'ORDER_BY_DECREASING_AREA', context),
                'lower_case': self.parameterAsBool(
                    parameters, 'LOWER_CASE', context),
                'draw_priority': self.parameterAsInt(
                    parameters, 'DRAW_PRIORITY', context),
                'min_size_polygon': self.parameterAsInt(
                    parameters, 'MIN_SIZE_POLYGON', context),
                'max_jobs': self.parameterAsInt(
                    parameters, 'MAX_JOBS', context),
                'reduce_point_density': self.parameterAsDouble(
                    parameters, 'REDUCE_POINT_DENSITY', context) or None,
                'reduce_point_density_polygon': self.parameterAsDouble(
                    parameters, 'REDUCE_POINT_DENSITY_POLYGON', context) or None,
                'java_xmx': self._java_heap(
                    parameters, context),
                'extra_args': self.parameterAsString(
                    parameters, 'EXTRA_ARGS', context),
            },
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
        manifest = os.path.join(
            folder, '.garmin_export', 'run_manifest.json')
        return {'OUTPUT': result['path'], 'MANIFEST': manifest}

    def _java_heap(self, parameters, context):
        value = self.parameterAsDouble(parameters, 'JAVA_HEAP_GB', context)
        return '{0:g}g'.format(value) if value > 0 else ''

    def createInstance(self):
        return ExportSelectedLayersAlgorithm()
