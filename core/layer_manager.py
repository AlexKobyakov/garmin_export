# -*- coding: utf-8 -*-
"""
Layer Manager for Garmin Export Plugin
Менеджер слоёв проекта QGIS

Идентификация слоёв выполняется по уникальному layer id, а не по имени,
чтобы корректно работать со слоями с одинаковыми именами.

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

from qgis.core import QgsProject, QgsVectorLayer, QgsWkbTypes


class LayerManager:
    """Менеджер векторных слоёв проекта"""

    @staticmethod
    def get_project_layers():
        """Возвращает все действительные векторные слои проекта.

        Порядок соответствует порядку отрисовки в дереве слоёв
        (первый в списке — верхний слой).
        """
        layers = []
        project = QgsProject.instance()

        # layerTreeRoot даёт порядок отрисовки, mapLayers - нет
        try:
            ordered = project.layerTreeRoot().layerOrder()
        except Exception:
            ordered = list(project.mapLayers().values())

        for layer in ordered:
            if isinstance(layer, QgsVectorLayer) and layer.isValid():
                layers.append({
                    'id': layer.id(),
                    'name': layer.name(),
                    'type': LayerManager.get_geometry_type(layer),
                    'layer': layer,
                })

        return layers

    @staticmethod
    def get_geometry_type(layer):
        """Определяет тип геометрии слоя"""
        geom_type = layer.geometryType()

        if geom_type == QgsWkbTypes.PointGeometry:
            return 'Point'
        elif geom_type == QgsWkbTypes.LineGeometry:
            return 'LineString'
        elif geom_type == QgsWkbTypes.PolygonGeometry:
            return 'Polygon'
        return 'Unknown'

    @staticmethod
    def get_layer_fields(layer):
        """Возвращает список полей слоя"""
        return [field.name() for field in layer.fields()]

    @staticmethod
    def get_layer_by_id(layer_id):
        """Возвращает слой по уникальному идентификатору"""
        layer = QgsProject.instance().mapLayer(layer_id)
        if isinstance(layer, QgsVectorLayer) and layer.isValid():
            return layer
        return None

    @staticmethod
    def get_layer_by_name(layer_name):
        """Возвращает первый слой с указанным именем (для совместимости)"""
        for layer in QgsProject.instance().mapLayers().values():
            if isinstance(layer, QgsVectorLayer) and layer.name() == layer_name:
                return layer
        return None
