# -*- coding: utf-8 -*-
"""
Translation Manager for Garmin Export Plugin
Менеджер переводов для плагина экспорта в Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""

import importlib

# Языки с письмом справа налево (для setLayoutDirection)
RTL_LANGUAGES = {'ar'}

# Отображаемые названия языков (флаг + эндоним) в порядке для UI
LANGUAGE_LABELS = [
    ('ru', '🇷🇺 Русский'),
    ('en', '🇺🇸 English'),
    ('zh', '🇨🇳 中文'),
    ('hi', '🇮🇳 हिन्दी'),
    ('es', '🇪🇸 Español'),
    ('ar', '🇸🇦 العربية'),
    ('fr', '🇫🇷 Français'),
    ('pt', '🇧🇷 Português'),
    ('de', '🇩🇪 Deutsch'),
    ('id', '🇮🇩 Bahasa Indonesia'),
    ('th', '🇹🇭 ไทย'),
    ('vi', '🇻🇳 Tiếng Việt'),
]


class TranslationManager:
    """Менеджер переводов с поддержкой модульной архитектуры"""

    def __init__(self):
        self.current_language = 'ru'
        self.fallback_language = 'en'
        self.loaded_languages = {}

        # Список поддерживаемых языков (соответствует файлам в translations/)
        self.supported_languages = [code for code, _ in LANGUAGE_LABELS]

        # Загружаем язык по умолчанию
        self._load_language(self.current_language)
        if self.current_language != self.fallback_language:
            self._load_language(self.fallback_language)

    def _load_language(self, language_code):
        """Загружает переводы для указанного языка (динамический импорт)"""
        if language_code in self.loaded_languages:
            return True

        if language_code not in self.supported_languages:
            return False

        try:
            package = __package__ or __name__.rpartition('.')[0]
            module = importlib.import_module(
                '.translations.{0}'.format(language_code), package)

            if hasattr(module, 'translations'):
                self.loaded_languages[language_code] = module.translations
                return True
            else:
                print("Warning: Module {0} has no 'translations' dictionary"
                      .format(language_code))
                return False

        except ImportError as e:
            print("Warning: Could not load translations for {0}: {1}"
                  .format(language_code, e))
            return False
        except Exception as e:
            print("Error loading translations for {0}: {1}"
                  .format(language_code, e))
            return False

    def get_language_labels(self):
        """Список (код, отображаемое_название) для заполнения UI"""
        return list(LANGUAGE_LABELS)

    def is_rtl(self, language_code=None):
        """Является ли язык письмом справа налево"""
        return (language_code or self.current_language) in RTL_LANGUAGES
    
    def set_language(self, language_code):
        """Устанавливает текущий язык"""
        if language_code in self.supported_languages:
            if self._load_language(language_code):
                self.current_language = language_code
                return True
        return False
    
    def get_text(self, key, language=None):
        """Получает переведенный текст по ключу с fallback механизмом"""
        # Определяем язык для поиска
        lang = language or self.current_language
        
        # Пытаемся найти в текущем языке
        if lang in self.loaded_languages:
            translations = self.loaded_languages[lang]
            if key in translations:
                return translations[key]
        
        # Пытаемся найти в резервном языке
        if self.fallback_language in self.loaded_languages and lang != self.fallback_language:
            translations = self.loaded_languages[self.fallback_language]
            if key in translations:
                return translations[key]
        
        # Возвращаем ключ, если перевод не найден
        return key
    
    def get_current_language(self):
        """Возвращает код текущего языка"""
        return self.current_language
    
    def get_supported_languages(self):
        """Возвращает список поддерживаемых языков"""
        return self.supported_languages.copy()
    
    def is_language_loaded(self, language_code):
        """Проверяет, загружен ли язык"""
        return language_code in self.loaded_languages
    
    def reload_language(self, language_code):
        """Перезагружает переводы для языка"""
        if language_code in self.loaded_languages:
            del self.loaded_languages[language_code]
        return self._load_language(language_code)


# Глобальный объект переводов
translations = TranslationManager()
