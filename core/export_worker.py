# -*- coding: utf-8 -*-
"""
Export Worker for Garmin Export Plugin
Worker для экспорта данных в формат Garmin

Этапы: обработка слоёв -> генерация MP -> (опционально) генерация TYP
из стилей QGIS -> компиляция mkgmap -> выдача IMG.

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

import json
import os
import shutil
import tempfile

from qgis.PyQt.QtCore import QObject, pyqtSignal

from .mp_generator import MPGenerator
from .mkgmap_compiler import MkgmapCompiler
from . import mkgmap_command
from .layer_processor import LayerProcessor
from .layer_manager import LayerManager
from .style_mapper import StyleMapper
from . import typ_generator


class ExportWorker(QObject):
    """Worker для экспорта векторных данных в Garmin IMG"""

    # Сигналы
    finished = pyqtSignal(bool, str)  # success, output_file
    error = pyqtSignal(str)  # error_message
    progress = pyqtSignal(int, str)  # value, message
    log_message = pyqtSignal(str)  # message
    layer_processed = pyqtSignal(str, bool, str)  # layer_name, success, message

    def __init__(self, selected_layers, settings):
        """
        Args:
            selected_layers: список словарей {'id': layer_id, 'name': ...}
            settings: словарь настроек экспорта (см. GuiEventHandlers)
        """
        super().__init__()
        self.selected_layers = selected_layers
        self.settings = settings
        self.is_cancelled = False

        self.mp_generator = MPGenerator()
        self.mkgmap_compiler = MkgmapCompiler()
        self.layer_processor = LayerProcessor()
        self.style_mapper = StyleMapper()

        self.processed_data = []
        self.temp_folder = None
        self.mp_file_path = None
        self.typ_file_path = None

    # ------------------------------------------------------------------

    def run(self):
        """Основной метод выполнения экспорта"""
        try:
            self.log_message.emit('🚀 Начало экспорта данных в формат Garmin IMG')
            self.progress.emit(0, 'Инициализация экспорта...')

            if self.is_cancelled:
                self.finished.emit(False, '')
                return

            self.prepare_export()
            self.process_layers()

            if self.is_cancelled:
                self.finished.emit(False, '')
                return

            if not self.processed_data:
                raise Exception('Ни один слой не был обработан успешно')

            self.generate_mp_file()
            self.generate_typ_file()

            if self.is_cancelled:
                self.finished.emit(False, '')
                return

            output_file = self.compile_to_img()

            self.progress.emit(100, 'Экспорт завершён успешно!')
            self.log_message.emit('🎉 Экспорт завершён успешно!')
            self.finished.emit(True, output_file)

        except Exception as e:
            self.log_message.emit('❌ Ошибка экспорта: {0}'.format(str(e)))
            self.error.emit(str(e))
            self.finished.emit(False, '')
        finally:
            self.cleanup_temp_files()

    # ------------------------------------------------------------------

    def prepare_export(self):
        """Подготовка к экспорту"""
        self.progress.emit(5, 'Подготовка к экспорту...')
        self.log_message.emit('📋 Подготовка параметров экспорта')

        # Временная папка вне выходного каталога пользователя
        self.temp_folder = tempfile.mkdtemp(prefix='garmin_export_')

        # Инициализируем style mapper
        if self.settings.get('mapping_json'):
            try:
                mapping_data = json.loads(self.settings['mapping_json'])
                self.style_mapper.load_mapping(mapping_data)
                self.log_message.emit('🎨 JSON-сопоставление загружено')
            except json.JSONDecodeError as e:
                self.log_message.emit(
                    '⚠️ Ошибка загрузки JSON-сопоставления: {0}'.format(str(e)))

        # Проверяем mkgmap
        if not self.mkgmap_compiler.validate_mkgmap(self.settings['mkgmap_path']):
            raise Exception(
                'Неверный путь к mkgmap.jar. Скачайте mkgmap кнопкой '
                '"Скачать mkgmap" или укажите файл вручную.')

        self.log_message.emit('✅ Подготовка завершена')

    def process_layers(self):
        """Обработка выбранных слоёв"""
        self.progress.emit(10, 'Обработка слоёв...')
        self.log_message.emit('📁 Начало обработки слоёв')

        total_layers = len(self.selected_layers)
        self.processed_data = []
        self._layer_entries_for_typ = []

        for i, layer_info in enumerate(self.selected_layers):
            if self.is_cancelled:
                return

            layer_name = layer_info.get('name', '?')
            self.log_message.emit('🔄 Обработка слоя: {0}'.format(layer_name))

            try:
                layer = None
                if layer_info.get('id'):
                    layer = LayerManager.get_layer_by_id(layer_info['id'])
                if layer is None:
                    layer = LayerManager.get_layer_by_name(layer_name)
                if layer is None:
                    raise Exception('Слой "{0}" не найден'.format(layer_name))

                layer_data = self.layer_processor.process_layer(
                    layer,
                    self.style_mapper,
                    self.settings.get('enabled_levels', [0, 1, 2, 3]),
                    log_callback=lambda msg: self.log_message.emit('⚠️ ' + msg),
                )

                self.processed_data.append(layer_data)
                self._layer_entries_for_typ.append({
                    'layer': layer,
                    'name': layer_name,
                    'garmin_type': layer_data.get('garmin_type', '0x01'),
                    'geometry_type': layer_data.get('geometry_type'),
                })

                progress_value = 10 + int((i + 1) / total_layers * 40)
                self.progress.emit(progress_value,
                                   'Обработан слой: {0}'.format(layer_name))
                self.layer_processed.emit(
                    layer_name, True,
                    'Обработано объектов: {0}'.format(layer_data.get('feature_count', 0)))

            except Exception as e:
                error_msg = str(e)
                self.log_message.emit(
                    '❌ Ошибка обработки слоя "{0}": {1}'.format(layer_name, error_msg))
                self.layer_processed.emit(layer_name, False, error_msg)
                continue

        self.log_message.emit('📊 Обработано слоёв: {0} из {1}'.format(
            len(self.processed_data), total_layers))

    def generate_mp_file(self):
        """Генерация MP файла"""
        self.progress.emit(55, 'Генерация MP файла...')
        self.log_message.emit('📝 Генерация файла формата Polish (MP)')

        if self.is_cancelled:
            return

        mp_filename = '{0}.mp'.format(self.settings.get('output_filename') or 'map')
        self.mp_file_path = os.path.join(self.temp_folder, mp_filename)

        mp_settings = {
            'family_id': self.settings['family_id'],
            'map_id': self.settings['map_id'],
            'map_name': self.settings['map_name'],
            'map_description': self.settings.get('map_description', ''),
            'transparent': self.settings.get('transparent', False),
            'routing': self.settings.get('routing', False),
            'enabled_levels': self.settings.get('enabled_levels', [0, 1, 2, 3]),
            'code_page': self.settings.get('code_page', '1251'),
        }

        try:
            self.mp_generator.generate_mp_file(
                self.processed_data, self.mp_file_path, mp_settings)
        except Exception as e:
            raise Exception('Ошибка генерации MP файла: {0}'.format(str(e)))

        stats = self.mp_generator.get_statistics()
        self.log_message.emit(
            '📄 MP файл создан: {0} (POI: {1}, линий: {2}, полигонов: {3})'.format(
                self.mp_file_path, stats['poi_count'],
                stats['polyline_count'], stats['polygon_count']))
        if stats.get('skipped_count'):
            self.log_message.emit(
                '⚠️ Пропущено некорректных геометрий: {0}'.format(stats['skipped_count']))

        if self.settings.get('keep_temp_files'):
            keep_path = os.path.join(self.settings['output_folder'], mp_filename)
            try:
                shutil.copy2(self.mp_file_path, keep_path)
                self.log_message.emit('💾 Копия MP файла: {0}'.format(keep_path))
            except OSError as e:
                self.log_message.emit(
                    '⚠️ Не удалось сохранить копию MP файла: {0}'.format(str(e)))

    def generate_typ_file(self):
        """Генерация TYP файла (стилизация из QGIS) при необходимости"""
        typ_mode = self.settings.get('typ_mode', 'none')

        if typ_mode == 'file':
            typ_path = self.settings.get('typ_file_path', '')
            if typ_path and os.path.isfile(typ_path):
                self.typ_file_path = typ_path
                self.log_message.emit('🎨 Используется TYP файл: {0}'.format(typ_path))
            else:
                self.log_message.emit(
                    '⚠️ TYP файл не найден, стилизация пропущена: {0}'.format(typ_path))
            return

        if typ_mode != 'generate':
            return

        self.progress.emit(65, 'Генерация TYP из стилей QGIS...')
        self.log_message.emit('🎨 Генерация TYP файла из символики слоёв QGIS')

        try:
            typ_text = typ_generator.build_typ_from_layers(
                self._layer_entries_for_typ,
                family_id=self.settings['family_id'],
                product_id=1,
                code_page=self.settings.get('code_page', '1251'),
                log_callback=lambda msg: self.log_message.emit('⚠️ ' + msg),
            )

            self.typ_file_path = os.path.join(self.temp_folder, 'style.txt')
            with open(self.typ_file_path, 'w', encoding='utf-8') as f:
                f.write('; -*- coding: utf-8 -*-\n')
                f.write(typ_text)

            self.log_message.emit('🎨 TYP файл сгенерирован: {0}'.format(
                self.typ_file_path))

            if self.settings.get('keep_temp_files'):
                keep_path = os.path.join(
                    self.settings['output_folder'], 'style.typ.txt')
                try:
                    shutil.copy2(self.typ_file_path, keep_path)
                    self.log_message.emit('💾 Копия TYP файла: {0}'.format(keep_path))
                except OSError:
                    pass

        except Exception as e:
            # TYP не критичен: карта соберётся со стилем Garmin по умолчанию
            self.typ_file_path = None
            self.log_message.emit(
                '⚠️ Не удалось сгенерировать TYP, используется стиль Garmin '
                'по умолчанию: {0}'.format(str(e)))

    def compile_to_img(self):
        """Компиляция MP в IMG через mkgmap"""
        self.progress.emit(70, 'Компиляция через mkgmap...')
        self.log_message.emit('⚙️ Запуск компиляции mkgmap')

        if self.is_cancelled:
            return ''

        input_files = [self.mp_file_path]
        if self.typ_file_path:
            # TYP файл должен идти после карт (см. Tuning документацию)
            input_files.append(self.typ_file_path)

        mkgmap_options = dict(self.settings.get('mkgmap_options') or {})
        mkgmap_options.setdefault('family_id', self.settings['family_id'])
        mkgmap_options.setdefault('family_name', self.settings['map_name'])
        mkgmap_options.setdefault('description', self.settings['map_name'])
        mkgmap_options.setdefault('code_page', self.settings.get('code_page', '1251'))
        mkgmap_options.setdefault('transparent', self.settings.get('transparent', False))
        mkgmap_options.setdefault('route', self.settings.get('routing', False))

        # Конфигурация логирования mkgmap
        if self.settings.get('mkgmap_logging'):
            log_file = os.path.join(self.settings['output_folder'], 'mkgmap.log')
            log_config_path = os.path.join(self.temp_folder, 'logging.properties')
            try:
                with open(log_config_path, 'w', encoding='utf-8') as f:
                    f.write(mkgmap_command.build_logging_config(
                        log_file, verbose=self.settings.get('mkgmap_verbose', False)))
                mkgmap_options['log_config'] = log_config_path
                self.log_message.emit('📜 Журнал mkgmap: {0}'.format(log_file))
            except OSError as e:
                self.log_message.emit(
                    '⚠️ Не удалось создать конфигурацию логирования: {0}'.format(str(e)))

        compilation_settings = {
            'mkgmap_path': self.settings['mkgmap_path'],
            'java_path': self.settings.get('java_path', ''),
            'input_files': input_files,
            'output_folder': self.settings['output_folder'],
            'output_filename': self.settings.get('output_filename', ''),
            'mkgmap_options': mkgmap_options,
        }

        try:
            output_file = self.mkgmap_compiler.compile_to_img(
                compilation_settings,
                progress_callback=self.on_mkgmap_progress)
        except Exception as e:
            raise Exception('Ошибка компиляции mkgmap: {0}'.format(str(e)))

        output_file = self._rename_output(output_file)

        self.log_message.emit('🎯 IMG файл создан: {0}'.format(output_file))
        self.log_message.emit(
            '💡 Для загрузки в навигатор скопируйте файл в папку /Garmin '
            'на устройстве или карте памяти.')

        return output_file

    def _rename_output(self, output_file):
        """Переименование gmapsupp.img в имя, заданное пользователем"""
        desired = (self.settings.get('output_filename') or '').strip()
        if not desired:
            return output_file

        base = os.path.basename(output_file).lower()
        if base != 'gmapsupp.img' or desired.lower() == 'gmapsupp':
            return output_file

        target = os.path.join(self.settings['output_folder'], desired + '.img')
        try:
            if os.path.exists(target):
                os.remove(target)
            os.replace(output_file, target)
            return target
        except OSError:
            return output_file

    def on_mkgmap_progress(self, message):
        """Обработчик прогресса mkgmap"""
        self.log_message.emit('⚙️ mkgmap: {0}'.format(message))

    def cleanup_temp_files(self):
        """Очистка временных файлов"""
        if not self.temp_folder:
            return
        try:
            shutil.rmtree(self.temp_folder, ignore_errors=True)
            self.temp_folder = None
        except OSError:
            pass

    def stop(self):
        """Остановка выполнения"""
        self.is_cancelled = True
        self.log_message.emit('🛑 Получена команда остановки экспорта')
        self.mkgmap_compiler.stop_compilation()
