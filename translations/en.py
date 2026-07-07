# -*- coding: utf-8 -*-
"""
English translations for Garmin Export Plugin
Английские переводы для плагина экспорта в Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

translations = {
    # Main interface
    'window_title': 'Garmin IMG Export - Vector Data Converter',
    'no_vector_layers': 'The project has no vector layers to export.\n\n'
                        'Add vector layers to the project and try again.',

    # Tabs
    'tab_layers': 'Layers',
    'tab_export': 'Export',
    'tab_tools': 'Tools',
    'tab_styles': 'Styles',
    'tab_typ': 'TYP',
    'tab_levels': 'Levels',
    'tab_tuning': 'Tuning',

    # Layer selection
    'select_layers': 'Layer Selection for Export',
    'select_all_layers': 'Select All Layers',
    'deselect_all_layers': 'Deselect All',
    'refresh': 'Refresh',
    'layers_list': 'Project Layers List:',

    # Export settings
    'output_files': 'Output Files',
    'output_folder': 'Output Folder:',
    'output_file_name': 'Map File Name:',
    'browse': 'Browse...',
    'map_settings': 'Map Settings',
    'family_id': 'Family ID:',
    'map_id': 'Map ID:',
    'map_name': 'Map Name:',
    'map_description': 'Description:',
    'transparent': 'Transparent Map',
    'routing': 'Routing Support',

    # Tools (mkgmap / splitter / java)
    'tools_mkgmap': 'mkgmap Tools',
    'add_mkgmap': 'Add mkgmap',
    'download_mkgmap': 'Download mkgmap',
    'add_splitter': 'Add splitter',
    'download_splitter': 'Download splitter',
    'detect_java': 'Auto-detect',
    'select_mkgmap': 'Select mkgmap.jar file',
    'select_splitter': 'Select splitter.jar file',
    'select_java': 'Select java executable',
    'jar_valid': 'file is valid',
    'jar_invalid': 'File is not a valid mkgmap.jar',
    'java_not_found': 'Java not found. Please install Java (JRE 8+).',
    'downloading': 'Downloading...',
    'download_in_progress': 'A download is already in progress.',
    'download_failed': 'Failed to download the file',
    'download_complete': 'Download complete',

    # Style mapping
    'style_mapping': 'JSON Style Mapping',
    'load_mapping': 'Load',
    'save_mapping': 'Save',
    'edit_mapping': 'Edit',
    'default_mapping': 'Default',
    'mapping_title': 'JSON Style Mapping Editor',
    'mapping_description': 'Configure mapping between QGIS layers and Garmin object types',
    'validate_json': 'Validate JSON',
    'json_valid': 'JSON syntax is valid!',
    'select_mapping_file': 'Select JSON mapping file',
    'save_mapping_file': 'Save JSON mapping file',

    # TYP styling
    'typ_styling': 'Map Styling (TYP)',
    'select_typ_file': 'Select TYP file',

    # Levels
    'export_levels': 'Map Display Levels',
    'level_0': 'Level 0 (Detailed)',
    'level_1': 'Level 1 (Main)',
    'level_2': 'Level 2 (Medium)',
    'level_3': 'Level 3 (Overview)',

    # Control buttons
    'compile_map': 'Compile Map',
    'compiling': 'Compiling...',
    'cancel': 'Cancel',
    'clear_logs': 'Clear Logs',
    'save': 'Save',
    'close': 'Close',
    'details': 'Details',

    # Progress / results
    'progress': 'Progress',
    'logs': 'Logs',
    'results': 'Results',
    'layer': 'Layer',
    'status': 'Status',
    'message': 'Message',
    'geometry_type': 'Geometry Type',
    'garmin_type': 'Garmin Type',
    'label_field': 'Label Field',

    # Common
    'success': 'Success',
    'error': 'Error',
    'warning': 'Warning',
    'info': 'Information',
    'confirmation': 'Confirmation',
    'critical_error': 'Critical Error',
    'select_output_folder': 'Select output folder for the IMG file',

    # Errors
    'error_no_layers': 'Select at least one layer for export',
    'error_no_output_folder': 'Specify output folder',
    'error_output_folder_missing': 'Output folder does not exist',
    'error_no_mkgmap': 'Specify the path to mkgmap.jar or download it '
                       'with the "Download mkgmap" button',
    'error_invalid_mkgmap': 'The specified file is not a valid mkgmap.jar',
    'error_java_not_found': 'Java not found on the system. Install Java (JRE 8+) '
                            'and set the path on the "Tools" tab.',
    'error_typ_not_found': 'The specified TYP file was not found',
    'error_invalid_json': 'Invalid JSON mapping format',
    'error_mkgmap_execution': 'mkgmap execution error: {error}',
    'confirm_close': 'Compilation in progress. Stop and close?',

    # Author dialog
    'about_author': 'About Author',
    'header_support': 'Support',
    'header_about_author': 'About Author',
    'version': 'Version',
    'author': 'Author',
    'contact': 'Contact',
    'year': 'Year',
    'organization': 'Organization',
    'plugin_description': 'Professional tool for exporting QGIS data '
                          'to Garmin IMG maps via mkgmap',
    'multilingual_support': 'QGIS styling, TYP generation, mkgmap fine-tuning, '
                            'multilingual interface',

    # Donation dialog
    'donation_title': '☕ Support Development',
    'donation_window_title': '☕ Support Plugin Development',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 Garmin Export Plugin</b></p>
            <p>this plugin is developed and maintained <b>for free</b>!</p>
            <p>Your support helps update and improve the plugin.</p>
            <p style="color: #7f8c8d; font-size: 13px;">Every coffee counts! ❤️</p>
        </div>''',
    'donation_kofi': '☕ Buy Coffee on Ko-fi',
    'donation_tbank': '💳 Donate via T-Bank',
    'donation_github': '💖 Sponsor on GitHub',
    'donation_maybe_later': '✅ Maybe Later',

    # Success messages
    'success_export_complete': 'Map compiled successfully! File saved:',
    'success_mapping_saved': 'Mapping saved successfully',
    'success_mapping_loaded': 'Mapping loaded successfully',
}
