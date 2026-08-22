# -*- coding: utf-8 -*-
"""Support / donation dialog for Garmin Export.

The layout and live-retranslation contract are shared with GPS Road Builder.
"""

from qgis.PyQt.QtCore import QUrl
from qgis.PyQt.QtGui import QDesktopServices
from qgis.PyQt.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QFrame

from ..translation_manager import translations
from ..qgis_compat import qt_enum


class SimpleDonationDialog(QDialog):
    """Стильное окно поддержки из зрелой реализации reference-плагина."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(500, 400)
        self.resize(500, 400)
        self.setModal(True)
        self.setupUi()
        self.retranslateUi()

    def setupUi(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(20)

        self.title_label = QLabel()
        self.title_label.setStyleSheet("""
            QLabel {
                color: #2c3e50;
                font-size: 18px;
                font-weight: bold;
                text-align: center;
                padding: 10px;
            }
        """)
        self.title_label.setAlignment(qt_enum('AlignmentFlag', 'AlignCenter'))

        self.description_label = QLabel()
        self.description_label.setWordWrap(True)
        self.description_label.setTextFormat(qt_enum('TextFormat', 'RichText'))
        self.description_label.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 15px;
                color: #495057;
            }
        """)

        buttons_frame = QFrame()
        buttons_layout = QVBoxLayout(buttons_frame)
        buttons_layout.setSpacing(10)

        self.kofi_button = QPushButton()
        self.kofi_button.setStyleSheet(
            self._button_style('#f45d22', '#e55a1f', 'white'))
        self.kofi_button.clicked.connect(self.openKofi)

        self.tbank_button = QPushButton()
        self.tbank_button.setStyleSheet(
            self._button_style('#ffdd2d', '#f5d000', '#333'))
        self.tbank_button.clicked.connect(self.openTBank)

        self.github_button = QPushButton()
        self.github_button.setStyleSheet(
            self._button_style('#24292e', '#1b1f23', 'white'))
        self.github_button.clicked.connect(self.openGitHub)

        buttons_layout.addWidget(self.kofi_button)
        buttons_layout.addWidget(self.tbank_button)
        buttons_layout.addWidget(self.github_button)

        # Пользователь закрывает окно крестиком; отдельная кнопка «позже» не нужна.
        layout.addWidget(self.title_label)
        layout.addWidget(self.description_label)
        layout.addWidget(buttons_frame)
        layout.addStretch()
        self.setStyleSheet(
            "QDialog { background-color: white; border-radius: 10px; }")

    def retranslateUi(self):
        t = translations.get_text
        self.setWindowTitle(t('donation_title'))
        self.title_label.setText(t('donation_window_title'))
        self.description_label.setText(t('donation_description'))
        self.kofi_button.setText(t('donation_kofi'))
        self.tbank_button.setText(t('donation_tbank'))
        self.github_button.setText(t('donation_github'))

    @staticmethod
    def _button_style(bg, hover, fg):
        return """
            QPushButton {{
                background-color: {0};
                color: {2};
                border: none;
                border-radius: 8px;
                padding: 15px 20px;
                font-weight: bold;
                font-size: 14px;
                min-height: 20px;
            }}
            QPushButton:hover {{ background-color: {1}; }}
        """.format(bg, hover, fg)

    def openKofi(self):
        QDesktopServices.openUrl(QUrl("https://ko-fi.com/kobyakov"))
        self.accept()

    def openTBank(self):
        QDesktopServices.openUrl(
            QUrl("https://www.tinkoff.ru/rm/r_nCoENhHIfi.KBsuiKmOgJ/ggPSE72306"))
        self.accept()

    def openGitHub(self):
        QDesktopServices.openUrl(QUrl("https://github.com/sponsors/AlexKobyakov"))
        self.accept()


# Совместимость имён
DonationDialog = SimpleDonationDialog
__all__ = ['SimpleDonationDialog', 'DonationDialog']
