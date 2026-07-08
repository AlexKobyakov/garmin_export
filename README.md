# Garmin Export Plugin для QGIS

🎯 **Профессиональный плагин для экспорта векторных данных QGIS в формат Garmin IMG**

Версия: 1.1.1  
Автор: Кобяков Александр Викторович (Alex Kobyakov)  
Email: kobyakov@lesburo.ru  
Год: 2025-2026

🌐 **Языки интерфейса / UI languages:** 🇷🇺 Русский · 🇺🇸 English · 🇩🇪 Deutsch · 🇪🇸 Español · 🇫🇷 Français · 🇧🇷 Português · 🇨🇳 中文 · 🇮🇳 हिन्दी · 🇸🇦 العربية

🇬🇧 [English description](#-english) · 🇷🇺 [Русское описание](#-описание)

---

## 🇬🇧 English

**Garmin Export Plugin** is a professional QGIS tool for exporting vector layers
to the Garmin IMG map format using the mkgmap compiler. It covers the whole
workflow — from selecting layers in QGIS to producing a ready-to-use map for
Garmin GPS devices.

### Key features

- 🗺️ **Exports every geometry type**: points (POI), lines (roads, rivers),
  polygons (forests, water bodies), including multipart geometries.
- 📥 **Built-in mkgmap/splitter download**: the "Download mkgmap" / "Download
  splitter" buttons fetch the latest version from mkgmap.org.uk (variable link)
  or from a permanent Yandex.Disk backup. You can also "Add" a local jar. QGIS
  rules forbid bundling jars, so the file is fetched on demand.
- 🖌️ **Automatic TYP styling**: the plugin generates a TYP file from the QGIS
  layer symbology (polygon fills, line width/color, POI icons) so the map on the
  device looks like it does in QGIS.
- 🎨 **Flexible style mapping**: a JSON system for configuring Garmin object types.
- 📊 **Multi-level maps**: 4 detail levels (Level0–Level3).
- 🔧 **mkgmap fine-tuning**: Java heap (-Xmx), threads (--max-jobs),
  generalization, draw priority, code page, address index — all following the
  official mkgmap documentation.
- ☕ **Java auto-detection**: the plugin finds Java on the system (PATH,
  JAVA_HOME, common install directories).
- 🔄 **Batch processing**: export all project layers at once.
- 🌐 **Multilingual interface**: 9 languages (EN, RU, DE, ES, FR, PT, ZH, HI, AR),
  including right-to-left layout for Arabic.
- 📋 **mkgmap logging**: optional mkgmap.log file with a configurable verbosity.
- 💾 **Persistent settings** between sessions.

### Requirements

- QGIS 3.22 or newer, Python 3.9+
- Java Runtime Environment (JRE 8+) for mkgmap (the plugin can auto-detect it)

### Quick start

1. Open a QGIS project with vector layers and run the plugin from the
   **Vector** menu → "🎯 Garmin IMG Export".
2. On the **Tools** tab click **Download mkgmap** (or **Add mkgmap** for a local
   jar); Java is detected automatically.
3. Select the layers to export, set the output folder and map settings.
4. Optionally choose a TYP styling mode and tune mkgmap options.
5. Click **Compile Map** and get the ready `.img` file.

### Tests

Core logic (MP/TYP generation, mkgmap command building, download link parsing,
jar validation, style mapping) is covered by offline tests that run without QGIS:

```bash
python tests/run_tests.py
```

---

## 📋 Описание

Garmin Export Plugin - это современный инструмент для экспорта векторных слоёв QGIS в формат карт Garmin IMG через компилятор mkgmap. Плагин обеспечивает полноценный рабочий процесс от выбора слоёв до получения готовой карты для GPS-навигаторов Garmin.

## ✨ Основные возможности

- 🗺️ **Экспорт всех типов геометрии**: точки (POI), линии (дороги, реки), полигоны (леса, водоёмы), включая мультигеометрии
- 📥 **Встроенное скачивание mkgmap/splitter**: кнопки «Скачать mkgmap» и «Скачать splitter» получают актуальную версию с mkgmap.org.uk (переменная ссылка) или с Яндекс.Диска (постоянная ссылка). Также можно «Добавить» локальный jar. QGIS запрещает включать jar в состав плагина, поэтому файл загружается по требованию
- 🖌️ **Автоматическая стилизация TYP**: плагин генерирует TYP-файл из символики слоёв QGIS (цвета полигонов, толщина и цвет линий, иконки точек) — карта на навигаторе выглядит как в QGIS
- 🎨 **Гибкое сопоставление стилей**: JSON-система для настройки типов объектов Garmin
- 📊 **Многоуровневые карты**: поддержка 4 уровней детализации (Level0-Level3)
- 🔧 **Тонкая настройка mkgmap**: память Java (-Xmx), число потоков (--max-jobs), генерализация, приоритет отрисовки, кодовая страница, адресный индекс — всё по официальной документации mkgmap
- ☕ **Автопоиск Java**: плагин сам находит Java в системе (PATH, JAVA_HOME, типовые каталоги)
- 🔄 **Пакетная обработка**: экспорт всех слоёв проекта одновременно
- 🌐 **Многоязычный интерфейс**: 9 языков (RU, EN, DE, ES, FR, PT, ZH, HI, AR), включая письмо справа налево для арабского
- 📋 **Логирование mkgmap**: опциональный файл журнала mkgmap.log с настраиваемым уровнем детализации
- 💾 **Сохранение настроек** между сеансами работы

## 🔧 Требования

### Обязательные:
- QGIS версии 3.22 или выше
- Python 3.9+
- Java Runtime Environment (JRE) для работы mkgmap

### Рекомендуемые:
- mkgmap r4900+ (последняя версия)
- Оперативная память: минимум 4 ГБ для больших проектов

## 📦 Установка

1. **Скачайте файлы плагина** в папку `C:\\AlexKo\\garmin_export`
2. **Скопируйте папку** в директорию плагинов QGIS:
   - Windows: `%APPDATA%\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\`
   - Linux: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
   - macOS: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`

3. **Активируйте плагин** в QGIS:
   - Зайдите в меню "Модули" → "Управление модулями"
   - Найдите "Garmin Export" и поставьте галочку

## 🚀 Быстрый старт

### Шаг 1: Подготовка данных
1. Откройте проект QGIS с векторными слоями
2. Убедитесь, что слои имеют корректную геометрию
3. Проверьте наличие полей с названиями объектов

### Шаг 2: Запуск плагина
1. В меню "Векторы" выберите "🎯 Garmin IMG Export"
2. Или нажмите кнопку на панели инструментов

### Шаг 3: Настройка экспорта
1. **Выбор слоёв**: отметьте нужные слои для экспорта
2. **Настройки карты**: укажите Family ID, название карты
3. **Путь к mkgmap**: выберите файл mkgmap.jar
4. **Выходная папка**: укажите, куда сохранить результат

### Шаг 4: Сопоставление стилей
1. Настройте JSON-сопоставление типов объектов
2. Или используйте настройки по умолчанию
3. При необходимости отредактируйте через встроенный редактор

### Шаг 5: Компиляция
1. Нажмите "🚀 Скомпилировать карту"
2. Дождитесь завершения процесса
3. Получите готовый файл .img

## 📝 Структура JSON-сопоставления

```json
{
  "layers": {
    "roads": {
      "geometry": "LineString",
      "type": "0x06",
      "label_field": "name",
      "level": 1,
      "style": {
        "color": "#FF0000",
        "width": 2
      }
    }
  }
}
```

### Поля сопоставления:
- **geometry**: тип геометрии (Point, LineString, Polygon)
- **type**: код типа объекта Garmin (например, 0x06 для дорог)
- **label_field**: поле атрибутов для подписей
- **level**: уровень отображения (0-3)
- **style**: дополнительные параметры стиля

## 🗺️ Типы объектов Garmin

### Дороги (LineString):
- `0x01` - Автомагистраль
- `0x06` - Основная дорога  
- `0x07` - Второстепенная дорога
- `0x14` - Железная дорога

### Водные объекты:
- `0x1F` - Река/ручей (LineString)
- `0x3C` - Озеро/пруд (Polygon)

### Точки интереса (Point):
- `0x0100` - Крупный город
- `0x2A00` - Больница
- `0x2B00` - Заправка
- `0x2F00` - Общая POI

### Области (Polygon):
- `0x13` - Здание
- `0x16` - Лес
- `0x1A` - Парк

## 📊 Уровни детализации

- **Level 0** - Самый детальный уровень (крупный масштаб)
- **Level 1** - Основной уровень отображения
- **Level 2** - Средний уровень детализации
- **Level 3** - Обзорный уровень (мелкий масштаб)

## 🔧 Настройка mkgmap

### Получение mkgmap (вкладка «Инструменты»):
Правила репозитория плагинов QGIS запрещают включать сторонние jar-библиотеки
в состав плагина, поэтому mkgmap загружается по требованию:

- **Скачать mkgmap** — плагин определяет последнюю версию на
  https://www.mkgmap.org.uk/download/mkgmap.html (переменная ссылка вида
  `mkgmap-rXXXX.jar`) и скачивает её; при недоступности сайта используется
  резервная копия на Яндекс.Диске. Файл сохраняется в профиле QGIS и
  проверяется на корректность.
- **Добавить mkgmap** — выбрать уже скачанный `mkgmap.jar` на диске.
- Аналогично для **splitter** (нужен только для нарезки очень больших карт).
- **Java** определяется автоматически кнопкой «Найти автоматически» или
  указывается вручную.

### Параметры компиляции:
Команда формируется строго по документации mkgmap (Java-опции до `-jar`,
опции mkgmap до входных файлов). Базовый набор:
- `--gmapsupp` — создание `gmapsupp.img` для загрузки в устройство;
- `--family-id`, `--product-id`, `--family-name`, `--description` — идентификация карты;
- `--code-page` / `--unicode` — кодировка подписей;
- `--keep-going` — не прерывать сборку из-за ошибки в одном тайле.

Дополнительно на вкладке «Тюнинг» доступны: `--index` (адресный поиск),
`--route` (маршрутизация), `--transparent`, `--draw-priority`,
`--add-pois-to-areas`, `--reduce-point-density[-polygon]`,
`--min-size-polygon`, `--order-by-decreasing-area`, `--max-jobs`, `-Xmx`,
а также поле произвольных аргументов и включение журнала `mkgmap.log`.

## 🐛 Решение проблем

### Ошибка "Java не найдена":
1. Установите Java Runtime Environment (JRE)
2. Убедитесь, что Java доступна в PATH
3. Перезапустите QGIS

### Ошибка "mkgmap.jar не найден":
1. Скачайте mkgmap с официального сайта
2. Укажите правильный путь к файлу mkgmap.jar
3. Убедитесь в корректности версии mkgmap

### Пустой результат экспорта:
1. Проверьте корректность геометрии слоёв
2. Убедитесь в наличии данных в выбранных слоях
3. Проверьте JSON-сопоставление

### Ошибки сопоставления:
1. Проверьте синтаксис JSON
2. Убедитесь в корректности типов Garmin
3. Используйте кнопку "Проверить JSON"

## 📚 Дополнительные ресурсы

- **Документация mkgmap**: https://www.mkgmap.org.uk/doc/
- **Типы объектов Garmin**: https://wiki.openstreetmap.org/wiki/Mkgmap/help/style_manual
- **Форум поддержки**: создайте issue в репозитории проекта

## 🤝 Поддержка проекта

Плагин разрабатывается бесплатно! Вы можете поддержать разработку:

- ☕ [Купить кофе на Ko-fi](https://ko-fi.com/alexkobyakov)
- 💳 [Пожертвовать через Т-Банк](https://www.tbank.ru/cf/9q8KdAItNPy)
- 💖 [Спонсировать на GitHub](https://github.com/sponsors/AlexKobyakov)

## 📄 Лицензия

GNU General Public License v3.0

Плагин распространяется бесплатно под лицензией GPL v3. Вы можете свободно использовать, модифицировать и распространять код согласно условиям лицензии.

## 👨‍💻 Об авторе

**Кобяков Александр Викторович (Alex Kobyakov)**
- Email: kobyakov@lesburo.ru
- Организация: Lesburo
- Специализация: ГИС-разработка, Python, QGIS

---

© 2025 Alex Kobyakov. Все права защищены.

## 🧪 Тесты

Логика ядра (генерация MP/TYP, построение команды mkgmap, разбор ссылок
скачивания, валидация jar, сопоставление стилей) покрыта офлайн-тестами,
которые запускаются без QGIS:

```bash
python tests/run_tests.py
```
