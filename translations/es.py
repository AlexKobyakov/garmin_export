# -*- coding: utf-8 -*-
"""
Spanish translations for Garmin Export Plugin
Traducciones al español para el complemento Garmin Export

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
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

    # Tools tab (labels, placeholders, info)
    'mkgmap_path_label': 'Ruta a mkgmap.jar:',
    'mkgmap_path_placeholder': 'Seleccione o descargue mkgmap.jar',
    'splitter_path_label': 'Ruta a splitter.jar (opcional):',
    'splitter_path_placeholder': 'splitter se necesita para dividir mapas grandes (opcional)',
    'java_path_label': 'Ruta a Java:',
    'java_path_placeholder': 'Vacío = java desde PATH; el botón de la derecha lo detecta',
    'tools_info': 'Las reglas de QGIS prohíben incluir mkgmap.jar en el complemento. '
                  'Haga clic en "Descargar mkgmap" y el complemento obtendrá la última '
                  'versión de mkgmap.org.uk (o de la copia de seguridad en Yandex.Disk), '
                  'o indique su propio archivo con "Añadir mkgmap".',
    'support_tip': '¡Apoye el desarrollo del complemento!',
    'author_tip': 'Información sobre el autor del complemento',

    # Tuning tab - group titles
    'map_params_group': 'Parámetros del mapa (mkgmap)',
    'generalization_group': 'Generalización',
    'performance_group': 'Rendimiento (ajuste)',
    'logging_group': 'Registro y depuración',

    # Tuning tab - options
    'code_page_label': 'Página de códigos de las etiquetas:',
    'draw_priority_label': 'Prioridad de dibujo (--draw-priority):',
    'draw_priority_tip': '25 es el estándar. Mayor = el mapa se dibuja sobre los demás. '
                         'Para mapas superpuestos transparentes use más de 25.',
    'opt_index': 'Índice de direcciones para la búsqueda (--index)',
    'opt_add_pois': 'Crear POI a partir de polígonos (--add-pois-to-areas)',
    'opt_lower_case': 'Permitir minúsculas en las etiquetas (--lower-case)',
    'opt_order_area': 'Polígonos pequeños sobre los grandes (--order-by-decreasing-area)',
    'reduce_density_label': 'Simplificación de líneas, m (--reduce-point-density):',
    'reduce_density_polygon_label': 'Simplificación de polígonos, m (--reduce-point-density-polygon):',
    'min_polygon_label': 'Tamaño mín. de polígono (--min-size-polygon):',
    'min_polygon_tip': 'Los polígonos más pequeños se eliminan. Se recomienda 8-15.',
    'java_heap_label': 'Memoria de Java, GB (-Xmx):',
    'java_heap_tip': 'mkgmap necesita ~500 MB por hilo. Para 8 núcleos, ponga 4 GB.',
    'max_jobs_label': 'Hilos (--max-jobs):',
    'max_jobs_tip': '0 = mkgmap decide según los núcleos y la memoria.',
    'opt_mkgmap_log': 'Mantener un archivo mkgmap.log en la carpeta de salida',
    'opt_verbose': 'Registro detallado (nivel INFO)',
    'opt_keep_temp': 'Conservar archivos intermedios (MP, TYP) en la carpeta de salida',
    'extra_args_label': 'Argumentos adicionales de mkgmap:',
    'extra_args_placeholder': 'p. ej.: --precomp-sea=C:/sea.zip --generate-sea',
    'value_auto': 'auto',
    'value_auto_default': 'auto (2.6)',

    # Code pages
    'cp_1251': 'CP1251 (cirílico)',
    'cp_1252': 'CP1252 (Latin-1, Europa Occidental)',
    'cp_1250': 'CP1250 (Europa Central)',
    'cp_1253': 'CP1253 (griego)',
    'cp_1254': 'CP1254 (turco)',
    'cp_1257': 'CP1257 (báltico)',
    'cp_65001': 'Unicode (no en todos los dispositivos)',

    # TYP tab
    'typ_info': 'Un archivo TYP define el aspecto de los objetos en el dispositivo Garmin: '
                'colores de polígonos, grosor de líneas, iconos de puntos. El complemento puede '
                'generar un TYP automáticamente a partir de la simbología actual de las capas de '
                'QGIS: el mapa en el navegador se verá como en QGIS.',
    'typ_none': 'Estilo estándar de Garmin (sin TYP)',
    'typ_generate': 'Generar TYP a partir de los estilos de QGIS (recomendado)',
    'typ_file': 'Usar un archivo TYP / typ.txt existente:',
    'typ_file_placeholder': 'Ruta a un archivo .typ o .txt',

    # Layers tab
    'layers_info': 'Seleccione las capas del proyecto para exportar al formato Garmin IMG',

    # Export tab (placeholders, tooltips)
    'output_folder_placeholder': 'Seleccione una carpeta para guardar el archivo IMG',
    'map_description_placeholder': 'Mapa creado con el complemento QGIS Garmin Export',
    'family_id_tip': 'Identificador de la familia de mapas. Debe ser único entre los mapas del dispositivo.',
    'map_id_tip': 'Número de tesela del mapa de 8 dígitos. Debe ser único.',
    'transparent_tip': 'Un mapa transparente se dibuja sobre otros mapas (p. ej., sobre un mapa base).',
    'routing_tip': 'Escribir datos NET/NOD (--route). Funciona si los datos contienen una red viaria.',

    # Styles tab
    'mapping_info': 'Configure la correspondencia entre las capas de QGIS y los tipos de objeto de Garmin',
    'mapping_placeholder': 'La asignación de estilos JSON se cargará automáticamente...',

    # Levels tab
    'levels_info': 'Los niveles definen en qué escalas son visibles los objetos en el dispositivo. '
                   'El nivel 0 (resolución 24) es el más detallado, el nivel 3 (resolución 18) es la '
                   'vista general. En la asignación de estilos, el parámetro "level" establece hasta '
                   'qué nivel permanece visible un objeto.',

    # Log widget
    'log_ready': 'Garmin Export Plugin cargado y listo',
    'log_hint': 'Los registros de operaciones aparecerán aquí...',
}
