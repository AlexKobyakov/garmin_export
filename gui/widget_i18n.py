# -*- coding: utf-8 -*-
"""Presentation-only translation handlers for Garmin export widgets."""

from ..translation_manager import PLUGIN_NAME, translations
from ..qgis_compat import qt_enum


def retranslate_header(widget):
    t = translations.get_text
    widget.refreshLanguageSelector()
    widget.title_label.setText('🎯 ' + PLUGIN_NAME)
    widget.donation_button.setText('☕ ' + t('header_support'))
    widget.donation_button.setToolTip('❤️ ' + t('support_tip'))
    widget.author_button.setText('👤 ' + t('header_about_author'))
    widget.author_button.setToolTip('📝 ' + t('author_tip'))


def retranslate_layer_selection(widget):
    t = translations.get_text
    widget.layers_group.setTitle('📁 ' + t('select_layers'))
    widget.select_all_button.setText('✅ ' + t('select_all_layers'))
    widget.deselect_all_button.setText('❌ ' + t('deselect_all_layers'))
    widget.refresh_button.setText('🔄 ' + t('refresh'))
    widget.info_label.setText(t('layers_info'))


def retranslate_export_settings(widget):
    t = translations.get_text
    widget.output_group.setTitle('📤 ' + t('output_files'))
    widget.output_folder_label.setText(t('output_folder'))
    widget.output_folder_line.setPlaceholderText(
        t('output_folder_placeholder'))
    widget.output_folder_button.setText('📂 ' + t('browse'))
    widget.output_filename_label.setText(t('output_file_name'))
    widget.map_group.setTitle('🗺️ ' + t('map_settings'))
    widget.family_id_label.setText(t('family_id'))
    widget.family_id_spin.setToolTip(t('family_id_tip'))
    widget.map_id_label.setText(t('map_id'))
    widget.map_id_spin.setToolTip(t('map_id_tip'))
    widget.map_name_label.setText(t('map_name'))
    widget.map_name_line.setPlaceholderText(t('map_name'))
    widget.map_description_label.setText(t('map_description'))
    widget.map_description_line.setPlaceholderText(
        t('map_description_placeholder'))
    widget.transparent_cb.setText(t('transparent'))
    widget.transparent_cb.setToolTip(t('transparent_tip'))
    widget.routing_cb.setText(t('routing'))
    widget.routing_cb.setToolTip(t('routing_tip'))


def retranslate_style_mapping(widget):
    t = translations.get_text
    widget.mapping_group.setTitle('🎨 ' + t('style_mapping'))
    widget.load_mapping_button.setText('📂 ' + t('load_mapping'))
    widget.save_mapping_button.setText('💾 ' + t('save_mapping'))
    widget.edit_mapping_button.setText('✏️ ' + t('edit_mapping'))
    widget.reset_mapping_button.setText('🔄 ' + t('default_mapping'))
    widget.info_label.setText(t('mapping_info'))
    widget.mapping_text.setPlaceholderText(t('mapping_placeholder'))


def retranslate_control_buttons(widget):
    t = translations.get_text
    compiling = not widget.compile_button.isEnabled()
    widget.compile_button.setText(
        ('⏳ ' + t('compiling')) if compiling
        else ('🚀 ' + t('compile_map')))
    widget.cancel_button.setText('❌ ' + t('cancel'))
    widget.clear_log_button.setText('🧹 ' + t('clear_logs'))


def retranslate_log(widget):
    if widget.document().blockCount() > 2 and not widget._initial_messages:
        return
    widget.clear()
    widget.append("🎯 <span style='color: #3498db;'>{0}</span>".format(
        translations.get_text('log_ready')))
    widget.append("📋 <span style='color: #95a5a6;'>{0}</span>".format(
        translations.get_text('log_hint')))
    widget._initial_messages = False


def retranslate_results(widget):
    t = translations.get_text
    widget.setHorizontalHeaderLabels([
        '📄 ' + t('layer'), '📊 ' + t('status'), '💬 ' + t('message')])
    for row in range(widget.rowCount()):
        status_item = widget.item(row, 1)
        if status_item is None:
            continue
        status = status_item.data(qt_enum('ItemDataRole', 'UserRole'))
        if status:
            icon = {'success': '✅', 'error': '❌', 'warning': '⚠️',
                    'processing': '⏳'}.get(status, '❓')
            status_item.setText('{0} {1}'.format(icon, t(status)))


def retranslate_levels(widget):
    t = translations.get_text
    widget.levels_group.setTitle('📊 ' + t('export_levels'))
    widget.level_0_cb.setText(t('level_0'))
    widget.level_1_cb.setText(t('level_1'))
    widget.level_2_cb.setText(t('level_2'))
    widget.level_3_cb.setText(t('level_3'))
    widget.info_label.setText(t('levels_info'))
