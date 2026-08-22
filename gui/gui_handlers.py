# -*- coding: utf-8 -*-
"""Backward-compatible event-handler facade.

Behavior is split by responsibility while ``GuiEventHandlers`` keeps the
public constructor and method surface used by the main dialog.
"""

from ..core.settings_manager import SettingsManager
from .handler_ui import UiHandlers
from .handler_download import DownloadHandlers
from .handler_mapping import MappingHandlers
from .handler_compile import CompilationHandlers
from .handler_settings import SettingsHandlers


class GuiEventHandlers(
        UiHandlers, DownloadHandlers, MappingHandlers,
        CompilationHandlers, SettingsHandlers):
    """Compose the GUI handler responsibilities behind the old public API."""

    def __init__(self, dialog):
        self.dialog = dialog
        self.worker = None
        self.worker_thread = None
        self.download_thread = None
        self.download_worker = None
        self.settings_manager = SettingsManager()


__all__ = ['GuiEventHandlers']
