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
from qgis.PyQt.QtCore import QThread, pyqtSignal
from qgis.PyQt.QtWidgets import QFileDialog, QMessageBox
from qgis.core import QgsProject, QgsVectorLayer

from .gui_dialogs import DonationDialog, AuthorDialog, MappingEditorDialog, ErrorDialog


class GuiEventHandlers:
    """Класс обработчиков событий GUI"""
    
    def __init__(self, dialog):
        self.dialog = dialog
        self.worker = None
        self.worker_thread = None
    
    def onLanguageChanged(self, index):
        """Обработчик смены языка"""
        from ..translation_manager import translations
        
        language_data = self.dialog.header.language_combo.itemData(index)
        if language_data and translations.set_language(language_data):
            self.dialog.updateLanguage()
            self.dialog.log_message(f"🌐 Язык изменен на: {language_data}")
    
    def showDonation(self):
        """Показывает диалог пожертвований"""
        donation_dialog = DonationDialog(self.dialog)
        donation_dialog.exec_()
        self.dialog.log_message("☕ Диалог поддержки разработки показан")
    
    def showAuthorInfo(self):
        """Показывает информацию об авторе"""
        author_dialog = AuthorDialog(self.dialog)
        author_dialog.exec_()
        self.dialog.log_message("👤 Информация об авторе показана")
    
    def selectOutputFolder(self):
        """Выбор выходной папки"""
        folder = QFileDialog.getExistingDirectory(
            self.dialog,
            "Выберите папку для сохранения IMG файла",
            os.path.expanduser("~")
        )
        
        if folder:
            self.dialog.export_settings.output_folder_line.setText(folder)
            self.dialog.log_message(f"📂 Выбрана выходная папка: {folder}")
    
    def selectMkgmapPath(self):
        """Выбор пути к mkgmap.jar"""
        file_path, _ = QFileDialog.getOpenFileName(
            self.dialog,
            "Выберите файл mkgmap.jar",
            os.path.expanduser("~"),
            "JAR файлы (*.jar);;Все файлы (*)"
        )
        
        if file_path:
            self.dialog.export_settings.mkgmap_path_line.setText(file_path)
            self.dialog.log_message(f"⚙️ Выбран mkgmap: {file_path}")
    
    def loadMapping(self):
        """Загрузка JSON-сопоставления"""
        file_path, _ = QFileDialog.getOpenFileName(
            self.dialog,
            "Выберите файл JSON-сопоставления",
            os.path.expanduser("~"),
            "JSON файлы (*.json);;Все файлы (*)"
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    mapping_json = f.read()
                
                # Проверяем JSON
                json.loads(mapping_json)
                
                self.dialog.mapping_widget.set_mapping_json(mapping_json)
                self.dialog.log_message(f"📂 Сопоставление загружено: {file_path}")
                
            except Exception as e:
                self.dialog.log_message(f"❌ Ошибка загрузки сопоставления: {str(e)}")
                QMessageBox.warning(self.dialog, "Ошибка", f"Не удалось загрузить файл:\n{str(e)}")
    
    def saveMapping(self):
        """Сохранение JSON-сопоставления"""
        file_path, _ = QFileDialog.getSaveFileName(
            self.dialog,
            "Сохранить файл JSON-сопоставления",
            os.path.expanduser("~/garmin_mapping.json"),
            "JSON файлы (*.json);;Все файлы (*)"
        )
        
        if file_path:
            try:
                mapping_json = self.dialog.mapping_widget.get_mapping_json()
                
                # Проверяем JSON
                json.loads(mapping_json)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(mapping_json)
                
                self.dialog.log_message(f"💾 Сопоставление сохранено: {file_path}")
                
            except Exception as e:
                self.dialog.log_message(f"❌ Ошибка сохранения сопоставления: {str(e)}")
                QMessageBox.warning(self.dialog, "Ошибка", f"Не удалось сохранить файл:\n{str(e)}")
    
    def editMapping(self):
        """Редактирование JSON-сопоставления"""
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
    
    def selectAllLayers(self):
        """Выбор всех слоёв"""
        self.dialog.layer_selection.select_all_layers()
        self.dialog.log_message("✅ Выбраны все слои")
    
    def deselectAllLayers(self):
        """Снятие выделения со всех слоёв"""
        self.dialog.layer_selection.deselect_all_layers()
        self.dialog.log_message("❌ Снято выделение со всех слоёв")
    
    def startCompilation(self):
        """Запуск компиляции карты"""
        # Проверяем входные данные
        if not self.validateInputs():
            return
        
        # Получаем выбранные слои
        selected_layers = self.dialog.layer_selection.get_selected_layers()
        if not selected_layers:
            QMessageBox.warning(self.dialog, "Ошибка", "Выберите хотя бы один слой для экспорта")
            return
        
        # Получаем настройки
        settings = self.getExportSettings()
        
        # Создаем и запускаем worker
        self.createWorker(selected_layers, settings)
        
        # Обновляем интерфейс
        self.setCompilationMode(True)
        
        self.dialog.log_message("🚀 Начало компиляции карты...")
    
    def cancelCompilation(self):
        """Отмена компиляции"""
        if self.worker and self.worker_thread:
            self.worker.stop()
            self.worker_thread.quit()
            self.worker_thread.wait(3000)  # Ждем до 3 секунд
            
            self.setCompilationMode(False)
            self.dialog.log_message("❌ Компиляция отменена пользователем")
    
    def clearLogs(self):
        """Очистка логов"""
        self.dialog.log_text.clear()
        self.dialog.results_table.clear_results()
        self.dialog.log_message("🧹 Логи очищены")
    
    def validateInputs(self):
        """Проверка входных данных"""
        # Проверяем выходную папку
        output_folder = self.dialog.export_settings.output_folder_line.text().strip()
        if not output_folder:
            QMessageBox.warning(self.dialog, "Ошибка", "Укажите выходную папку")
            return False
        
        if not os.path.exists(output_folder):
            QMessageBox.warning(self.dialog, "Ошибка", "Выходная папка не существует")
            return False
        
        # Проверяем путь к mkgmap
        mkgmap_path = self.dialog.export_settings.mkgmap_path_line.text().strip()
        if not mkgmap_path:
            QMessageBox.warning(self.dialog, "Ошибка", "Укажите путь к файлу mkgmap.jar")
            return False
        
        if not os.path.exists(mkgmap_path):
            QMessageBox.warning(self.dialog, "Ошибка", "Файл mkgmap.jar не найден")
            return False
        
        # Проверяем JSON-сопоставление
        try:
            mapping_text = self.dialog.mapping_widget.get_mapping_json().strip()
            if mapping_text:
                json.loads(mapping_text)
        except json.JSONDecodeError as e:
            QMessageBox.warning(self.dialog, "Ошибка", f"Неверный формат JSON-сопоставления:\n{str(e)}")
            return False
        
        return True
    
    def getExportSettings(self):
        """Получение настроек экспорта"""
        settings = {
            'output_folder': self.dialog.export_settings.output_folder_line.text().strip(),
            'output_filename': self.dialog.export_settings.output_filename_line.text().strip() or 'map',
            'mkgmap_path': self.dialog.export_settings.mkgmap_path_line.text().strip(),
            'family_id': self.dialog.export_settings.family_id_spin.value(),
            'map_id': self.dialog.export_settings.map_id_spin.value(),
            'map_name': self.dialog.export_settings.map_name_line.text().strip() or 'QGIS Map',
            'map_description': self.dialog.export_settings.map_description_line.text().strip(),
            'transparent': self.dialog.export_settings.transparent_cb.isChecked(),
            'routing': self.dialog.export_settings.routing_cb.isChecked(),
            'mapping_json': self.dialog.mapping_widget.get_mapping_json(),
            'enabled_levels': self.dialog.level_settings.get_enabled_levels()
        }
        
        return settings
    
    def createWorker(self, selected_layers, settings):
        """Создание и запуск worker-а для компиляции"""
        # Импортируем worker (будет создан позже)
        from ..core.export_worker import ExportWorker
        
        # Создаем thread и worker
        self.worker_thread = QThread()
        self.worker = ExportWorker(selected_layers, settings)
        
        # Перемещаем worker в thread
        self.worker.moveToThread(self.worker_thread)
        
        # Подключаем сигналы
        self.worker_thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.onCompilationFinished)
        self.worker.error.connect(self.onCompilationError)
        self.worker.progress.connect(self.onProgressUpdate)
        self.worker.log_message.connect(self.onLogMessage)
        self.worker.layer_processed.connect(self.onLayerProcessed)
        
        # Запускаем thread
        self.worker_thread.start()
    
    def setCompilationMode(self, compiling):
        """Переключение режима компиляции"""
        from ..translation_manager import translations
        
        if compiling:
            self.dialog.control_buttons.compile_button.setText(f"⏳ {translations.get_text('compiling')}")
            self.dialog.control_buttons.compile_button.setEnabled(False)
            self.dialog.control_buttons.cancel_button.setEnabled(True)
            self.dialog.progress_bar.setVisible(True)
            self.dialog.progress_bar.setValue(0)
        else:
            self.dialog.control_buttons.compile_button.setText(f"🚀 {translations.get_text('compile_map')}")
            self.dialog.control_buttons.compile_button.setEnabled(True)
            self.dialog.control_buttons.cancel_button.setEnabled(False)
            self.dialog.progress_bar.setVisible(False)
    
    def onCompilationFinished(self, success, output_file):
        """Обработчик завершения компиляции"""
        self.setCompilationMode(False)
        
        if success:
            self.dialog.log_message(f"🎉 Компиляция завершена успешно! Файл: {output_file}")
            QMessageBox.information(
                self.dialog, 
                "Успех", 
                f"Карта успешно скомпилирована!\n\nФайл сохранен: {output_file}"
            )
        else:
            self.dialog.log_message("💥 Компиляция завершена с ошибками")
        
        # Очищаем worker
        if self.worker_thread:
            self.worker_thread.quit()
            self.worker_thread.wait()
            self.worker_thread = None
            self.worker = None
    
    def onCompilationError(self, error_message):
        """Обработчик ошибки компиляции"""
        self.dialog.log_message(f"❌ Ошибка компиляции: {error_message}")
        
        error_dialog = ErrorDialog(
            "Ошибка компиляции",
            "Произошла ошибка при компиляции карты",
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
        
        if success:
            self.dialog.log_message(f"✅ Слой '{layer_name}' обработан успешно")
        else:
            self.dialog.log_message(f"❌ Ошибка обработки слоя '{layer_name}': {message}")
    
    def closeEvent(self, event):
        """Обработчик закрытия окна"""
        # Если идет компиляция, спрашиваем подтверждение
        if self.worker and self.worker_thread and self.worker_thread.isRunning():
            from ..translation_manager import translations
            
            reply = QMessageBox.question(
                self.dialog,
                translations.get_text('confirmation'),
                translations.get_text('confirm_close'),
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                # Останавливаем worker
                self.cancelCompilation()
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()


class LayerManager:
    """Менеджер слоёв проекта"""
    
    @staticmethod
    def get_project_layers():
        """Получает все векторные слои проекта"""
        layers = []
        project = QgsProject.instance()
        
        for layer_id, layer in project.mapLayers().items():
            if isinstance(layer, QgsVectorLayer) and layer.isValid():
                geometry_type = LayerManager.get_geometry_type(layer)
                layers.append({
                    'id': layer_id,
                    'name': layer.name(),
                    'type': geometry_type,
                    'layer': layer
                })
        
        return layers
    
    @staticmethod
    def get_geometry_type(layer):
        """Определяет тип геометрии слоя"""
        from qgis.core import QgsWkbTypes
        
        geom_type = layer.geometryType()
        
        if geom_type == QgsWkbTypes.PointGeometry:
            return 'Point'
        elif geom_type == QgsWkbTypes.LineGeometry:
            return 'LineString'
        elif geom_type == QgsWkbTypes.PolygonGeometry:
            return 'Polygon'
        else:
            return 'Unknown'
    
    @staticmethod
    def get_layer_fields(layer):
        """Получает список полей слоя"""
        fields = []
        for field in layer.fields():
            fields.append(field.name())
        return fields
    
    @staticmethod
    def get_layer_by_name(layer_name):
        """Получает слой по имени"""
        project = QgsProject.instance()
        
        for layer_id, layer in project.mapLayers().items():
            if isinstance(layer, QgsVectorLayer) and layer.name() == layer_name:
                return layer
        
        return None
