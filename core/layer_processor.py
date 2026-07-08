# -*- coding: utf-8 -*-
"""
Layer Processor for Garmin Export Plugin
Процессор слоёв для плагина экспорта в Garmin

Обрабатывает все части мультигеометрий (мультилинии, мультиполигоны),
трансформирует координаты в WGS84 и готовит данные для MPGenerator.

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""

from qgis.core import (
    QgsCoordinateReferenceSystem, QgsCoordinateTransform,
    QgsProject, QgsWkbTypes
)


class LayerProcessor:
    """Процессор для обработки векторных слоёв"""

    def __init__(self):
        # Целевая система координат - WGS84
        self.target_crs = QgsCoordinateReferenceSystem('EPSG:4326')

    def process_layer(self, layer, style_mapper, enabled_levels, log_callback=None):
        """Обработка слоя для экспорта.

        Args:
            layer: QgsVectorLayer
            style_mapper: StyleMapper для получения сопоставления
            enabled_levels: список включённых уровней
            log_callback: функция для сообщений (str) -> None
        """
        if not layer or not layer.isValid():
            raise Exception('Недействительный слой')

        layer_name = layer.name()
        geometry_type = self._get_geometry_type(layer)

        if geometry_type == 'Unknown':
            raise Exception(
                'Неподдерживаемый тип геометрии слоя "{0}"'.format(layer_name))

        mapping_info = style_mapper.get_layer_mapping(layer_name, geometry_type)

        # Настройка трансформации координат
        transform = None
        if layer.crs() != self.target_crs:
            transform = QgsCoordinateTransform(
                layer.crs(), self.target_crs, QgsProject.instance())

        features = []
        error_count = 0

        for feature in layer.getFeatures():
            try:
                processed_feature = self._process_feature(feature, transform)
                if processed_feature:
                    features.append(processed_feature)
                else:
                    error_count += 1
            except Exception as e:
                error_count += 1
                if log_callback:
                    log_callback('Ошибка обработки объекта {0} в слое "{1}": {2}'.format(
                        feature.id(), layer_name, str(e)))
                continue

        if error_count and log_callback:
            log_callback('Слой "{0}": пропущено объектов с ошибками/пустой геометрией: {1}'.format(
                layer_name, error_count))

        return {
            'layer_name': layer_name,
            'geometry_type': geometry_type,
            'garmin_type': mapping_info.get('type', mapping_info.get('garmin_type', '0x01')),
            'label_field': mapping_info.get('label_field'),
            'level': mapping_info.get('level', 1),
            'features': features,
            'feature_count': len(features),
            'error_count': error_count,
        }

    def _get_geometry_type(self, layer):
        """Определение типа геометрии слоя"""
        geom_type = layer.geometryType()

        if geom_type == QgsWkbTypes.PointGeometry:
            return 'Point'
        elif geom_type == QgsWkbTypes.LineGeometry:
            return 'LineString'
        elif geom_type == QgsWkbTypes.PolygonGeometry:
            return 'Polygon'
        return 'Unknown'

    def _process_feature(self, feature, transform):
        """Обработка отдельного объекта"""
        geometry = feature.geometry()

        if not geometry or geometry.isEmpty():
            return None

        # Трансформируем координаты (на копии, чтобы не менять слой)
        if transform:
            geometry = type(geometry)(geometry)
            result = geometry.transform(transform)
            if result != 0:
                return None

        # Атрибуты как строки
        attributes = {}
        for field in feature.fields():
            field_name = field.name()
            value = feature[field_name]
            attributes[field_name] = '' if value is None else str(value)

        geom_data = self._geometry_to_coords(geometry)
        if not geom_data:
            return None

        return {
            'geometry': geom_data,
            'attributes': attributes,
        }

    def _geometry_to_coords(self, geometry):
        """Преобразование геометрии QGIS в структуру координат.

        Возвращает словарь:
            Point:      {'type': 'Point', 'coordinates': [x, y]}
            LineString: {'type': 'LineString', 'parts': [[[x, y], ...], ...]}
            Polygon:    {'type': 'Polygon', 'parts': [[ring1, ring2...], ...]}
        Все части мультигеометрий сохраняются.
        """
        if geometry.isEmpty():
            return None

        geom_type = QgsWkbTypes.geometryType(geometry.wkbType())

        if geom_type == QgsWkbTypes.PointGeometry:
            return self._point_to_coords(geometry)
        elif geom_type == QgsWkbTypes.LineGeometry:
            return self._linestring_to_coords(geometry)
        elif geom_type == QgsWkbTypes.PolygonGeometry:
            return self._polygon_to_coords(geometry)

        return None

    def _point_to_coords(self, geometry):
        """Преобразование точки (для мультиточки берётся центроид части)"""
        try:
            if geometry.isMultipart():
                points = geometry.asMultiPoint()
                if not points:
                    return None
                point = points[0]
            else:
                point = geometry.asPoint()
            return {
                'type': 'Point',
                'coordinates': [point.x(), point.y()],
            }
        except Exception:
            return None

    def _linestring_to_coords(self, geometry):
        """Преобразование линии со всеми частями мультилинии"""
        try:
            if geometry.isMultipart():
                lines = geometry.asMultiPolyline()
            else:
                line = geometry.asPolyline()
                lines = [line] if line else []

            parts = []
            for line in lines:
                if line and len(line) >= 2:
                    parts.append([[p.x(), p.y()] for p in line])

            if not parts:
                return None

            return {
                'type': 'LineString',
                'parts': parts,
            }
        except Exception:
            return None

    def _polygon_to_coords(self, geometry):
        """Преобразование полигона со всеми частями мультиполигона"""
        try:
            if geometry.isMultipart():
                polygons = geometry.asMultiPolygon()
            else:
                polygon = geometry.asPolygon()
                polygons = [polygon] if polygon else []

            parts = []
            for polygon in polygons:
                rings = []
                for ring in polygon:
                    if len(ring) >= 3:
                        rings.append([[p.x(), p.y()] for p in ring])
                if rings:
                    parts.append(rings)

            if not parts:
                return None

            return {
                'type': 'Polygon',
                'parts': parts,
            }
        except Exception:
            return None

    def get_layer_statistics(self, layer):
        """Получение статистики слоя"""
        if not layer or not layer.isValid():
            return {}

        return {
            'name': layer.name(),
            'geometry_type': self._get_geometry_type(layer),
            'feature_count': layer.featureCount(),
            'crs': layer.crs().authid(),
            'extent': layer.extent(),
            'fields': [field.name() for field in layer.fields()],
        }
