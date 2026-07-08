# -*- coding: utf-8 -*-
"""
mkgmap Tool Widgets for Garmin Export Plugin
Виджеты настройки инструментов mkgmap: пути, скачивание, тонкая настройка

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""

from qgis.PyQt.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QCheckBox, QSpinBox, QComboBox, QRadioButton,
    QButtonGroup, QDoubleSpinBox
)

from .gui_components import create_styled_button, create_info_label


# Поддерживаемые кодовые страницы: (код, ключ перевода названия)
# см. --code-page в документации mkgmap
CODE_PAGES = [
    ('1251', 'cp_1251'),
    ('1252', 'cp_1252'),
    ('1250', 'cp_1250'),
    ('1253', 'cp_1253'),
    ('1254', 'cp_1254'),
    ('1257', 'cp_1257'),
    ('65001', 'cp_65001'),
]


def _t(key):
    from ..translation_manager import translations
    return translations.get_text(key)


class MkgmapToolsWidget(QWidget):
    """Виджет путей к инструментам: mkgmap, splitter, Java"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(15)

        self.tools_group = QGroupBox()
        grid = QGridLayout(self.tools_group)
        grid.setSpacing(10)

        # --- mkgmap.jar ---
        self.mkgmap_label = QLabel()
        grid.addWidget(self.mkgmap_label, 0, 0)

        mkgmap_layout = QHBoxLayout()
        self.mkgmap_path_line = QLineEdit()
        self.mkgmap_browse_button = create_styled_button("", icon_text="📂")
        self.mkgmap_download_button = create_styled_button("", "success-button", "📥")

        mkgmap_layout.addWidget(self.mkgmap_path_line)
        mkgmap_layout.addWidget(self.mkgmap_browse_button)
        mkgmap_layout.addWidget(self.mkgmap_download_button)
        grid.addLayout(mkgmap_layout, 0, 1)

        self.mkgmap_status_label = QLabel("")
        self.mkgmap_status_label.setStyleSheet("color: #7f8c8d; font-size: 10px;")
        grid.addWidget(self.mkgmap_status_label, 1, 1)

        # --- splitter.jar ---
        self.splitter_label = QLabel()
        grid.addWidget(self.splitter_label, 2, 0)

        splitter_layout = QHBoxLayout()
        self.splitter_path_line = QLineEdit()
        self.splitter_browse_button = create_styled_button("", icon_text="📂")
        self.splitter_download_button = create_styled_button("", "success-button", "📥")

        splitter_layout.addWidget(self.splitter_path_line)
        splitter_layout.addWidget(self.splitter_browse_button)
        splitter_layout.addWidget(self.splitter_download_button)
        grid.addLayout(splitter_layout, 2, 1)

        # --- Java ---
        self.java_label = QLabel()
        grid.addWidget(self.java_label, 3, 0)

        java_layout = QHBoxLayout()
        self.java_path_line = QLineEdit()
        self.java_browse_button = create_styled_button("", icon_text="📂")
        self.java_detect_button = create_styled_button("", "warning-button", "🔍")

        java_layout.addWidget(self.java_path_line)
        java_layout.addWidget(self.java_browse_button)
        java_layout.addWidget(self.java_detect_button)
        grid.addLayout(java_layout, 3, 1)

        self.java_status_label = QLabel("")
        self.java_status_label.setStyleSheet("color: #7f8c8d; font-size: 10px;")
        grid.addWidget(self.java_status_label, 4, 1)

        self.tools_info_label = create_info_label("")
        grid.addWidget(self.tools_info_label, 5, 0, 1, 2)

        layout.addWidget(self.tools_group)

        self.retranslateUi()

    def retranslateUi(self):
        self.tools_group.setTitle("🧰 " + _t('tools_mkgmap'))
        self.mkgmap_label.setText(_t('mkgmap_path_label'))
        self.mkgmap_path_line.setPlaceholderText(_t('mkgmap_path_placeholder'))
        self.mkgmap_browse_button.setText("📂 " + _t('add_mkgmap'))
        self.mkgmap_download_button.setText("📥 " + _t('download_mkgmap'))
        self.splitter_label.setText(_t('splitter_path_label'))
        self.splitter_path_line.setPlaceholderText(_t('splitter_path_placeholder'))
        self.splitter_browse_button.setText("📂 " + _t('add_splitter'))
        self.splitter_download_button.setText("📥 " + _t('download_splitter'))
        self.java_label.setText(_t('java_path_label'))
        self.java_path_line.setPlaceholderText(_t('java_path_placeholder'))
        self.java_browse_button.setText("📂 " + _t('browse'))
        self.java_detect_button.setText("🔍 " + _t('detect_java'))
        self.tools_info_label.setText(_t('tools_info'))


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

        self.retranslateUi()

    def createGeneralGroup(self):
        """Основные опции карты"""
        self.general_group = QGroupBox()
        grid = QGridLayout(self.general_group)
        grid.setSpacing(10)

        self.code_page_label = QLabel()
        grid.addWidget(self.code_page_label, 0, 0)
        self.code_page_combo = QComboBox()
        for code, key in CODE_PAGES:
            self.code_page_combo.addItem("", code)
        grid.addWidget(self.code_page_combo, 0, 1)

        self.draw_priority_label = QLabel()
        grid.addWidget(self.draw_priority_label, 1, 0)
        self.draw_priority_spin = QSpinBox()
        self.draw_priority_spin.setRange(0, 127)
        self.draw_priority_spin.setValue(25)
        grid.addWidget(self.draw_priority_spin, 1, 1)

        self.index_cb = QCheckBox()
        grid.addWidget(self.index_cb, 2, 0, 1, 2)

        self.pois_to_areas_cb = QCheckBox()
        grid.addWidget(self.pois_to_areas_cb, 3, 0, 1, 2)

        self.lower_case_cb = QCheckBox()
        grid.addWidget(self.lower_case_cb, 4, 0, 1, 2)

        self.order_area_cb = QCheckBox()
        grid.addWidget(self.order_area_cb, 5, 0, 1, 2)

    def createGeneralizationGroup(self):
        """Опции генерализации геометрии"""
        self.generalization_group = QGroupBox()
        grid = QGridLayout(self.generalization_group)
        grid.setSpacing(10)

        self.reduce_density_label = QLabel()
        grid.addWidget(self.reduce_density_label, 0, 0)
        self.reduce_density_spin = QDoubleSpinBox()
        self.reduce_density_spin.setRange(0.0, 50.0)
        self.reduce_density_spin.setDecimals(1)
        self.reduce_density_spin.setSingleStep(0.5)
        self.reduce_density_spin.setValue(0.0)
        grid.addWidget(self.reduce_density_spin, 0, 1)

        self.reduce_density_polygon_label = QLabel()
        grid.addWidget(self.reduce_density_polygon_label, 1, 0)
        self.reduce_density_polygon_spin = QDoubleSpinBox()
        self.reduce_density_polygon_spin.setRange(0.0, 50.0)
        self.reduce_density_polygon_spin.setDecimals(1)
        self.reduce_density_polygon_spin.setSingleStep(0.5)
        self.reduce_density_polygon_spin.setValue(0.0)
        grid.addWidget(self.reduce_density_polygon_spin, 1, 1)

        self.min_polygon_label = QLabel()
        grid.addWidget(self.min_polygon_label, 2, 0)
        self.min_polygon_spin = QSpinBox()
        self.min_polygon_spin.setRange(0, 100)
        self.min_polygon_spin.setValue(8)
        grid.addWidget(self.min_polygon_spin, 2, 1)

    def createPerformanceGroup(self):
        """Опции производительности (Tuning документация mkgmap)"""
        self.performance_group = QGroupBox()
        grid = QGridLayout(self.performance_group)
        grid.setSpacing(10)

        self.java_heap_label = QLabel()
        grid.addWidget(self.java_heap_label, 0, 0)
        self.java_heap_spin = QSpinBox()
        self.java_heap_spin.setRange(0, 64)
        self.java_heap_spin.setValue(0)
        grid.addWidget(self.java_heap_spin, 0, 1)

        self.max_jobs_label = QLabel()
        grid.addWidget(self.max_jobs_label, 1, 0)
        self.max_jobs_spin = QSpinBox()
        self.max_jobs_spin.setRange(0, 64)
        self.max_jobs_spin.setValue(0)
        grid.addWidget(self.max_jobs_spin, 1, 1)

    def createLoggingGroup(self):
        """Опции логирования (Logging документация mkgmap)"""
        self.logging_group = QGroupBox()
        grid = QGridLayout(self.logging_group)
        grid.setSpacing(10)

        self.mkgmap_log_cb = QCheckBox()
        grid.addWidget(self.mkgmap_log_cb, 0, 0, 1, 2)

        self.verbose_cb = QCheckBox()
        self.verbose_cb.setEnabled(False)
        grid.addWidget(self.verbose_cb, 1, 0, 1, 2)

        self.keep_temp_cb = QCheckBox()
        grid.addWidget(self.keep_temp_cb, 2, 0, 1, 2)

        self.extra_args_label = QLabel()
        grid.addWidget(self.extra_args_label, 3, 0)
        self.extra_args_line = QLineEdit()
        grid.addWidget(self.extra_args_line, 3, 1)

        self.mkgmap_log_cb.toggled.connect(self.verbose_cb.setEnabled)

    def retranslateUi(self):
        # Группы
        self.general_group.setTitle("🗺️ " + _t('map_params_group'))
        self.generalization_group.setTitle("📐 " + _t('generalization_group'))
        self.performance_group.setTitle("🚀 " + _t('performance_group'))
        self.logging_group.setTitle("📜 " + _t('logging_group'))

        # Кодовые страницы (сохраняем текущий выбор)
        current = self.code_page_combo.currentData()
        for i, (code, key) in enumerate(CODE_PAGES):
            self.code_page_combo.setItemText(i, _t(key))
        if current:
            idx = self.code_page_combo.findData(current)
            if idx >= 0:
                self.code_page_combo.setCurrentIndex(idx)

        # Основные опции
        self.code_page_label.setText(_t('code_page_label'))
        self.draw_priority_label.setText(_t('draw_priority_label'))
        self.draw_priority_spin.setToolTip(_t('draw_priority_tip'))
        self.index_cb.setText(_t('opt_index'))
        self.pois_to_areas_cb.setText(_t('opt_add_pois'))
        self.lower_case_cb.setText(_t('opt_lower_case'))
        self.order_area_cb.setText(_t('opt_order_area'))

        # Генерализация
        self.reduce_density_label.setText(_t('reduce_density_label'))
        self.reduce_density_spin.setSpecialValueText(_t('value_auto_default'))
        self.reduce_density_polygon_label.setText(_t('reduce_density_polygon_label'))
        self.reduce_density_polygon_spin.setSpecialValueText(_t('value_auto'))
        self.min_polygon_label.setText(_t('min_polygon_label'))
        self.min_polygon_spin.setToolTip(_t('min_polygon_tip'))

        # Производительность
        self.java_heap_label.setText(_t('java_heap_label'))
        self.java_heap_spin.setSpecialValueText(_t('value_auto'))
        self.java_heap_spin.setToolTip(_t('java_heap_tip'))
        self.max_jobs_label.setText(_t('max_jobs_label'))
        self.max_jobs_spin.setSpecialValueText(_t('value_auto'))
        self.max_jobs_spin.setToolTip(_t('max_jobs_tip'))

        # Логирование
        self.mkgmap_log_cb.setText(_t('opt_mkgmap_log'))
        self.verbose_cb.setText(_t('opt_verbose'))
        self.keep_temp_cb.setText(_t('opt_keep_temp'))
        self.extra_args_label.setText(_t('extra_args_label'))
        self.extra_args_line.setPlaceholderText(_t('extra_args_placeholder'))

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

        self.typ_group = QGroupBox()
        group_layout = QVBoxLayout(self.typ_group)
        group_layout.setSpacing(10)

        self.typ_info_label = create_info_label("")

        self.typ_none_rb = QRadioButton()
        self.typ_generate_rb = QRadioButton()
        self.typ_file_rb = QRadioButton()

        self.typ_mode_group = QButtonGroup(self)
        self.typ_mode_group.addButton(self.typ_none_rb)
        self.typ_mode_group.addButton(self.typ_generate_rb)
        self.typ_mode_group.addButton(self.typ_file_rb)

        self.typ_generate_rb.setChecked(True)

        file_layout = QHBoxLayout()
        self.typ_file_line = QLineEdit()
        self.typ_file_line.setEnabled(False)
        self.typ_file_browse_button = create_styled_button("", icon_text="📂")
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

        self.retranslateUi()

    def retranslateUi(self):
        self.typ_group.setTitle("🖌️ " + _t('typ_styling'))
        self.typ_info_label.setText(_t('typ_info'))
        self.typ_none_rb.setText(_t('typ_none'))
        self.typ_generate_rb.setText(_t('typ_generate'))
        self.typ_file_rb.setText(_t('typ_file'))
        self.typ_file_line.setPlaceholderText(_t('typ_file_placeholder'))
        self.typ_file_browse_button.setText("📂 " + _t('browse'))

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
