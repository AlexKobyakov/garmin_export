# -*- coding: utf-8 -*-
"""
Spanish translations for Garmin Export Plugin
Traducciones al español para el complemento Garmin Export

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

translations = {
    # Main interface
    'window_title': 'Exportar a Garmin IMG - Conversor de datos vectoriales',
    'no_vector_layers': 'El proyecto no tiene capas vectoriales para exportar.\n\n'
                        'Añada capas vectoriales al proyecto e inténtelo de nuevo.',

    # Tabs
    'tab_layers': 'Capas',
    'tab_export': 'Exportar',
    'tab_tools': 'Herramientas',
    'tab_styles': 'Estilos',
    'tab_typ': 'TYP',
    'tab_levels': 'Niveles',
    'tab_tuning': 'Ajuste',

    # Layer selection
    'select_layers': 'Selección de capas para exportar',
    'select_all_layers': 'Seleccionar todas las capas',
    'deselect_all_layers': 'Deseleccionar todo',
    'refresh': 'Actualizar',
    'layers_list': 'Lista de capas del proyecto:',

    # Export settings
    'output_files': 'Archivos de salida',
    'output_folder': 'Carpeta de salida:',
    'output_file_name': 'Nombre del archivo de mapa:',
    'browse': 'Examinar...',
    'map_settings': 'Ajustes del mapa',
    'family_id': 'Family ID:',
    'map_id': 'Map ID:',
    'map_name': 'Nombre del mapa:',
    'map_description': 'Descripción:',
    'transparent': 'Mapa transparente',
    'routing': 'Compatibilidad con rutas',

    # Tools (mkgmap / splitter / java)
    'tools_mkgmap': 'Herramientas mkgmap',
    'add_mkgmap': 'Añadir mkgmap',
    'download_mkgmap': 'Descargar mkgmap',
    'add_splitter': 'Añadir splitter',
    'download_splitter': 'Descargar splitter',
    'detect_java': 'Detección automática',
    'select_mkgmap': 'Seleccionar archivo mkgmap.jar',
    'select_splitter': 'Seleccionar archivo splitter.jar',
    'select_java': 'Seleccionar ejecutable de java',
    'jar_valid': 'el archivo es válido',
    'jar_invalid': 'El archivo no es un mkgmap.jar válido',
    'java_not_found': 'Java no encontrado. Instale Java (JRE 8+).',
    'downloading': 'Descargando...',
    'download_in_progress': 'Ya hay una descarga en curso.',
    'download_failed': 'No se pudo descargar el archivo',
    'download_complete': 'Descarga completada',

    # Style mapping
    'style_mapping': 'Asignación de estilos JSON',
    'load_mapping': 'Cargar',
    'save_mapping': 'Guardar',
    'edit_mapping': 'Editar',
    'default_mapping': 'Predeterminado',
    'mapping_title': 'Editor de asignación de estilos JSON',
    'mapping_description': 'Configure la correspondencia entre las capas de QGIS y los tipos de objeto de Garmin',
    'validate_json': 'Validar JSON',
    'json_valid': '¡La sintaxis JSON es válida!',
    'select_mapping_file': 'Seleccionar archivo de asignación JSON',
    'save_mapping_file': 'Guardar archivo de asignación JSON',

    # TYP styling
    'typ_styling': 'Estilo del mapa (TYP)',
    'select_typ_file': 'Seleccionar archivo TYP',

    # Levels
    'export_levels': 'Niveles de visualización del mapa',
    'level_0': 'Nivel 0 (detallado)',
    'level_1': 'Nivel 1 (principal)',
    'level_2': 'Nivel 2 (medio)',
    'level_3': 'Nivel 3 (general)',

    # Control buttons
    'compile_map': 'Compilar mapa',
    'compiling': 'Compilando...',
    'cancel': 'Cancelar',
    'clear_logs': 'Borrar registros',
    'save': 'Guardar',
    'close': 'Cerrar',
    'details': 'Detalles',

    # Progress / results
    'progress': 'Progreso',
    'logs': 'Registros',
    'results': 'Resultados',
    'layer': 'Capa',
    'status': 'Estado',
    'message': 'Mensaje',
    'geometry_type': 'Tipo de geometría',
    'garmin_type': 'Tipo Garmin',
    'label_field': 'Campo de etiqueta',

    # Common
    'success': 'Éxito',
    'error': 'Error',
    'warning': 'Advertencia',
    'info': 'Información',
    'confirmation': 'Confirmación',
    'critical_error': 'Error crítico',
    'select_output_folder': 'Seleccione la carpeta de salida para el archivo IMG',

    # Errors
    'error_no_layers': 'Seleccione al menos una capa para exportar',
    'error_no_output_folder': 'Especifique la carpeta de salida',
    'error_output_folder_missing': 'La carpeta de salida no existe',
    'error_no_mkgmap': 'Especifique la ruta a mkgmap.jar o descárguelo '
                       'con el botón "Descargar mkgmap"',
    'error_invalid_mkgmap': 'El archivo especificado no es un mkgmap.jar válido',
    'error_java_not_found': 'Java no se encontró en el sistema. Instale Java (JRE 8+) '
                            'y establezca la ruta en la pestaña "Herramientas".',
    'error_typ_not_found': 'No se encontró el archivo TYP especificado',
    'error_invalid_json': 'Formato de asignación JSON no válido',
    'error_mkgmap_execution': 'Error de ejecución de mkgmap: {error}',
    'confirm_close': 'Compilación en curso. ¿Detener y cerrar?',

    # Author dialog
    'about_author': 'Acerca del autor',
    'header_support': 'Apoyar',
    'header_about_author': 'Acerca del autor',
    'version': 'Versión',
    'author': 'Autor',
    'contact': 'Contacto',
    'year': 'Año',
    'organization': 'Organización',
    'plugin_description': 'Herramienta profesional para exportar datos de QGIS '
                          'a mapas Garmin IMG mediante mkgmap',
    'multilingual_support': 'Estilo desde QGIS, generación de TYP, ajuste fino de mkgmap, '
                            'interfaz multilingüe',

    # Donation dialog
    'donation_title': '☕ Apoyar el desarrollo',
    'donation_window_title': '☕ Apoye el desarrollo del complemento',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 Garmin Export Plugin</b></p>
            <p>¡este complemento se desarrolla y mantiene <b>gratis</b>!</p>
            <p>Su apoyo ayuda a actualizar y mejorar el complemento.</p>
            <p style="color: #7f8c8d; font-size: 13px;">¡Cada café cuenta! ❤️</p>
        </div>''',
    'donation_kofi': '☕ Invitar a un café en Ko-fi',
    'donation_tbank': '💳 Donar a través de T-Bank',
    'donation_github': '💖 Patrocinar en GitHub',
    'donation_maybe_later': '✅ Quizás más tarde',

    # Success messages
    'success_export_complete': '¡Mapa compilado correctamente! Archivo guardado:',
    'success_mapping_saved': 'Asignación guardada correctamente',
    'success_mapping_loaded': 'Asignación cargada correctamente',
}
