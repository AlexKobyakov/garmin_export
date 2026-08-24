# -*- coding: utf-8 -*-
"""Qt5/Qt6 and QGIS 3/4 compatibility helpers.

All compatibility decisions live here so GUI and core modules can keep a
single import boundary for QGIS-provided Qt classes and scoped enums.
"""

from qgis.PyQt.QtCore import Qt, QVariant
from qgis.PyQt.QtGui import QFont
from qgis.core import Qgis, QgsSymbolLayer, QgsTask


def qt_enum(scope, name):
    """Return a Qt6 scoped enum member with a Qt5 fallback."""
    return getattr(getattr(Qt, scope, Qt), name)


def qt_class_enum(owner, scope, name):
    """Return a class-scoped Qt6 enum member with a Qt5 fallback."""
    return getattr(getattr(owner, scope, owner), name)


def qvariant_type(name):
    """Return a QVariant.Type member on Qt6 or its Qt5 equivalent."""
    return getattr(getattr(QVariant, 'Type', QVariant), name)


def qfont_weight(name):
    """Return a QFont.Weight member on Qt6 or its Qt5 equivalent."""
    return getattr(getattr(QFont, 'Weight', QFont), name)


def qgis_enum(scope, name, legacy_owner=None, legacy_name=None):
    """Return a QGIS 4 scoped enum member or its QGIS 3 counterpart."""
    scoped = getattr(Qgis, scope, None)
    if scoped is not None and hasattr(scoped, name):
        return getattr(scoped, name)
    return getattr(legacy_owner or Qgis, legacy_name or name)


def qgis_geometry_type(name, legacy_owner):
    """Return a QGIS geometry type compatible with QGIS 3 and QGIS 4."""
    return qgis_enum('GeometryType', name, legacy_owner,
                     f'{name}Geometry')


def task_can_cancel():
    """Return the QgsTask cancellation flag on either QGIS generation."""
    return qgis_enum('TaskFlag', 'CanCancel', QgsTask)


def symbol_layer_property(name):
    """Return a QgsSymbolLayer property on either QGIS generation."""
    return qgis_enum('SymbolLayerProperty', name, QgsSymbolLayer)
