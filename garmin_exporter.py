# -*- coding: utf-8 -*-
"""
Garmin Exporter Plugin for QGIS
Основной модуль плагина экспорта в формат Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

import os
from qgis.PyQt.QtCore import QTranslator, qVersion, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction
from qgis.core import QgsApplication

from .gui.gui_main import GarminExportDialog
from .translation_manager import translations


class GarminExporter:
    """Основной класс плагина Garmin Export"""
    
    def __init__(self, iface):
        """Инициализация плагина"""
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        
        # Инициализация переводов
        locale = QgsApplication.instance().locale()
        locale_path = os.path.join(self.plugin_dir, 'translations', f'{locale}.py')
        
        # Устанавливаем язык
        if locale in translations.get_supported_languages():
            translations.set_language(locale)
        elif locale.startswith('ru'):
            translations.set_language('ru')
        else:
            translations.set_language('en')
        
        # Переменные для UI
        self.actions = []
        self.menu = translations.get_text('window_title')
        self.dialog = None
        self.toolbar = None
    
    def add_action(self, icon_path, text, callback, enabled_flag=True, 
                   add_to_menu=True, add_to_toolbar=True, status_tip=None, 
                   whats_this=None, parent=None):
        """Добавление действия в интерфейс QGIS"""
        
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)
        
        if status_tip is not None:
            action.setStatusTip(status_tip)
        
        if whats_this is not None:
            action.setWhatsThis(whats_this)
        
        if add_to_toolbar:
            # Добавляем на панель инструментов
            self.iface.addToolBarIcon(action)
        
        if add_to_menu:
            # Добавляем в меню
            self.iface.addPluginToVectorMenu(self.menu, action)
        
        self.actions.append(action)
        return action
    
    def initGui(self):
        """Создание GUI элементов"""
        # Иконка плагина
        icon_path = os.path.join(self.plugin_dir, 'icon.png')
        if not os.path.exists(icon_path):
            # Создаем простую иконку, если файл не найден
            icon_path = None
        
        # Добавляем действие
        self.add_action(
            icon_path,
            text=f"🎯 {translations.get_text('window_title')}",
            callback=self.run,
            parent=self.iface.mainWindow(),
            status_tip=translations.get_text('plugin_description'),
            whats_this=translations.get_text('plugin_description')
        )
        
        # Первый запуск
        self.first_start = True
    
    def unload(self):
        """Удаление элементов GUI при выгрузке плагина"""
        for action in self.actions:
            self.iface.removePluginVectorMenu(self.menu, action)
            self.iface.removeToolBarIcon(action)
        
        # Закрываем диалог если открыт
        if self.dialog:
            self.dialog.close()
    
    def run(self):
        """Запуск основного диалога плагина"""
        # Создаем диалог при первом запуске
        if self.first_start:
            self.first_start = False
            
            # Проверяем наличие векторных слоёв
            from .gui.gui_handlers import LayerManager
            layers = LayerManager.get_project_layers()
            
            if not layers:
                from qgis.PyQt.QtWidgets import QMessageBox
                QMessageBox.information(
                    self.iface.mainWindow(),
                    translations.get_text('info'),
                    "В проекте нет векторных слоёв для экспорта.\n\n"
                    "Добавьте векторные слои в проект и повторите попытку."
                )
                return
        
        # Создаем новый диалог
        self.dialog = GarminExportDialog(self.iface.mainWindow())
        
        # Показываем диалог
        self.dialog.show()
        
        # Центрируем диалог
        self.center_dialog()
    
    def center_dialog(self):
        """Центрирование диалога на экране"""
        if self.dialog:
            # Получаем размеры экрана
            screen = QgsApplication.instance().desktop().screenGeometry()
            
            # Вычисляем позицию для центрирования
            x = (screen.width() - self.dialog.width()) // 2
            y = (screen.height() - self.dialog.height()) // 2
            
            # Устанавливаем позицию
            self.dialog.move(x, y)
    
    def get_plugin_info(self):
        """Получение информации о плагине"""
        return {
            'name': 'Garmin Export',
            'version': '1.0.0',
            'author': 'Кобяков Александр Викторович (Alex Kobyakov)',
            'email': 'kobyakov@lesburo.ru',
            'description': translations.get_text('plugin_description'),
            'languages': translations.get_supported_languages()
        }
    
    def check_dependencies(self):
        """Проверка зависимостей плагина"""
        missing_deps = []
        
        # Проверяем наличие Java (для mkgmap)
        from .core.mkgmap_compiler import MkgmapCompiler
        compiler = MkgmapCompiler()
        
        if not compiler.check_java_available():
            missing_deps.append("Java Runtime Environment (JRE)")
        
        return missing_deps
    
    def show_about_dialog(self):
        """Показать диалог 'О программе'"""
        from .gui.gui_dialogs import AuthorDialog
        
        dialog = AuthorDialog(self.iface.mainWindow())
        dialog.exec_()
    
    def show_donation_dialog(self):
        """Показать диалог поддержки разработки"""
        from .gui.gui_dialogs import DonationDialog
        
        dialog = DonationDialog(self.iface.mainWindow())
        dialog.exec_()
    
    def export_sample_data(self):
        """Экспорт тестовых данных"""
        try:
            # Создаем примеры JSON сопоставления
            sample_folder = os.path.join(self.plugin_dir, 'examples')
            os.makedirs(sample_folder, exist_ok=True)
            
            from .core.style_mapper import StyleMapper
            mapper = StyleMapper()
            
            sample_file = os.path.join(sample_folder, 'default_mapping.json')
            mapper.export_mapping_to_json(sample_file)
            
            return sample_file
            
        except Exception as e:
            return None
    
    def validate_installation(self):
        """Проверка корректности установки плагина"""
        issues = []
        
        # Проверяем основные модули
        required_modules = [
            'gui.gui_main',
            'core.export_worker', 
            'core.mp_generator',
            'core.mkgmap_compiler',
            'core.layer_processor',
            'core.style_mapper'
        ]
        
        for module_name in required_modules:
            try:
                __import__(f'.{module_name}', package=__package__)
            except ImportError as e:
                issues.append(f"Отсутствует модуль: {module_name} ({str(e)})")
        
        # Проверяем переводы
        if not translations.is_language_loaded('en'):
            issues.append("Отсутствуют английские переводы")
        
        if not translations.is_language_loaded('ru'):
            issues.append("Отсутствуют русские переводы")
        
        # Проверяем зависимости
        missing_deps = self.check_dependencies()
        if missing_deps:
            issues.extend([f"Отсутствует зависимость: {dep}" for dep in missing_deps])
        
        return issues
    
    def create_default_icon(self):
        """Создание иконки по умолчанию"""
        icon_path = os.path.join(self.plugin_dir, 'icon.png')
        
        if not os.path.exists(icon_path):
            try:
                # Создаем простую иконку программно
                from qgis.PyQt.QtGui import QPixmap, QPainter, QColor
                from qgis.PyQt.QtCore import Qt
                
                pixmap = QPixmap(32, 32)
                pixmap.fill(Qt.transparent)
                
                painter = QPainter(pixmap)
                painter.setRenderHint(QPainter.Antialiasing)
                
                # Рисуем простую иконку GPS
                painter.setBrush(QColor(52, 152, 219))  # Синий цвет
                painter.setPen(QColor(255, 255, 255))   # Белая обводка
                
                # Круг
                painter.drawEllipse(4, 4, 24, 24)
                
                # Точка в центре
                painter.setBrush(QColor(255, 255, 255))
                painter.drawEllipse(14, 14, 4, 4)
                
                painter.end()
                
                # Сохраняем
                pixmap.save(icon_path, 'PNG')
                
                return icon_path
                
            except Exception:
                return None
        
        return icon_path
    
    def get_log_file_path(self):
        """Получение пути к файлу логов"""
        from qgis.core import QgsApplication
        
        user_dir = QgsApplication.qgisSettingsDirPath()
        log_dir = os.path.join(user_dir, 'python', 'plugins', 'garmin_export', 'logs')
        os.makedirs(log_dir, exist_ok=True)
        
        return os.path.join(log_dir, 'garmin_export.log')
    
    def setup_logging(self):
        """Настройка логирования"""
        import logging
        
        log_file = self.get_log_file_path()
        
        # Настраиваем логгер
        logger = logging.getLogger('garmin_export')
        logger.setLevel(logging.INFO)
        
        # Создаем handler для файла
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        
        # Создаем formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        
        # Добавляем handler
        if not logger.handlers:
            logger.addHandler(file_handler)
        
        return logger
