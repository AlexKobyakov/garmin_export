# -*- coding: utf-8 -*-
"""Stable Garmin Export Processing provider registration."""

from qgis.core import QgsProcessingProvider

from .algorithms import (
    BuildTypMappingAlgorithm,
    ExportSelectedLayersAlgorithm,
    ValidateEnvironmentAlgorithm,
)
from .extra_algorithms import (
    DependencyDiagnosticsDownloadAlgorithm,
    GenerateMpPreviewAlgorithm,
    ValidateMappingJsonAlgorithm,
    ValidateTypCodePageAlgorithm,
)


class GarminProcessingProvider(QgsProcessingProvider):
    """Processing registry entry; no GUI or iface dependency."""

    def id(self):
        return 'garmin_export'

    def name(self):
        return 'Garmin Export'

    def longName(self):
        return self.name()

    def icon(self):
        from qgis.PyQt.QtGui import QIcon
        import os
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                            'icon.png')
        return QIcon(path)

    def loadAlgorithms(self):
        self.addAlgorithm(ValidateEnvironmentAlgorithm())
        self.addAlgorithm(BuildTypMappingAlgorithm())
        self.addAlgorithm(ExportSelectedLayersAlgorithm())
        self.addAlgorithm(ValidateTypCodePageAlgorithm())
        self.addAlgorithm(GenerateMpPreviewAlgorithm())
        self.addAlgorithm(ValidateMappingJsonAlgorithm())
        self.addAlgorithm(DependencyDiagnosticsDownloadAlgorithm())
