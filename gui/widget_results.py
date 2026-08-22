# -*- coding: utf-8 -*-
"""Mapping, controls, log, result and level widgets."""

from qgis.PyQt.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox, QLabel,
    QTextEdit, QTableWidget, QTableWidgetItem, QCheckBox,
    QAbstractItemView, QHeaderView,
)
from qgis.PyQt.QtGui import QFont

from .gui_components import create_styled_button, create_info_label
from .widget_i18n import (
    retranslate_style_mapping, retranslate_control_buttons, retranslate_log,
    retranslate_results, retranslate_levels,
)
from ..translation_manager import translations
from ..qgis_compat import qt_class_enum, qt_enum


class StyleMappingWidget(QWidget):
    """JSON style mapping editor controls."""

    retranslateUi = retranslate_style_mapping

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.retranslateUi()

    def setupUi(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)
        self.mapping_group = QGroupBox()
        group = QVBoxLayout(self.mapping_group)
        group.setSpacing(10)
        self.info_label = create_info_label('')
        buttons = QHBoxLayout()
        self.load_mapping_button = create_styled_button(
            '', 'success-button', '📂')
        self.save_mapping_button = create_styled_button(
            '', 'warning-button', '💾')
        self.edit_mapping_button = create_styled_button('', icon_text='✏️')
        self.reset_mapping_button = create_styled_button(
            '', 'danger-button', '🔄')
        for button in (self.load_mapping_button, self.save_mapping_button,
                       self.edit_mapping_button, self.reset_mapping_button):
            buttons.addWidget(button)
        buttons.addStretch()
        self.mapping_text = QTextEdit()
        self.mapping_text.setMinimumHeight(200)
        self.mapping_text.setFont(QFont('Consolas', 10))
        group.addWidget(self.info_label)
        group.addLayout(buttons)
        group.addWidget(self.mapping_text)
        layout.addWidget(self.mapping_group)

    def get_mapping_json(self):
        return self.mapping_text.toPlainText()

    def set_mapping_json(self, json_text):
        self.mapping_text.setPlainText(json_text)

    def get_default_mapping(self):
        from ..core.style_mapper import StyleMapper
        import json
        return json.dumps(StyleMapper()._get_default_mapping(),
                          indent=2, ensure_ascii=False)


class ControlButtonsWidget(QWidget):
    """Compilation, cancellation and log controls."""

    retranslateUi = retranslate_control_buttons

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.retranslateUi()

    def setupUi(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(15)
        self.compile_button = create_styled_button('', 'success-button', '🚀')
        self.compile_button.setMinimumHeight(40)
        self.compile_button.setStyleSheet(
            self.compile_button.styleSheet() +
            ' QPushButton { font-size: 14px; font-weight: bold;'
            ' padding: 12px 24px; }')
        self.cancel_button = create_styled_button('', 'danger-button', '❌')
        self.cancel_button.setEnabled(False)
        self.clear_log_button = create_styled_button(
            '', 'warning-button', '🧹')
        layout.addWidget(self.compile_button)
        layout.addWidget(self.cancel_button)
        layout.addStretch()
        layout.addWidget(self.clear_log_button)


class LogTextWidget(QTextEdit):
    """Read-only operation log preserving runtime messages."""

    retranslateUi = retranslate_log

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.retranslateUi()

    def setupUi(self):
        self.setReadOnly(True)
        self.setMinimumHeight(150)
        self.setFont(QFont('Consolas', 9))
        self.setStyleSheet(
            'QTextEdit { background-color: #2c3e50; color: #ecf0f1;'
            ' border: 2px solid #34495e; border-radius: 6px; padding: 8px; }')
        self._initial_messages = True


class ResultsTableWidget(QTableWidget):
    """Table of processed layer results."""

    retranslateUi = retranslate_results

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.retranslateUi()

    def setupUi(self):
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(['', '', ''])
        header = self.horizontalHeader()
        header.setStretchLastSection(True)
        for index in (0, 1):
            header.setSectionResizeMode(
                index, qt_class_enum(QHeaderView, 'ResizeMode',
                                     'ResizeToContents'))
        header.setSectionResizeMode(
            2, qt_class_enum(QHeaderView, 'ResizeMode', 'Stretch'))
        self.setAlternatingRowColors(True)
        self.setSelectionBehavior(qt_class_enum(
            QAbstractItemView, 'SelectionBehavior', 'SelectRows'))
        self.setMinimumHeight(150)
        self.verticalHeader().setVisible(False)

    def add_result(self, layer_name, status, message):
        icons = {'success': '✅', 'error': '❌', 'warning': '⚠️',
                 'processing': '⏳'}
        row = self.rowCount()
        self.insertRow(row)
        self.setItem(row, 0, QTableWidgetItem(layer_name))
        item = QTableWidgetItem(
            '{0} {1}'.format(icons.get(status, '❓'),
                             translations.get_text(status)))
        item.setData(qt_enum('ItemDataRole', 'UserRole'), status)
        self.setItem(row, 1, item)
        self.setItem(row, 2, QTableWidgetItem(message))

    def clear_results(self):
        self.setRowCount(0)


class LevelSettingsWidget(QWidget):
    """Map level checkboxes."""

    retranslateUi = retranslate_levels

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.retranslateUi()

    def setupUi(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)
        self.levels_group = QGroupBox()
        grid = QGridLayout(self.levels_group)
        grid.setSpacing(10)
        self.level_0_cb = QCheckBox()
        self.level_1_cb = QCheckBox()
        self.level_2_cb = QCheckBox()
        self.level_3_cb = QCheckBox()
        for checkbox in (self.level_0_cb, self.level_1_cb,
                         self.level_2_cb, self.level_3_cb):
            checkbox.setChecked(True)
        self.level_0_cb.setEnabled(False)
        grid.addWidget(self.level_0_cb, 0, 0)
        grid.addWidget(self.level_1_cb, 0, 1)
        grid.addWidget(self.level_2_cb, 1, 0)
        grid.addWidget(self.level_3_cb, 1, 1)
        self.info_label = create_info_label('')
        grid.addWidget(self.info_label, 2, 0, 1, 2)
        layout.addWidget(self.levels_group)

    def get_enabled_levels(self):
        levels = [0]
        if self.level_1_cb.isChecked():
            levels.append(1)
        if self.level_2_cb.isChecked():
            levels.append(2)
        if self.level_3_cb.isChecked():
            levels.append(3)
        return levels
