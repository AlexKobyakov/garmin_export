# -*- coding: utf-8 -*-
"""
English translations for Garmin Export Plugin
Английские переводы для плагина экспорта в Garmin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

translations = {
    # Main interface translations
    'window_title': 'Garmin IMG Export - Vector Data Converter',
    'select_layers': 'Layer Selection for Export',
    'layer_mapping': 'Style Mapping',
    'export_settings': 'Export Settings',
    'mkgmap_settings': 'mkgmap Settings',
    'select_all_layers': 'Select All Layers',
    'deselect_all_layers': 'Deselect All',
    'layers_list': 'Project Layers List:',
    'output_folder': 'Output Folder:',
    'output_file_name': 'Map File Name:',
    'browse': 'Browse...',
    'map_settings': 'Map Settings',
    'family_id': 'Family ID:',
    'map_id': 'Map ID:',
    'map_name': 'Map Name:',
    'map_description': 'Map Description:',
    'transparent': 'Transparent Map',
    'routing': 'Routing Support',
    'mkgmap_path': 'Path to mkgmap.jar:',
    'style_mapping': 'JSON Style Mapping:',
    'edit_mapping': 'Edit Mapping',
    'load_mapping': 'Load Mapping',
    'save_mapping': 'Save Mapping',
    'compile_map': 'Compile Map',
    'cancel': 'Cancel',
    'progress': 'Progress:',
    'logs': 'Logs',
    'results': 'Results',
    'clear_logs': 'Clear Logs',
    'compiling': 'Compiling...',
    'language': 'Language:',
    'layer': 'Layer',
    'geometry_type': 'Geometry Type',
    'garmin_type': 'Garmin Type',
    'label_field': 'Label Field',
    'export_levels': 'Export Levels',
    'level_0': 'Level 0 (Detailed)',
    'level_1': 'Level 1 (Main)',
    'level_2': 'Level 2 (Medium)',
    'level_3': 'Level 3 (Overview)',
    'success': 'Success',
    'error': 'Error',
    'warning': 'Warning',
    'info': 'Information',
    'select_output_folder': 'Select output folder',
    'select_mkgmap': 'Select mkgmap.jar file',
    'select_mapping_file': 'Select JSON mapping file',
    'save_mapping_file': 'Save JSON mapping file',
    'error_no_layers': 'Select at least one layer for export',
    'error_no_output_folder': 'Specify output folder',
    'error_no_mkgmap': 'Specify path to mkgmap.jar file',
    'error_invalid_mkgmap': 'Invalid path to mkgmap.jar',
    'error_java_not_found': 'Java not found in system',
    'compilation_cancelled': 'Cancelling compilation...',
    'confirm_close': 'Compilation in progress. Stop and close?',
    'confirmation': 'Confirmation',
    'critical_error': 'Critical Error',
    'author_info': 'Author: Кобяков Александр Викторович (Alex Kobyakov)\\nEmail: kobyakov@lesburo.ru\\nYear: 2025',
    'about_author': 'About Author',
    'settings': 'Settings',
    'layer_selection': 'Layer Selection',
    'export_options': 'Export Options',
    
    # Style mapping translations
    'mapping_title': 'JSON Style Mapping Editor',
    'mapping_description': 'Configure mapping between QGIS layers and Garmin object types',
    'default_mapping': 'Default Mapping',
    'custom_mapping': 'Custom Mapping',
    'geometry_point': 'Point',
    'geometry_line': 'Line',
    'geometry_polygon': 'Polygon',
    'garmin_types_poi': 'POI (Points of Interest)',
    'garmin_types_roads': 'Roads',
    'garmin_types_areas': 'Areas',
    'garmin_types_other': 'Other',
    
    # Donation dialog translations
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
    'donation_support_development': '☕ Support Plugin Development',
    'donation_plugin_info': 'this plugin is developed and maintained for free!',
    'donation_help_improve': 'Your support helps update and improve the plugin.',
    'donation_every_coffee': 'Every coffee counts! ❤️',
    
    # Header buttons translations
    'header_support': 'Support',
    'header_about_author': 'About Author',
    
    # Author dialog translations
    'version': 'Version',
    'author': 'Author',
    'contact': 'Contact',
    'year': 'Year',
    'organization': 'Organization',
    'plugin_description': 'Professional GIS data export tool to Garmin format',
    'multilingual_support': 'Supporting multiple languages and formats',
    
    # Processing messages
    'processing_start': 'Starting layer processing...',
    'processing_layer': 'Processing layer: {layer_name}',
    'processing_complete': 'Processing completed successfully!',
    'mp_generation_start': 'Generating MP file...',
    'mp_generation_complete': 'MP file created: {file_path}',
    'mkgmap_compilation_start': 'Starting mkgmap compilation...',
    'mkgmap_compilation_complete': 'Compilation completed: {file_path}',
    'export_statistics': 'Export statistics: {count} objects processed',
    
    # File operations
    'creating_folder': 'Creating folder: {folder_path}',
    'writing_file': 'Writing file: {file_path}',
    'reading_mapping': 'Reading mapping from: {file_path}',
    'saving_mapping': 'Saving mapping to: {file_path}',
    
    # Error messages
    'error_layer_processing': 'Error processing layer {layer_name}: {error}',
    'error_mp_generation': 'Error generating MP file: {error}',
    'error_mkgmap_execution': 'Error executing mkgmap: {error}',
    'error_file_not_found': 'File not found: {file_path}',
    'error_permission_denied': 'Permission denied: {file_path}',
    'error_invalid_json': 'Invalid JSON format in mapping file',
    'error_unsupported_geometry': 'Unsupported geometry type: {geometry_type}',
    
    # Success messages
    'success_export_complete': 'Export completed successfully!',
    'success_mapping_saved': 'Mapping saved successfully',
    'success_mapping_loaded': 'Mapping loaded successfully',
    'success_layer_processed': 'Layer {layer_name} processed successfully',
}
