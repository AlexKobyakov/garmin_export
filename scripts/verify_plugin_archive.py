# -*- coding: utf-8 -*-
"""Validate that a release ZIP contains only the installable QGIS plugin."""

import argparse
import os
import zipfile


PLUGIN_ROOT = "garmin_export/"
FORBIDDEN_DIRS = {
    ".git", ".github", "docs", "docs_mkgmap", "examples", "plan", "tests",
    "scripts", "dist", "wheels", "pics_gui_different", "__pycache__",
}
REQUIRED_FILES = {
    "garmin_export/__init__.py",
    "garmin_export/garmin_exporter.py",
    "garmin_export/metadata.txt",
    "garmin_export/icon.png",
    "garmin_export/LICENSE",
    "garmin_export/qgis_compat.py",
    "garmin_export/processing_provider/__init__.py",
}


def validate(path):
    with zipfile.ZipFile(path) as archive:
        names = set(archive.namelist())
    if not names:
        raise ValueError("archive is empty")
    if any(not name.startswith(PLUGIN_ROOT) for name in names):
        raise ValueError("archive contains paths outside garmin_export/")
    for name in names:
        parts = name.rstrip("/").split("/")
        if len(parts) > 1 and parts[1] in FORBIDDEN_DIRS:
            raise ValueError("forbidden release path: {0}".format(name))
        if name.lower().endswith((".jar", ".pyc", ".pyo")):
            raise ValueError("bundled runtime or bytecode file: {0}".format(name))
    missing = REQUIRED_FILES.difference(names)
    if missing:
        raise ValueError("missing required files: {0}".format(sorted(missing)))
    return len(names)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("archive")
    args = parser.parse_args()
    count = validate(os.path.abspath(args.archive))
    print("Validated plugin archive: {0} files".format(count))
