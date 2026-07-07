# -*- coding: utf-8 -*-
"""
MP Generator for Garmin Export Plugin
Генератор файлов Polish format (MP) для плагина экспорта в Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

import os
from datetime import datetime


class MPGenerator:
    """Генератор файлов формата Polish (MP) для Garmin"""
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Сброс состояния генератора"""
        self.header_sections = []
        self.data_sections = []
        self.current_polyline_id = 1
        self.current_polygon_id = 1
        self.current_poi_id = 1
    
    def generate_mp_file(self, processed_data, output_path, settings):
        """Генерация MP файла из обработанных данных"""
        self.reset()
        
        # Генерируем заголовок
        self._generate_header(settings)
        
        # Генерируем секции данных
        for layer_data in processed_data:
            self._generate_layer_sections(layer_data)
        
        # Записываем файл
        self._write_mp_file(output_path)
    
    def _generate_header(self, settings):
        """Генерация заголовочных секций MP файла"""
        # Основная секция [IMG ID]
        img_section = [
            "[IMG ID]",
            f"ID={settings['map_id']}",
            f"Name={settings['map_name']}",
            f"Elevation=M",
            f"Preprocess=F",
            f"CodePage=1251",
            f"LblCoding=9",
            f"TreSize=2048",
            f"RgnLimit=127",
            f"POIIndex=Y"
        ]
        
        # Настройка уровней
        enabled_levels = settings.get('enabled_levels', [0, 1, 2, 3])
        
        # Уровни детализации
        for i, level in enumerate(enabled_levels):
            img_section.append(f"Level{i}={24 - level * 2}")
            img_section.append(f"Zoom{i}={level}")
        
        # Дополнительные настройки
        if settings.get('transparent'):
            img_section.append("Transparent=Y")
        
        if settings.get('routing'):
            img_section.append("Routing=Y")
        
        img_section.append("End")
        self.header_sections.append("\n".join(img_section))
        
        # Секция описания
        if settings.get('map_description'):
            description_section = [
                "[END-IMG ID]",
                f"Description={settings['map_description']}",
                f"Created={datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                "End"
            ]
            self.header_sections.append("\n".join(description_section))
    
    def _generate_layer_sections(self, layer_data):
        """Генерация секций для слоя"""
        geometry_type = layer_data.get('geometry_type')
        features = layer_data.get('features', [])
        garmin_type = layer_data.get('garmin_type', '0x01')
        label_field = layer_data.get('label_field')
        level = layer_data.get('level', 1)
        
        for feature in features:
            if geometry_type == 'Point':
                self._generate_poi_section(feature, garmin_type, label_field, level)
            elif geometry_type == 'LineString':
                self._generate_polyline_section(feature, garmin_type, label_field, level)
            elif geometry_type == 'Polygon':
                self._generate_polygon_section(feature, garmin_type, label_field, level)
    
    def _generate_poi_section(self, feature, garmin_type, label_field, level):
        """Генерация секции POI (точка)"""
        geometry = feature.get('geometry')
        attributes = feature.get('attributes', {})
        
        if not geometry or 'coordinates' not in geometry:
            return
        
        coords = geometry['coordinates']
        
        # Координаты в формате (долгота, широта)
        lon, lat = coords[0], coords[1]
        
        # Метка
        label = ""
        if label_field and label_field in attributes:
            label = str(attributes[label_field])
        
        section = [
            "[POI]",
            f"Type={garmin_type}",
            f"Label={label}",
            f"Data0=({lat:.6f},{lon:.6f})",
            f"EndLevel={level}",
            "End"
        ]
        
        self.data_sections.append("\n".join(section))
        self.current_poi_id += 1
    
    def _generate_polyline_section(self, feature, garmin_type, label_field, level):
        """Генерация секции POLYLINE (линия)"""
        geometry = feature.get('geometry')
        attributes = feature.get('attributes', {})
        
        if not geometry or 'coordinates' not in geometry:
            return
        
        coords = geometry['coordinates']
        
        # Метка
        label = ""
        if label_field and label_field in attributes:
            label = str(attributes[label_field])
        
        # Формируем координаты
        coord_pairs = []
        for coord in coords:
            if len(coord) >= 2:
                lon, lat = coord[0], coord[1]
                coord_pairs.append(f"({lat:.6f},{lon:.6f})")
        
        if not coord_pairs:
            return
        
        section = [
            "[POLYLINE]",
            f"Type={garmin_type}",
            f"Label={label}",
        ]
        
        # Добавляем координаты (максимум 255 точек на секцию)
        for i in range(0, len(coord_pairs), 255):
            chunk = coord_pairs[i:i+255]
            section.append(f"Data{i//255}={','.join(chunk)}")
        
        section.extend([
            f"EndLevel={level}",
            "End"
        ])
        
        self.data_sections.append("\n".join(section))
        self.current_polyline_id += 1
    
    def _generate_polygon_section(self, feature, garmin_type, label_field, level):
        """Генерация секции POLYGON (полигон)"""
        geometry = feature.get('geometry')
        attributes = feature.get('attributes', {})
        
        if not geometry or 'coordinates' not in geometry:
            return
        
        coords = geometry['coordinates']
        
        # Метка
        label = ""
        if label_field and label_field in attributes:
            label = str(attributes[label_field])
        
        # Обрабатываем только внешнее кольцо (первый элемент)
        if len(coords) > 0 and len(coords[0]) > 0:
            ring_coords = coords[0]
            
            # Формируем координаты
            coord_pairs = []
            for coord in ring_coords:
                if len(coord) >= 2:
                    lon, lat = coord[0], coord[1]
                    coord_pairs.append(f"({lat:.6f},{lon:.6f})")
            
            if len(coord_pairs) < 3:  # Минимум 3 точки для полигона
                return
            
            section = [
                "[POLYGON]",
                f"Type={garmin_type}",
                f"Label={label}",
            ]
            
            # Добавляем координаты (максимум 255 точек на секцию)
            for i in range(0, len(coord_pairs), 255):
                chunk = coord_pairs[i:i+255]
                section.append(f"Data{i//255}={','.join(chunk)}")
            
            section.extend([
                f"EndLevel={level}",
                "End"
            ])
            
            self.data_sections.append("\n".join(section))
            self.current_polygon_id += 1
    
    def _write_mp_file(self, output_path):
        """Запись MP файла"""
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                # Записываем заголовочные секции
                for section in self.header_sections:
                    f.write(section + "\n\n")
                
                # Записываем секции данных
                for section in self.data_sections:
                    f.write(section + "\n\n")
                
        except Exception as e:
            raise Exception(f"Ошибка записи MP файла: {str(e)}")
    
    def get_statistics(self):
        """Получение статистики генерации"""
        return {
            'total_sections': len(self.data_sections),
            'poi_count': self.current_poi_id - 1,
            'polyline_count': self.current_polyline_id - 1,
            'polygon_count': self.current_polygon_id - 1
        }
