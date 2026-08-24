# -*- coding: utf-8 -*-
"""Downloader error contracts shared by the Qt worker and pure downloader."""

ERROR_NETWORK = 'network'
ERROR_ARCHIVE = 'archive'
ERROR_DEPENDENCIES = 'dependencies'
ERROR_PERMISSION = 'permission'
ERROR_CANCELLED = 'cancelled'


class DownloadError(Exception):
    """Ошибка загрузки с устойчивым кодом для UI и логов."""

    def __init__(self, tool, code, failures):
        self.tool = tool
        self.code = code
        self.failures = tuple(failures)
        details = '\n'.join('- {0}: {1}'.format(item[0], item[1])
                            for item in self.failures)
        super().__init__(
            'Не удалось скачать {0} [{1}] из доступных источников:\n{2}'.format(
                tool, code, details))


class ArchiveValidationError(ValueError):
    """Скачанный файл не является ожидаемым архивом."""


class DependencyValidationError(ValueError):
    """Архив не содержит обязательного дерева зависимостей."""
