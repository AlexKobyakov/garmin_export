# -*- coding: utf-8 -*-
"""
Main GUI Dialog for Garmin Export Plugin
Главное диалоговое окно для плагина экспорта в Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
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
from .gui_mkgmap_widgets import (
    MkgmapToolsWidget, AdvancedOptionsWidget, TypSettingsWidget
)
from .gui_handlers import GuiEventHandlers
from ..core.layer_manager import LayerManager


class GarminExportDialog(QDialog):
    """Главное диалоговое окно экспорта в Garmin с модульной архитектурой"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.worker = None
        self.worker_thread = None

        # Применяем сохранённый язык ДО построения интерфейса,
        # чтобы комбобокс и все подписи сразу отобразились правильно
        self._applySavedLanguage()

        self.setupWindow()
        self.setupUi()

        self.handlers = GuiEventHandlers(self)

        self.connectSignals()
        self.applyStyles()

        self.loadProjectLayers()
        self.loadDefaultSettings()

        # Восстанавливаем сохранённые настройки
        self.handlers.loadSettings()

        self.updateLanguage()
        self._applyLayoutDirection()

    def _applySavedLanguage(self):
        """Применяет сохранённый язык интерфейса, если он выбирался ранее"""
        from ..core.settings_manager import SettingsManager
        from ..translation_manager import translations

        saved = SettingsManager().get('language')
        if saved:
            translations.set_language(saved)

    def _applyLayoutDirection(self):
        """Направление письма по текущему языку (RTL для арабского)"""
        from qgis.PyQt.QtCore import Qt
        from ..translation_manager import translations

        self.setLayoutDirection(
            Qt.RightToLeft if translations.is_rtl() else Qt.LeftToRight)

    def setupWindow(self):
        """Настройка основных параметров окна"""
        from ..translation_manager import translations

        self.setWindowTitle(f"🎯 {translations.get_text('window_title')}")
        self.setMinimumSize(1100, 820)
        self.resize(1300, 950)

        flags = Qt.Dialog
        flags |= Qt.WindowTitleHint
        flags |= Qt.WindowCloseButtonHint
        flags |= Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)

    def setupUi(self):
        """Создание основного интерфейса"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        self.createHeader()
        self.createMainContent()

        main_layout.addWidget(self.header)
        main_layout.addWidget(self.main_splitter, 1)

    def createHeader(self):
        """Создание заголовка"""
        self.header = HeaderWidget()

    def createMainContent(self):
        """Создание основного содержимого"""
        self.main_splitter = QSplitter(Qt.Vertical)
        self.main_splitter.setChildrenCollapsible(False)

        self.createSettingsArea()
        self.createControlButtonsArea()
        self.createResultsArea()

        self.main_splitter.addWidget(self.settings_area)
        self.main_splitter.addWidget(self.control_buttons_area)
        self.main_splitter.addWidget(self.results_area)
        self.main_splitter.setSizes([520, 80, 250])

    def createSettingsArea(self):
        """Создание области настроек"""
        self.settings_scroll = QScrollArea()
        self.settings_scroll.setWidgetResizable(True)
        self.settings_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.settings_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        settings_container = QWidget()
        settings_layout = QVBoxLayout(settings_container)
        settings_layout.setContentsMargins(15, 15, 15, 15)
        settings_layout.setSpacing(20)

        self.createSettingsTabs()

        settings_layout.addWidget(self.settings_tabs)

        self.settings_scroll.setWidget(settings_container)
        self.settings_area = self.settings_scroll

    def createControlButtonsArea(self):
        """Создание фиксированной области кнопок управления"""
        self.control_buttons_area = QFrame()
        self.control_buttons_area.setFixedHeight(80)
        self.control_buttons_area.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border-top: 2px solid #e9ecef;
                border-bottom: 2px solid #e9ecef;
            }
        """)

        buttons_layout = QHBoxLayout(self.control_buttons_area)
        buttons_layout.setContentsMargins(20, 15, 20, 15)
        buttons_layout.setSpacing(15)

        self.control_buttons = ControlButtonsWidget()
        self.control_buttons.setContentsMargins(0, 0, 0, 0)

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
                padding: 8px 14px;
                margin-right: 2px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                min-width: 120px;
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

        # Создаём виджеты вкладок
        self.layer_selection = LayerSelectionWidget()
        self.export_settings = ExportSettingsWidget()
        self.tools_widget = MkgmapToolsWidget()
        self.mapping_widget = StyleMappingWidget()
        self.typ_settings = TypSettingsWidget()
        self.level_settings = LevelSettingsWidget()
        self.advanced_options = AdvancedOptionsWidget()

        self.settings_tabs.addTab(
            self._wrap_tab(self.layer_selection), "📁 Слои")
        self.settings_tabs.addTab(
            self._wrap_tab(self.export_settings), "⚙️ Экспорт")
        self.settings_tabs.addTab(
            self._wrap_tab(self.tools_widget), "🧰 Инструменты")
        self.settings_tabs.addTab(
            self._wrap_tab(self.mapping_widget), "🎨 Стили")
        self.settings_tabs.addTab(
            self._wrap_tab(self.typ_settings), "🖌️ TYP")
        self.settings_tabs.addTab(
            self._wrap_tab(self.level_settings), "📊 Уровни")
        self.settings_tabs.addTab(
            self._wrap_tab(self.advanced_options), "🔧 Тюнинг")

    def _wrap_tab(self, widget):
        """Оборачивает виджет вкладки в контейнер с отступами и растяжкой"""
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        layout.addWidget(widget)
        layout.addStretch()
        return container

    def createResultsArea(self):
        """Создание области результатов"""
        self.results_area = QWidget()
        results_layout = QVBoxLayout(self.results_area)
        results_layout.setContentsMargins(15, 15, 15, 15)
        results_layout.setSpacing(15)

        self.createProgressSection()
        self.createResultsTabs()

        results_layout.addWidget(self.progress_frame)
        results_layout.addWidget(self.results_tabs, 1)

    def createProgressSection(self):
        """Создание секции прогресса"""
        self.progress_frame = QFrame()
        progress_layout = QVBoxLayout(self.progress_frame)
        progress_layout.setContentsMargins(0, 0, 0, 0)

        self.progress_label = QLabel("📊 Прогресс")
        self.progress_label.setStyleSheet("font-weight: bold; color: #2c3e50;")

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

        self.log_text = LogTextWidget()
        self.results_table = ResultsTableWidget()

        self.results_tabs.addTab(self.log_text, "📋 Логи")
        self.results_tabs.addTab(self.results_table, "📈 Результаты")

    def connectSignals(self):
        """Подключение сигналов к обработчикам"""
        # Заголовок
        self.header.language_combo.currentIndexChanged.connect(
            self.handlers.onLanguageChanged)
        self.header.donation_button.clicked.connect(self.handlers.showDonation)
        self.header.author_button.clicked.connect(self.handlers.showAuthorInfo)

        # Выбор слоёв
        self.layer_selection.select_all_button.clicked.connect(
            self.handlers.selectAllLayers)
        self.layer_selection.deselect_all_button.clicked.connect(
            self.handlers.deselectAllLayers)
        self.layer_selection.refresh_button.clicked.connect(
            self.handlers.refreshLayers)

        # Настройки экспорта
        self.export_settings.output_folder_button.clicked.connect(
            self.handlers.selectOutputFolder)

        # Инструменты mkgmap
        self.tools_widget.mkgmap_browse_button.clicked.connect(
            self.handlers.selectMkgmapPath)
        self.tools_widget.mkgmap_download_button.clicked.connect(
            self.handlers.downloadMkgmap)
        self.tools_widget.splitter_browse_button.clicked.connect(
            self.handlers.selectSplitterPath)
        self.tools_widget.splitter_download_button.clicked.connect(
            self.handlers.downloadSplitter)
        self.tools_widget.java_browse_button.clicked.connect(
            self.handlers.selectJavaPath)
        self.tools_widget.java_detect_button.clicked.connect(
            self.handlers.detectJava)
        self.tools_widget.mkgmap_path_line.editingFinished.connect(
            self.handlers.onMkgmapPathChanged)

        # Сопоставление стилей
        self.mapping_widget.load_mapping_button.clicked.connect(
            self.handlers.loadMapping)
        self.mapping_widget.save_mapping_button.clicked.connect(
            self.handlers.saveMapping)
        self.mapping_widget.edit_mapping_button.clicked.connect(
            self.handlers.editMapping)
        self.mapping_widget.reset_mapping_button.clicked.connect(
            self.handlers.resetMapping)

        # TYP
        self.typ_settings.typ_file_browse_button.clicked.connect(
            self.handlers.selectTypFile)

        # Кнопки управления
        self.control_buttons.compile_button.clicked.connect(
            self.handlers.startCompilation)
        self.control_buttons.cancel_button.clicked.connect(
            self.handlers.cancelCompilation)
        self.control_buttons.clear_log_button.clicked.connect(
            self.handlers.clearLogs)

    def applyStyles(self):
        """Применение глобальных стилей"""
        self.setStyleSheet(apply_global_styles())

    def loadProjectLayers(self):
        """Загрузка слоёв проекта"""
        layers = LayerManager.get_project_layers()

        self.layer_selection.layers_list.clear()

        for layer_info in layers:
            self.layer_selection.add_layer_item(
                layer_info['id'],
                layer_info['name'],
                layer_info['type'],
                is_checked=True
            )

        self.log_message(f"📁 Загружено слоёв проекта: {len(layers)}")

    def loadDefaultSettings(self):
        """Загрузка настроек по умолчанию"""
        default_mapping = self.mapping_widget.get_default_mapping()
        self.mapping_widget.set_mapping_json(default_mapping)

    def updateLanguage(self):
        """Обновление языка интерфейса"""
        from ..translation_manager import translations
        t = translations.get_text

        self.setWindowTitle(f"🎯 {t('window_title')}")

        # Кнопки в заголовке
        self.header.donation_button.setText(f"☕ {t('header_support')}")
        self.header.author_button.setText(f"👤 {t('header_about_author')}")

        # Табы настроек
        self.settings_tabs.setTabText(0, f"📁 {t('tab_layers')}")
        self.settings_tabs.setTabText(1, f"⚙️ {t('tab_export')}")
        self.settings_tabs.setTabText(2, f"🧰 {t('tab_tools')}")
        self.settings_tabs.setTabText(3, f"🎨 {t('tab_styles')}")
        self.settings_tabs.setTabText(4, f"🖌️ {t('tab_typ')}")
        self.settings_tabs.setTabText(5, f"📊 {t('tab_levels')}")
        self.settings_tabs.setTabText(6, f"🔧 {t('tab_tuning')}")

        # Кнопки в заголовке (подсказки)
        self.header.donation_button.setToolTip("❤️ " + t('support_tip'))
        self.header.author_button.setToolTip("📝 " + t('author_tip'))

        # Выбор слоёв
        self.layer_selection.layers_group.setTitle(f"📁 {t('select_layers')}")
        self.layer_selection.select_all_button.setText(f"✅ {t('select_all_layers')}")
        self.layer_selection.deselect_all_button.setText(f"❌ {t('deselect_all_layers')}")
        self.layer_selection.refresh_button.setText(f"🔄 {t('refresh')}")
        self.layer_selection.info_label.setText(t('layers_info'))

        # Настройки экспорта
        self.export_settings.output_group.setTitle(f"📤 {t('output_files')}")
        self.export_settings.output_folder_label.setText(t('output_folder'))
        self.export_settings.output_folder_button.setText(f"📂 {t('browse')}")
        self.export_settings.output_folder_line.setPlaceholderText(t('output_folder_placeholder'))
        self.export_settings.output_filename_label.setText(t('output_file_name'))
        self.export_settings.map_group.setTitle(f"🗺️ {t('map_settings')}")
        self.export_settings.family_id_label.setText(t('family_id'))
        self.export_settings.family_id_spin.setToolTip(t('family_id_tip'))
        self.export_settings.map_id_label.setText(t('map_id'))
        self.export_settings.map_id_spin.setToolTip(t('map_id_tip'))
        self.export_settings.map_name_label.setText(t('map_name'))
        self.export_settings.map_description_label.setText(t('map_description'))
        self.export_settings.map_description_line.setPlaceholderText(t('map_description_placeholder'))
        self.export_settings.transparent_cb.setText(t('transparent'))
        self.export_settings.transparent_cb.setToolTip(t('transparent_tip'))
        self.export_settings.routing_cb.setText(t('routing'))
        self.export_settings.routing_cb.setToolTip(t('routing_tip'))

        # Инструменты, Тюнинг, TYP — полностью через retranslateUi виджетов
        self.tools_widget.retranslateUi()
        self.advanced_options.retranslateUi()
        self.typ_settings.retranslateUi()

        # Сопоставление стилей
        self.mapping_widget.mapping_group.setTitle(f"🎨 {t('style_mapping')}")
        self.mapping_widget.load_mapping_button.setText(f"📂 {t('load_mapping')}")
        self.mapping_widget.save_mapping_button.setText(f"💾 {t('save_mapping')}")
        self.mapping_widget.edit_mapping_button.setText(f"✏️ {t('edit_mapping')}")
        self.mapping_widget.reset_mapping_button.setText(f"🔄 {t('default_mapping')}")
        self.mapping_widget.info_label.setText(t('mapping_info'))
        self.mapping_widget.mapping_text.setPlaceholderText(t('mapping_placeholder'))

        # Уровни
        self.level_settings.levels_group.setTitle(f"📊 {t('export_levels')}")
        self.level_settings.level_0_cb.setText(t('level_0'))
        self.level_settings.level_1_cb.setText(t('level_1'))
        self.level_settings.level_2_cb.setText(t('level_2'))
        self.level_settings.level_3_cb.setText(t('level_3'))
        self.level_settings.info_label.setText(t('levels_info'))

        # Прогресс и результаты
        self.progress_label.setText(f"📊 {t('progress')}")
        self.results_tabs.setTabText(0, f"📋 {t('logs')}")
        self.results_tabs.setTabText(1, f"📈 {t('results')}")
        self.results_table.setHorizontalHeaderLabels([
            f"📄 {t('layer')}",
            f"📊 {t('status')}",
            f"💬 {t('message')}"
        ])

        # Кнопки управления
        if not self.control_buttons.compile_button.isEnabled():
            self.control_buttons.compile_button.setText(f"⏳ {t('compiling')}")
        else:
            self.control_buttons.compile_button.setText(f"🚀 {t('compile_map')}")
        self.control_buttons.cancel_button.setText(f"❌ {t('cancel')}")
        self.control_buttons.clear_log_button.setText(f"🧹 {t('clear_logs')}")

        self.update()

    def log_message(self, message):
        """Добавление сообщения в лог с цветовой раскраской"""
        timestamp = datetime.now().strftime('%H:%M:%S')

        if message.startswith('🚀') or message.startswith('🎉'):
            color = '#2ecc71'
        elif message.startswith('⚠️'):
            color = '#f39c12'
        elif message.startswith('🔥') or message.startswith('❌'):
            color = '#e74c3c'
        elif message.startswith('✅'):
            color = '#27ae60'
        elif message.startswith('✗'):
            color = '#c0392b'
        elif message.startswith('📊') or message.startswith('📁'):
            color = '#3498db'
        else:
            color = '#ecf0f1'

        formatted_message = (
            f'<span style="color: #95a5a6;">[{timestamp}]</span> '
            f'<span style="color: {color};">{message}</span>')
        self.log_text.append(formatted_message)

        cursor = self.log_text.textCursor()
        cursor.movePosition(cursor.End)
        self.log_text.setTextCursor(cursor)

    def closeEvent(self, event):
        """Обработка закрытия окна"""
        self.handlers.closeEvent(event)
