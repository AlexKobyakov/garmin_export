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

Начиная с версии 1.1, **mkgmap не нужно скачивать вручную**. Откройте плагин,
перейдите на вкладку **«Инструменты»** и нажмите **«Скачать mkgmap»** — плагин
сам получит полный ZIP-дистрибутив с официального сайта или из резервных
источников GitHub, Dropbox и Яндекс.Диска, распакует его вместе с lib/ и
сохранит рабочую установку в профиле QGIS.

Если у вас уже есть `mkgmap.jar`, нажмите **«Добавить mkgmap»** и укажите файл.

### Ручное скачивание (по желанию)
1. Перейдите на https://www.mkgmap.org.uk/download/mkgmap.html
2. Скачайте последнюю версию `mkgmap-rXXXX.jar`
3. В плагине нажмите «Добавить mkgmap» и укажите путь к файлу

### splitter (необязательно)
Файл `splitter.jar` нужен только для нарезки очень больших карт на тайлы.
Его можно скачать кнопкой «Скачать splitter» или взять с
https://www.mkgmap.org.uk/download/splitter.html

## ✅ Проверка установки

### Тест 1: Активация плагина
1. В QGIS должна появиться кнопка 🎯 на панели инструментов
2. В меню "Векторы" должен быть пункт "🎯 Garmin IMG Export"

### Тест 2: Запуск плагина
1. Откройте любой проект с векторными слоями
2. Запустите плагин
3. Должно открыться окно с интерфейсом экспорта

### Тест 3: Проверка зависимостей
1. В плагине перейдите на вкладку "Инструменты"
2. Нажмите "Скачать mkgmap" (или "Добавить mkgmap" для локального файла)
3. Плагин должен подтвердить корректность пути (зелёная отметка ✅)
4. Нажмите "Найти автоматически" рядом с Java — путь заполнится, если Java установлена

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
│   ├── export_worker.py       # оркестрация экспорта (Qt worker)
│   ├── mp_generator.py        # Polish MP формат
│   ├── mkgmap_command.py      # построитель команды mkgmap (по документации)
│   ├── mkgmap_compiler.py     # запуск mkgmap, валидация jar, поиск Java
│   ├── typ_generator.py       # генерация TYP из символики QGIS
│   ├── layer_processor.py     # обработка геометрии слоёв
│   ├── layer_manager.py       # доступ к слоям проекта
│   ├── downloader.py          # логика скачивания mkgmap/splitter
│   ├── download_worker.py     # Qt worker скачивания
│   ├── settings_manager.py    # хранение настроек (QSettings)
│   └── style_mapper.py        # сопоставление QGIS -> Garmin типы
├── gui/
│   ├── __init__.py
│   ├── gui_main.py
│   ├── gui_components.py
│   ├── gui_widgets.py
│   ├── gui_mkgmap_widgets.py  # вкладки Инструменты/Тюнинг/TYP
│   ├── gui_dialogs.py
│   ├── gui_handlers.py
│   └── simple_donation.py     # диалог поддержки (как в референсном плагине)
├── translations/
│   ├── __init__.py
│   ├── ru.py
│   └── en.py
├── examples/
│   └── default_mapping.json
├── tests/                     # офлайн-тесты ядра (без QGIS)
│   └── run_tests.py
└── docs/
    ├── install.md
    └── user_guide.md
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


## G4/G5 reliability notes (release 1.2.1)

The Tools tab downloads complete mkgmap and splitter ZIP distributions, including
the required lib/ directory. Source order is language-aware:

- Russian UI: Yandex.Disk -> GitHub wheels -> Dropbox -> official site.
- Other UI languages: official site -> GitHub wheels -> Dropbox -> Yandex.Disk.

A download is staged and validated before promotion. A failed or cancelled attempt
does not replace a working installation. The UI distinguishes network, archive,
missing-dependency, permission and cancellation failures.

During export, Cancel is terminal: it cannot be followed by a false success
notification. A successful or failed run writes a redacted
.garmin_export/run_manifest.json; output path and size are recorded only after
success. The manifest is useful for support diagnostics and contains no raw
settings or secrets.


### Правило полного дистрибутива

Для mkgmap и splitter нужен полный ZIP-дистрибутив, а не одиночный JAR:
рядом с главным JAR должен находиться каталог lib/. Плагин проверяет это
условие до установки и оставляет прежнюю рабочую версию при ошибке.

## 🧰 Проверка Processing Toolbox

После активации проверьте **Обработка → Панель инструментов → Garmin Export**.
Если группа не видна, перезапустите QGIS и убедитесь, что
hasProcessingProvider=yes есть в metadata.txt. Должны быть семь алгоритмов,
включая Validate mapping JSON и Dependency diagnostics/download.

Validate environment с AUTO_DOWNLOAD выключенным проверяет Java и автоматически
ищет полный mkgmap/splitter в профиле QGIS. Загрузка запускается отдельно и
только после явного включения AUTO_DOWNLOAD. Export selected layers принимает
выбранные или все проектные векторные слои и возвращает IMG плюс MANIFEST.

QGIS Modeler и Batch могут выполнять независимые ветви параллельно; задавайте
разные output/map id и временные каталоги. В скриптах используйте
processing.run("garmin_export:<algorithm_id>", {...}); имена параметров
одинаковы во всех 12 языках.
