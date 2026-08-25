# -*- coding: utf-8 -*-
"""Persistent settings and close-event handlers."""

from qgis.PyQt.QtWidgets import QMessageBox

from ..qgis_compat import qt_class_enum


class SettingsHandlers:
    def loadSettings(self):
        sm = self.settings_manager
        dialog = self.dialog
        tools = dialog.tools_widget
        export = dialog.export_settings
        tools.mkgmap_path_line.setText(sm.get('mkgmap_path'))
        tools.splitter_path_line.setText(sm.get('splitter_path'))
        tools.java_path_line.setText(sm.get('java_path'))
        if sm.get('output_folder'):
            export.output_folder_line.setText(sm.get('output_folder'))
        export.output_filename_line.setText(sm.get('output_filename') or 'map')
        export.family_id_spin.setValue(sm.get('family_id'))
        export.map_id_spin.setValue(sm.get('map_id'))
        export.map_name_line.setText(sm.get('map_name') or 'QGIS Map')
        export.map_description_line.setText(sm.get('map_description'))
        export.transparent_cb.setChecked(sm.get('transparent'))
        export.routing_cb.setChecked(sm.get('routing'))
        advanced = dialog.advanced_options
        advanced.set_code_page(sm.get('code_page'))
        advanced.draw_priority_spin.setValue(sm.get('draw_priority'))
        advanced.index_cb.setChecked(sm.get('index'))
        advanced.pois_to_areas_cb.setChecked(sm.get('add_pois_to_areas'))
        advanced.lower_case_cb.setChecked(sm.get('lower_case'))
        advanced.order_area_cb.setChecked(sm.get('order_by_decreasing_area'))
        try:
            advanced.reduce_density_spin.setValue(
                float(sm.get('reduce_point_density') or 0))
            advanced.reduce_density_polygon_spin.setValue(
                float(sm.get('reduce_point_density_polygon') or 0))
        except (TypeError, ValueError):
            pass
        advanced.min_polygon_spin.setValue(sm.get('min_size_polygon'))
        advanced.java_heap_spin.setValue(sm.get('java_xmx_gb'))
        advanced.max_jobs_spin.setValue(sm.get('max_jobs'))
        advanced.mkgmap_log_cb.setChecked(sm.get('mkgmap_logging'))
        advanced.verbose_cb.setChecked(sm.get('mkgmap_verbose'))
        advanced.keep_temp_cb.setChecked(sm.get('keep_temp_files'))
        advanced.extra_args_line.setText(sm.get('extra_args'))
        dialog.typ_settings.set_typ_mode(sm.get('typ_mode'))
        dialog.typ_settings.set_typ_file_path(sm.get('typ_file_path'))
        if sm.get('mkgmap_path'):
            self.onMkgmapPathChanged()
        if sm.get('splitter_path'):
            self.onSplitterPathChanged()

    def saveSettings(self):
        dialog = self.dialog
        advanced = dialog.advanced_options
        export = dialog.export_settings
        options = advanced.get_mkgmap_options()
        self.settings_manager.set_many({
            'mkgmap_path': dialog.tools_widget.mkgmap_path_line.text().strip(),
            'splitter_path': (
                dialog.tools_widget.splitter_path_line.text().strip()),
            'java_path': dialog.tools_widget.java_path_line.text().strip(),
            'output_folder': export.output_folder_line.text().strip(),
            'output_filename': export.output_filename_line.text().strip(),
            'family_id': export.family_id_spin.value(),
            'map_id': export.map_id_spin.value(),
            'map_name': export.map_name_line.text().strip(),
            'map_description': export.map_description_line.text().strip(),
            'transparent': export.transparent_cb.isChecked(),
            'routing': export.routing_cb.isChecked(),
            'code_page': advanced.get_code_page(),
            'index': advanced.index_cb.isChecked(),
            'add_pois_to_areas': advanced.pois_to_areas_cb.isChecked(),
            'draw_priority': advanced.draw_priority_spin.value(),
            'lower_case': advanced.lower_case_cb.isChecked(),
            'order_by_decreasing_area': advanced.order_area_cb.isChecked(),
            'reduce_point_density': options['reduce_point_density'] or '',
            'reduce_point_density_polygon': (
                options['reduce_point_density_polygon'] or ''),
            'min_size_polygon': advanced.min_polygon_spin.value(),
            'java_xmx_gb': advanced.java_heap_spin.value(),
            'max_jobs': advanced.max_jobs_spin.value(),
            'mkgmap_logging': advanced.mkgmap_log_cb.isChecked(),
            'mkgmap_verbose': advanced.verbose_cb.isChecked(),
            'keep_temp_files': advanced.keep_temp_cb.isChecked(),
            'extra_args': advanced.extra_args_line.text().strip(),
            'typ_mode': dialog.typ_settings.get_typ_mode(),
            'typ_file_path': dialog.typ_settings.get_typ_file_path(),
        })

    def closeEvent(self, event):
        from ..translation_manager import translations
        running = (self.worker and self.worker_thread and
                   self.worker_thread.isRunning())
        if running:
            yes = qt_class_enum(QMessageBox, 'StandardButton', 'Yes')
            no = qt_class_enum(QMessageBox, 'StandardButton', 'No')
            reply = QMessageBox.question(
                self.dialog, translations.get_text('confirmation'),
                translations.get_text('confirm_close'), yes | no, no)
            if reply == yes:
                self.cancelCompilation()
                self.saveSettings()
                event.accept()
            else:
                event.ignore()
        else:
            self.saveSettings()
            event.accept()
