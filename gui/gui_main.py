# -*- coding: utf-8 -*-
"""
Main GUI Dialog for Garmin Export Plugin
Главное диалоговое окно для плагина экспорта в Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

from datetime import datetime

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QSplitter, 
    QScrollArea, QWidget, QTabWidget, QFrame, QLabel
)

from .gui_components import ModernProgressBar, apply_global_styles
from .gui_widgets import (
    HeaderWidget, LayerSelectionWidget, ExportSettingsWidget,
    StyleMappingWidget, ControlButtonsWidget, LogTextWidget,
    ResultsTableWidget, LevelSettingsWidget
)
from .gui_handlers import GuiEventHandlers, LayerManager


class GarminExportDialog(QDialog):
    """Главное диалоговое окно экспорта в Garmin с модульной архитектурой"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Инициализация переменных
        self.worker = None
        self.worker_thread = None
        
        # Настройка окна
        self.setupWindow()
        
        # Создание интерфейса
        self.setupUi()
        
        # Создание обработчиков событий
        self.handlers = GuiEventHandlers(self)
        
        # Подключение сигналов
        self.connectSignals()
        
        # Применение стилей
        self.applyStyles()
        
        # Загрузка слоёв проекта
        self.loadProjectLayers()
        
        # Загрузка настроек по умолчанию
        self.loadDefaultSettings()
        
        # Обновление языка
        self.updateLanguage()
    
    def setupWindow(self):
        """Настройка основных параметров окна"""
        from ..translation_manager import translations
        
        self.setWindowTitle(f"🎯 {translations.get_text('window_title')}")
        self.setMinimumSize(1200, 900)
        self.resize(1400, 1000)
        
        # Центрирование окна
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
    
    def setupUi(self):
        """Создание основного интерфейса"""
        # Главный макет
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)
        
        # Создание компонентов
        self.createHeader()
        self.createMainContent()
        
        # Добавление в главный макет
        main_layout.addWidget(self.header)
        main_layout.addWidget(self.main_splitter, 1)
    
    def createHeader(self):
        """Создание заголовка"""
        self.header = HeaderWidget()
    
    def createMainContent(self):
        """Создание основного содержимого"""
        # Главный сплиттер
        self.main_splitter = QSplitter(Qt.Vertical)
        self.main_splitter.setChildrenCollapsible(False)
        
        # Верхняя часть - настройки
        self.createSettingsArea()
        
        # Средняя часть - кнопки управления (фиксированная позиция)
        self.createControlButtonsArea()
        
        # Нижняя часть - прогресс и результаты
        self.createResultsArea()
        
        # Добавление в сплиттер
        self.main_splitter.addWidget(self.settings_area)
        self.main_splitter.addWidget(self.control_buttons_area)
        self.main_splitter.addWidget(self.results_area)
        self.main_splitter.setSizes([500, 80, 250])
    
    def createSettingsArea(self):
        """Создание области настроек"""
        # Прокручиваемая область
        self.settings_scroll = QScrollArea()
        self.settings_scroll.setWidgetResizable(True)
        self.settings_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.settings_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        # Контейнер настроек
        settings_container = QWidget()
        settings_layout = QVBoxLayout(settings_container)
        settings_layout.setContentsMargins(15, 15, 15, 15)
        settings_layout.setSpacing(20)
        
        # Создание табов настроек
        self.createSettingsTabs()
        
        # Добавление в макет
        settings_layout.addWidget(self.settings_tabs)
        settings_layout.addStretch()
        
        # Установка виджета в scroll area
        self.settings_scroll.setWidget(settings_container)
        self.settings_area = self.settings_scroll
    
    def createControlButtonsArea(self):
        """Создание фиксированной области кнопок управления"""
        # Контейнер для кнопок
        self.control_buttons_area = QFrame()
        self.control_buttons_area.setFixedHeight(80)
        self.control_buttons_area.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border-top: 2px solid #e9ecef;
                border-bottom: 2px solid #e9ecef;
            }
        """)
        
        # Макет для кнопок
        buttons_layout = QHBoxLayout(self.control_buttons_area)
        buttons_layout.setContentsMargins(20, 15, 20, 15)
        buttons_layout.setSpacing(15)
        
        # Кнопки управления
        self.control_buttons = ControlButtonsWidget()
        self.control_buttons.setContentsMargins(0, 0, 0, 0)
        
        # Добавляем кнопки в макет
        buttons_layout.addWidget(self.control_buttons)
    
    def createSettingsTabs(self):
        """Создание табов настроек"""
        self.settings_tabs = QTabWidget()
        self.settings_tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid #bdc3c7;
                border-radius: 8px;
                background-color: #f8f9fa;
            }
            QTabBar::tab {
                background: #ecf0f1;
                border: 1px solid #bdc3c7;
                padding: 8px 16px;
                margin-right: 2px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                min-width: 200px;
            }
            QTabBar::tab:selected {
                background: #3498db;
                color: white;
                font-weight: bold;
            }
            QTabBar::tab:hover:!selected {
                background: #d5dbdb;
            }
        """)
        
        # Создание табов
        self.createLayerSelectionTab()
        self.createExportSettingsTab()
        self.createStyleMappingTab()
        self.createLevelSettingsTab()
        
        # Добавление табов
        self.settings_tabs.addTab(self.layer_tab_widget, "📁 Выбор слоёв")
        self.settings_tabs.addTab(self.export_tab_widget, "⚙️ Настройки экспорта")
        self.settings_tabs.addTab(self.mapping_tab_widget, "🎨 Сопоставление стилей")
        self.settings_tabs.addTab(self.levels_tab_widget, "📊 Уровни карты")
    
    def createLayerSelectionTab(self):
        """Создание таба выбора слоёв"""
        self.layer_tab_widget = QWidget()
        layer_layout = QVBoxLayout(self.layer_tab_widget)
        layer_layout.setContentsMargins(20, 20, 20, 20)
        layer_layout.setSpacing(20)
        
        # Виджет выбора слоёв
        self.layer_selection = LayerSelectionWidget()
        
        # Добавление в макет
        layer_layout.addWidget(self.layer_selection)
        layer_layout.addStretch()
    
    def createExportSettingsTab(self):
        """Создание таба настроек экспорта"""
        self.export_tab_widget = QWidget()
        export_layout = QVBoxLayout(self.export_tab_widget)
        export_layout.setContentsMargins(20, 20, 20, 20)
        export_layout.setSpacing(20)
        
        # Виджет настроек экспорта
        self.export_settings = ExportSettingsWidget()
        
        # Добавление в макет
        export_layout.addWidget(self.export_settings)
        export_layout.addStretch()
    
    def createStyleMappingTab(self):
        """Создание таба сопоставления стилей"""
        self.mapping_tab_widget = QWidget()
        mapping_layout = QVBoxLayout(self.mapping_tab_widget)
        mapping_layout.setContentsMargins(20, 20, 20, 20)
        mapping_layout.setSpacing(20)
        
        # Виджет сопоставления стилей
        self.mapping_widget = StyleMappingWidget()
        
        # Добавление в макет
        mapping_layout.addWidget(self.mapping_widget)
        mapping_layout.addStretch()
    
    def createLevelSettingsTab(self):
        """Создание таба настроек уровней"""
        self.levels_tab_widget = QWidget()
        levels_layout = QVBoxLayout(self.levels_tab_widget)
        levels_layout.setContentsMargins(20, 20, 20, 20)
        levels_layout.setSpacing(20)
        
        # Виджет настроек уровней
        self.level_settings = LevelSettingsWidget()
        
        # Добавление в макет
        levels_layout.addWidget(self.level_settings)
        levels_layout.addStretch()
    
    def createResultsArea(self):
        """Создание области результатов"""
        self.results_area = QWidget()
        results_layout = QVBoxLayout(self.results_area)
        results_layout.setContentsMargins(15, 15, 15, 15)
        results_layout.setSpacing(15)
        
        # Прогресс-бар
        self.createProgressSection()
        
        # Табы результатов
        self.createResultsTabs()
        
        # Добавление в макет
        results_layout.addWidget(self.progress_frame)
        results_layout.addWidget(self.results_tabs, 1)
    
    def createProgressSection(self):
        """Создание секции прогресса"""
        self.progress_frame = QFrame()
        progress_layout = QVBoxLayout(self.progress_frame)
        progress_layout.setContentsMargins(0, 0, 0, 0)
        
        # Метка прогресса
        self.progress_label = QLabel("📊 Прогресс")
        self.progress_label.setStyleSheet("font-weight: bold; color: #2c3e50;")
        
        # Прогресс-бар
        self.progress_bar = ModernProgressBar()
        self.progress_bar.setVisible(False)
        
        progress_layout.addWidget(self.progress_label)
        progress_layout.addWidget(self.progress_bar)
    
    def createResultsTabs(self):
        """Создание табов результатов"""
        self.results_tabs = QTabWidget()
        self.results_tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid #bdc3c7;
                border-radius: 8px;
                background-color: white;
            }
            QTabBar::tab {
                background: #ecf0f1;
                border: 1px solid #bdc3c7;
                padding: 6px 12px;
                margin-right: 2px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
            }
            QTabBar::tab:selected {
                background: white;
                border-bottom-color: white;
                font-weight: bold;
            }
        """)
        
        # Таб логов
        self.log_text = LogTextWidget()
        
        # Таб результатов
        self.results_table = ResultsTableWidget()
        
        # Добавление табов
        self.results_tabs.addTab(self.log_text, "📋 Логи")
        self.results_tabs.addTab(self.results_table, "📈 Результаты")
    
    def connectSignals(self):
        """Подключение сигналов к обработчикам"""
        # Заголовок
        self.header.language_combo.currentIndexChanged.connect(self.handlers.onLanguageChanged)
        self.header.donation_button.clicked.connect(self.handlers.showDonation)
        self.header.author_button.clicked.connect(self.handlers.showAuthorInfo)
        
        # Выбор слоёв
        self.layer_selection.select_all_button.clicked.connect(self.handlers.selectAllLayers)
        self.layer_selection.deselect_all_button.clicked.connect(self.handlers.deselectAllLayers)
        
        # Настройки экспорта
        self.export_settings.output_folder_button.clicked.connect(self.handlers.selectOutputFolder)
        self.export_settings.mkgmap_path_button.clicked.connect(self.handlers.selectMkgmapPath)
        
        # Сопоставление стилей
        self.mapping_widget.load_mapping_button.clicked.connect(self.handlers.loadMapping)
        self.mapping_widget.save_mapping_button.clicked.connect(self.handlers.saveMapping)
        self.mapping_widget.edit_mapping_button.clicked.connect(self.handlers.editMapping)
        self.mapping_widget.reset_mapping_button.clicked.connect(self.handlers.resetMapping)
        
        # Кнопки управления
        self.control_buttons.compile_button.clicked.connect(self.handlers.startCompilation)
        self.control_buttons.cancel_button.clicked.connect(self.handlers.cancelCompilation)
        self.control_buttons.clear_log_button.clicked.connect(self.handlers.clearLogs)
    
    def applyStyles(self):
        """Применение глобальных стилей"""
        self.setStyleSheet(apply_global_styles())
    
    def loadProjectLayers(self):
        """Загрузка слоёв проекта"""
        layers = LayerManager.get_project_layers()
        
        # Очищаем список
        self.layer_selection.layers_list.clear()
        
        # Добавляем слои
        for layer_info in layers:
            self.layer_selection.add_layer_item(
                layer_info['name'],
                layer_info['type'],
                is_checked=True  # По умолчанию выбираем все слои
            )
        
        self.log_message(f"📁 Загружено слоёв проекта: {len(layers)}")
    
    def loadDefaultSettings(self):
        """Загрузка настроек по умолчанию"""
        # Устанавливаем JSON-сопоставление по умолчанию
        default_mapping = self.mapping_widget.get_default_mapping()
        self.mapping_widget.set_mapping_json(default_mapping)
        
        self.log_message("⚙️ Загружены настройки по умолчанию")
    
    def updateLanguage(self):
        """Обновление языка интерфейса"""
        from ..translation_manager import translations
        
        # Обновление заголовка окна
        self.setWindowTitle(f"🎯 {translations.get_text('window_title')}")
        
        # Обновление кнопок в заголовке
        support_text = f"☕ {translations.get_text('header_support')}"
        author_text = f"👤 {translations.get_text('header_about_author')}"
        
        self.header.donation_button.setText(support_text)
        self.header.author_button.setText(author_text)
        
        # Обновление табов настроек
        self.settings_tabs.setTabText(0, f"📁 {translations.get_text('layer_selection')}")
        self.settings_tabs.setTabText(1, f"⚙️ {translations.get_text('export_options')}")
        self.settings_tabs.setTabText(2, f"🎨 {translations.get_text('layer_mapping')}")
        self.settings_tabs.setTabText(3, f"📊 {translations.get_text('export_levels')}")
        
        # Обновление выбора слоёв
        self.layer_selection.layers_group.setTitle(f"📁 {translations.get_text('select_layers')}")
        self.layer_selection.select_all_button.setText(f"✅ {translations.get_text('select_all_layers')}")
        self.layer_selection.deselect_all_button.setText(f"❌ {translations.get_text('deselect_all_layers')}")
        
        # Обновление настроек экспорта
        self.export_settings.output_group.setTitle(f"📤 {translations.get_text('output_folder')}")
        self.export_settings.output_folder_line.setPlaceholderText(translations.get_text('select_output_folder'))
        self.export_settings.output_folder_button.setText(f"📂 {translations.get_text('browse')}")
        
        self.export_settings.map_group.setTitle(f"🗺️ {translations.get_text('map_settings')}")
        self.export_settings.map_name_line.setPlaceholderText(translations.get_text('map_name'))
        self.export_settings.transparent_cb.setText(translations.get_text('transparent'))
        self.export_settings.routing_cb.setText(translations.get_text('routing'))
        
        self.export_settings.mkgmap_group.setTitle(f"⚙️ {translations.get_text('mkgmap_settings')}")
        self.export_settings.mkgmap_path_line.setPlaceholderText(translations.get_text('select_mkgmap'))
        self.export_settings.mkgmap_path_button.setText(f"📂 {translations.get_text('browse')}")
        
        # Обновление сопоставления стилей
        self.mapping_widget.mapping_group.setTitle(f"🎨 {translations.get_text('style_mapping')}")
        self.mapping_widget.load_mapping_button.setText(f"📂 {translations.get_text('load_mapping')}")
        self.mapping_widget.save_mapping_button.setText(f"💾 {translations.get_text('save_mapping')}")
        self.mapping_widget.edit_mapping_button.setText(f"✏️ {translations.get_text('edit_mapping')}")
        self.mapping_widget.reset_mapping_button.setText(f"🔄 {translations.get_text('default_mapping')}")
        
        # Обновление уровней
        self.level_settings.levels_group.setTitle(f"📊 {translations.get_text('export_levels')}")
        self.level_settings.level_0_cb.setText(translations.get_text('level_0'))
        self.level_settings.level_1_cb.setText(translations.get_text('level_1'))
        self.level_settings.level_2_cb.setText(translations.get_text('level_2'))
        self.level_settings.level_3_cb.setText(translations.get_text('level_3'))
        
        # Обновление прогресса
        self.progress_label.setText(f"📊 {translations.get_text('progress')}")
        
        # Обновление табов результатов
        self.results_tabs.setTabText(0, f"📋 {translations.get_text('logs')}")
        self.results_tabs.setTabText(1, f"📈 {translations.get_text('results')}")
        
        # Обновление заголовков таблицы
        self.results_table.setHorizontalHeaderLabels([
            f"📄 {translations.get_text('layer')}",
            f"📊 {translations.get_text('status')}",
            f"💬 {translations.get_text('message')}"
        ])
        
        # Обновление кнопок
        if 'Compiling' in self.control_buttons.compile_button.text() or 'Компиляция' in self.control_buttons.compile_button.text():
            self.control_buttons.compile_button.setText(f"⏳ {translations.get_text('compiling')}")
        else:
            self.control_buttons.compile_button.setText(f"🚀 {translations.get_text('compile_map')}")
            
        self.control_buttons.cancel_button.setText(f"❌ {translations.get_text('cancel')}")
        self.control_buttons.clear_log_button.setText(f"🧹 {translations.get_text('clear_logs')}")
        
        # Принудительное обновление размеров
        self.settings_tabs.adjustSize()
        self.header.adjustSize()
        self.adjustSize()
        self.update()
    
    def log_message(self, message):
        """Добавление сообщения в лог с цветовой раскраской"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        # Определение цвета на основе типа сообщения
        if message.startswith('🚀') or message.startswith('🎉'):
            color = '#2ecc71'  # Зеленый для успеха
        elif message.startswith('⚠️'):
            color = '#f39c12'  # Оранжевый для предупреждений
        elif message.startswith('🔥') or message.startswith('❌'):
            color = '#e74c3c'  # Красный для ошибок
        elif message.startswith('✅'):
            color = '#27ae60'  # Темно-зеленый для успешных файлов
        elif message.startswith('✗'):
            color = '#c0392b'  # Темно-красный для ошибок файлов
        elif message.startswith('📊') or message.startswith('📁'):
            color = '#3498db'  # Синий для информации
        else:
            color = '#ecf0f1'  # Белый для обычных сообщений
        
        formatted_message = f'<span style="color: #95a5a6;">[{timestamp}]</span> <span style="color: {color};">{message}</span>'
        self.log_text.append(formatted_message)
        
        # Автопрокрутка к концу
        cursor = self.log_text.textCursor()
        cursor.movePosition(cursor.End)
        self.log_text.setTextCursor(cursor)
    
    def closeEvent(self, event):
        """Обработка закрытия окна"""
        self.handlers.closeEvent(event)
