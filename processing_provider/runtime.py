# -*- coding: utf-8 -*-
"""Processing-side discovery and explicit tool installation.

This module reuses the UI downloader's atomic archive transaction. Processing
never installs silently: callers must opt in with AUTO_DOWNLOAD.
"""

import os

from ..core import downloader
from ..core.download_worker import get_tools_directory
from ..core.mkgmap_compiler import validate_tool_installation
from ..translation_manager import translations


def discover_tool(tool, explicit_path=''):
    """Return a valid installed JAR, preferring an explicit path."""
    if explicit_path and validate_tool_installation(explicit_path, tool):
        return os.path.abspath(explicit_path)
    root = get_tools_directory()
    candidates = []
    for dirpath, _dirnames, filenames in os.walk(root):
        jar_name = '{0}.jar'.format(tool)
        if jar_name in filenames:
            candidates.append(os.path.join(dirpath, jar_name))
    for candidate in sorted(candidates):
        if validate_tool_installation(candidate, tool):
            return os.path.abspath(candidate)
    return ''


def ensure_tool(tool, explicit_path, auto_download, feedback, start=0,
                span=30):
    """Discover or explicitly download a complete tool distribution."""
    found = discover_tool(tool, explicit_path)
    if found:
        feedback.pushInfo('{0} found: {1}'.format(tool, found))
        return found
    if not auto_download:
        raise ValueError('{0}_missing: provide a valid path or enable '
                         'AUTO_DOWNLOAD'.format(tool))

    tools_dir = get_tools_directory()

    def progress(received, total, status):
        if total:
            value = start + span * min(1.0, float(received) / total)
            feedback.setProgress(value)
        if status:
            feedback.pushInfo('{0}: {1}'.format(tool, status))

    try:
        path = downloader.download_tool(
            tool, tools_dir, progress_callback=progress,
            cancelled_callback=feedback.isCanceled,
            language=translations.get_current_language())
    except downloader.DownloadCancelledError:
        raise ValueError('cancelled')
    except Exception as exc:
        code = getattr(exc, 'code', 'download_failed')
        raise ValueError('{0}_download_{1}'.format(tool, code))
    if feedback.isCanceled():
        raise ValueError('cancelled')
    feedback.pushInfo('{0} downloaded: {1}'.format(tool, path))
    return path
