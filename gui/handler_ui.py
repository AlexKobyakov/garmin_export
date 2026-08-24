# -*- coding: utf-8 -*-
"""Header, file chooser and tool-status handlers."""

import os

from qgis.PyQt.QtWidgets import QFileDialog

from ..core import mkgmap_compiler
from ..qgis_compat import qt_enum


class UiHandlers:
    def onLanguageChanged(self, index):
        from ..translation_manager import translations
        code = self.dialog.header.language_code_at(index)
        if code and translations.set_language(code):
            self.dialog.updateLanguage()
            self.dialog.updatePluginAction()
            direction = (qt_enum('LayoutDirection', 'RightToLeft')
                         if translations.is_rtl(code)
                         else qt_enum('LayoutDirection', 'LeftToRight'))
            self.dialog.setLayoutDirection(direction)
            self.settings_manager.set('language', code)
            self.dialog.log_message('🌐 {0}'.format(code))

    def showDonation(self):
        from .simple_donation import SimpleDonationDialog
        SimpleDonationDialog(self.dialog).exec()

    def showAuthorInfo(self):
        from .gui_dialogs import AuthorInfoDialog
        AuthorInfoDialog(self.dialog).exec()

    def selectOutputFolder(self):
        from ..translation_manager import translations
        line = self.dialog.export_settings.output_folder_line
        start = line.text().strip() or os.path.expanduser('~')
        folder = QFileDialog.getExistingDirectory(
            self.dialog, translations.get_text('select_output_folder'), start)
        if folder:
            line.setText(folder)
            self.settings_manager.set('output_folder', folder)
            self.dialog.log_message('📂 {0}'.format(folder))

    def selectMkgmapPath(self):
        from ..translation_manager import translations
        path, _ = QFileDialog.getOpenFileName(
            self.dialog, translations.get_text('select_mkgmap'),
            os.path.expanduser('~'), 'JAR files (*.jar);;All files (*)')
        if path:
            self.dialog.tools_widget.mkgmap_path_line.setText(path)
            self.onMkgmapPathChanged()
            self.dialog.log_message('⚙️ {0}'.format(path))

    def selectSplitterPath(self):
        from ..translation_manager import translations
        path, _ = QFileDialog.getOpenFileName(
            self.dialog, translations.get_text('select_splitter'),
            os.path.expanduser('~'), 'JAR files (*.jar);;All files (*)')
        if path:
            self.dialog.tools_widget.splitter_path_line.setText(path)
            self.onSplitterPathChanged()
            self.dialog.log_message('⚙️ {0}'.format(path))

    def selectJavaPath(self):
        from ..translation_manager import translations
        path, _ = QFileDialog.getOpenFileName(
            self.dialog, translations.get_text('select_java'),
            os.path.expanduser('~'),
            'Java executable (java.exe);;All files (*)')
        if path:
            self.dialog.tools_widget.java_path_line.setText(path)
            self.onJavaPathChanged()

    def detectJava(self):
        from ..translation_manager import translations
        path = mkgmap_compiler.find_java()
        if path:
            self.dialog.tools_widget.java_path_line.setText(path)
            self.onJavaPathChanged()
            self.dialog.log_message('☕ {0}'.format(path))
        else:
            message = '❌ ' + translations.get_text('java_not_found')
            self.dialog.tools_widget.java_status_label.setText(message)
            self.dialog.log_message(
                '⚠️ ' + translations.get_text('java_not_found'))

    def selectTypFile(self):
        from ..translation_manager import translations
        path, _ = QFileDialog.getOpenFileName(
            self.dialog, translations.get_text('select_typ_file'),
            os.path.expanduser('~'),
            'TYP files (*.typ *.txt);;All files (*)')
        if path:
            self.dialog.typ_settings.set_typ_file_path(path)
            self.settings_manager.set('typ_file_path', path)
            self.dialog.log_message('🖌️ {0}'.format(path))

    def onMkgmapPathChanged(self):
        from ..translation_manager import translations
        path = self.dialog.tools_widget.mkgmap_path_line.text().strip()
        label = self.dialog.tools_widget.mkgmap_status_label
        if not path:
            label.setText('')
            return
        if mkgmap_compiler.validate_tool_installation(path, 'mkgmap'):
            label.setText(
                '✅ mkgmap.jar + lib/: ' + translations.get_text('jar_valid'))
            label.setStyleSheet('color: #27ae60; font-size: 10px;')
            self.settings_manager.set('mkgmap_path', path)
        else:
            label.setText('❌ mkgmap.jar + lib/: ' +
                          translations.get_text('jar_invalid'))
            label.setStyleSheet('color: #e74c3c; font-size: 10px;')

    def onSplitterPathChanged(self):
        from ..translation_manager import translations
        path = self.dialog.tools_widget.splitter_path_line.text().strip()
        label = self.dialog.tools_widget.splitter_status_label
        if not path:
            label.setText('')
            self.settings_manager.set('splitter_path', '')
            return
        if mkgmap_compiler.validate_tool_installation(path, 'splitter'):
            label.setText(
                '✅ splitter.jar + lib/: ' + translations.get_text('jar_valid'))
            label.setStyleSheet(
                'color: #27ae60; font-size: 10px; padding: 2px 4px;')
            self.settings_manager.set('splitter_path', path)
        else:
            label.setText('❌ splitter.jar + lib/: ' +
                          translations.get_text('tool_invalid'))
            label.setStyleSheet(
                'color: #e74c3c; font-size: 10px; padding: 2px 4px;')

    def onJavaPathChanged(self):
        from ..translation_manager import translations
        path = self.dialog.tools_widget.java_path_line.text().strip()
        label = self.dialog.tools_widget.java_status_label
        version = mkgmap_compiler.get_java_version(path or None)
        if version:
            label.setText('✅ ' + version)
            label.setStyleSheet('color: #27ae60; font-size: 10px;')
            self.settings_manager.set('java_path', path)
        else:
            label.setText('❌ ' + translations.get_text('java_not_found'))
            label.setStyleSheet('color: #e74c3c; font-size: 10px;')
