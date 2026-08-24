# -*- coding: utf-8 -*-
"""
GUI Components for Garmin Export Plugin
Компоненты графического интерфейса для плагина экспорта в Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""

import os

from qgis.PyQt.QtCore import QRect, QSize
from qgis.PyQt.QtGui import QColor, QFont, QPalette
from qgis.PyQt.QtWidgets import (
    QComboBox, QGroupBox, QPushButton, QProgressBar, QLabel, QFrame,
    QStyledItemDelegate, QStyle)

from ..qgis_compat import qfont_weight, qt_class_enum, qt_enum


class ModernGroupBox(QGroupBox):
    """Стилизованная группа с современным дизайном"""

    def __init__(self, title="", parent=None):
        super().__init__(title, parent)
        self.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                font-size: 12px;
                color: #2c3e50;
                border: 2px solid #bdc3c7;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 5px;
                background-color: #f8f9fa;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 8px;
                background-color: white;
                border-radius: 4px;
            }
        """)


class ModernButton(QPushButton):
    """Стилизованная кнопка с современным дизайном"""

    def __init__(self, text="", button_type="primary", parent=None):
        super().__init__(text, parent)
        self.button_type = button_type
        self.setMinimumHeight(40)
        self.setFont(QFont("Segoe UI", 10, qfont_weight('Medium')))
        self.apply_style()

    def apply_style(self):
        """Применение стиля в зависимости от типа кнопки"""
        if self.button_type == "primary":
            self.setStyleSheet("""
                QPushButton {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                stop:0 #3498db, stop:1 #2980b9);
                    color: white;
                    border: none;
                    border-radius: 6px;
                    padding: 8px 16px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                stop:0 #5dade2, stop:1 #3498db);
                }
                QPushButton:pressed {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                stop:0 #2980b9, stop:1 #21618c);
                }
                QPushButton:disabled {
                    background: #bdc3c7;
                    color: #7f8c8d;
                }
            """)
        else:  # secondary
            self.setStyleSheet("""
                QPushButton {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                stop:0 #ecf0f1, stop:1 #d5dbdb);
                    color: #2c3e50;
                    border: 1px solid #bdc3c7;
                    border-radius: 6px;
                    padding: 8px 16px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                stop:0 #f8f9fa, stop:1 #ecf0f1);
                    border: 1px solid #95a5a6;
                }
                QPushButton:pressed {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                stop:0 #d5dbdb, stop:1 #bdc3c7);
                }
            """)


class ModernProgressBar(QProgressBar):
    """Стилизованный прогресс-бар с современным дизайном"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QProgressBar {
                border: 2px solid #bdc3c7;
                border-radius: 8px;
                text-align: center;
                font-weight: bold;
                color: white;
                background-color: #ecf0f1;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                            stop:0 #3498db, stop:1 #2ecc71);
                border-radius: 6px;
            }
        """)
        self.setMinimumHeight(25)


def apply_global_styles():
    """Применение глобальных стилей"""
    checkmark = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'resources', 'checkmark.svg').replace('\\', '/')
    radio_dot = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'resources', 'radio_dot.svg').replace('\\', '/')
    spin_up = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'resources', 'spin_up.svg').replace('\\', '/')
    spin_down = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'resources', 'spin_down.svg').replace('\\', '/')
    return """
        QDialog {
            background-color: #f8f9fa;
        }
        QLineEdit {
            padding: 8px;
            border: 2px solid #bdc3c7;
            border-radius: 6px;
            background-color: white;
            selection-background-color: #3498db;
        }
        QLineEdit:focus {
            border-color: #3498db;
        }
        QTextEdit {
            border: 2px solid #bdc3c7;
            border-radius: 6px;
            background-color: white;
            padding: 8px;
        }
        QTextEdit:focus {
            border-color: #3498db;
        }
        QComboBox {
            padding: 6px 12px;
            border: 2px solid #bdc3c7;
            border-radius: 6px;
            background-color: white;
        }
        QComboBox:focus {
            border-color: #3498db;
        }
        QComboBox::drop-down {
            border: none;
            width: 20px;
        }
        QComboBox::down-arrow {
            image: none;
            border-left: 5px solid transparent;
            border-right: 5px solid transparent;
            border-top: 5px solid #7f8c8d;
        }
        QComboBox QAbstractItemView::item {
            color: #2c3e50;
            background-color: #ffffff;
        }
        QComboBox QAbstractItemView::item:hover,
        QComboBox QAbstractItemView::item:selected {
            color: #ffffff;
            background-color: #3498db;
        }
        QAbstractItemView::item:selected,
        QListView::item:selected {
            color: #ffffff;
            background-color: #3498db;
        }
        QAbstractItemView::item:hover,
        QListView::item:hover {
            color: #ffffff;
            background-color: #3498db;
        }
        QSpinBox, QDoubleSpinBox {
            padding: 6px;
            border: 2px solid #bdc3c7;
            border-radius: 6px;
            background-color: white;
        }
        QSpinBox::up-button, QDoubleSpinBox::up-button,
        QSpinBox::down-button, QDoubleSpinBox::down-button {
            subcontrol-origin: border;
            width: 22px;
            height: 16px;
            border-left: 1px solid #bdc3c7;
            background-color: #ecf0f1;
        }
        QSpinBox::up-button, QDoubleSpinBox::up-button {
            subcontrol-position: top right;
            border-bottom: 1px solid #bdc3c7;
        }
        QSpinBox::down-button, QDoubleSpinBox::down-button {
            subcontrol-position: bottom right;
        }
        QSpinBox::up-button:hover, QDoubleSpinBox::up-button:hover,
        QSpinBox::down-button:hover, QDoubleSpinBox::down-button:hover {
            background-color: #3498db;
        }
        QSpinBox::up-arrow, QDoubleSpinBox::up-arrow {
            image: url("__SPIN_UP__");
        }
        QSpinBox::down-arrow, QDoubleSpinBox::down-arrow {
            image: url("__SPIN_DOWN__");
        }
        QSpinBox:focus, QDoubleSpinBox:focus {
            border-color: #3498db;
        }
        QCheckBox {
            spacing: 8px;
        }
        QCheckBox::indicator {
            width: 18px;
            height: 18px;
            border: 2px solid #bdc3c7;
            border-radius: 4px;
            background-color: white;
        }
        QCheckBox::indicator:checked {
            background-color: #3498db;
            border-color: #3498db;
            image: url("__CHECKMARK__");
        }
        QRadioButton {
            spacing: 8px;
        }
        QRadioButton::indicator {
            width: 18px;
            height: 18px;
            border: 2px solid #bdc3c7;
            border-radius: 9px;
            background-color: white;
        }
        QRadioButton::indicator:checked {
            background-color: #3498db;
            border-color: #3498db;
            image: url("__RADIO_DOT__");
        }
        QScrollArea {
            border: none;
            background-color: transparent;
        }
        QScrollBar:vertical {
            background: #ecf0f1;
            width: 12px;
            border-radius: 6px;
        }
        QScrollBar::handle:vertical {
            background: #bdc3c7;
            border-radius: 6px;
            min-height: 20px;
        }
        QScrollBar::handle:vertical:hover {
            background: #95a5a6;
        }
    """.replace('__CHECKMARK__', checkmark).replace(
        '__RADIO_DOT__', radio_dot).replace('__SPIN_UP__', spin_up).replace(
            '__SPIN_DOWN__', spin_down)


def create_styled_button(text, button_class="primary", icon_text=""):
    """Создает стилизованную кнопку с иконкой"""
    button = ModernButton(f"{icon_text} {text}" if icon_text else text, button_class)
    return button


class ComboPopupDelegate(QStyledItemDelegate):
    """Paint combo rows explicitly, bypassing the native Qt6 delegate."""

    def paint(self, painter, option, index):
        painter.save()
        selected_flag = qt_class_enum(
            QStyle, 'StateFlag', 'State_Selected')
        hover_flag = qt_class_enum(QStyle, 'StateFlag', 'State_MouseOver')
        active = bool(option.state & (selected_flag | hover_flag))
        painter.fillRect(option.rect, QColor('#3498db' if active else '#ffffff'))

        rect = option.rect.adjusted(8, 0, -8, 0)
        icon = index.data(qt_enum('ItemDataRole', 'DecorationRole'))
        if hasattr(icon, 'isNull') and not icon.isNull():
            side = min(option.rect.height() - 6, 20)
            icon_rect = QRect(rect.left(), option.rect.top() + 3, side, side)
            icon.paint(painter, icon_rect,
                       qt_enum('AlignmentFlag', 'AlignCenter'))
            rect.setLeft(icon_rect.right() + 8)

        painter.setPen(QColor('#ffffff' if active else '#2c3e50'))
        painter.drawText(
            rect,
            qt_enum('AlignmentFlag', 'AlignLeft')
            | qt_enum('AlignmentFlag', 'AlignVCenter'),
            str(index.data(qt_enum('ItemDataRole', 'DisplayRole')) or ''))
        painter.restore()

    def sizeHint(self, option, index):
        size = super().sizeHint(option, index)
        return QSize(size.width(), max(size.height(), 28))


class StyledComboBox(QComboBox):
    """Combo whose popup colours survive the QGIS 4 Windows delegate."""

    _POPUP_STYLE = """
        QListView, QAbstractItemView {
            background-color: #ffffff;
            color: #2c3e50;
        }
        QListView::item, QAbstractItemView::item {
            background-color: #ffffff;
            color: #2c3e50;
        }
        QListView::item:hover, QListView::item:selected,
        QAbstractItemView::item:hover, QAbstractItemView::item:selected {
            background-color: #3498db;
            color: #ffffff;
        }
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._style_popup()

    def _style_popup(self):
        self.view().setStyleSheet(self._POPUP_STYLE)
        self.view().setItemDelegate(ComboPopupDelegate(self.view()))

    def showPopup(self):
        self._style_popup()
        super().showPopup()


ReadableComboDelegate = ComboPopupDelegate


def apply_combo_popup_style(combo):
    """Make Qt5/Qt6 combo popup rows readable on Windows delegates."""
    view = combo.view()
    view.setItemDelegate(ComboPopupDelegate(view))
    view.setStyleSheet("""
        QListView {
            background-color: #ffffff;
            color: #2c3e50;
            outline: none;
        }
        QListView::item {
            color: #2c3e50;
            background-color: #ffffff;
            padding: 4px 8px;
        }
        QListView::item:hover, QListView::item:selected {
            color: #ffffff;
            background-color: #3498db;
        }
    """)
    palette = view.palette()
    palette.setColor(
        qt_class_enum(QPalette, 'ColorRole', 'Base'), QColor('#ffffff'))
    palette.setColor(
        qt_class_enum(QPalette, 'ColorRole', 'Text'), QColor('#2c3e50'))
    palette.setColor(
        qt_class_enum(QPalette, 'ColorRole', 'Highlight'), QColor('#3498db'))
    palette.setColor(
        qt_class_enum(QPalette, 'ColorRole', 'HighlightedText'),
        QColor('#ffffff'))
    view.setPalette(palette)


def create_section_separator():
    """Создает разделитель секций"""
    separator = QFrame()
    separator.setFrameShape(qt_class_enum(QFrame, 'Shape', 'HLine'))
    separator.setFrameShadow(qt_class_enum(QFrame, 'Shadow', 'Sunken'))
    separator.setStyleSheet("""
        QFrame {
            color: #bdc3c7;
            background-color: #bdc3c7;
            height: 1px;
            margin: 10px 0;
        }
    """)

    return separator


def create_info_label(text, label_class="description"):
    """Создает информационную метку"""
    label = QLabel(text)
    label.setProperty("class", label_class)
    label.setWordWrap(True)

    return label
