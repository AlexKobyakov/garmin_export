# -*- coding: utf-8 -*-
"""
Export Worker for Garmin Export Plugin
Worker для экспорта данных в формат Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

import os
import json
import subprocess
from qgis.PyQt.QtCore import QObject, pyqtSignal

from .mp_generator import MPGenerator
from .mkgmap_compiler import MkgmapCompiler
from .layer_processor import LayerProcessor
from .style_mapper import StyleMapper


class ExportWorker(QObject):
    """Worker для экспорта векторных данных в Garmin IMG"""
    
    # Сигналы
    finished = pyqtSignal(bool, str)  # success, output_file
    error = pyqtSignal(str)  # error_message
    progress = pyqtSignal(int, str)  # value, message
    log_message = pyqtSignal(str)  # message
    layer_processed = pyqtSignal(str, bool, str)  # layer_name, success, message
    
    def __init__(self, selected_layers, settings):
        super().__init__()
        self.selected_layers = selected_layers
        self.settings = settings
        self.is_cancelled = False
        
        # Инициализация компонентов
        self.mp_generator = MPGenerator()
        self.mkgmap_compiler = MkgmapCompiler()
        self.layer_processor = LayerProcessor()
        self.style_mapper = StyleMapper()
        
        # Обработанные данные
        self.processed_data = []
    
    def run(self):
        """Основной метод выполнения экспорта"""
        try:
            self.log_message.emit("🚀 Начало экспорта данных в формат Garmin IMG")
            self.progress.emit(0, "Инициализация экспорта...")
            
            # Проверяем отмену
            if self.is_cancelled:
                return
            
            # Подготовка
            self.prepare_export()
            
            # Обработка слоёв
            self.process_layers()
            
            # Генерация MP файла
            self.generate_mp_file()
            
            # Компиляция в IMG
            output_file = self.compile_to_img()
            
            # Завершение
            self.progress.emit(100, "Экспорт завершён успешно!")
            self.log_message.emit("🎉 Экспорт завершён успешно!")
            self.finished.emit(True, output_file)
            
        except Exception as e:
            self.log_message.emit(f"❌ Ошибка экспорта: {str(e)}")
            self.error.emit(str(e))
            self.finished.emit(False, "")
    
    def prepare_export(self):
        """Подготовка к экспорту"""
        self.progress.emit(10, "Подготовка к экспорту...")
        self.log_message.emit("📋 Подготовка параметров экспорта")
        
        # Создаём временные папки
        self.temp_folder = os.path.join(self.settings['output_folder'], 'temp')
        os.makedirs(self.temp_folder, exist_ok=True)
        
        # Инициализируем style mapper
        if self.settings['mapping_json']:
            try:
                mapping_data = json.loads(self.settings['mapping_json'])
                self.style_mapper.load_mapping(mapping_data)
                self.log_message.emit("🎨 JSON-сопоставление загружено")
            except json.JSONDecodeError as e:
                self.log_message.emit(f"⚠️ Ошибка загрузки JSON-сопоставления: {str(e)}")
        
        # Проверяем mkgmap
        if not self.mkgmap_compiler.validate_mkgmap(self.settings['mkgmap_path']):
            raise Exception("Неверный путь к mkgmap.jar")
        
        self.log_message.emit("✅ Подготовка завершена")
    
    def process_layers(self):
        """Обработка выбранных слоёв"""
        self.progress.emit(20, "Обработка слоёв...")
        self.log_message.emit("📁 Начало обработки слоёв")
        
        total_layers = len(self.selected_layers)
        self.processed_data = []
        
        for i, layer_info in enumerate(self.selected_layers):
            if self.is_cancelled:
                return
            
            layer_name = layer_info['name']
            self.log_message.emit(f"🔄 Обработка слоя: {layer_name}")
            
            try:
                # Получаем слой по имени
                from ..gui.gui_handlers import LayerManager
                layer = LayerManager.get_layer_by_name(layer_name)
                
                if not layer:
                    raise Exception(f"Слой '{layer_name}' не найден")
                
                # Обрабатываем слой
                layer_data = self.layer_processor.process_layer(
                    layer, 
                    self.style_mapper,
                    self.settings['enabled_levels']
                )
                
                self.processed_data.append(layer_data)
                
                # Обновляем прогресс
                progress_value = 20 + int((i + 1) / total_layers * 40)
                self.progress.emit(progress_value, f"Обработан слой: {layer_name}")
                
                self.layer_processed.emit(layer_name, True, f"Обработано объектов: {len(layer_data.get('features', []))}")
                
            except Exception as e:
                error_msg = str(e)
                self.log_message.emit(f"❌ Ошибка обработки слоя '{layer_name}': {error_msg}")
                self.layer_processed.emit(layer_name, False, error_msg)
                # Продолжаем обработку других слоёв
                continue
        
        self.log_message.emit(f"📊 Обработано слоёв: {len(self.processed_data)} из {total_layers}")
    
    def generate_mp_file(self):
        """Генерация MP файла"""
        self.progress.emit(60, "Генерация MP файла...")
        self.log_message.emit("📝 Генерация файла формата Polish (MP)")
        
        if self.is_cancelled:
            return
        
        # Путь к выходному MP файлу
        mp_filename = f"{self.settings['output_filename']}.mp"
        self.mp_file_path = os.path.join(self.temp_folder, mp_filename)
        
        # Настройки MP файла
        mp_settings = {
            'family_id': self.settings['family_id'],
            'map_id': self.settings['map_id'],
            'map_name': self.settings['map_name'],
            'map_description': self.settings.get('map_description', ''),
            'transparent': self.settings.get('transparent', False),
            'routing': self.settings.get('routing', False),
            'enabled_levels': self.settings['enabled_levels']
        }
        
        # Генерируем MP файл
        try:
            self.mp_generator.generate_mp_file(
                self.processed_data,
                self.mp_file_path,
                mp_settings
            )
            
            self.log_message.emit(f"📄 MP файл создан: {self.mp_file_path}")
            
        except Exception as e:
            raise Exception(f"Ошибка генерации MP файла: {str(e)}")
    
    def compile_to_img(self):
        """Компиляция MP в IMG через mkgmap"""
        self.progress.emit(80, "Компиляция через mkgmap...")
        self.log_message.emit("⚙️ Запуск компиляции mkgmap")
        
        if self.is_cancelled:
            return ""
        
        # Настройки компиляции
        compilation_settings = {
            'mkgmap_path': self.settings['mkgmap_path'],
            'input_file': self.mp_file_path,
            'output_folder': self.settings['output_folder'],
            'output_filename': self.settings['output_filename'],
            'family_id': self.settings['family_id'],
            'map_name': self.settings['map_name']
        }
        
        try:
            output_file = self.mkgmap_compiler.compile_to_img(
                compilation_settings,
                progress_callback=self.on_mkgmap_progress
            )
            
            self.log_message.emit(f"🎯 IMG файл создан: {output_file}")
            
            # Очищаем временные файлы
            self.cleanup_temp_files()
            
            return output_file
            
        except Exception as e:
            raise Exception(f"Ошибка компиляции mkgmap: {str(e)}")
    
    def on_mkgmap_progress(self, message):
        """Обработчик прогресса mkgmap"""
        self.log_message.emit(f"⚙️ mkgmap: {message}")
    
    def cleanup_temp_files(self):
        """Очистка временных файлов"""
        try:
            if hasattr(self, 'mp_file_path') and os.path.exists(self.mp_file_path):
                os.remove(self.mp_file_path)
            
            if hasattr(self, 'temp_folder') and os.path.exists(self.temp_folder):
                import shutil
                shutil.rmtree(self.temp_folder, ignore_errors=True)
            
            self.log_message.emit("🧹 Временные файлы очищены")
            
        except Exception as e:
            self.log_message.emit(f"⚠️ Ошибка очистки временных файлов: {str(e)}")
    
    def stop(self):
        """Остановка выполнения"""
        self.is_cancelled = True
        self.log_message.emit("🛑 Получена команда остановки экспорта")
        
        # Останавливаем mkgmap если запущен
        if hasattr(self, 'mkgmap_compiler'):
            self.mkgmap_compiler.stop_compilation()
