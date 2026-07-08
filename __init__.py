# -*- coding: utf-8 -*-
"""
Garmin Export Plugin for QGIS
Плагин экспорта данных QGIS в формат Garmin IMG через mkgmap

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Organization: Lesburo
Year: 2025
Version: 1.1.1

Modular Architecture:
- garmin_exporter.py: Main plugin class
- gui/: GUI components and design
- translations/: Multi-language support (EN, RU, DE, ES, FR, PT, ZH, HI, AR)
- core/: Core functionality modules (MP/TYP generation, mkgmap command,
  downloader, settings, layer processing)
"""

def classFactory(iface):
    """
    Точка входа для QGIS плагина
    
    Args:
        iface: QGIS interface object
        
    Returns:
        GarminExporter: Экземпляр основного класса плагина
    """
    from .garmin_exporter import GarminExporter
    return GarminExporter(iface)
