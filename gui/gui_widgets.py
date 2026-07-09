# -*- coding: utf-8 -*-
"""
GUI Widgets for Garmin Export Plugin
Виджеты графического интерфейса для плагина экспорта в Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""

import json

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton, QComboBox,
    QCheckBox, QSpinBox, QTextEdit, QListWidget, QListWidgetItem,
    QTableWidget, QTableWidgetItem, QHeaderView, QFrame
)
from qgis.PyQt.QtGui import QFont

from .gui_components import create_styled_button, create_info_label, ModernButton


def get_default_mapping_json():
    """JSON-сопоставление по умолчанию (единый источник - StyleMapper)"""
    from ..core.style_mapper import StyleMapper
    return json.dumps(StyleMapper()._get_default_mapping(),
                      indent=2, ensure_ascii=False)


class HeaderWidget(QFrame):
    """Виджет градиентного заголовка (идентичен референсному плагину)"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(90)
        self.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                            stop:0 #3498db, stop:1 #2ecc71);
                border-radius: 10px;
                margin: 5px;
            }
        """)
        self.setupUi()

    def setupUi(self):
        """Настройка интерфейса заголовка"""
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(20, 15, 20, 15)
        main_layout.setSpacing(20)

        # Заголовок
        self.title_label = QLabel("🎯 Garmin Export Plugin")
        self.title_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 18px;
                font-weight: bold;
                background: transparent;
            }
        """)

        # Правая панель с элементами управления
        self.controls_widget = QWidget()
        controls_layout = QHBoxLayout(self.controls_widget)
        controls_layout.setContentsMargins(0, 0, 0, 0)
        controls_layout.setSpacing(15)

        self.createLanguageSelector(controls_layout)
        self.createDonationButton(controls_layout)
        self.createAuthorButton(controls_layout)

        main_layout.addWidget(self.title_label)
        main_layout.addStretch()
        main_layout.addWidget(self.controls_widget)

    def createLanguageSelector(self, layout):
        """Создание селектора языка"""
        lang_container = QWidget()
        lang_layout = QHBoxLayout(lang_container)
        lang_layout.setContentsMargins(0, 0, 0, 0)
        lang_layout.setSpacing(8)

        lang_icon = QLabel("🌐")
        lang_icon.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 16px;
                background: transparent;
                min-width: 20px;
                min-height: 20px;
            }
        """)

        from qgis.PyQt.QtGui import QColor
        from ..translation_manager import translations

        self.language_combo = QComboBox()
        self.language_combo.setFixedSize(165, 32)

        # Заполняем языки из менеджера переводов (единый источник).
        # ВАЖНО: цвет текста и фона КАЖДОГО пункта задаётся на уровне модели
        # (ForegroundRole/BackgroundRole). QSS-правило QComboBox QAbstractItemView
        # на некоторых сборках Qt/Windows НЕ доходит до всплывающего списка, а
        # цвет color:white из стиля комбо наследуется пунктами — получался
        # белый текст на белом фоне (невидимые названия). Роли модели уважает
        # делегат отрисовки на всех платформах.
        dark = QColor('#2c3e50')
        white = QColor('#ffffff')
        for code, label in translations.get_language_labels():
            self.language_combo.addItem(label, code)
            i = self.language_combo.count() - 1
            self.language_combo.setItemData(i, dark, Qt.ForegroundRole)
            self.language_combo.setItemData(i, white, Qt.BackgroundRole)

        # Устанавливаем текущий язык
        current = translations.get_current_language()
        index = self.language_combo.findData(current)
        if index >= 0:
            self.language_combo.setCurrentIndex(index)

        # Само поле комбобокса — тёмный текст на почти белом фоне (читается
        # на градиентной шапке; исключает эффект «белое на белом»).
        self.language_combo.setStyleSheet("""
            QComboBox {
                background: rgba(255, 255, 255, 0.95);
                color: #2c3e50;
                border: 2px solid rgba(255, 255, 255, 0.6);
                border-radius: 6px;
                padding: 4px 10px;
                font-weight: bold;
                font-size: 11px;
            }
            QComboBox:hover {
                background: #ffffff;
                border-color: #ffffff;
            }
            QComboBox::drop-down {
                border: none;
                width: 20px;
                background: transparent;
            }
            QComboBox QAbstractItemView {
                background-color: #ffffff;
                color: #2c3e50;
                border: 2px solid #bdc3c7;
                outline: none;
                selection-background-color: #3498db;
                selection-color: #ffffff;
            }
        """)

        lang_layout.addWidget(lang_icon)
        lang_layout.addWidget(self.language_combo)
        layout.addWidget(lang_container)

    def createDonationButton(self, layout):
        """Создание кнопки поддержки"""
        from ..translation_manager import translations

        self.donation_button = ModernButton(f"☕ {translations.get_text('header_support')}")
        self.donation_button.setFixedSize(120, 32)
        self.donation_button.setToolTip("❤️ Поддержите разработку плагина!")
        self.donation_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 rgba(244, 93, 34, 0.9),
                                            stop:1 rgba(230, 81, 0, 0.9));
                color: white;
                border: 2px solid rgba(255, 255, 255, 0.3);
                border-radius: 8px;
                font-weight: bold;
                font-size: 11px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 rgba(244, 93, 34, 1.0),
                                            stop:1 rgba(230, 81, 0, 1.0));
                border-color: rgba(255, 255, 255, 0.5);
            }
        """)
        layout.addWidget(self.donation_button)

    def createAuthorButton(self, layout):
        """Создание кнопки автора"""
        from ..translation_manager import translations

        self.author_button = ModernButton(f"👤 {translations.get_text('header_about_author')}")
        self.author_button.setFixedSize(100, 32)
        self.author_button.setToolTip("📝 Информация об авторе плагина")
        self.author_button.setStyleSheet("""
            QPushButton {
                background: rgba(255, 255, 255, 0.2);
                color: white;
                border: 2px solid rgba(255, 255, 255, 0.3);
                border-radius: 8px;
                font-weight: bold;
                font-size: 11px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background: rgba(255, 255, 255, 0.3);
                border-color: rgba(255, 255, 255, 0.5);
            }
        """)
        layout.addWidget(self.author_button)


class LayerSelectionWidget(QWidget):
    """Виджет выбора слоёв для экспорта"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        """Настройка интерфейса выбора слоёв"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        self.layers_group = QGroupBox("📁 Выбор слоёв для экспорта")
        group_layout = QVBoxLayout(self.layers_group)
        group_layout.setSpacing(10)

        buttons_layout = QHBoxLayout()

        self.select_all_button = create_styled_button("Выбрать все", "success-button", "✅")
        self.deselect_all_button = create_styled_button("Снять выделение", "warning-button", "❌")
        self.refresh_button = create_styled_button("Обновить", icon_text="🔄")

        buttons_layout.addWidget(self.select_all_button)
        buttons_layout.addWidget(self.deselect_all_button)
        buttons_layout.addWidget(self.refresh_button)
        buttons_layout.addStretch()

        self.layers_list = QListWidget()
        self.layers_list.setMinimumHeight(200)
        self.layers_list.setStyleSheet("""
            QListWidget::item {
                padding: 8px;
                border-bottom: 1px solid #ecf0f1;
            }
            QListWidget::item:hover {
                background-color: #ebf3fd;
            }
        """)

        self.info_label = create_info_label(
            "Выберите слои проекта для экспорта в формат Garmin IMG")

        group_layout.addWidget(self.info_label)
        group_layout.addLayout(buttons_layout)
        group_layout.addWidget(self.layers_list)

        layout.addWidget(self.layers_group)

    def add_layer_item(self, layer_id, layer_name, layer_type, is_checked=False):
        """Добавляет элемент слоя в список (идентификация по layer_id)"""
        item = QListWidgetItem()

        icon_map = {
            'Point': '📍',
            'LineString': '〰️',
            'Polygon': '⬜',
            'Unknown': '❓'
        }
        icon = icon_map.get(layer_type, '❓')

        item.setText(f"{icon} {layer_name} ({layer_type})")
        item.setData(Qt.UserRole, {
            'id': layer_id, 'name': layer_name, 'type': layer_type})
        item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        item.setCheckState(Qt.Checked if is_checked else Qt.Unchecked)

        self.layers_list.addItem(item)

    def get_selected_layers(self):
        """Возвращает список выбранных слоёв"""
        selected = []
        for i in range(self.layers_list.count()):
            item = self.layers_list.item(i)
            if item.checkState() == Qt.Checked:
                selected.append(item.data(Qt.UserRole))
        return selected

    def select_all_layers(self):
        """Выбирает все слои"""
        for i in range(self.layers_list.count()):
            self.layers_list.item(i).setCheckState(Qt.Checked)

    def deselect_all_layers(self):
        """Снимает выделение со всех слоёв"""
        for i in range(self.layers_list.count()):
            self.layers_list.item(i).setCheckState(Qt.Unchecked)


class ExportSettingsWidget(QWidget):
    """Виджет настроек экспорта (выходные файлы и параметры карты)"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        """Настройка интерфейса настроек экспорта"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(15)

        self.createOutputSection()
        self.createMapSettingsSection()

        layout.addWidget(self.output_group)
        layout.addWidget(self.map_group)
        layout.addStretch()

    def createOutputSection(self):
        """Создание секции выходных файлов"""
        self.output_group = QGroupBox("📤 Выходные файлы")
        layout = QGridLayout(self.output_group)
        layout.setSpacing(10)

        self.output_folder_label = QLabel("Выходная папка:")
        layout.addWidget(self.output_folder_label, 0, 0)

        folder_layout = QHBoxLayout()
        self.output_folder_line = QLineEdit()
        self.output_folder_line.setPlaceholderText("Выберите папку для сохранения IMG файла")
        self.output_folder_button = create_styled_button("Обзор...", icon_text="📂")

        folder_layout.addWidget(self.output_folder_line)
        folder_layout.addWidget(self.output_folder_button)
        layout.addLayout(folder_layout, 0, 1)

        self.output_filename_label = QLabel("Имя файла карты:")
        layout.addWidget(self.output_filename_label, 1, 0)
        self.output_filename_line = QLineEdit()
        self.output_filename_line.setPlaceholderText("map")
        self.output_filename_line.setText("map")
        layout.addWidget(self.output_filename_line, 1, 1)

    def createMapSettingsSection(self):
        """Создание секции настроек карты"""
        self.map_group = QGroupBox("🗺️ Настройки карты")
        layout = QGridLayout(self.map_group)
        layout.setSpacing(10)

        self.family_id_label = QLabel("Family ID:")
        layout.addWidget(self.family_id_label, 0, 0)
        self.family_id_spin = QSpinBox()
        self.family_id_spin.setRange(1, 65535)
        self.family_id_spin.setValue(1234)
        self.family_id_spin.setToolTip(
            "Идентификатор семейства карт. Должен быть уникален среди "
            "карт на устройстве.")
        layout.addWidget(self.family_id_spin, 0, 1)

        self.map_id_label = QLabel("Map ID:")
        layout.addWidget(self.map_id_label, 0, 2)
        self.map_id_spin = QSpinBox()
        self.map_id_spin.setRange(1, 99999999)
        self.map_id_spin.setValue(12340001)
        self.map_id_spin.setToolTip(
            "8-значный номер тайла карты. Должен быть уникален.")
        layout.addWidget(self.map_id_spin, 0, 3)

        self.map_name_label = QLabel("Название карты:")
        layout.addWidget(self.map_name_label, 1, 0)
        self.map_name_line = QLineEdit()
        self.map_name_line.setPlaceholderText("QGIS Map")
        self.map_name_line.setText("QGIS Map")
        layout.addWidget(self.map_name_line, 1, 1, 1, 3)

        self.map_description_label = QLabel("Описание:")
        layout.addWidget(self.map_description_label, 2, 0)
        self.map_description_line = QLineEdit()
        self.map_description_line.setPlaceholderText("Map created with QGIS Garmin Export Plugin")
        layout.addWidget(self.map_description_line, 2, 1, 1, 3)

        checkbox_layout = QHBoxLayout()
        self.transparent_cb = QCheckBox("Прозрачная карта")
        self.transparent_cb.setToolTip(
            "Прозрачная карта отображается поверх других карт "
            "(например, поверх базовой карты).")
        self.routing_cb = QCheckBox("Поддержка маршрутизации")
        self.routing_cb.setToolTip(
            "Записать данные NET/NOD (--route). Работает, если данные "
            "содержат дорожную сеть.")

        checkbox_layout.addWidget(self.transparent_cb)
        checkbox_layout.addWidget(self.routing_cb)
        checkbox_layout.addStretch()

        layout.addLayout(checkbox_layout, 3, 0, 1, 4)


class StyleMappingWidget(QWidget):
    """Виджет настройки сопоставления стилей"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        """Настройка интерфейса сопоставления стилей"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        self.mapping_group = QGroupBox("🎨 JSON-сопоставление стилей")
        group_layout = QVBoxLayout(self.mapping_group)
        group_layout.setSpacing(10)

        buttons_layout = QHBoxLayout()

        self.load_mapping_button = create_styled_button("Загрузить", "success-button", "📂")
        self.save_mapping_button = create_styled_button("Сохранить", "warning-button", "💾")
        self.edit_mapping_button = create_styled_button("Редактировать", icon_text="✏️")
        self.reset_mapping_button = create_styled_button("По умолчанию", "danger-button", "🔄")

        buttons_layout.addWidget(self.load_mapping_button)
        buttons_layout.addWidget(self.save_mapping_button)
        buttons_layout.addWidget(self.edit_mapping_button)
        buttons_layout.addWidget(self.reset_mapping_button)
        buttons_layout.addStretch()

        self.mapping_text = QTextEdit()
        self.mapping_text.setMinimumHeight(200)
        self.mapping_text.setFont(QFont("Consolas", 10))
        self.mapping_text.setPlaceholderText("JSON-сопоставление стилей будет загружено автоматически...")

        self.info_label = create_info_label(
            "Настройте соответствие между слоями QGIS и типами объектов Garmin")

        group_layout.addWidget(self.info_label)
        group_layout.addLayout(buttons_layout)
        group_layout.addWidget(self.mapping_text)

        layout.addWidget(self.mapping_group)

    def get_mapping_json(self):
        """Возвращает JSON сопоставления"""
        return self.mapping_text.toPlainText()

    def set_mapping_json(self, json_text):
        """Устанавливает JSON сопоставления"""
        self.mapping_text.setPlainText(json_text)

    def get_default_mapping(self):
        """Возвращает сопоставление по умолчанию"""
        return get_default_mapping_json()


class ControlButtonsWidget(QWidget):
    """Виджет кнопок управления"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        """Настройка интерфейса кнопок управления"""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(15)

        self.compile_button = create_styled_button("Скомпилировать карту", "success-button", "🚀")
        self.compile_button.setMinimumHeight(40)
        self.compile_button.setStyleSheet(self.compile_button.styleSheet() + """
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                padding: 12px 24px;
            }
        """)

        self.cancel_button = create_styled_button("Отмена", "danger-button", "❌")
        self.cancel_button.setEnabled(False)

        self.clear_log_button = create_styled_button("Очистить логи", "warning-button", "🧹")

        layout.addWidget(self.compile_button)
        layout.addWidget(self.cancel_button)
        layout.addStretch()
        layout.addWidget(self.clear_log_button)


class LogTextWidget(QTextEdit):
    """Виджет для отображения логов"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        """Настройка виджета логов"""
        self.setReadOnly(True)
        self.setMinimumHeight(150)
        self.setFont(QFont("Consolas", 9))
        self.setStyleSheet("""
            QTextEdit {
                background-color: #2c3e50;
                color: #ecf0f1;
                border: 2px solid #34495e;
                border-radius: 6px;
                padding: 8px;
            }
        """)

        from ..translation_manager import translations
        self.append("🎯 <span style='color: #3498db;'>{0}</span>".format(
            translations.get_text('log_ready')))
        self.append("📋 <span style='color: #95a5a6;'>{0}</span>".format(
            translations.get_text('log_hint')))


class ResultsTableWidget(QTableWidget):
    """Виджет таблицы результатов"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        """Настройка таблицы результатов"""
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(["📄 Слой", "📊 Статус", "💬 Сообщение"])

        header = self.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        self.setAlternatingRowColors(True)
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.setMinimumHeight(150)

        self.verticalHeader().setVisible(False)

    def add_result(self, layer_name, status, message):
        """Добавляет результат в таблицу"""
        row = self.rowCount()
        self.insertRow(row)

        status_icons = {
            'success': '✅',
            'error': '❌',
            'warning': '⚠️',
            'processing': '⏳'
        }

        icon = status_icons.get(status, '❓')

        self.setItem(row, 0, QTableWidgetItem(layer_name))
        self.setItem(row, 1, QTableWidgetItem(f"{icon} {status.title()}"))
        self.setItem(row, 2, QTableWidgetItem(message))

    def clear_results(self):
        """Очищает таблицу результатов"""
        self.setRowCount(0)


class LevelSettingsWidget(QWidget):
    """Виджет настройки уровней карты"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        """Настройка интерфейса уровней"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        self.levels_group = QGroupBox("📊 Уровни отображения карты")
        group_layout = QGridLayout(self.levels_group)
        group_layout.setSpacing(10)

        self.level_0_cb = QCheckBox("Уровень 0 (детальный)")
        self.level_1_cb = QCheckBox("Уровень 1 (основной)")
        self.level_2_cb = QCheckBox("Уровень 2 (средний)")
        self.level_3_cb = QCheckBox("Уровень 3 (обзорный)")

        self.level_0_cb.setChecked(True)
        self.level_1_cb.setChecked(True)
        self.level_2_cb.setChecked(True)
        self.level_3_cb.setChecked(True)

        # Уровень 0 обязателен: без детального уровня карта пуста
        self.level_0_cb.setEnabled(False)

        group_layout.addWidget(self.level_0_cb, 0, 0)
        group_layout.addWidget(self.level_1_cb, 0, 1)
        group_layout.addWidget(self.level_2_cb, 1, 0)
        group_layout.addWidget(self.level_3_cb, 1, 1)

        self.info_label = create_info_label(
            "Уровни определяют, при каких масштабах объекты видны на "
            "устройстве. Уровень 0 (разрешение 24) - самый детальный, "
            "уровень 3 (разрешение 18) - обзорный. В сопоставлении стилей "
            "параметр \"level\" задаёт, до какого уровня виден объект.")
        group_layout.addWidget(self.info_label, 2, 0, 1, 2)

        layout.addWidget(self.levels_group)

    def get_enabled_levels(self):
        """Возвращает список включенных уровней"""
        levels = [0]
        if self.level_1_cb.isChecked():
            levels.append(1)
        if self.level_2_cb.isChecked():
            levels.append(2)
        if self.level_3_cb.isChecked():
            levels.append(3)
        return levels
