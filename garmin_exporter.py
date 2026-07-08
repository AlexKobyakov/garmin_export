# -*- coding: utf-8 -*-
"""
Garmin Exporter Plugin for QGIS
Основной модуль плагина экспорта в формат Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""

import os
import configparser

from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QMessageBox
from qgis.core import QgsApplication

from .translation_manager import translations


class GarminExporter:
    """Основной класс плагина Garmin Export"""

    def __init__(self, iface):
        """Инициализация плагина"""
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)

        # Инициализация языка интерфейса
        try:
            locale = QgsApplication.instance().locale()
        except Exception:
            locale = 'en'

        if locale in translations.get_supported_languages():
            translations.set_language(locale)
        elif locale and locale.startswith('ru'):
            translations.set_language('ru')
        else:
            translations.set_language('en')

        self.actions = []
        self.menu = 'Garmin Export'
        self.dialog = None
        self.first_start = True

    # ------------------------------------------------------------------
    # Метаданные плагина (читаются из metadata.txt)
    # ------------------------------------------------------------------

    @staticmethod
    def get_plugin_version():
        """Версия плагина из metadata.txt"""
        try:
            plugin_dir = os.path.dirname(__file__)
            metadata_file = os.path.join(plugin_dir, 'metadata.txt')
            if os.path.exists(metadata_file):
                config = configparser.ConfigParser()
                config.read(metadata_file, encoding='utf-8')
                if 'general' in config and 'version' in config['general']:
                    return config['general']['version']
        except Exception as e:
            print(f"Error reading plugin version: {e}")
        return "Unknown"

    @staticmethod
    def get_plugin_info():
        """Полная информация о плагине из metadata.txt"""
        default = {
            'name': 'Garmin Export',
            'version': 'Unknown',
            'author': 'Кобяков Александр Викторович',
            'email': 'kobyakov@lesburo.ru',
            'description': '',
        }
        try:
            plugin_dir = os.path.dirname(__file__)
            metadata_file = os.path.join(plugin_dir, 'metadata.txt')
            if os.path.exists(metadata_file):
                config = configparser.ConfigParser()
                config.read(metadata_file, encoding='utf-8')
                if 'general' in config:
                    section = config['general']
                    return {
                        'name': section.get('name', default['name']),
                        'version': section.get('version', default['version']),
                        'author': section.get('author', default['author']),
                        'email': section.get('email', default['email']),
                        'description': section.get('description', ''),
                    }
        except Exception as e:
            print(f"Error reading plugin info: {e}")
        return default

    # ------------------------------------------------------------------
    # Интеграция с QGIS
    # ------------------------------------------------------------------

    def add_action(self, icon_path, text, callback, enabled_flag=True,
                   add_to_menu=True, add_to_toolbar=True, status_tip=None,
                   whats_this=None, parent=None):
        """Добавление действия в интерфейс QGIS"""
        icon = QIcon(icon_path) if icon_path else QIcon()
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)
        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.iface.addToolBarIcon(action)
        if add_to_menu:
            self.iface.addPluginToVectorMenu(self.menu, action)

        self.actions.append(action)
        return action

    def initGui(self):
        """Создание GUI элементов"""
        icon_path = os.path.join(self.plugin_dir, 'icon.png')
        if not os.path.exists(icon_path):
            icon_path = None

        self.add_action(
            icon_path,
            text=f"🎯 {translations.get_text('window_title')}",
            callback=self.run,
            parent=self.iface.mainWindow(),
            status_tip=translations.get_text('plugin_description'),
            whats_this=translations.get_text('plugin_description')
        )

        self.first_start = True

    def unload(self):
        """Удаление элементов GUI при выгрузке плагина"""
        for action in self.actions:
            self.iface.removePluginVectorMenu(self.menu, action)
            self.iface.removeToolBarIcon(action)

        if self.dialog:
            self.dialog.close()
            self.dialog = None

    def run(self):
        """Запуск основного диалога плагина"""
        from .core.layer_manager import LayerManager

        layers = LayerManager.get_project_layers()
        if not layers:
            QMessageBox.information(
                self.iface.mainWindow(),
                translations.get_text('info'),
                translations.get_text('no_vector_layers')
            )
            return

        # Пересоздаём диалог каждый раз, чтобы подхватить актуальные слои
        if self.dialog is None:
            from .gui.gui_main import GarminExportDialog
            self.dialog = GarminExportDialog(self.iface.mainWindow())
        else:
            self.dialog.loadProjectLayers()

        self.dialog.show()
        self.dialog.raise_()
        self.dialog.activateWindow()

    def check_dependencies(self):
        """Проверка зависимостей плагина (Java)"""
        from .core import mkgmap_compiler
        missing = []
        if not mkgmap_compiler.check_java_available():
            if not mkgmap_compiler.find_java():
                missing.append("Java Runtime Environment (JRE 8+)")
        return missing
