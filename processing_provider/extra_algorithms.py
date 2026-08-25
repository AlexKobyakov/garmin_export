# -*- coding: utf-8 -*-
"""Bounded Processing algorithms that do not invoke mkgmap."""

import json

from qgis.core import (
    QgsProcessingParameterBoolean, QgsProcessingParameterEnum,
    QgsProcessingParameterFileDestination, QgsProcessingParameterMultipleLayers,
    QgsProcessingParameterString, QgsProcessingOutputString,
    QgsProcessingException,
)

from ..core.layer_processor import LayerProcessor
from ..core.mp_generator import MPGenerator
from ..core.style_mapper import StyleMapper
from .algorithms import (
    _BaseAlgorithm, _optional, _optional_file, _parse_levels,
    _project_layers, _validate_code_page, _vector_type,
)
from .runtime import discover_tool, ensure_tool
from ..core.downloader import tool_manifest


class ValidateTypCodePageAlgorithm(_BaseAlgorithm):
    """Validate a Garmin code page and an optional TYP/TXT file."""

    def name(self):
        return 'validate_typ_code_page'

    def displayName(self):
        return 'Validate TYP and code page'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterString(
            'CODE_PAGE', 'Code page', defaultValue='1252'))
        self.addParameter(_optional_file('TYP_FILE', 'TYP/TXT file'))
        self.addParameter(QgsProcessingParameterBoolean(
            'REQUIRE_TYP', 'Require a TYP file', defaultValue=False))
        self.addOutput(QgsProcessingOutputString(
            'CODE_PAGE_STATUS', 'Code page status'))
        self.addOutput(QgsProcessingOutputString(
            'TYP_STATUS', 'TYP status'))

    def processAlgorithm(self, parameters, context, feedback):
        code_page = _validate_code_page(
            self.parameterAsString(parameters, 'CODE_PAGE', context) or '1252')
        typ_path = self.parameterAsFile(parameters, 'TYP_FILE', context)
        required = self.parameterAsBool(parameters, 'REQUIRE_TYP', context)
        if not typ_path:
            if required:
                raise QgsProcessingException('typ_file_missing')
            typ_status = 'not_requested'
        else:
            if not typ_path.lower().endswith(('.typ', '.txt')):
                raise QgsProcessingException('typ_file_extension_invalid')
            try:
                with open(typ_path, encoding='utf-8', errors='replace') as stream:
                    content = stream.read(4096)
            except OSError as exc:
                raise QgsProcessingException('typ_file_unreadable: {0}'.format(exc))
            if not content.strip() or '[' not in content:
                raise QgsProcessingException('typ_file_invalid')
            typ_status = 'valid'
        feedback.pushInfo('Code page {0} and TYP {1}'.format(
            code_page, typ_status))
        feedback.setProgress(100)
        return {
            'CODE_PAGE_STATUS': 'valid:{0}'.format(code_page),
            'TYP_STATUS': typ_status,
        }

    def createInstance(self):
        return ValidateTypCodePageAlgorithm()


class GenerateMpPreviewAlgorithm(_BaseAlgorithm):
    """Generate an MP preview without requiring Java or mkgmap."""

    def name(self):
        return 'generate_mp_preview'

    def displayName(self):
        return 'Generate MP preview'

    def initAlgorithm(self, config=None):
        layers = QgsProcessingParameterMultipleLayers(
            'LAYERS', 'Vector layers', _vector_type())
        self.addParameter(_optional(layers))
        self.addParameter(QgsProcessingParameterBoolean(
            'USE_PROJECT_LAYERS', 'Use all valid project vector layers',
            defaultValue=False))
        self.addParameter(QgsProcessingParameterString(
            'MAP_NAME', 'Map name', defaultValue='Garmin Map'))
        self.addParameter(QgsProcessingParameterString(
            'MAP_DESCRIPTION', 'Map description', defaultValue=''))
        self.addParameter(QgsProcessingParameterString(
            'CODE_PAGE', 'Code page', defaultValue='1252'))
        self.addParameter(QgsProcessingParameterString(
            'ENABLED_LEVELS', 'Enabled levels (comma-separated)',
            defaultValue='0,1,2,3'))
        self.addParameter(QgsProcessingParameterFileDestination(
            'OUTPUT', 'MP output', 'Polish MP (*.mp);;All files (*.*)'))

    def processAlgorithm(self, parameters, context, feedback):
        layers = self.parameterAsLayerList(parameters, 'LAYERS', context)
        if self.parameterAsBool(parameters, 'USE_PROJECT_LAYERS', context):
            layers = _project_layers()
        if not layers:
            raise QgsProcessingException('layers_empty')
        code_page = _validate_code_page(
            self.parameterAsString(parameters, 'CODE_PAGE', context) or '1252')
        levels = _parse_levels(
            self.parameterAsString(parameters, 'ENABLED_LEVELS', context)
            or '0,1,2,3')
        output = self.parameterAsFileOutput(parameters, 'OUTPUT', context)
        if not output:
            raise QgsProcessingException('output_missing')
        processor = LayerProcessor()
        mapper = StyleMapper()
        processed = []
        for index, layer in enumerate(layers):
            if feedback.isCanceled():
                raise QgsProcessingException('cancelled')
            try:
                processed.append(processor.process_layer(
                    layer, mapper, levels,
                    log_callback=feedback.pushWarning))
            except Exception as exc:
                raise QgsProcessingException(
                    'layer_failed:{0}'.format(exc))
            feedback.setProgress((index + 1) * 80.0 / len(layers))
        try:
            MPGenerator().generate_mp_file(
                processed, output, {
                    'map_id': 1,
                    'map_name': self.parameterAsString(
                        parameters, 'MAP_NAME', context),
                    'map_description': self.parameterAsString(
                        parameters, 'MAP_DESCRIPTION', context),
                    'code_page': code_page,
                    'enabled_levels': levels,
                    'transparent': False,
                    'routing': False,
                })
        except OSError as exc:
            raise QgsProcessingException('output_write_failed: {0}'.format(exc))
        feedback.setProgress(100)
        return {'OUTPUT': output}

    def createInstance(self):
        return GenerateMpPreviewAlgorithm()


class ValidateMappingJsonAlgorithm(_BaseAlgorithm):
    """Validate the mapping JSON used by the export worker."""

    def name(self):
        return 'validate_mapping_json'

    def displayName(self):
        return 'Validate mapping JSON'

    def initAlgorithm(self, config=None):
        self.addParameter(_optional_file(
            'MAPPING_FILE', 'Mapping JSON file'))
        self.addParameter(_optional(QgsProcessingParameterString(
            'MAPPING_JSON', 'Mapping JSON text', defaultValue='')))
        self.addOutput(QgsProcessingOutputString('STATUS', 'Mapping status'))
        self.addOutput(QgsProcessingOutputString(
            'ENTRY_COUNT', 'Mapping entry count'))
        self.addOutput(QgsProcessingOutputString('ERRORS', 'Validation errors'))

    @staticmethod
    def _validate(data):
        errors = []
        if not isinstance(data, dict):
            return ['root must be an object']
        layers = data.get('layers')
        if not isinstance(layers, dict) or not layers:
            return ['layers must be a non-empty object']
        geometries = {'Point', 'POI', 'point', 'LineString', 'Line',
                      'Polyline', 'line', 'Polygon', 'Area', 'polygon', 'area'}
        for name, mapping in layers.items():
            if not isinstance(name, str) or not name.strip():
                errors.append('layer name must be non-empty')
                continue
            if not isinstance(mapping, dict):
                errors.append('{0}: mapping must be an object'.format(name))
                continue
            if mapping.get('geometry') not in geometries:
                errors.append('{0}: invalid geometry'.format(name))
            type_value = mapping.get('type')
            try:
                if not isinstance(type_value, str) or not type_value.lower().startswith('0x'):
                    raise ValueError
                value = int(type_value, 16)
                if value < 0 or value > 0xffff:
                    raise ValueError
            except (TypeError, ValueError):
                errors.append('{0}: invalid Garmin type'.format(name))
            if 'level' in mapping:
                try:
                    level = int(mapping['level'])
                    if level < 0 or level > 7:
                        raise ValueError
                except (TypeError, ValueError):
                    errors.append('{0}: invalid level'.format(name))
        return errors

    def processAlgorithm(self, parameters, context, feedback):
        file_path = self.parameterAsFile(parameters, 'MAPPING_FILE', context)
        text = self.parameterAsString(parameters, 'MAPPING_JSON', context) or ''
        if file_path:
            try:
                with open(file_path, encoding='utf-8') as stream:
                    text = stream.read()
            except OSError as exc:
                raise QgsProcessingException(
                    'mapping_file_unreadable: {0}'.format(exc))
        if not text.strip():
            raise QgsProcessingException('mapping_input_missing')
        try:
            data = json.loads(text)
        except json.JSONDecodeError as exc:
            raise QgsProcessingException(
                'mapping_json_invalid:{0}'.format(exc))
        errors = self._validate(data)
        if errors:
            raise QgsProcessingException('mapping_invalid:' + '; '.join(errors))
        feedback.setProgress(100)
        return {
            'STATUS': 'valid',
            'ENTRY_COUNT': str(len(data['layers'])),
            'ERRORS': '',
        }

    def createInstance(self):
        return ValidateMappingJsonAlgorithm()


class DependencyDiagnosticsDownloadAlgorithm(_BaseAlgorithm):
    """Diagnose or explicitly install one complete Java tool distribution."""

    def name(self):
        return 'dependency_diagnostics_download'

    def displayName(self):
        return 'Diagnose/download Garmin dependency'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterEnum(
            'TOOL', 'Tool', options=['mkgmap', 'splitter'], defaultValue=0))
        self.addParameter(_optional_file('JAR_PATH', 'Existing tool JAR'))
        self.addParameter(QgsProcessingParameterBoolean(
            'AUTO_DOWNLOAD', 'Download when missing', defaultValue=False))
        self.addOutput(QgsProcessingOutputString('STATUS', 'Dependency status'))
        self.addOutput(QgsProcessingOutputString('PATH', 'Resolved JAR path'))
        self.addOutput(QgsProcessingOutputString('DETAILS', 'Dependency details'))

    def processAlgorithm(self, parameters, context, feedback):
        index = self.parameterAsInt(parameters, 'TOOL', context)
        tools = ('mkgmap', 'splitter')
        if index not in range(len(tools)):
            raise QgsProcessingException('tool_invalid')
        tool = tools[index]
        explicit = self.parameterAsFile(parameters, 'JAR_PATH', context)
        auto_download = self.parameterAsBool(
            parameters, 'AUTO_DOWNLOAD', context)
        path = discover_tool(tool, explicit)
        status = 'valid' if path else 'missing'
        if not path and auto_download:
            try:
                path = ensure_tool(
                    tool, explicit, True, feedback, start=0, span=100)
            except ValueError as exc:
                raise QgsProcessingException(str(exc))
            status = 'downloaded'
        manifest = tool_manifest(tool)
        details = json.dumps({
            'tool': tool,
            'main_jar_name': manifest['main_jar_name'],
            'required_dirs': list(manifest['required_dirs']),
            'archive_url': manifest['archive_url'],
        }, ensure_ascii=False, sort_keys=True)
        feedback.pushInfo('{0}: {1}'.format(tool, status))
        feedback.setProgress(100)
        return {'STATUS': status, 'PATH': path or '', 'DETAILS': details}

    def createInstance(self):
        return DependencyDiagnosticsDownloadAlgorithm()
