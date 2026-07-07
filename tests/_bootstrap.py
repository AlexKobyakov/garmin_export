# -*- coding: utf-8 -*-
"""
Общий bootstrap для офлайн-тестов.

Добавляет каталог, содержащий пакет garmin_export, в sys.path, чтобы тесты
можно было запускать без установленного QGIS. Тестируется только чистая
логика (генерация MP/TYP, построение команды, парсинг ссылок), которая не
импортирует qgis на уровне модуля.
"""

import os
import sys

# Каталог на два уровня выше: .../garmin_export/tests/_bootstrap.py -> .../
_PLUGIN_PARENT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..'))

if _PLUGIN_PARENT not in sys.path:
    sys.path.insert(0, _PLUGIN_PARENT)

PACKAGE = 'garmin_export'
