# -*- coding: utf-8 -*-
"""
GUI Dialogs for Garmin Export Plugin
Диалоговые окна для плагина экспорта в Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

import webbrowser
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QPushButton, QTextEdit, QGroupBox, QSpacerItem, QSizePolicy
)
from qgis.PyQt.QtGui import QFont, QPixmap, QPalette

from .gui_components import create_styled_button, create_info_label


class DonationDialog(QDialog):
    """Диалоговое окно пожертвований"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса диалога пожертвований"""
        from ..translation_manager import translations
        
        self.setWindowTitle(translations.get_text('donation_window_title'))
        self.setFixedSize(450, 320)
        self.setModal(True)
        
        # Основной макет
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(25, 25, 25, 25)
        
        # Заголовок с иконкой
        header_layout = QHBoxLayout()
        
        icon_label = QLabel("☕")
        icon_label.setStyleSheet("font-size: 32px;")
        
        title_label = QLabel(translations.get_text('donation_title'))
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50;")
        
        header_layout.addWidget(icon_label)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        # Описание
        description_label = QLabel(translations.get_text('donation_description'))
        description_label.setWordWrap(True)
        description_label.setAlignment(Qt.AlignCenter)
        description_label.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                border: 2px solid #e9ecef;
                border-radius: 10px;
                padding: 15px;
                line-height: 1.6;
            }
        """)
        
        # Кнопки пожертвований
        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(10)
        
        # Ko-fi
        kofi_button = create_styled_button(translations.get_text('donation_kofi'), "success-button")
        kofi_button.clicked.connect(lambda: webbrowser.open("https://ko-fi.com/alexkobyakov"))
        
        # T-Bank
        tbank_button = create_styled_button(translations.get_text('donation_tbank'), "warning-button")
        tbank_button.clicked.connect(lambda: webbrowser.open("https://www.tbank.ru/cf/9q8KdAItNPy"))
        
        # GitHub Sponsors
        github_button = create_styled_button(translations.get_text('donation_github'))
        github_button.clicked.connect(lambda: webbrowser.open("https://github.com/sponsors/AlexKobyakov"))
        
        # Может быть позже
        later_button = create_styled_button(translations.get_text('donation_maybe_later'), "danger-button")
        later_button.clicked.connect(self.accept)
        
        buttons_layout.addWidget(kofi_button)
        buttons_layout.addWidget(tbank_button)
        buttons_layout.addWidget(github_button)
        buttons_layout.addWidget(later_button)
        
        # Сборка макета
        main_layout.addLayout(header_layout)
        main_layout.addWidget(description_label)
        main_layout.addLayout(buttons_layout)
        main_layout.addStretch()


class AuthorDialog(QDialog):
    """Диалоговое окно информации об авторе"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса диалога об авторе"""
        from ..translation_manager import translations
        
        self.setWindowTitle(translations.get_text('about_author'))
        self.setFixedSize(400, 350)
        self.setModal(True)
        
        # Основной макет
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(25, 25, 25, 25)
        
        # Заголовок с иконкой
        header_layout = QHBoxLayout()
        
        icon_label = QLabel("👤")
        icon_label.setStyleSheet("font-size: 32px;")
        
        title_label = QLabel(translations.get_text('about_author'))
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50;")
        
        header_layout.addWidget(icon_label)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        # Информация об авторе
        info_group = QGroupBox("ℹ️ Информация")
        info_layout = QGridLayout(info_group)
        info_layout.setSpacing(10)
        
        # Данные автора
        author_data = [
            (translations.get_text('author'), "Кобяков Александр Викторович (Alex Kobyakov)"),
            (translations.get_text('contact'), "kobyakov@lesburo.ru"),
            (translations.get_text('organization'), "Lesburo"),
            (translations.get_text('year'), "2025"),
            (translations.get_text('version'), "1.0.0")
        ]
        
        for i, (label, value) in enumerate(author_data):
            label_widget = QLabel(f"{label}:")
            label_widget.setStyleSheet("font-weight: bold; color: #2c3e50;")
            value_widget = QLabel(value)
            value_widget.setWordWrap(True)
            
            info_layout.addWidget(label_widget, i, 0)
            info_layout.addWidget(value_widget, i, 1)
        
        # Описание плагина
        description_group = QGroupBox("📋 Описание")
        description_layout = QVBoxLayout(description_group)
        
        description_text = QLabel(translations.get_text('plugin_description'))
        description_text.setWordWrap(True)
        description_text.setStyleSheet("color: #34495e; line-height: 1.4;")
        
        multilingual_text = QLabel(translations.get_text('multilingual_support'))
        multilingual_text.setWordWrap(True)
        multilingual_text.setStyleSheet("color: #7f8c8d; font-size: 10px;")
        
        description_layout.addWidget(description_text)
        description_layout.addWidget(multilingual_text)
        
        # Кнопка закрытия
        close_button = create_styled_button("Закрыть", "success-button", "✅")
        close_button.clicked.connect(self.accept)
        
        # Сборка макета
        main_layout.addLayout(header_layout)
        main_layout.addWidget(info_group)
        main_layout.addWidget(description_group)
        main_layout.addWidget(close_button)


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
        
        # Основной макет
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
        
        validate_button = create_styled_button("Проверить JSON", "warning-button", "✅")
        validate_button.clicked.connect(self.validate_json)
        
        reset_button = create_styled_button("По умолчанию", "danger-button", "🔄")
        reset_button.clicked.connect(self.reset_to_default)
        
        save_button = create_styled_button("Сохранить", "success-button", "💾")
        save_button.clicked.connect(self.accept)
        
        cancel_button = create_styled_button("Отмена", icon_text="❌")
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
        import json
        from qgis.PyQt.QtWidgets import QMessageBox
        
        try:
            json.loads(self.json_editor.toPlainText())
            QMessageBox.information(self, "Проверка JSON", "✅ JSON синтаксически корректен!")
        except json.JSONDecodeError as e:
            QMessageBox.warning(self, "Ошибка JSON", f"❌ Ошибка в JSON:\n{str(e)}")
    
    def reset_to_default(self):
        """Сбрасывает к настройкам по умолчанию"""
        default_mapping = """{
  "layers": {
    "roads": {
      "geometry": "LineString",
      "type": "0x06",
      "label_field": "name",
      "style": {
        "color": "#FF0000",
        "width": 2
      },
      "level": 1
    },
    "rivers": {
      "geometry": "LineString", 
      "type": "0x1F",
      "label_field": "name",
      "style": {
        "color": "#0000FF",
        "width": 1
      },
      "level": 2
    },
    "forests": {
      "geometry": "Polygon",
      "type": "0x16",
      "label_field": "name",
      "style": {
        "fill_color": "#00FF00"
      },
      "level": 3
    },
    "poi": {
      "geometry": "Point",
      "type": "0x2f00",
      "label_field": "name",
      "icon": "tree",
      "level": 1
    }
  }
}"""
        self.json_editor.setPlainText(default_mapping)
    
    def get_mapping_json(self):
        """Возвращает отредактированный JSON"""
        return self.json_editor.toPlainText()


class ProgressDialog(QDialog):
    """Диалоговое окно прогресса компиляции"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса диалога прогресса"""
        from ..translation_manager import translations
        
        self.setWindowTitle("🚀 Компиляция карты")
        self.setFixedSize(500, 300)
        self.setModal(True)
        
        # Убираем кнопку закрытия
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint)
        
        # Основной макет
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(25, 25, 25, 25)
        
        # Заголовок
        header_layout = QHBoxLayout()
        
        icon_label = QLabel("🚀")
        icon_label.setStyleSheet("font-size: 32px;")
        
        title_label = QLabel("Компиляция карты в процессе...")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #2c3e50;")
        
        header_layout.addWidget(icon_label)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        # Прогресс-бар
        from .gui_components import ModernProgressBar
        self.progress_bar = ModernProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        
        # Текущая операция
        self.operation_label = QLabel("Подготовка к экспорту...")
        self.operation_label.setStyleSheet("font-size: 12px; color: #7f8c8d;")
        self.operation_label.setAlignment(Qt.AlignCenter)
        
        # Лог операций
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMaximumHeight(120)
        self.log_text.setFont(QFont("Consolas", 9))
        self.log_text.setStyleSheet("""
            QTextEdit {
                background-color: #2c3e50;
                color: #ecf0f1;
                border: 2px solid #34495e;
                border-radius: 6px;
                padding: 8px;
            }
        """)
        
        # Кнопка отмены
        self.cancel_button = create_styled_button("Отменить компиляцию", "danger-button", "❌")
        
        # Сборка макета
        main_layout.addLayout(header_layout)
        main_layout.addWidget(self.progress_bar)
        main_layout.addWidget(self.operation_label)
        main_layout.addWidget(self.log_text)
        main_layout.addWidget(self.cancel_button)
    
    def update_progress(self, value, operation_text=""):
        """Обновляет прогресс"""
        self.progress_bar.setValue(value)
        if operation_text:
            self.operation_label.setText(operation_text)
    
    def add_log_message(self, message):
        """Добавляет сообщение в лог"""
        self.log_text.append(message)
        # Автопрокрутка к концу
        cursor = self.log_text.textCursor()
        cursor.movePosition(cursor.End)
        self.log_text.setTextCursor(cursor)
    
    def set_completed(self, success=True):
        """Устанавливает состояние завершения"""
        if success:
            self.progress_bar.setValue(100)
            self.operation_label.setText("✅ Компиляция завершена успешно!")
            self.cancel_button.setText("🎉 Закрыть")
            self.cancel_button.setProperty("class", "success-button")
        else:
            self.operation_label.setText("❌ Компиляция завершена с ошибками")
            self.cancel_button.setText("😞 Закрыть")
            self.cancel_button.setProperty("class", "danger-button")
        
        # Обновляем стили кнопки
        self.cancel_button.style().unpolish(self.cancel_button)
        self.cancel_button.style().polish(self.cancel_button)
        
        # Меняем обработчик на закрытие
        self.cancel_button.clicked.disconnect()
        self.cancel_button.clicked.connect(self.accept)


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
        self.setWindowTitle(self.title)
        self.setMinimumSize(450, 300)
        self.setModal(True)
        
        # Основной макет
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
        if self.details:
            details_group = QGroupBox("📋 Подробности")
            details_layout = QVBoxLayout(details_group)
            
            self.details_text = QTextEdit()
            self.details_text.setPlainText(self.details)
            self.details_text.setReadOnly(True)
            self.details_text.setMaximumHeight(150)
            self.details_text.setFont(QFont("Consolas", 9))
            
            details_layout.addWidget(self.details_text)
        
        # Кнопка закрытия
        close_button = create_styled_button("Закрыть", "danger-button", "❌")
        close_button.clicked.connect(self.accept)
        
        # Сборка макета
        main_layout.addLayout(header_layout)
        main_layout.addWidget(message_label)
        if self.details:
            main_layout.addWidget(details_group)
        main_layout.addWidget(close_button)
