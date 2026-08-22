# -*- coding: utf-8 -*-
"""Header and language selector widget."""

from qgis.PyQt.QtWidgets import QFrame, QHBoxLayout, QLabel, QComboBox, QWidget
from qgis.PyQt.QtGui import QColor

from .gui_components import ModernButton
from .widget_i18n import retranslate_header
from ..translation_manager import translations
from ..qgis_compat import qt_enum


class HeaderWidget(QFrame):
    """Gradient header with language, support and author controls."""

    retranslateUi = retranslate_header

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(90)
        self.setStyleSheet(
            'QFrame { background: qlineargradient(x1:0, y1:0, x2:1, y2:0,'
            ' stop:0 #3498db, stop:1 #2ecc71); border-radius: 10px;'
            ' margin: 5px; }')
        self.setupUi()
        self.retranslateUi()

    def setupUi(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 15, 20, 15)
        layout.setSpacing(20)
        self.title_label = QLabel()
        self.title_label.setStyleSheet(
            'color: white; font-size: 18px; font-weight: bold;'
            ' background: transparent;')
        self.controls_widget = QWidget()
        controls = QHBoxLayout(self.controls_widget)
        controls.setContentsMargins(0, 0, 0, 0)
        controls.setSpacing(15)
        self.createLanguageSelector(controls)
        self.createDonationButton(controls)
        self.createAuthorButton(controls)
        layout.addWidget(self.title_label)
        layout.addStretch()
        layout.addWidget(self.controls_widget)

    def createLanguageSelector(self, layout):
        container = QWidget()
        row = QHBoxLayout(container)
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(8)
        icon = QLabel('🌐')
        icon.setStyleSheet(
            'color: white; font-size: 16px; background: transparent;')
        self.language_combo = QComboBox()
        self.language_combo.setFixedSize(165, 32)
        foreground = QColor('#2c3e50')
        background = QColor('#ffffff')
        for code, label in translations.get_language_labels():
            self.language_combo.addItem(label, code)
            index = self.language_combo.count() - 1
            self.language_combo.setItemData(
                index, foreground, qt_enum('ItemDataRole', 'ForegroundRole'))
            self.language_combo.setItemData(
                index, background, qt_enum('ItemDataRole', 'BackgroundRole'))
        current = self.language_combo.findData(
            translations.get_current_language())
        if current >= 0:
            self.language_combo.setCurrentIndex(current)
        self.language_combo.setStyleSheet(
            'QComboBox { background: rgba(255,255,255,0.95);'
            ' color: #2c3e50; border: 2px solid rgba(255,255,255,0.6);'
            ' border-radius: 6px; padding: 4px 10px; font-weight: bold;'
            ' font-size: 11px; } QComboBox:hover { background: #ffffff;'
            ' border-color: #ffffff; } QComboBox::drop-down { border: none;'
            ' width: 20px; background: transparent; }'
            ' QComboBox QAbstractItemView { background-color: #ffffff;'
            ' color: #2c3e50; border: 2px solid #bdc3c7; outline: none;'
            ' selection-background-color: #3498db;'
            ' selection-color: #ffffff; }')
        row.addWidget(icon)
        row.addWidget(self.language_combo)
        layout.addWidget(container)

    def createDonationButton(self, layout):
        self.donation_button = ModernButton()
        self.donation_button.setFixedSize(120, 32)
        self.donation_button.setToolTip('')
        self.donation_button.setStyleSheet(
            'QPushButton { background: rgba(244,93,34,0.9); color: white;'
            ' border: 2px solid rgba(255,255,255,0.3); border-radius: 8px;'
            ' font-weight: bold; font-size: 11px; padding: 6px 12px; }'
            ' QPushButton:hover { background: rgba(244,93,34,1.0); }')
        layout.addWidget(self.donation_button)

    def createAuthorButton(self, layout):
        self.author_button = ModernButton()
        self.author_button.setFixedSize(100, 32)
        self.author_button.setToolTip('')
        self.author_button.setStyleSheet(
            'QPushButton { background: rgba(255,255,255,0.2); color: white;'
            ' border: 2px solid rgba(255,255,255,0.3); border-radius: 8px;'
            ' font-weight: bold; font-size: 11px; padding: 6px 12px; }'
            ' QPushButton:hover { background: rgba(255,255,255,0.3); }')
        layout.addWidget(self.author_button)
