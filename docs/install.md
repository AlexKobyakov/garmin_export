# Инструкция по установке Garmin Export Plugin

## 🚀 Автоматическая установка

### Шаг 1: Копирование файлов
1. Скопируйте всю папку `garmin_export` в директорию плагинов QGIS
2. Пути к папкам плагинов по операционным системам:

**Windows:**
```
%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\
```
Полный путь обычно выглядит как:
```
C:\Users\[ИМЯ_ПОЛЬЗОВАТЕЛЯ]\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\
```

**Linux:**
```
~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
```

**macOS:**
```
~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/
```

### Шаг 2: Активация в QGIS
1. Откройте QGIS
2. Зайдите в меню **"Модули"** → **"Управление модулями"**
3. В списке найдите **"Garmin Export"**
4. Поставьте галочку для активации плагина
5. Плагин появится в меню **"Векторы"** и на панели инструментов

## 🔧 Настройка зависимостей

### Java Runtime Environment
Плагин требует установленной Java для работы с mkgmap:

**Windows:**
1. Скачайте JRE с https://www.oracle.com/java/technologies/downloads/
2. Установите, следуя инструкциям
3. Убедитесь, что Java доступна в системном PATH

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install default-jre
```

**Linux (CentOS/RHEL):**
```bash
sudo yum install java-11-openjdk
```

**macOS:**
```bash
# Используя Homebrew
brew install openjdk
```

### Проверка установки Java
Откройте командную строку/терминал и выполните:
```bash
java -version
```

Должна появиться информация о версии Java.

## 📦 Установка mkgmap

### Скачивание mkgmap
1. Перейдите на https://www.mkgmap.org.uk/
2. В разделе "Download" скачайте последнюю версию
3. Распакуйте архив в удобную папку (например, `C:\Tools\mkgmap\`)

### Альтернативные источники
- GitHub releases: https://github.com/openstreetmap/mkgmap/releases
- Mirror sites: проверьте актуальные ссылки на официальном сайте

## ✅ Проверка установки

### Тест 1: Активация плагина
1. В QGIS должна появиться кнопка 🎯 на панели инструментов
2. В меню "Векторы" должен быть пункт "🎯 Garmin IMG Export"

### Тест 2: Запуск плагина
1. Откройте любой проект с векторными слоями
2. Запустите плагин
3. Должно открыться окно с интерфейсом экспорта

### Тест 3: Проверка зависимостей
1. В плагине перейдите на вкладку "Настройки экспорта"
2. Укажите путь к mkgmap.jar
3. Плагин должен подтвердить корректность пути

## 🐛 Решение проблем установки

### Плагин не появляется в списке
1. Убедитесь, что папка `garmin_export` находится в правильной директории
2. Проверьте, что все файлы скопированы полностью
3. Перезапустите QGIS
4. Проверьте логи QGIS на наличие ошибок

### Ошибки при активации
1. Откройте **Консоль Python** в QGIS (F12)
2. Выполните команду:
```python
import sys
print(sys.path)
```
3. Убедитесь, что путь к плагинам присутствует в списке

### Плагин активируется, но не работает
1. Проверьте установку Java
2. Убедитесь в наличии векторных слоёв в проекте
3. Проверьте права доступа к папкам плагина
4. Посмотрите логи в папке плагина

## 📂 Структура файлов плагина

После установки должна быть следующая структура:
```
plugins/garmin_export/
├── __init__.py
├── garmin_exporter.py
├── metadata.txt
├── translation_manager.py
├── icon.png
├── LICENSE
├── README.md
├── core/
│   ├── __init__.py
│   ├── export_worker.py
│   ├── mp_generator.py
│   ├── mkgmap_compiler.py
│   ├── layer_processor.py
│   └── style_mapper.py
├── gui/
│   ├── __init__.py
│   ├── gui_main.py
│   ├── gui_components.py
│   ├── gui_widgets.py
│   ├── gui_dialogs.py
│   └── gui_handlers.py
├── translations/
│   ├── __init__.py
│   ├── ru.py
│   └── en.py
├── examples/
│   └── default_mapping.json
└── docs/
    └── install.md
```

## 🔄 Обновление плагина

### Ручное обновление
1. Деактивируйте старую версию плагина в QGIS
2. Замените папку `garmin_export` новой версией
3. Перезапустите QGIS
4. Активируйте плагин заново

### Сохранение настроек
Пользовательские JSON-сопоставления сохраняются автоматически и не удаляются при обновлении.

## 📞 Поддержка

При возникновении проблем с установкой:

1. **Проверьте требования**: QGIS 3.22+, Python 3.9+, Java
2. **Изучите логи**: консоль Python в QGIS, логи плагина
3. **Свяжитесь с автором**: kobyakov@lesburo.ru

---

🎯 **Успешной установки и работы с плагином!**
