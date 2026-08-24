# -*- coding: utf-8 -*-
"""Compilation, worker lifecycle and result handlers."""

import json
import os

from qgis.PyQt.QtCore import QThread
from qgis.PyQt.QtWidgets import QMessageBox

from ..core import mkgmap_compiler


class CompilationHandlers:
    def startCompilation(self):
        from ..translation_manager import translations
        if self.worker is not None or self.worker_thread is not None:
            self.dialog.log_message(
                '⚠️ ' + translations.get_text('compiling'))
            return
        if not self.validateInputs():
            return
        layers = self.dialog.layer_selection.get_selected_layers()
        if not layers:
            QMessageBox.warning(
                self.dialog, translations.get_text('error'),
                translations.get_text('error_no_layers'))
            return
        settings = self.getExportSettings()
        self.saveSettings()
        self.dialog.results_table.clear_results()
        self.current_export_status = 'idle'
        self.createWorker(layers, settings)
        self.setCompilationMode(True)
        self.dialog.log_message('🚀 ' + translations.get_text('compile_map'))

    def cancelCompilation(self):
        if self.worker and self.worker_thread:
            self.worker.stop()
            self.setCompilationMode(False)
            self.worker_thread.quit()
            self.worker_thread.wait(10000)
            from ..translation_manager import translations
            self.dialog.log_message('❌ ' + translations.get_text('cancel'))

    def clearLogs(self):
        self.dialog.log_text.clear()
        self.dialog.results_table.clear_results()

    def validateInputs(self):
        from ..translation_manager import translations
        output = self.dialog.export_settings.output_folder_line.text().strip()
        if not output:
            QMessageBox.warning(
                self.dialog, translations.get_text('error'),
                translations.get_text('error_no_output_folder'))
            return False
        if not os.path.isdir(output):
            QMessageBox.warning(
                self.dialog, translations.get_text('error'),
                translations.get_text('error_output_folder_missing'))
            return False
        mkgmap = self.dialog.tools_widget.mkgmap_path_line.text().strip()
        if not mkgmap:
            QMessageBox.warning(
                self.dialog, translations.get_text('error'),
                translations.get_text('error_no_mkgmap'))
            return False
        if not mkgmap_compiler.validate_tool_installation(mkgmap, 'mkgmap'):
            QMessageBox.warning(
                self.dialog, translations.get_text('error'),
                translations.get_text('error_invalid_mkgmap'))
            return False
        java = self.dialog.tools_widget.java_path_line.text().strip()
        if not mkgmap_compiler.check_java_available(java or None):
            detected = mkgmap_compiler.find_java()
            if detected:
                self.dialog.tools_widget.java_path_line.setText(detected)
                self.dialog.log_message('☕ {0}'.format(detected))
            else:
                QMessageBox.warning(
                    self.dialog, translations.get_text('error'),
                    translations.get_text('error_java_not_found'))
                return False
        try:
            mapping = self.dialog.mapping_widget.get_mapping_json().strip()
            if mapping:
                json.loads(mapping)
        except json.JSONDecodeError as error:
            QMessageBox.warning(
                self.dialog, translations.get_text('error'),
                '{0}:\n{1}'.format(
                    translations.get_text('error_invalid_json'), error))
            return False
        if self.dialog.typ_settings.get_typ_mode() == 'file':
            path = self.dialog.typ_settings.get_typ_file_path()
            if not path or not os.path.isfile(path):
                QMessageBox.warning(
                    self.dialog, translations.get_text('error'),
                    translations.get_text('error_typ_not_found'))
                return False
        return True

    def getExportSettings(self):
        advanced = self.dialog.advanced_options
        export = self.dialog.export_settings
        return {
            'output_folder': export.output_folder_line.text().strip(),
            'output_filename': (
                export.output_filename_line.text().strip() or 'map'),
            'mkgmap_path': (
                self.dialog.tools_widget.mkgmap_path_line.text().strip()),
            'splitter_path': (
                self.dialog.tools_widget.splitter_path_line.text().strip()),
            'java_path': (
                self.dialog.tools_widget.java_path_line.text().strip()),
            'family_id': export.family_id_spin.value(),
            'map_id': export.map_id_spin.value(),
            'map_name': export.map_name_line.text().strip() or 'QGIS Map',
            'map_description': export.map_description_line.text().strip(),
            'transparent': export.transparent_cb.isChecked(),
            'routing': export.routing_cb.isChecked(),
            'mapping_json': self.dialog.mapping_widget.get_mapping_json(),
            'enabled_levels': self.dialog.level_settings.get_enabled_levels(),
            'code_page': advanced.get_code_page(),
            'mkgmap_options': advanced.get_mkgmap_options(),
            'mkgmap_logging': advanced.mkgmap_log_cb.isChecked(),
            'mkgmap_verbose': advanced.verbose_cb.isChecked(),
            'keep_temp_files': advanced.keep_temp_cb.isChecked(),
            'typ_mode': self.dialog.typ_settings.get_typ_mode(),
            'typ_file_path': self.dialog.typ_settings.get_typ_file_path(),
        }

    def createWorker(self, selected_layers, settings):
        from ..core.export_worker import ExportWorker
        self.worker_thread = QThread()
        self.worker = ExportWorker(selected_layers, settings)
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.worker.run)
        worker = self.worker
        worker.finished.connect(
            lambda success, path, source=worker:
            self.onCompilationFinished(success, path, source))
        worker.error.connect(
            lambda message, source=worker:
            self.onCompilationError(message, source))
        worker.progress.connect(
            lambda value, message, source=worker:
            self.onProgressUpdate(value, message, source))
        worker.log_message.connect(
            lambda message, source=worker:
            self.onLogMessage(message, source))
        worker.layer_processed.connect(
            lambda name, success, message, source=worker:
            self.onLayerProcessed(name, success, message, source))
        worker.status.connect(
            lambda status, source=worker:
            self.onWorkerStatus(status, source))
        self.worker_thread.start()

    def setCompilationMode(self, compiling):
        from ..translation_manager import translations
        button = self.dialog.control_buttons
        if compiling:
            button.compile_button.setText(
                '⏳ ' + translations.get_text('compiling'))
            button.compile_button.setEnabled(False)
            button.cancel_button.setEnabled(True)
            self.dialog.progress_bar.setVisible(True)
            self.dialog.progress_bar.setValue(0)
        else:
            button.compile_button.setText(
                '🚀 ' + translations.get_text('compile_map'))
            button.compile_button.setEnabled(True)
            button.cancel_button.setEnabled(False)
            self.dialog.progress_bar.setVisible(False)

    def _is_current_worker(self, worker):
        return worker is None or worker is self.worker

    def _cleanup_worker(self):
        thread = self.worker_thread
        self.worker_thread = None
        self.worker = None
        if thread:
            thread.quit()
            thread.wait(10000)
            thread.deleteLater()

    def onCompilationFinished(self, success, output_file, worker=None):
        from ..translation_manager import translations
        if not self._is_current_worker(worker):
            return
        self.setCompilationMode(False)
        if success:
            text = translations.get_text('success_export_complete')
            self.dialog.log_message('🎉 {0} {1}'.format(text, output_file))
            QMessageBox.information(
                self.dialog, translations.get_text('success'),
                '{0}\n\n{1}'.format(text, output_file))
        self._cleanup_worker()

    def onCompilationError(self, error_message, worker=None):
        from ..translation_manager import translations
        from .gui_dialogs import ErrorDialog
        if not self._is_current_worker(worker):
            return
        self.setCompilationMode(False)
        ErrorDialog(
            translations.get_text('critical_error'),
            translations.get_text('error_mkgmap_execution').format(error=''),
            error_message, self.dialog, title_key='critical_error',
            message_key='error_mkgmap_execution').exec()

    def onProgressUpdate(self, value, message='', worker=None):
        if not self._is_current_worker(worker):
            return
        self.dialog.progress_bar.setValue(value)
        if message:
            self.dialog.log_message('📊 {0}'.format(message))

    def onLogMessage(self, message, worker=None):
        if not self._is_current_worker(worker):
            return
        self.dialog.log_message(message)

    def onLayerProcessed(self, layer_name, success, message, worker=None):
        if not self._is_current_worker(worker):
            return
        self.dialog.results_table.add_result(
            layer_name, 'success' if success else 'error', message)

    def onWorkerStatus(self, status, worker=None):
        if not self._is_current_worker(worker):
            return
        self.current_export_status = status
