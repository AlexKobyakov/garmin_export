# -*- coding: utf-8 -*-
"""
Download Worker for Garmin Export Plugin
Qt-обёртка для фонового скачивания mkgmap/splitter

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

import os

from qgis.PyQt.QtCore import QObject, pyqtSignal

from . import downloader


def get_tools_directory():
    """Каталог для скачанных инструментов внутри профиля QGIS"""
    try:
        from qgis.core import QgsApplication
        base = QgsApplication.qgisSettingsDirPath()
    except Exception:
        base = os.path.expanduser('~')
    tools_dir = os.path.join(base, 'garmin_export', 'tools')
    os.makedirs(tools_dir, exist_ok=True)
    return tools_dir


class DownloadWorker(QObject):
    """Worker для скачивания инструмента в отдельном потоке"""

    # получено_байт, всего_байт
    progress = pyqtSignal(int, int)
    # текст статуса
    status = pyqtSignal(str)
    # успех, путь_к_файлу_или_сообщение_об_ошибке
    finished = pyqtSignal(bool, str)

    def __init__(self, tool, dest_dir=None):
        super().__init__()
        self.tool = tool
        self.dest_dir = dest_dir or get_tools_directory()
        self.is_cancelled = False

    def run(self):
        """Выполнение скачивания (вызывается в рабочем потоке)"""
        try:
            path = downloader.download_tool(
                self.tool,
                self.dest_dir,
                progress_callback=self._on_progress,
                cancelled_callback=lambda: self.is_cancelled,
            )
            self.finished.emit(True, path)
        except Exception as e:
            self.finished.emit(False, str(e))

    def _on_progress(self, received, total, status_text):
        if status_text:
            self.status.emit(status_text)
        self.progress.emit(received, total)

    def cancel(self):
        """Запрос отмены скачивания"""
        self.is_cancelled = True
