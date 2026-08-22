# -*- coding: utf-8 -*-
"""
GUI Dialogs for Garmin Export Plugin
Диалоговые окна для плагина экспорта в Garmin

Диалоги "Об авторе" и "Поддержка" идентичны референсному плагину
MIF/TAB to SHP/GeoJSON Converter.

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""

import json

from qgis.PyQt.QtWidgets import (
    QMessageBox, QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QTextEdit, QGroupBox
)
from qgis.PyQt.QtGui import QFont

from .gui_components import create_styled_button, create_info_label
from ..translation_manager import translations
from ..qgis_compat import qt_enum


class AuthorInfoDialog(QDialog):
    """Стильное окно «Об авторе» из зрелой реализации reference-плагина."""

    def __init__(self, parent=None):
        super().__init__(parent)
        try:
            from ..garmin_exporter import GarminExporter
            self._info = GarminExporter.get_plugin_info()
        except Exception:
            self._info = {
                'name': 'Garmin Export',
                'version': 'Unknown',
                'author': 'Кобяков Александр Викторович',
                'email': 'kobyakov@lesburo.ru',
            }
        self.setMinimumSize(560, 640)
        self.resize(560, 640)
        self.setModal(True)
        self.setWindowFlags(
            qt_enum('WindowType', 'Dialog')
            | qt_enum('WindowType', 'WindowTitleHint')
            | qt_enum('WindowType', 'WindowCloseButtonHint'))
        self.setupUi()
        self.retranslateUi()

    def setupUi(self):
        t = translations.get_text
        layout = QVBoxLayout(self)
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(14)

        self.title_label = QLabel()
        self.title_label.setAlignment(qt_enum('AlignmentFlag', 'AlignCenter'))
        self.title_label.setStyleSheet(
            'color: #2c3e50; font-size: 20px; font-weight: bold;')

        self.subtitle_label = QLabel()
        self.subtitle_label.setAlignment(qt_enum('AlignmentFlag', 'AlignCenter'))
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setStyleSheet('color: #7f8c8d; font-size: 12px;')

        self.version_label = QLabel()
        self.version_label.setAlignment(qt_enum('AlignmentFlag', 'AlignCenter'))
        self.version_label.setStyleSheet('color: #95a5a6; font-size: 11px;')

        self.about_label = QLabel()
        self.about_label.setWordWrap(True)
        self.about_label.setTextFormat(qt_enum('TextFormat', 'RichText'))
        self.about_label.setStyleSheet(self._card('#eaf4fb', '#bfe0f5'))

        self.contact_label = QLabel()
        self.contact_label.setWordWrap(True)
        self.contact_label.setTextFormat(qt_enum('TextFormat', 'RichText'))
        self.contact_label.setOpenExternalLinks(True)
        self.contact_label.setStyleSheet(self._card('#f8f9fa', '#dee2e6'))

        self.close_button = create_styled_button(t('close'), 'secondary', '✖️')
        self.close_button.clicked.connect(self.accept)

        layout.addWidget(self.title_label)
        layout.addWidget(self.subtitle_label)
        layout.addWidget(self.version_label)
        layout.addWidget(self.about_label)
        layout.addWidget(self.contact_label)
        layout.addStretch()
        layout.addWidget(
            self.close_button, 0, qt_enum('AlignmentFlag', 'AlignCenter'))
        self.setStyleSheet(
            'QDialog { background-color: white; border-radius: 10px; }')

    def retranslateUi(self):
        t = translations.get_text
        info = self._info
        self.setWindowTitle('👤 ' + t('header_about_author'))
        self.title_label.setText('🗺️ ' + info['name'])
        self.subtitle_label.setText(t('plugin_description'))
        self.version_label.setText(
            '📜 {0}: v{1}'.format(t('version'), info['version']))
        self.about_label.setText(
            '<b style="color:#2980b9;">🧭 Garmin IMG / mkgmap</b><br>{0}'.format(
                t('multilingual_support')))
        self.contact_label.setText(
            '<b>👨‍💻 {author_l}:</b> {author} <i>(Alex Kobyakov)</i><br>'
            '<b>📧 {contact_l}:</b> <a href="mailto:{email}">{email}</a><br>'
            '<b>💬 Telegram:</b> <a href="https://t.me/AKobyakov">@AKobyakov</a><br>'
            '<b>🏢 {org_l}:</b> Lesburo &nbsp;·&nbsp; <b>📅 {year_l}:</b> 2025–2026<br>'
            '<span style="color:#7f8c8d;">{multi}</span>'.format(
                author_l=t('author'), author=info['author'],
                contact_l=t('contact'), email=info['email'],
                org_l=t('organization'), year_l=t('year'),
                multi=t('multilingual_support')))
        self.close_button.setText('✖️ ' + t('close'))

    @staticmethod
    def _card(bg, border):
        return ('QLabel {{ background-color: {0}; border: 1px solid {1}; '
                'border-radius: 8px; padding: 15px; color: #2c3e50; }}'
                .format(bg, border))


# Совместимость со старым именем
AuthorDialog = AuthorInfoDialog


class MappingEditorDialog(QDialog):
    """Диалоговое окно редактора JSON-сопоставления"""

    def __init__(self, mapping_json="", parent=None):
        super().__init__(parent)
        self.mapping_json = mapping_json
        self.setupUi()

    def setupUi(self):
        """Настройка интерфейса редактора сопоставления"""
        from ..translation_manager import translations

        self.setWindowTitle(translations.get_text('mapping_title'))
        self.setMinimumSize(600, 500)
        self.setModal(True)

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Заголовок
        header_layout = QHBoxLayout()

        icon_label = QLabel("🎨")
        icon_label.setStyleSheet("font-size: 24px;")

        title_label = QLabel(translations.get_text('mapping_title'))
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #2c3e50;")

        header_layout.addWidget(icon_label)
        header_layout.addWidget(title_label)
        header_layout.addStretch()

        # Описание
        description_label = create_info_label(translations.get_text('mapping_description'))

        # Редактор JSON
        self.json_editor = QTextEdit()
        self.json_editor.setFont(QFont("Consolas", 10))
        self.json_editor.setPlainText(self.mapping_json)
        self.json_editor.setMinimumHeight(300)
        self.json_editor.setStyleSheet("""
            QTextEdit {
                background-color: #2c3e50;
                color: #ecf0f1;
                border: 2px solid #34495e;
                border-radius: 6px;
                padding: 10px;
                font-family: 'Consolas', 'Monaco', monospace;
            }
        """)

        # Кнопки управления
        buttons_layout = QHBoxLayout()

        validate_button = create_styled_button(
            translations.get_text('validate_json'), "warning-button", "✅")
        validate_button.clicked.connect(self.validate_json)

        reset_button = create_styled_button(
            translations.get_text('default_mapping'), "danger-button", "🔄")
        reset_button.clicked.connect(self.reset_to_default)

        save_button = create_styled_button(
            translations.get_text('save'), "success-button", "💾")
        save_button.clicked.connect(self.accept)

        cancel_button = create_styled_button(
            translations.get_text('cancel'), icon_text="❌")
        cancel_button.clicked.connect(self.reject)

        buttons_layout.addWidget(validate_button)
        buttons_layout.addWidget(reset_button)
        buttons_layout.addStretch()
        buttons_layout.addWidget(save_button)
        buttons_layout.addWidget(cancel_button)

        # Сборка макета
        main_layout.addLayout(header_layout)
        main_layout.addWidget(description_label)
        main_layout.addWidget(self.json_editor)
        main_layout.addLayout(buttons_layout)

    def validate_json(self):
        """Проверяет корректность JSON"""
        from ..translation_manager import translations

        try:
            json.loads(self.json_editor.toPlainText())
            QMessageBox.information(
                self, translations.get_text('validate_json'),
                '✅ ' + translations.get_text('json_valid'))
        except json.JSONDecodeError as e:
            QMessageBox.warning(
                self, translations.get_text('error'),
                '❌ {0}:\n{1}'.format(
                    translations.get_text('error_invalid_json'), str(e)))

    def reset_to_default(self):
        """Сбрасывает к настройкам по умолчанию"""
        from .gui_widgets import get_default_mapping_json
        self.json_editor.setPlainText(get_default_mapping_json())

    def get_mapping_json(self):
        """Возвращает отредактированный JSON"""
        return self.json_editor.toPlainText()


class DownloadProgressDialog(QDialog):
    """Диалог прогресса скачивания mkgmap/splitter"""

    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.is_cancelled = False
        self.setWindowTitle(title)
        self.setFixedSize(480, 190)
        self.setModal(True)
        self.setWindowFlags(
            qt_enum('WindowType', 'Dialog') |
            qt_enum('WindowType', 'WindowTitleHint'))
        self.setupUi(title)

    def setupUi(self, title):
        """Настройка интерфейса"""
        from ..translation_manager import translations
        from .gui_components import ModernProgressBar

        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        header_layout = QHBoxLayout()
        icon_label = QLabel("📥")
        icon_label.setStyleSheet("font-size: 28px;")
        title_label = QLabel(title)
        title_label.setStyleSheet(
            "font-size: 14px; font-weight: bold; color: #2c3e50;")
        header_layout.addWidget(icon_label)
        header_layout.addWidget(title_label)
        header_layout.addStretch()

        self.status_label = QLabel(translations.get_text('downloading'))
        self.status_label.setStyleSheet("font-size: 11px; color: #7f8c8d;")

        self.progress_bar = ModernProgressBar()
        self.progress_bar.setRange(0, 0)  # неопределённый до первого прогресса

        self.cancel_button = create_styled_button(
            translations.get_text('cancel'), "danger-button", "❌")
        self.cancel_button.clicked.connect(self.on_cancel)

        layout.addLayout(header_layout)
        layout.addWidget(self.status_label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(
            self.cancel_button, 0, qt_enum('AlignmentFlag', 'AlignCenter'))

    def on_cancel(self):
        """Отмена скачивания"""
        self.is_cancelled = True
        self.cancel_button.setEnabled(False)

    def update_progress(self, received, total):
        """Обновление прогресса (байты)"""
        if total > 0:
            self.progress_bar.setRange(0, 100)
            self.progress_bar.setValue(int(received * 100 / total))
            self.status_label.setText('{0:.1f} / {1:.1f} MB'.format(
                received / 1048576.0, total / 1048576.0))
        else:
            self.status_label.setText('{0:.1f} MB'.format(received / 1048576.0))

    def set_status(self, text):
        """Установка строки статуса"""
        self.status_label.setText(text)


class ErrorDialog(QDialog):
    """Диалоговое окно отображения ошибок"""

    def __init__(self, title, message, details="", parent=None):
        super().__init__(parent)
        self.title = title
        self.message = message
        self.details = details
        self.setupUi()

    def setupUi(self):
        """Настройка интерфейса диалога ошибок"""
        from ..translation_manager import translations

        self.setWindowTitle(self.title)
        self.setMinimumSize(450, 300)
        self.setModal(True)

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Заголовок с иконкой
        header_layout = QHBoxLayout()

        icon_label = QLabel("❌")
        icon_label.setStyleSheet("font-size: 32px;")

        title_label = QLabel(self.title)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #e74c3c;")

        header_layout.addWidget(icon_label)
        header_layout.addWidget(title_label)
        header_layout.addStretch()

        # Сообщение об ошибке
        message_label = QLabel(self.message)
        message_label.setWordWrap(True)
        message_label.setStyleSheet("""
            QLabel {
                background-color: #fdeded;
                border: 2px solid #f5c6cb;
                border-radius: 8px;
                padding: 15px;
                color: #721c24;
            }
        """)

        # Детали ошибки (если есть)
        details_group = None
        if self.details:
            details_group = QGroupBox('📋 ' + translations.get_text('details'))
            details_layout = QVBoxLayout(details_group)

            self.details_text = QTextEdit()
            self.details_text.setPlainText(self.details)
            self.details_text.setReadOnly(True)
            self.details_text.setMaximumHeight(150)
            self.details_text.setFont(QFont("Consolas", 9))

            details_layout.addWidget(self.details_text)

        # Кнопка закрытия
        close_button = create_styled_button(
            translations.get_text('close'), "danger-button", "❌")
        close_button.clicked.connect(self.accept)

        # Сборка макета
        main_layout.addLayout(header_layout)
        main_layout.addWidget(message_label)
        if details_group is not None:
            main_layout.addWidget(details_group)
        main_layout.addWidget(close_button)
