# -*- coding: utf-8 -*-
"""mkgmap and splitter download handlers."""

from qgis.PyQt.QtCore import QThread
from qgis.PyQt.QtWidgets import QMessageBox


class DownloadHandlers:
    def downloadMkgmap(self):
        self._download_tool('mkgmap')

    def downloadSplitter(self):
        self._download_tool('splitter')

    def _download_tool(self, tool):
        from ..translation_manager import translations
        from ..core.download_worker import DownloadWorker
        from .gui_dialogs import DownloadProgressDialog

        if self.download_thread is not None:
            QMessageBox.information(
                self.dialog, translations.get_text('info'),
                translations.get_text('download_in_progress'))
            return
        title_key = ('download_mkgmap' if tool == 'mkgmap'
                     else 'download_splitter')
        title = translations.get_text(title_key)
        progress = DownloadProgressDialog(
            title, self.dialog, title_key=title_key)
        self.download_thread = QThread(self.dialog)
        self.download_worker = DownloadWorker(tool)
        self.download_worker.moveToThread(self.download_thread)
        self.download_thread.started.connect(self.download_worker.run)
        self.download_worker.progress.connect(progress.update_progress)
        self.download_worker.status.connect(progress.set_status)
        progress.cancel_button.clicked.connect(self.download_worker.cancel)
        result = {}

        def on_finished(success, payload):
            result['success'] = success
            result['payload'] = payload
            progress.accept()

        self.download_worker.finished.connect(on_finished)
        self.download_thread.start()
        self.dialog.log_message('📥 {0}...'.format(title))
        progress.exec()
        if 'success' not in result:
            self.download_worker.cancel()
        self.download_thread.quit()
        self.download_thread.wait(15000)
        error_code = getattr(self.download_worker, 'error_code', 'download_failed')
        self.download_thread = None
        self.download_worker = None
        success = result.get('success', False)
        payload = result.get('payload', '')
        if success:
            self._apply_downloaded_tool(tool, payload)
        elif payload:
            category_key = {'archive': 'tool_invalid', 'dependencies': 'tool_invalid', 'cancelled': 'cancel', 'network': 'download_failed', 'permission': 'download_failed'}.get(error_code, 'download_failed')
            category = translations.get_text(category_key)
            message = '[{0}] {1}'.format(category, payload)
            self.dialog.log_message('❌ {0}: {1}'.format(translations.get_text('download_failed'), message))
            QMessageBox.warning(self.dialog, translations.get_text('download_failed'), message)

    def _apply_downloaded_tool(self, tool, path):
        from ..translation_manager import translations
        if tool == 'mkgmap':
            self.dialog.tools_widget.mkgmap_path_line.setText(path)
            self.onMkgmapPathChanged()
        else:
            self.dialog.tools_widget.splitter_path_line.setText(path)
            self.onSplitterPathChanged()
        self.dialog.log_message(
            '✅ {0}: {1}'.format(
                translations.get_text('download_complete'), path))
