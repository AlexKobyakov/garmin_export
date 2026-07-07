# -*- coding: utf-8 -*-
"""
mkgmap Tool Widgets for Garmin Export Plugin
Виджеты настройки инструментов mkgmap: пути, скачивание, тонкая настройка

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

from qgis.PyQt.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QCheckBox, QSpinBox, QComboBox, QRadioButton,
    QButtonGroup, QDoubleSpinBox
)

from .gui_components import create_styled_button, create_info_label


# Поддерживаемые кодовые страницы (см. --code-page в документации mkgmap)
CODE_PAGES = [
    ('1251', 'CP1251 (кириллица)'),
    ('1252', 'CP1252 (Latin-1, Западная Европа)'),
    ('1250', 'CP1250 (Центральная Европа)'),
    ('1253', 'CP1253 (греческий)'),
    ('1254', 'CP1254 (турецкий)'),
    ('1257', 'CP1257 (балтийский)'),
    ('65001', 'Unicode (не все устройства)'),
]


class MkgmapToolsWidget(QWidget):
    """Виджет путей к инструментам: mkgmap, splitter, Java"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(15)

        self.tools_group = QGroupBox("🧰 Инструменты mkgmap")
        grid = QGridLayout(self.tools_group)
        grid.setSpacing(10)

        # --- mkgmap.jar ---
        self.mkgmap_label = QLabel("Путь к mkgmap.jar:")
        grid.addWidget(self.mkgmap_label, 0, 0)

        mkgmap_layout = QHBoxLayout()
        self.mkgmap_path_line = QLineEdit()
        self.mkgmap_path_line.setPlaceholderText("Выберите или скачайте mkgmap.jar")
        self.mkgmap_browse_button = create_styled_button("Добавить mkgmap", icon_text="📂")
        self.mkgmap_download_button = create_styled_button(
            "Скачать mkgmap", "success-button", "📥")

        mkgmap_layout.addWidget(self.mkgmap_path_line)
        mkgmap_layout.addWidget(self.mkgmap_browse_button)
        mkgmap_layout.addWidget(self.mkgmap_download_button)
        grid.addLayout(mkgmap_layout, 0, 1)

        self.mkgmap_status_label = QLabel("")
        self.mkgmap_status_label.setStyleSheet("color: #7f8c8d; font-size: 10px;")
        grid.addWidget(self.mkgmap_status_label, 1, 1)

        # --- splitter.jar ---
        self.splitter_label = QLabel("Путь к splitter.jar (необязательно):")
        grid.addWidget(self.splitter_label, 2, 0)

        splitter_layout = QHBoxLayout()
        self.splitter_path_line = QLineEdit()
        self.splitter_path_line.setPlaceholderText(
            "splitter нужен для нарезки больших карт (необязательно)")
        self.splitter_browse_button = create_styled_button("Добавить splitter", icon_text="📂")
        self.splitter_download_button = create_styled_button(
            "Скачать splitter", "success-button", "📥")

        splitter_layout.addWidget(self.splitter_path_line)
        splitter_layout.addWidget(self.splitter_browse_button)
        splitter_layout.addWidget(self.splitter_download_button)
        grid.addLayout(splitter_layout, 2, 1)

        # --- Java ---
        self.java_label = QLabel("Путь к Java:")
        grid.addWidget(self.java_label, 3, 0)

        java_layout = QHBoxLayout()
        self.java_path_line = QLineEdit()
        self.java_path_line.setPlaceholderText(
            "Пусто = java из PATH; кнопка справа найдёт автоматически")
        self.java_browse_button = create_styled_button("Обзор...", icon_text="📂")
        self.java_detect_button = create_styled_button(
            "Найти автоматически", "warning-button", "🔍")

        java_layout.addWidget(self.java_path_line)
        java_layout.addWidget(self.java_browse_button)
        java_layout.addWidget(self.java_detect_button)
        grid.addLayout(java_layout, 3, 1)

        self.java_status_label = QLabel("")
        self.java_status_label.setStyleSheet("color: #7f8c8d; font-size: 10px;")
        grid.addWidget(self.java_status_label, 4, 1)

        self.tools_info_label = create_info_label(
            "Правила QGIS запрещают включать mkgmap.jar в состав плагина. "
            "Нажмите «Скачать mkgmap» — плагин получит последнюю версию с "
            "mkgmap.org.uk (или с резервного Яндекс.Диска), либо укажите "
            "свой файл кнопкой «Добавить mkgmap».")
        grid.addWidget(self.tools_info_label, 5, 0, 1, 2)

        layout.addWidget(self.tools_group)


class AdvancedOptionsWidget(QWidget):
    """Виджет тонкой настройки mkgmap: опции, генерализация,
    производительность, логирование"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(15)

        self.createGeneralGroup()
        self.createGeneralizationGroup()
        self.createPerformanceGroup()
        self.createLoggingGroup()

        layout.addWidget(self.general_group)
        layout.addWidget(self.generalization_group)
        layout.addWidget(self.performance_group)
        layout.addWidget(self.logging_group)
        layout.addStretch()

    def createGeneralGroup(self):
        """Основные опции карты"""
        self.general_group = QGroupBox("🗺️ Параметры карты (mkgmap)")
        grid = QGridLayout(self.general_group)
        grid.setSpacing(10)

        self.code_page_label = QLabel("Кодовая страница подписей:")
        grid.addWidget(self.code_page_label, 0, 0)
        self.code_page_combo = QComboBox()
        for code, title in CODE_PAGES:
            self.code_page_combo.addItem(title, code)
        grid.addWidget(self.code_page_combo, 0, 1)

        self.draw_priority_label = QLabel("Приоритет отрисовки (--draw-priority):")
        grid.addWidget(self.draw_priority_label, 1, 0)
        self.draw_priority_spin = QSpinBox()
        self.draw_priority_spin.setRange(0, 127)
        self.draw_priority_spin.setValue(25)
        self.draw_priority_spin.setToolTip(
            "25 - стандарт. Больше = карта рисуется поверх других. "
            "Для прозрачных карт-надстроек ставьте больше 25.")
        grid.addWidget(self.draw_priority_spin, 1, 1)

        self.index_cb = QCheckBox("Адресный индекс для поиска (--index)")
        grid.addWidget(self.index_cb, 2, 0, 1, 2)

        self.pois_to_areas_cb = QCheckBox(
            "Создавать POI из полигонов (--add-pois-to-areas)")
        grid.addWidget(self.pois_to_areas_cb, 3, 0, 1, 2)

        self.lower_case_cb = QCheckBox(
            "Разрешить строчные буквы в подписях (--lower-case)")
        grid.addWidget(self.lower_case_cb, 4, 0, 1, 2)

        self.order_area_cb = QCheckBox(
            "Мелкие полигоны поверх крупных (--order-by-decreasing-area)")
        grid.addWidget(self.order_area_cb, 5, 0, 1, 2)

    def createGeneralizationGroup(self):
        """Опции генерализации геометрии"""
        self.generalization_group = QGroupBox("📐 Генерализация")
        grid = QGridLayout(self.generalization_group)
        grid.setSpacing(10)

        self.reduce_density_label = QLabel("Упрощение линий, м (--reduce-point-density):")
        grid.addWidget(self.reduce_density_label, 0, 0)
        self.reduce_density_spin = QDoubleSpinBox()
        self.reduce_density_spin.setRange(0.0, 50.0)
        self.reduce_density_spin.setDecimals(1)
        self.reduce_density_spin.setSingleStep(0.5)
        self.reduce_density_spin.setValue(0.0)
        self.reduce_density_spin.setSpecialValueText("авто (2.6)")
        grid.addWidget(self.reduce_density_spin, 0, 1)

        self.reduce_density_polygon_label = QLabel(
            "Упрощение полигонов, м (--reduce-point-density-polygon):")
        grid.addWidget(self.reduce_density_polygon_label, 1, 0)
        self.reduce_density_polygon_spin = QDoubleSpinBox()
        self.reduce_density_polygon_spin.setRange(0.0, 50.0)
        self.reduce_density_polygon_spin.setDecimals(1)
        self.reduce_density_polygon_spin.setSingleStep(0.5)
        self.reduce_density_polygon_spin.setValue(0.0)
        self.reduce_density_polygon_spin.setSpecialValueText("авто")
        grid.addWidget(self.reduce_density_polygon_spin, 1, 1)

        self.min_polygon_label = QLabel("Мин. размер полигона (--min-size-polygon):")
        grid.addWidget(self.min_polygon_label, 2, 0)
        self.min_polygon_spin = QSpinBox()
        self.min_polygon_spin.setRange(0, 100)
        self.min_polygon_spin.setValue(8)
        self.min_polygon_spin.setToolTip(
            "Полигоны меньше этого размера удаляются. 8-15 рекомендовано.")
        grid.addWidget(self.min_polygon_spin, 2, 1)

    def createPerformanceGroup(self):
        """Опции производительности (Tuning документация mkgmap)"""
        self.performance_group = QGroupBox("🚀 Производительность (тюнинг)")
        grid = QGridLayout(self.performance_group)
        grid.setSpacing(10)

        self.java_heap_label = QLabel("Память Java, ГБ (-Xmx):")
        grid.addWidget(self.java_heap_label, 0, 0)
        self.java_heap_spin = QSpinBox()
        self.java_heap_spin.setRange(0, 64)
        self.java_heap_spin.setValue(0)
        self.java_heap_spin.setSpecialValueText("авто")
        self.java_heap_spin.setToolTip(
            "mkgmap требует ~500 МБ на поток. Для 8 ядер задайте 4 ГБ.")
        grid.addWidget(self.java_heap_spin, 0, 1)

        self.max_jobs_label = QLabel("Потоки (--max-jobs):")
        grid.addWidget(self.max_jobs_label, 1, 0)
        self.max_jobs_spin = QSpinBox()
        self.max_jobs_spin.setRange(0, 64)
        self.max_jobs_spin.setValue(0)
        self.max_jobs_spin.setSpecialValueText("авто")
        self.max_jobs_spin.setToolTip(
            "0 = mkgmap определит по количеству ядер и памяти.")
        grid.addWidget(self.max_jobs_spin, 1, 1)

    def createLoggingGroup(self):
        """Опции логирования (Logging документация mkgmap)"""
        self.logging_group = QGroupBox("📜 Логирование и отладка")
        grid = QGridLayout(self.logging_group)
        grid.setSpacing(10)

        self.mkgmap_log_cb = QCheckBox(
            "Вести файл журнала mkgmap.log в выходной папке")
        grid.addWidget(self.mkgmap_log_cb, 0, 0, 1, 2)

        self.verbose_cb = QCheckBox("Подробный журнал (уровень INFO)")
        self.verbose_cb.setEnabled(False)
        grid.addWidget(self.verbose_cb, 1, 0, 1, 2)

        self.keep_temp_cb = QCheckBox(
            "Сохранять промежуточные файлы (MP, TYP) в выходной папке")
        grid.addWidget(self.keep_temp_cb, 2, 0, 1, 2)

        self.extra_args_label = QLabel("Доп. аргументы mkgmap:")
        grid.addWidget(self.extra_args_label, 3, 0)
        self.extra_args_line = QLineEdit()
        self.extra_args_line.setPlaceholderText(
            "например: --precomp-sea=C:/sea.zip --generate-sea")
        grid.addWidget(self.extra_args_line, 3, 1)

        self.mkgmap_log_cb.toggled.connect(self.verbose_cb.setEnabled)

    # ------------------------------------------------------------------

    def get_code_page(self):
        """Выбранная кодовая страница"""
        return self.code_page_combo.currentData() or '1251'

    def set_code_page(self, code):
        """Установка кодовой страницы"""
        index = self.code_page_combo.findData(str(code))
        if index >= 0:
            self.code_page_combo.setCurrentIndex(index)

    def get_mkgmap_options(self):
        """Словарь опций для mkgmap_command"""
        rpd = self.reduce_density_spin.value()
        rpdp = self.reduce_density_polygon_spin.value()
        return {
            'code_page': self.get_code_page(),
            'draw_priority': self.draw_priority_spin.value(),
            'index': self.index_cb.isChecked(),
            'add_pois_to_areas': self.pois_to_areas_cb.isChecked(),
            'lower_case': self.lower_case_cb.isChecked(),
            'order_by_decreasing_area': self.order_area_cb.isChecked(),
            'reduce_point_density': rpd if rpd > 0 else None,
            'reduce_point_density_polygon': rpdp if rpdp > 0 else None,
            'min_size_polygon': self.min_polygon_spin.value(),
            'java_xmx': '{0}g'.format(self.java_heap_spin.value())
                        if self.java_heap_spin.value() > 0 else '',
            'max_jobs': self.max_jobs_spin.value(),
            'extra_args': self.extra_args_line.text().strip(),
        }


class TypSettingsWidget(QWidget):
    """Виджет выбора режима стилизации TYP"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        self.typ_group = QGroupBox("🖌️ Стилизация карты (TYP)")
        group_layout = QVBoxLayout(self.typ_group)
        group_layout.setSpacing(10)

        self.typ_info_label = create_info_label(
            "TYP-файл задаёт внешний вид объектов на устройстве Garmin: "
            "цвета полигонов, толщину линий, иконки точек. Плагин может "
            "сгенерировать TYP автоматически из текущей символики слоёв QGIS "
            "— карта на навигаторе будет выглядеть как в QGIS.")

        self.typ_none_rb = QRadioButton("Стандартный стиль Garmin (без TYP)")
        self.typ_generate_rb = QRadioButton(
            "Сгенерировать TYP из стилей QGIS (рекомендуется)")
        self.typ_file_rb = QRadioButton("Использовать готовый файл TYP / typ.txt:")

        self.typ_mode_group = QButtonGroup(self)
        self.typ_mode_group.addButton(self.typ_none_rb)
        self.typ_mode_group.addButton(self.typ_generate_rb)
        self.typ_mode_group.addButton(self.typ_file_rb)

        self.typ_generate_rb.setChecked(True)

        file_layout = QHBoxLayout()
        self.typ_file_line = QLineEdit()
        self.typ_file_line.setPlaceholderText("Путь к файлу .typ или .txt")
        self.typ_file_line.setEnabled(False)
        self.typ_file_browse_button = create_styled_button("Обзор...", icon_text="📂")
        self.typ_file_browse_button.setEnabled(False)

        file_layout.addWidget(self.typ_file_line)
        file_layout.addWidget(self.typ_file_browse_button)

        self.typ_file_rb.toggled.connect(self.typ_file_line.setEnabled)
        self.typ_file_rb.toggled.connect(self.typ_file_browse_button.setEnabled)

        group_layout.addWidget(self.typ_info_label)
        group_layout.addWidget(self.typ_none_rb)
        group_layout.addWidget(self.typ_generate_rb)
        group_layout.addWidget(self.typ_file_rb)
        group_layout.addLayout(file_layout)

        layout.addWidget(self.typ_group)

    def get_typ_mode(self):
        """Режим TYP: 'none' | 'generate' | 'file'"""
        if self.typ_generate_rb.isChecked():
            return 'generate'
        if self.typ_file_rb.isChecked():
            return 'file'
        return 'none'

    def set_typ_mode(self, mode):
        """Установка режима TYP"""
        if mode == 'generate':
            self.typ_generate_rb.setChecked(True)
        elif mode == 'file':
            self.typ_file_rb.setChecked(True)
        else:
            self.typ_none_rb.setChecked(True)

    def get_typ_file_path(self):
        return self.typ_file_line.text().strip()

    def set_typ_file_path(self, path):
        self.typ_file_line.setText(path or '')
