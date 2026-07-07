# -*- coding: utf-8 -*-
"""
Layer Processor for Garmin Export Plugin
Процессор слоёв для плагина экспорта в Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

from qgis.core import QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsProject, QgsWkbTypes


class LayerProcessor:
    """Процессор для обработки векторных слоёв"""
    
    def __init__(self):
        # Целевая система координат - WGS84
        self.target_crs = QgsCoordinateReferenceSystem('EPSG:4326')
    
    def process_layer(self, layer, style_mapper, enabled_levels):
        """Обработка слоя для экспорта"""
        if not layer or not layer.isValid():
            raise Exception("Недействительный слой")
        
        # Получаем информацию о слое
        layer_name = layer.name()
        geometry_type = self._get_geometry_type(layer)
        
        # Получаем сопоставление стилей
        mapping_info = style_mapper.get_layer_mapping(layer_name, geometry_type)
        
        # Настройка трансформации координат
        transform = None
        if layer.crs() != self.target_crs:
            transform = QgsCoordinateTransform(
                layer.crs(),
                self.target_crs,
                QgsProject.instance()
            )
        
        # Обрабатываем объекты
        features = []
        feature_count = 0
        
        for feature in layer.getFeatures():
            try:
                processed_feature = self._process_feature(
                    feature, transform, mapping_info
                )
                
                if processed_feature:
                    features.append(processed_feature)
                    feature_count += 1
                    
            except Exception as e:
                # Логируем ошибку, но продолжаем обработку
                print(f"Ошибка обработки объекта в слое '{layer_name}': {str(e)}")
                continue
        
        # Формируем результат
        layer_data = {
            'layer_name': layer_name,
            'geometry_type': geometry_type,
            'garmin_type': mapping_info.get('garmin_type', '0x01'),
            'label_field': mapping_info.get('label_field'),
            'level': mapping_info.get('level', 1),
            'features': features,
            'feature_count': feature_count
        }
        
        return layer_data
    
    def _get_geometry_type(self, layer):
        """Определение типа геометрии слоя"""
        geom_type = layer.geometryType()
        
        if geom_type == QgsWkbTypes.PointGeometry:
            return 'Point'
        elif geom_type == QgsWkbTypes.LineGeometry:
            return 'LineString'
        elif geom_type == QgsWkbTypes.PolygonGeometry:
            return 'Polygon'
        else:
            return 'Unknown'
    
    def _process_feature(self, feature, transform, mapping_info):
        """Обработка отдельного объекта"""
        geometry = feature.geometry()
        
        if not geometry or geometry.isEmpty():
            return None
        
        # Трансформируем координаты
        if transform:
            try:
                geometry.transform(transform)
            except Exception as e:
                print(f"Ошибка трансформации координат: {str(e)}")
                return None
        
        # Получаем атрибуты
        attributes = {}
        for field in feature.fields():
            field_name = field.name()
            value = feature[field_name]
            
            # Преобразуем значение в строку
            if value is not None:
                attributes[field_name] = str(value)
            else:
                attributes[field_name] = ""
        
        # Преобразуем геометрию в GeoJSON-подобный формат
        geom_data = self._geometry_to_coords(geometry)
        
        if not geom_data:
            return None
        
        return {
            'geometry': geom_data,
            'attributes': attributes
        }
    
    def _geometry_to_coords(self, geometry):
        """Преобразование геометрии QGIS в координаты"""
        if geometry.isEmpty():
            return None
        
        geom_type = geometry.wkbType()
        
        # Точка
        if QgsWkbTypes.geometryType(geom_type) == QgsWkbTypes.PointGeometry:
            return self._point_to_coords(geometry)
        
        # Линия
        elif QgsWkbTypes.geometryType(geom_type) == QgsWkbTypes.LineGeometry:
            return self._linestring_to_coords(geometry)
        
        # Полигон
        elif QgsWkbTypes.geometryType(geom_type) == QgsWkbTypes.PolygonGeometry:
            return self._polygon_to_coords(geometry)
        
        return None
    
    def _point_to_coords(self, geometry):
        """Преобразование точки в координаты"""
        try:
            point = geometry.asPoint()
            return {
                'type': 'Point',
                'coordinates': [point.x(), point.y()]
            }
        except Exception:
            return None
    
    def _linestring_to_coords(self, geometry):
        """Преобразование линии в координаты"""
        try:
            if geometry.isMultipart():
                # Мультилиния - берём первую часть
                multiline = geometry.asMultiPolyline()
                if multiline and len(multiline) > 0:
                    line = multiline[0]
                else:
                    return None
            else:
                # Простая линия
                line = geometry.asPolyline()
            
            if not line or len(line) < 2:
                return None
            
            coordinates = []
            for point in line:
                coordinates.append([point.x(), point.y()])
            
            return {
                'type': 'LineString',
                'coordinates': coordinates
            }
            
        except Exception:
            return None
    
    def _polygon_to_coords(self, geometry):
        """Преобразование полигона в координаты"""
        try:
            if geometry.isMultipart():
                # Мультиполигон - берём первую часть
                multipolygon = geometry.asMultiPolygon()
                if multipolygon and len(multipolygon) > 0:
                    polygon = multipolygon[0]
                else:
                    return None
            else:
                # Простой полигон
                polygon = geometry.asPolygon()
            
            if not polygon or len(polygon) == 0:
                return None
            
            # Преобразуем кольца полигона
            rings = []
            for ring in polygon:
                if len(ring) < 3:  # Минимум 3 точки для кольца
                    continue
                
                ring_coords = []
                for point in ring:
                    ring_coords.append([point.x(), point.y()])
                
                rings.append(ring_coords)
            
            if not rings:
                return None
            
            return {
                'type': 'Polygon',
                'coordinates': rings
            }
            
        except Exception:
            return None
    
    def validate_geometry(self, geometry):
        """Проверка корректности геометрии"""
        if not geometry or geometry.isEmpty():
            return False
        
        # Проверяем, что геометрия действительна
        if not geometry.isGeosValid():
            return False
        
        # Дополнительные проверки в зависимости от типа
        geom_type = QgsWkbTypes.geometryType(geometry.wkbType())
        
        if geom_type == QgsWkbTypes.LineGeometry:
            # Линия должна иметь минимум 2 точки
            try:
                if geometry.isMultipart():
                    multiline = geometry.asMultiPolyline()
                    return len(multiline) > 0 and len(multiline[0]) >= 2
                else:
                    line = geometry.asPolyline()
                    return len(line) >= 2
            except:
                return False
        
        elif geom_type == QgsWkbTypes.PolygonGeometry:
            # Полигон должен иметь минимум 3 точки
            try:
                if geometry.isMultipart():
                    multipolygon = geometry.asMultiPolygon()
                    return (len(multipolygon) > 0 and 
                           len(multipolygon[0]) > 0 and 
                           len(multipolygon[0][0]) >= 3)
                else:
                    polygon = geometry.asPolygon()
                    return len(polygon) > 0 and len(polygon[0]) >= 3
            except:
                return False
        
        return True
    
    def get_layer_statistics(self, layer):
        """Получение статистики слоя"""
        if not layer or not layer.isValid():
            return {}
        
        stats = {
            'name': layer.name(),
            'geometry_type': self._get_geometry_type(layer),
            'feature_count': layer.featureCount(),
            'crs': layer.crs().authid(),
            'extent': layer.extent(),
            'fields': [field.name() for field in layer.fields()]
        }
        
        return stats
