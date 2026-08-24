# -*- coding: utf-8 -*-
"""Собирает установочный ZIP Garmin Export для локальной проверки QGIS."""

import argparse
import os
import zipfile


PLUGIN_NAME = 'garmin_export'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, 'dist')
EXCLUDE_DIRS = {
    '.git', '.github', '.claude', 'docs', 'docs_mkgmap', 'examples', 'plan',
    'tests', 'scripts', 'dist', 'wheels', '__pycache__', '.pytest_cache', '.venv',
    'pics_gui_different',
}
EXCLUDE_TOP_FILES = {'README.md', '.gitignore', 'setup.cfg'}
EXCLUDE_SUFFIXES = ('.pyc', '.pyo')


def _included_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel_dir = os.path.relpath(dirpath, ROOT)
        top = rel_dir.split(os.sep)[0]
        if rel_dir != '.' and top in EXCLUDE_DIRS:
            dirnames[:] = []
            continue
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for name in filenames:
            if name.endswith(EXCLUDE_SUFFIXES):
                continue
            if rel_dir == '.' and name in EXCLUDE_TOP_FILES:
                continue
            full = os.path.join(dirpath, name)
            yield full, os.path.relpath(full, ROOT)


def build(output=None):
    os.makedirs(DIST, exist_ok=True)
    out = output or os.path.join(DIST, PLUGIN_NAME + '.zip')
    count = 0
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as archive:
        for full, rel in _included_files():
            archive.write(full, os.path.join(PLUGIN_NAME, rel))
            count += 1
    print('Wrote {0} ({1} files)'.format(out, count))
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default=None)
    build(parser.parse_args().output)
