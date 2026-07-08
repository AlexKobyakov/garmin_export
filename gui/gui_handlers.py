# -*- coding: utf-8 -*-
"""
GUI Event Handlers for Garmin Export Plugin
Обработчики событий GUI для плагина экспорта в Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

import os
import json

from qgis.PyQt.QtCore import QThread
from qgis.PyQt.QtWidgets import QFileDialog, QMessageBox

from ..core.layer_manager import LayerManager
from ..core.settings_manager import SettingsManager
from ..core import mkgmap_compiler


class GuiEventHandlers:
    """Класс обработчиков событий GUI"""

    def __init__(self, dialog):
        self.dialog = dialog
        self.worker = None
        self.worker_thread = None
        self.download_thread = None
        self.download_worker = None
        self.settings_manager = SettingsManager()

    # ------------------------------------------------------------------
    # Заголовок: язык, поддержка, автор
    # ------------------------------------------------------------------

    def onLanguageChanged(self, index):
        """Обработчик смены языка"""
        from qgis.PyQt.QtCore import Qt
        from ..translation_manager import translations

        language_data = self.dialog.header.language_combo.itemData(index)
        if language_data and translations.set_language(language_data):
            self.dialog.updateLanguage()

            # Направление письма (арабский - справа налево)
            direction = (Qt.RightToLeft if translations.is_rtl(language_data)
                         else Qt.LeftToRight)
            self.dialog.setLayoutDirection(direction)

            self.settings_manager.set('language', language_data)
            self.dialog.log_message(f"🌐 Язык изменен на: {language_data}")

    def showDonation(self):
        """Показывает диалог пожертвований"""
        from .simple_donation import SimpleDonationDialog

        dialog = SimpleDonationDialog(self.dialog)
        dialog.exec_()

    def showAuthorInfo(self):
        """Показывает информацию об авторе"""
        from .gui_dialogs import AuthorInfoDialog

        dialog = AuthorInfoDialog(self.dialog)
        dialog.exec_()

    # ------------------------------------------------------------------
    # Выбор путей
    # ------------------------------------------------------------------

    def selectOutputFolder(self):
        """Выбор выходной папки"""
        from ..translation_manager import translations

        start_dir = (self.dialog.export_settings.output_folder_line.text().strip()
                     or os.path.expanduser("~"))
        folder = QFileDialog.getExistingDirectory(
            self.dialog,
            translations.get_text('select_output_folder'),
            start_dir
        )

        if folder:
            self.dialog.export_settings.output_folder_line.setText(folder)
            self.settings_manager.set('output_folder', folder)
            self.dialog.log_message(f"📂 Выбрана выходная папка: {folder}")

    def selectMkgmapPath(self):
        """Выбор пути к mkgmap.jar (кнопка 'Добавить mkgmap')"""
        from ..translation_manager import translations

        file_path, _ = QFileDialog.getOpenFileName(
            self.dialog,
            translations.get_text('select_mkgmap'),
            os.path.expanduser("~"),
            "JAR файлы (*.jar);;Все файлы (*)"
        )

        if file_path:
            self.dialog.tools_widget.mkgmap_path_line.setText(file_path)
            self.onMkgmapPathChanged()
            self.dialog.log_message(f"⚙️ Выбран mkgmap: {file_path}")

    def selectSplitterPath(self):
        """Выбор пути к splitter.jar (кнопка 'Добавить splitter')"""
        from ..translation_manager import translations

        file_path, _ = QFileDialog.getOpenFileName(
            self.dialog,
            translations.get_text('select_splitter'),
            os.path.expanduser("~"),
            "JAR файлы (*.jar);;Все файлы (*)"
        )

        if file_path:
            self.dialog.tools_widget.splitter_path_line.setText(file_path)
            self.settings_manager.set('splitter_path', file_path)
            self.dialog.log_message(f"⚙️ Выбран splitter: {file_path}")

    def selectJavaPath(self):
        """Выбор пути к java"""
        from ..translation_manager import translations

        file_path, _ = QFileDialog.getOpenFileName(
            self.dialog,
            translations.get_text('select_java'),
            os.path.expanduser("~"),
            "java (java.exe java);;Все файлы (*)"
        )

        if file_path:
            self.dialog.tools_widget.java_path_line.setText(file_path)
            self.onJavaPathChanged()

    def detectJava(self):
        """Автоопределение пути к Java"""
        from ..translation_manager import translations

        java_path = mkgmap_compiler.find_java()
        if java_path:
            self.dialog.tools_widget.java_path_line.setText(java_path)
            self.onJavaPathChanged()
            self.dialog.log_message(f"☕ Java найдена: {java_path}")
        else:
            self.dialog.tools_widget.java_status_label.setText(
                '❌ ' + translations.get_text('java_not_found'))
            self.dialog.log_message(
                '⚠️ ' + translations.get_text('java_not_found'))

    def selectTypFile(self):
        """Выбор файла TYP / typ.txt"""
        from ..translation_manager import translations

        file_path, _ = QFileDialog.getOpenFileName(
            self.dialog,
            translations.get_text('select_typ_file'),
            os.path.expanduser("~"),
            "TYP файлы (*.typ *.txt);;Все файлы (*)"
        )

        if file_path:
            self.dialog.typ_settings.set_typ_file_path(file_path)
            self.settings_manager.set('typ_file_path', file_path)
            self.dialog.log_message(f"🖌️ Выбран TYP файл: {file_path}")

    # ------------------------------------------------------------------
    # Статусы инструментов
    # ------------------------------------------------------------------

    def onMkgmapPathChanged(self):
        """Проверка mkgmap.jar и обновление статуса"""
        from ..translation_manager import translations

        path = self.dialog.tools_widget.mkgmap_path_line.text().strip()
        label = self.dialog.tools_widget.mkgmap_status_label

        if not path:
            label.setText('')
            return

        if mkgmap_compiler.validate_mkgmap_jar(path):
            label.setText('✅ mkgmap.jar: ' + translations.get_text('jar_valid'))
            label.setStyleSheet("color: #27ae60; font-size: 10px;")
            self.settings_manager.set('mkgmap_path', path)
        else:
            label.setText('❌ ' + translations.get_text('jar_invalid'))
            label.setStyleSheet("color: #e74c3c; font-size: 10px;")

    def onJavaPathChanged(self):
        """Проверка Java и обновление статуса"""
        from ..translation_manager import translations

        path = self.dialog.tools_widget.java_path_line.text().strip()
        label = self.dialog.tools_widget.java_status_label

        version = mkgmap_compiler.get_java_version(path or None)
        if version:
            label.setText('✅ ' + version)
            label.setStyleSheet("color: #27ae60; font-size: 10px;")
            self.settings_manager.set('java_path', path)
        else:
            label.setText('❌ ' + translations.get_text('java_not_found'))
            label.setStyleSheet("color: #e74c3c; font-size: 10px;")

    # ------------------------------------------------------------------
    # Скачивание mkgmap / splitter
    # ------------------------------------------------------------------

    def downloadMkgmap(self):
        """Скачивание mkgmap.jar"""
        self._download_tool('mkgmap')

    def downloadSplitter(self):
        """Скачивание splitter.jar"""
        self._download_tool('splitter')

    def _download_tool(self, tool):
        """Общий сценарий скачивания инструмента"""
        from ..translation_manager import translations
        from ..core.download_worker import DownloadWorker
        from .gui_dialogs import DownloadProgressDialog

        if self.download_thread is not None:
            QMessageBox.information(
                self.dialog, translations.get_text('info'),
                translations.get_text('download_in_progress'))
            return

        title = (translations.get_text('download_mkgmap') if tool == 'mkgmap'
                 else translations.get_text('download_splitter'))

        progress_dialog = DownloadProgressDialog(title, self.dialog)

        self.download_thread = QThread(self.dialog)
        self.download_worker = DownloadWorker(tool)
        self.download_worker.moveToThread(self.download_thread)

        self.download_thread.started.connect(self.download_worker.run)
        self.download_worker.progress.connect(progress_dialog.update_progress)
        self.download_worker.status.connect(progress_dialog.set_status)
        progress_dialog.cancel_button.clicked.connect(self.download_worker.cancel)

        result = {}

        def on_finished(success, payload):
            result['success'] = success
            result['payload'] = payload
            progress_dialog.accept()

        self.download_worker.finished.connect(on_finished)

        self.download_thread.start()
        self.dialog.log_message(f"📥 {title}...")

        progress_dialog.exec_()

        # Если диалог закрыт до завершения - отменяем
        if 'success' not in result:
            self.download_worker.cancel()

        self.download_thread.quit()
        self.download_thread.wait(15000)
        self.download_thread = None
        self.download_worker = None

        success = result.get('success', False)
        payload = result.get('payload', '')

        if success:
            self._apply_downloaded_tool(tool, payload)
        elif payload:
            self.dialog.log_message(
                f"❌ {translations.get_text('download_failed')}: {payload}")
            QMessageBox.warning(
                self.dialog,
                translations.get_text('download_failed'),
                payload)

    def _apply_downloaded_tool(self, tool, path):
        """Применение скачанного инструмента"""
        from ..translation_manager import translations

        if tool == 'mkgmap':
            self.dialog.tools_widget.mkgmap_path_line.setText(path)
            self.onMkgmapPathChanged()
        else:
            self.dialog.tools_widget.splitter_path_line.setText(path)
            self.settings_manager.set('splitter_path', path)

        self.dialog.log_message(
            f"✅ {translations.get_text('download_complete')}: {path}")

    # ------------------------------------------------------------------
    # Сопоставление стилей
    # ------------------------------------------------------------------

    def loadMapping(self):
        """Загрузка JSON-сопоставления"""
        from ..translation_manager import translations

        file_path, _ = QFileDialog.getOpenFileName(
            self.dialog,
            translations.get_text('select_mapping_file'),
            os.path.expanduser("~"),
            "JSON файлы (*.json);;Все файлы (*)"
        )

        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    mapping_json = f.read()

                json.loads(mapping_json)

                self.dialog.mapping_widget.set_mapping_json(mapping_json)
                self.dialog.log_message(f"📂 Сопоставление загружено: {file_path}")

            except Exception as e:
                self.dialog.log_message(f"❌ Ошибка загрузки сопоставления: {str(e)}")
                QMessageBox.warning(
                    self.dialog, translations.get_text('error'),
                    f"{translations.get_text('error_invalid_json')}:\n{str(e)}")

    def saveMapping(self):
        """Сохранение JSON-сопоставления"""
        from ..translation_manager import translations

        file_path, _ = QFileDialog.getSaveFileName(
            self.dialog,
            translations.get_text('save_mapping_file'),
            os.path.expanduser("~/garmin_mapping.json"),
            "JSON файлы (*.json);;Все файлы (*)"
        )

        if file_path:
            try:
                mapping_json = self.dialog.mapping_widget.get_mapping_json()
                json.loads(mapping_json)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(mapping_json)

                self.dialog.log_message(f"💾 Сопоставление сохранено: {file_path}")

            except Exception as e:
                self.dialog.log_message(f"❌ Ошибка сохранения сопоставления: {str(e)}")
                QMessageBox.warning(
                    self.dialog, translations.get_text('error'),
                    f"{translations.get_text('error_invalid_json')}:\n{str(e)}")

    def editMapping(self):
        """Редактирование JSON-сопоставления"""
        from .gui_dialogs import MappingEditorDialog

        current_mapping = self.dialog.mapping_widget.get_mapping_json()
        editor_dialog = MappingEditorDialog(current_mapping, self.dialog)

        if editor_dialog.exec_() == MappingEditorDialog.Accepted:
            new_mapping = editor_dialog.get_mapping_json()
            self.dialog.mapping_widget.set_mapping_json(new_mapping)
            self.dialog.log_message("✏️ JSON-сопоставление отредактировано")

    def resetMapping(self):
        """Сброс сопоставления к значениям по умолчанию"""
        default_mapping = self.dialog.mapping_widget.get_default_mapping()
        self.dialog.mapping_widget.set_mapping_json(default_mapping)
        self.dialog.log_message("🔄 Сопоставление сброшено к значениям по умолчанию")

    # ------------------------------------------------------------------
    # Слои
    # ------------------------------------------------------------------

    def selectAllLayers(self):
        """Выбор всех слоёв"""
        self.dialog.layer_selection.select_all_layers()

    def deselectAllLayers(self):
        """Снятие выделения со всех слоёв"""
        self.dialog.layer_selection.deselect_all_layers()

    def refreshLayers(self):
        """Обновление списка слоёв проекта"""
        self.dialog.loadProjectLayers()

    # ------------------------------------------------------------------
    # Компиляция
    # ------------------------------------------------------------------

    def startCompilation(self):
        """Запуск компиляции карты"""
        from ..translation_manager import translations

        if not self.validateInputs():
            return

        selected_layers = self.dialog.layer_selection.get_selected_layers()
        if not selected_layers:
            QMessageBox.warning(
                self.dialog, translations.get_text('error'),
                translations.get_text('error_no_layers'))
            return

        settings = self.getExportSettings()
        self.saveSettings()

        self.createWorker(selected_layers, settings)
        self.setCompilationMode(True)

        self.dialog.log_message("🚀 Начало компиляции карты...")

    def cancelCompilation(self):
        """Отмена компиляции"""
        if self.worker and self.worker_thread:
            self.worker.stop()
            self.worker_thread.quit()
            self.worker_thread.wait(5000)

            self.setCompilationMode(False)
            self.dialog.log_message("❌ Компиляция отменена пользователем")

    def clearLogs(self):
        """Очистка логов"""
        self.dialog.log_text.clear()
        self.dialog.results_table.clear_results()

    def validateInputs(self):
        """Проверка входных данных"""
        from ..translation_manager import translations

        output_folder = self.dialog.export_settings.output_folder_line.text().strip()
        if not output_folder:
            QMessageBox.warning(
                self.dialog, translations.get_text('error'),
                translations.get_text('error_no_output_folder'))
            return False

        if not os.path.isdir(output_folder):
            QMessageBox.warning(
                self.dialog, translations.get_text('error'),
                translations.get_text('error_output_folder_missing'))
            return False

        mkgmap_path = self.dialog.tools_widget.mkgmap_path_line.text().strip()
        if not mkgmap_path:
            QMessageBox.warning(
                self.dialog, translations.get_text('error'),
                translations.get_text('error_no_mkgmap'))
            return False

        if not mkgmap_compiler.validate_mkgmap_jar(mkgmap_path):
            QMessageBox.warning(
                self.dialog, translations.get_text('error'),
                translations.get_text('error_invalid_mkgmap'))
            return False

        java_path = self.dialog.tools_widget.java_path_line.text().strip()
        if not mkgmap_compiler.check_java_available(java_path or None):
            detected = mkgmap_compiler.find_java()
            if detected:
                self.dialog.tools_widget.java_path_line.setText(detected)
                self.dialog.log_message(f"☕ Java найдена автоматически: {detected}")
            else:
                QMessageBox.warning(
                    self.dialog, translations.get_text('error'),
                    translations.get_text('error_java_not_found'))
                return False

        try:
            mapping_text = self.dialog.mapping_widget.get_mapping_json().strip()
            if mapping_text:
                json.loads(mapping_text)
        except json.JSONDecodeError as e:
            QMessageBox.warning(
                self.dialog, translations.get_text('error'),
                f"{translations.get_text('error_invalid_json')}:\n{str(e)}")
            return False

        typ_mode = self.dialog.typ_settings.get_typ_mode()
        if typ_mode == 'file':
            typ_path = self.dialog.typ_settings.get_typ_file_path()
            if not typ_path or not os.path.isfile(typ_path):
                QMessageBox.warning(
                    self.dialog, translations.get_text('error'),
                    translations.get_text('error_typ_not_found'))
                return False

        return True

    def getExportSettings(self):
        """Получение настроек экспорта из всех виджетов"""
        advanced = self.dialog.advanced_options

        settings = {
            'output_folder': self.dialog.export_settings.output_folder_line.text().strip(),
            'output_filename': self.dialog.export_settings.output_filename_line.text().strip() or 'map',
            'mkgmap_path': self.dialog.tools_widget.mkgmap_path_line.text().strip(),
            'splitter_path': self.dialog.tools_widget.splitter_path_line.text().strip(),
            'java_path': self.dialog.tools_widget.java_path_line.text().strip(),
            'family_id': self.dialog.export_settings.family_id_spin.value(),
            'map_id': self.dialog.export_settings.map_id_spin.value(),
            'map_name': self.dialog.export_settings.map_name_line.text().strip() or 'QGIS Map',
            'map_description': self.dialog.export_settings.map_description_line.text().strip(),
            'transparent': self.dialog.export_settings.transparent_cb.isChecked(),
            'routing': self.dialog.export_settings.routing_cb.isChecked(),
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

        return settings

    def createWorker(self, selected_layers, settings):
        """Создание и запуск worker-а для компиляции"""
        from ..core.export_worker import ExportWorker

        self.worker_thread = QThread()
        self.worker = ExportWorker(selected_layers, settings)

        self.worker.moveToThread(self.worker_thread)

        self.worker_thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.onCompilationFinished)
        self.worker.error.connect(self.onCompilationError)
        self.worker.progress.connect(self.onProgressUpdate)
        self.worker.log_message.connect(self.onLogMessage)
        self.worker.layer_processed.connect(self.onLayerProcessed)

        self.worker_thread.start()

    def setCompilationMode(self, compiling):
        """Переключение режима компиляции"""
        from ..translation_manager import translations

        if compiling:
            self.dialog.control_buttons.compile_button.setText(
                f"⏳ {translations.get_text('compiling')}")
            self.dialog.control_buttons.compile_button.setEnabled(False)
            self.dialog.control_buttons.cancel_button.setEnabled(True)
            self.dialog.progress_bar.setVisible(True)
            self.dialog.progress_bar.setValue(0)
        else:
            self.dialog.control_buttons.compile_button.setText(
                f"🚀 {translations.get_text('compile_map')}")
            self.dialog.control_buttons.compile_button.setEnabled(True)
            self.dialog.control_buttons.cancel_button.setEnabled(False)
            self.dialog.progress_bar.setVisible(False)

    def onCompilationFinished(self, success, output_file):
        """Обработчик завершения компиляции"""
        from ..translation_manager import translations

        self.setCompilationMode(False)

        if success:
            self.dialog.log_message(
                f"🎉 Компиляция завершена успешно! Файл: {output_file}")
            QMessageBox.information(
                self.dialog,
                translations.get_text('success'),
                f"{translations.get_text('success_export_complete')}\n\n{output_file}")

        if self.worker_thread:
            self.worker_thread.quit()
            self.worker_thread.wait()
            self.worker_thread = None
            self.worker = None

    def onCompilationError(self, error_message):
        """Обработчик ошибки компиляции"""
        from ..translation_manager import translations
        from .gui_dialogs import ErrorDialog

        error_dialog = ErrorDialog(
            translations.get_text('critical_error'),
            translations.get_text('error_mkgmap_execution').format(error=''),
            error_message,
            self.dialog
        )
        error_dialog.exec_()

    def onProgressUpdate(self, value, message=""):
        """Обработчик обновления прогресса"""
        self.dialog.progress_bar.setValue(value)
        if message:
            self.dialog.log_message(f"📊 {message}")

    def onLogMessage(self, message):
        """Обработчик сообщений лога"""
        self.dialog.log_message(message)

    def onLayerProcessed(self, layer_name, success, message):
        """Обработчик обработки слоя"""
        status = 'success' if success else 'error'
        self.dialog.results_table.add_result(layer_name, status, message)

    # ------------------------------------------------------------------
    # Настройки (персистентность)
    # ------------------------------------------------------------------

    def loadSettings(self):
        """Загрузка сохранённых настроек в виджеты"""
        sm = self.settings_manager
        d = self.dialog

        d.tools_widget.mkgmap_path_line.setText(sm.get('mkgmap_path'))
        d.tools_widget.splitter_path_line.setText(sm.get('splitter_path'))
        d.tools_widget.java_path_line.setText(sm.get('java_path'))

        if sm.get('output_folder'):
            d.export_settings.output_folder_line.setText(sm.get('output_folder'))
        d.export_settings.output_filename_line.setText(
            sm.get('output_filename') or 'map')
        d.export_settings.family_id_spin.setValue(sm.get('family_id'))
        d.export_settings.map_id_spin.setValue(sm.get('map_id'))
        d.export_settings.map_name_line.setText(sm.get('map_name') or 'QGIS Map')
        d.export_settings.map_description_line.setText(sm.get('map_description'))
        d.export_settings.transparent_cb.setChecked(sm.get('transparent'))
        d.export_settings.routing_cb.setChecked(sm.get('routing'))

        adv = d.advanced_options
        adv.set_code_page(sm.get('code_page'))
        adv.draw_priority_spin.setValue(sm.get('draw_priority'))
        adv.index_cb.setChecked(sm.get('index'))
        adv.pois_to_areas_cb.setChecked(sm.get('add_pois_to_areas'))
        adv.lower_case_cb.setChecked(sm.get('lower_case'))
        adv.order_area_cb.setChecked(sm.get('order_by_decreasing_area'))
        try:
            adv.reduce_density_spin.setValue(
                float(sm.get('reduce_point_density') or 0))
            adv.reduce_density_polygon_spin.setValue(
                float(sm.get('reduce_point_density_polygon') or 0))
        except (TypeError, ValueError):
            pass
        adv.min_polygon_spin.setValue(sm.get('min_size_polygon'))
        adv.java_heap_spin.setValue(sm.get('java_xmx_gb'))
        adv.max_jobs_spin.setValue(sm.get('max_jobs'))
        adv.mkgmap_log_cb.setChecked(sm.get('mkgmap_logging'))
        adv.verbose_cb.setChecked(sm.get('mkgmap_verbose'))
        adv.keep_temp_cb.setChecked(sm.get('keep_temp_files'))
        adv.extra_args_line.setText(sm.get('extra_args'))

        d.typ_settings.set_typ_mode(sm.get('typ_mode'))
        d.typ_settings.set_typ_file_path(sm.get('typ_file_path'))

        # Обновляем статусы инструментов
        if sm.get('mkgmap_path'):
            self.onMkgmapPathChanged()

    def saveSettings(self):
        """Сохранение настроек из виджетов"""
        d = self.dialog
        adv = d.advanced_options
        opts = adv.get_mkgmap_options()

        self.settings_manager.set_many({
            'mkgmap_path': d.tools_widget.mkgmap_path_line.text().strip(),
            'splitter_path': d.tools_widget.splitter_path_line.text().strip(),
            'java_path': d.tools_widget.java_path_line.text().strip(),
            'output_folder': d.export_settings.output_folder_line.text().strip(),
            'output_filename': d.export_settings.output_filename_line.text().strip(),
            'family_id': d.export_settings.family_id_spin.value(),
            'map_id': d.export_settings.map_id_spin.value(),
            'map_name': d.export_settings.map_name_line.text().strip(),
            'map_description': d.export_settings.map_description_line.text().strip(),
            'transparent': d.export_settings.transparent_cb.isChecked(),
            'routing': d.export_settings.routing_cb.isChecked(),
            'code_page': adv.get_code_page(),
            'index': adv.index_cb.isChecked(),
            'add_pois_to_areas': adv.pois_to_areas_cb.isChecked(),
            'draw_priority': adv.draw_priority_spin.value(),
            'lower_case': adv.lower_case_cb.isChecked(),
            'order_by_decreasing_area': adv.order_area_cb.isChecked(),
            'reduce_point_density': opts['reduce_point_density'] or '',
            'reduce_point_density_polygon': opts['reduce_point_density_polygon'] or '',
            'min_size_polygon': adv.min_polygon_spin.value(),
            'java_xmx_gb': adv.java_heap_spin.value(),
            'max_jobs': adv.max_jobs_spin.value(),
            'mkgmap_logging': adv.mkgmap_log_cb.isChecked(),
            'mkgmap_verbose': adv.verbose_cb.isChecked(),
            'keep_temp_files': adv.keep_temp_cb.isChecked(),
            'extra_args': adv.extra_args_line.text().strip(),
            'typ_mode': d.typ_settings.get_typ_mode(),
            'typ_file_path': d.typ_settings.get_typ_file_path(),
        })

    # ------------------------------------------------------------------

    def closeEvent(self, event):
        """Обработчик закрытия окна"""
        from ..translation_manager import translations

        if self.worker and self.worker_thread and self.worker_thread.isRunning():
            reply = QMessageBox.question(
                self.dialog,
                translations.get_text('confirmation'),
                translations.get_text('confirm_close'),
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                self.cancelCompilation()
                self.saveSettings()
                event.accept()
            else:
                event.ignore()
        else:
            self.saveSettings()
            event.accept()
