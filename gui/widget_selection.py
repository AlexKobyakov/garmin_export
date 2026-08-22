# -*- coding: utf-8 -*-
"""Layer selection and export parameter widgets."""

from qgis.PyQt.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QCheckBox, QSpinBox, QListWidget, QListWidgetItem,
)

from .gui_components import create_styled_button, create_info_label
from .widget_i18n import (
    retranslate_layer_selection, retranslate_export_settings,
)
from ..translation_manager import translations
from ..qgis_compat import qt_enum


class LayerSelectionWidget(QWidget):
    """Selectable list of project layers."""

    retranslateUi = retranslate_layer_selection

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.retranslateUi()

    def setupUi(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)
        self.layers_group = QGroupBox()
        group = QVBoxLayout(self.layers_group)
        group.setSpacing(10)
        buttons = QHBoxLayout()
        self.select_all_button = create_styled_button(
            '', 'success-button', '✅')
        self.deselect_all_button = create_styled_button(
            '', 'warning-button', '❌')
        self.refresh_button = create_styled_button('', icon_text='🔄')
        for button in (self.select_all_button, self.deselect_all_button,
                       self.refresh_button):
            buttons.addWidget(button)
        buttons.addStretch()
        self.layers_list = QListWidget()
        self.layers_list.setMinimumHeight(200)
        self.layers_list.setStyleSheet(
            'QListWidget::item { padding: 8px;'
            ' border-bottom: 1px solid #ecf0f1; }'
            ' QListWidget::item:hover { background-color: #ebf3fd; }')
        self.info_label = create_info_label('')
        group.addWidget(self.info_label)
        group.addLayout(buttons)
        group.addWidget(self.layers_list)
        layout.addWidget(self.layers_group)

    def add_layer_item(
            self, layer_id, layer_name, layer_type, is_checked=False):
        icons = {'Point': '📍', 'LineString': '〰️', 'Polygon': '⬜',
                 'Unknown': '❓'}
        item = QListWidgetItem(
            '{0} {1} ({2})'.format(icons.get(layer_type, '❓'), layer_name,
                                   layer_type))
        item.setData(qt_enum('ItemDataRole', 'UserRole'), {
            'id': layer_id, 'name': layer_name, 'type': layer_type})
        item.setFlags(qt_enum('ItemFlag', 'ItemIsUserCheckable') |
                      qt_enum('ItemFlag', 'ItemIsEnabled'))
        item.setCheckState(qt_enum('CheckState', 'Checked') if is_checked
                           else qt_enum('CheckState', 'Unchecked'))
        self.layers_list.addItem(item)

    def get_selected_layers(self):
        selected = []
        for index in range(self.layers_list.count()):
            item = self.layers_list.item(index)
            if item.checkState() == qt_enum('CheckState', 'Checked'):
                selected.append(item.data(qt_enum('ItemDataRole', 'UserRole')))
        return selected

    def select_all_layers(self):
        for index in range(self.layers_list.count()):
            self.layers_list.item(index).setCheckState(
                qt_enum('CheckState', 'Checked'))

    def deselect_all_layers(self):
        for index in range(self.layers_list.count()):
            self.layers_list.item(index).setCheckState(
                qt_enum('CheckState', 'Unchecked'))


class ExportSettingsWidget(QWidget):
    """Output folder, file and map metadata controls."""

    retranslateUi = retranslate_export_settings

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.retranslateUi()

    def setupUi(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(15)
        self.createOutputSection()
        self.createMapSettingsSection()
        layout.addWidget(self.output_group)
        layout.addWidget(self.map_group)
        layout.addStretch()

    def createOutputSection(self):
        self.output_group = QGroupBox()
        grid = QGridLayout(self.output_group)
        grid.setSpacing(10)
        self.output_folder_label = QLabel()
        self.output_folder_line = QLineEdit()
        self.output_folder_button = create_styled_button('', icon_text='📂')
        folder = QHBoxLayout()
        folder.addWidget(self.output_folder_line)
        folder.addWidget(self.output_folder_button)
        grid.addWidget(self.output_folder_label, 0, 0)
        grid.addLayout(folder, 0, 1)
        self.output_filename_label = QLabel()
        self.output_filename_line = QLineEdit('map')
        grid.addWidget(self.output_filename_label, 1, 0)
        grid.addWidget(self.output_filename_line, 1, 1)

    def createMapSettingsSection(self):
        self.map_group = QGroupBox()
        grid = QGridLayout(self.map_group)
        grid.setSpacing(10)
        self.family_id_label = QLabel()
        self.family_id_spin = QSpinBox()
        self.family_id_spin.setRange(1, 65535)
        self.family_id_spin.setValue(1234)
        self.map_id_label = QLabel()
        self.map_id_spin = QSpinBox()
        self.map_id_spin.setRange(1, 99999999)
        self.map_id_spin.setValue(12340001)
        grid.addWidget(self.family_id_label, 0, 0)
        grid.addWidget(self.family_id_spin, 0, 1)
        grid.addWidget(self.map_id_label, 0, 2)
        grid.addWidget(self.map_id_spin, 0, 3)
        self.map_name_label = QLabel()
        self.map_name_line = QLineEdit()
        self.map_description_label = QLabel()
        self.map_description_line = QLineEdit()
        grid.addWidget(self.map_name_label, 1, 0)
        grid.addWidget(self.map_name_line, 1, 1, 1, 3)
        grid.addWidget(self.map_description_label, 2, 0)
        grid.addWidget(self.map_description_line, 2, 1, 1, 3)
        checks = QHBoxLayout()
        self.transparent_cb = QCheckBox()
        self.routing_cb = QCheckBox()
        checks.addWidget(self.transparent_cb)
        checks.addWidget(self.routing_cb)
        checks.addStretch()
        grid.addLayout(checks, 3, 0, 1, 4)
