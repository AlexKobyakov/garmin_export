# -*- coding: utf-8 -*-
"""JSON style-mapping and layer-selection handlers."""

import json
import os

from qgis.PyQt.QtWidgets import QDialog, QFileDialog, QMessageBox

from ..qgis_compat import qt_class_enum


class MappingHandlers:
    def loadMapping(self):
        from ..translation_manager import translations
        path, _ = QFileDialog.getOpenFileName(
            self.dialog, translations.get_text('select_mapping_file'),
            os.path.expanduser('~'), 'JSON files (*.json);;All files (*)')
        if not path:
            return
        try:
            with open(path, 'r', encoding='utf-8') as stream:
                mapping = stream.read()
            json.loads(mapping)
            self.dialog.mapping_widget.set_mapping_json(mapping)
            self.dialog.log_message('📂 {0}'.format(path))
        except Exception as error:
            self.dialog.log_message('❌ {0}'.format(error))
            QMessageBox.warning(
                self.dialog, translations.get_text('error'),
                '{0}:\n{1}'.format(
                    translations.get_text('error_invalid_json'), error))

    def saveMapping(self):
        from ..translation_manager import translations
        path, _ = QFileDialog.getSaveFileName(
            self.dialog, translations.get_text('save_mapping_file'),
            os.path.expanduser('~/garmin_mapping.json'),
            'JSON files (*.json);;All files (*)')
        if not path:
            return
        try:
            mapping = self.dialog.mapping_widget.get_mapping_json()
            json.loads(mapping)
            with open(path, 'w', encoding='utf-8') as stream:
                stream.write(mapping)
            self.dialog.log_message('💾 {0}'.format(path))
        except Exception as error:
            self.dialog.log_message('❌ {0}'.format(error))
            QMessageBox.warning(
                self.dialog, translations.get_text('error'),
                '{0}:\n{1}'.format(
                    translations.get_text('error_invalid_json'), error))

    def editMapping(self):
        from ..translation_manager import translations
        from .gui_dialogs import MappingEditorDialog
        editor = MappingEditorDialog(
            self.dialog.mapping_widget.get_mapping_json(), self.dialog)
        if editor.exec() == qt_class_enum(QDialog, 'DialogCode', 'Accepted'):
            self.dialog.mapping_widget.set_mapping_json(
                editor.get_mapping_json())
            self.dialog.log_message(
                '✏️ ' + translations.get_text('edit_mapping'))

    def resetMapping(self):
        from ..translation_manager import translations
        self.dialog.mapping_widget.set_mapping_json(
            self.dialog.mapping_widget.get_default_mapping())
        self.dialog.log_message(
            '🔄 ' + translations.get_text('default_mapping'))

    def selectAllLayers(self):
        self.dialog.layer_selection.select_all_layers()

    def deselectAllLayers(self):
        self.dialog.layer_selection.deselect_all_layers()

    def refreshLayers(self):
        self.dialog.loadProjectLayers()
