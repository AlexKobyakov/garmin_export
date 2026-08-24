# -*- coding: utf-8 -*-
"""Backward-compatible widget exports.

The concrete widgets live in focused modules.  Existing imports from
``gui.gui_widgets`` remain supported for plugin and third-party callers.
"""

import json

from .widget_header import HeaderWidget
from .widget_selection import LayerSelectionWidget, ExportSettingsWidget
from .widget_results import (
    StyleMappingWidget, ControlButtonsWidget, LogTextWidget,
    ResultsTableWidget, LevelSettingsWidget,
)


def get_default_mapping_json():
    """Return the canonical JSON mapping used by the mapping editor."""
    from ..core.style_mapper import StyleMapper
    return json.dumps(StyleMapper()._get_default_mapping(),
                      indent=2, ensure_ascii=False)


__all__ = [
    'HeaderWidget', 'LayerSelectionWidget', 'ExportSettingsWidget',
    'StyleMappingWidget', 'ControlButtonsWidget', 'LogTextWidget',
    'ResultsTableWidget', 'LevelSettingsWidget', 'get_default_mapping_json',
]
