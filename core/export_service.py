# -*- coding: utf-8 -*-
"""Pure export-run lifecycle and redacted observability contract."""

import datetime
import hashlib
import json
import os
import re
import tempfile


STATUS_IDLE = 'idle'
STATUS_VALIDATING = 'validating'
STATUS_DOWNLOADING = 'downloading'
STATUS_EXPORTING = 'exporting'
STATUS_CANCELLED = 'cancelled'
STATUS_FAILED = 'failed'
STATUS_SUCCESS = 'success'

STATUSES = {
    STATUS_IDLE, STATUS_VALIDATING, STATUS_DOWNLOADING, STATUS_EXPORTING,
    STATUS_CANCELLED, STATUS_FAILED, STATUS_SUCCESS,
}


def _utc_now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def _settings_fingerprint(settings):
    payload = json.dumps(settings or {}, sort_keys=True, default=str,
                         ensure_ascii=False).encode('utf-8')
    return hashlib.sha256(payload).hexdigest()


def _tool_version(path, tool):
    match = re.search(r'{0}-r(\d+)'.format(re.escape(tool)),
                      str(path or ''), re.IGNORECASE)
    return 'r' + match.group(1) if match else 'unknown'


class ExportService:
    """Owns one run's state; it never imports QGIS or emits GUI signals."""

    def __init__(self, selected_layers, settings, plugin_version='1.2.1'):
        self.selected_layers = [
            {'id': str(item.get('id') or ''),
             'name': str(item.get('name') or '')}
            for item in (selected_layers or [])
        ]
        self.settings = settings or {}
        self.plugin_version = plugin_version
        self.status = STATUS_IDLE
        self.cancel_requested = False
        self.started_at = _utc_now()
        self.finished_at = None
        self.output_file = ''
        self.error_class = None
        self.manifest_error = None

    def set_status(self, status):
        if status not in STATUSES:
            raise ValueError('Unknown export status: {0}'.format(status))
        self.status = status

    def request_cancel(self):
        self.cancel_requested = True
        self.set_status(STATUS_CANCELLED)

    def is_cancelled(self):
        return self.cancel_requested

    def finish_success(self, output_file):
        if self.cancel_requested:
            self.set_status(STATUS_CANCELLED)
            return False
        self.output_file = output_file or ''
        self.set_status(STATUS_SUCCESS)
        self.finished_at = _utc_now()
        return True

    def finish_failure(self, error):
        if self.cancel_requested:
            self.set_status(STATUS_CANCELLED)
        else:
            self.error_class = type(error).__name__ if error else 'Exception'
            self.set_status(STATUS_FAILED)
        self.finished_at = _utc_now()

    def _manifest(self):
        output = None
        if self.status == STATUS_SUCCESS and self.output_file:
            size = None
            try:
                size = os.path.getsize(self.output_file)
            except OSError:
                pass
            output = {'path': self.output_file, 'size': size}
        return {
            'schema_version': 1,
            'status': self.status,
            'started_at': self.started_at,
            'finished_at': self.finished_at or _utc_now(),
            'plugin_version': self.plugin_version,
            'tool_versions': {
                'mkgmap': _tool_version(self.settings.get('mkgmap_path'),
                                        'mkgmap'),
                'splitter': _tool_version(self.settings.get('splitter_path'),
                                          'splitter'),
                'java': 'configured' if self.settings.get('java_path')
                else 'auto-detect',
            },
            'selected_layers': self.selected_layers,
            'settings_fingerprint': _settings_fingerprint(self.settings),
            'output': output,
            'error_class': self.error_class,
        }

    def write_manifest(self, path=None):
        """Atomically persist one redacted manifest; return path or None."""
        target = path or os.path.join(
            self.settings.get('output_folder') or '',
            '.garmin_export', 'run_manifest.json')
        if not os.path.dirname(target):
            return None
        try:
            directory = os.path.dirname(os.path.abspath(target))
            os.makedirs(directory, exist_ok=True)
            fd, temporary = tempfile.mkstemp(
                prefix='.run_manifest-', suffix='.part', dir=directory)
            with os.fdopen(fd, 'w', encoding='utf-8') as stream:
                json.dump(self._manifest(), stream, ensure_ascii=False,
                          indent=2, sort_keys=True)
                stream.write('\n')
            os.replace(temporary, target)
            return target
        except (OSError, TypeError, ValueError) as error:
            self.manifest_error = type(error).__name__
            try:
                os.remove(temporary)
            except (OSError, UnboundLocalError):
                pass
            return None
