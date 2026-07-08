# -*- coding: utf-8 -*-
"""
German translations for Garmin Export Plugin
Deutsche Übersetzungen für das Garmin-Export-Plugin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""

translations = {
    # Main interface
    'window_title': 'Garmin-IMG-Export - Vektordaten-Konverter',
    'no_vector_layers': 'Das Projekt enthält keine Vektorlayer zum Exportieren.\n\n'
                        'Fügen Sie dem Projekt Vektorlayer hinzu und versuchen Sie es erneut.',

    # Tabs
    'tab_layers': 'Layer',
    'tab_export': 'Export',
    'tab_tools': 'Werkzeuge',
    'tab_styles': 'Stile',
    'tab_typ': 'TYP',
    'tab_levels': 'Ebenen',
    'tab_tuning': 'Feineinstellung',

    # Layer selection
    'select_layers': 'Layer-Auswahl für den Export',
    'select_all_layers': 'Alle Layer auswählen',
    'deselect_all_layers': 'Auswahl aufheben',
    'refresh': 'Aktualisieren',
    'layers_list': 'Liste der Projektlayer:',

    # Export settings
    'output_files': 'Ausgabedateien',
    'output_folder': 'Ausgabeordner:',
    'output_file_name': 'Name der Kartendatei:',
    'browse': 'Durchsuchen...',
    'map_settings': 'Karteneinstellungen',
    'family_id': 'Family-ID:',
    'map_id': 'Map-ID:',
    'map_name': 'Kartenname:',
    'map_description': 'Beschreibung:',
    'transparent': 'Transparente Karte',
    'routing': 'Routing-Unterstützung',

    # Tools (mkgmap / splitter / java)
    'tools_mkgmap': 'mkgmap-Werkzeuge',
    'add_mkgmap': 'mkgmap hinzufügen',
    'download_mkgmap': 'mkgmap herunterladen',
    'add_splitter': 'splitter hinzufügen',
    'download_splitter': 'splitter herunterladen',
    'detect_java': 'Automatisch erkennen',
    'select_mkgmap': 'mkgmap.jar-Datei auswählen',
    'select_splitter': 'splitter.jar-Datei auswählen',
    'select_java': 'Java-Programmdatei auswählen',
    'jar_valid': 'Datei ist gültig',
    'jar_invalid': 'Datei ist keine gültige mkgmap.jar',
    'java_not_found': 'Java nicht gefunden. Bitte installieren Sie Java (JRE 8+).',
    'downloading': 'Herunterladen...',
    'download_in_progress': 'Ein Download läuft bereits.',
    'download_failed': 'Die Datei konnte nicht heruntergeladen werden',
    'download_complete': 'Download abgeschlossen',

    # Style mapping
    'style_mapping': 'JSON-Stilzuordnung',
    'load_mapping': 'Laden',
    'save_mapping': 'Speichern',
    'edit_mapping': 'Bearbeiten',
    'default_mapping': 'Standard',
    'mapping_title': 'Editor für JSON-Stilzuordnung',
    'mapping_description': 'Zuordnung zwischen QGIS-Layern und Garmin-Objekttypen konfigurieren',
    'validate_json': 'JSON prüfen',
    'json_valid': 'JSON-Syntax ist gültig!',
    'select_mapping_file': 'JSON-Zuordnungsdatei auswählen',
    'save_mapping_file': 'JSON-Zuordnungsdatei speichern',

    # TYP styling
    'typ_styling': 'Kartengestaltung (TYP)',
    'select_typ_file': 'TYP-Datei auswählen',

    # Levels
    'export_levels': 'Kartendarstellungsebenen',
    'level_0': 'Ebene 0 (detailliert)',
    'level_1': 'Ebene 1 (Haupt)',
    'level_2': 'Ebene 2 (mittel)',
    'level_3': 'Ebene 3 (Übersicht)',

    # Control buttons
    'compile_map': 'Karte kompilieren',
    'compiling': 'Kompilierung...',
    'cancel': 'Abbrechen',
    'clear_logs': 'Protokoll leeren',
    'save': 'Speichern',
    'close': 'Schließen',
    'details': 'Details',

    # Progress / results
    'progress': 'Fortschritt',
    'logs': 'Protokoll',
    'results': 'Ergebnisse',
    'layer': 'Layer',
    'status': 'Status',
    'message': 'Meldung',
    'geometry_type': 'Geometrietyp',
    'garmin_type': 'Garmin-Typ',
    'label_field': 'Beschriftungsfeld',

    # Common
    'success': 'Erfolg',
    'error': 'Fehler',
    'warning': 'Warnung',
    'info': 'Information',
    'confirmation': 'Bestätigung',
    'critical_error': 'Kritischer Fehler',
    'select_output_folder': 'Ausgabeordner für die IMG-Datei auswählen',

    # Errors
    'error_no_layers': 'Wählen Sie mindestens einen Layer zum Exportieren aus',
    'error_no_output_folder': 'Geben Sie einen Ausgabeordner an',
    'error_output_folder_missing': 'Der Ausgabeordner existiert nicht',
    'error_no_mkgmap': 'Geben Sie den Pfad zu mkgmap.jar an oder laden Sie es '
                       'mit der Schaltfläche "mkgmap herunterladen" herunter',
    'error_invalid_mkgmap': 'Die angegebene Datei ist keine gültige mkgmap.jar',
    'error_java_not_found': 'Java wurde im System nicht gefunden. Installieren Sie '
                            'Java (JRE 8+) und legen Sie den Pfad im Reiter "Werkzeuge" fest.',
    'error_typ_not_found': 'Die angegebene TYP-Datei wurde nicht gefunden',
    'error_invalid_json': 'Ungültiges JSON-Zuordnungsformat',
    'error_mkgmap_execution': 'mkgmap-Ausführungsfehler: {error}',
    'confirm_close': 'Kompilierung läuft. Anhalten und schließen?',

    # Author dialog
    'about_author': 'Über den Autor',
    'header_support': 'Unterstützen',
    'header_about_author': 'Über den Autor',
    'version': 'Version',
    'author': 'Autor',
    'contact': 'Kontakt',
    'year': 'Jahr',
    'organization': 'Organisation',
    'plugin_description': 'Professionelles Werkzeug zum Exportieren von QGIS-Daten '
                          'in Garmin-IMG-Karten über mkgmap',
    'multilingual_support': 'QGIS-Gestaltung, TYP-Erzeugung, mkgmap-Feineinstellung, '
                            'mehrsprachige Oberfläche',

    # Donation dialog
    'donation_title': '☕ Entwicklung unterstützen',
    'donation_window_title': '☕ Plugin-Entwicklung unterstützen',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 Garmin Export Plugin</b></p>
            <p>Dieses Plugin wird <b>kostenlos</b> entwickelt und gepflegt!</p>
            <p>Ihre Unterstützung hilft, das Plugin zu aktualisieren und zu verbessern.</p>
            <p style="color: #7f8c8d; font-size: 13px;">Jeder Kaffee zählt! ❤️</p>
        </div>''',
    'donation_kofi': '☕ Kaffee auf Ko-fi spendieren',
    'donation_tbank': '💳 Über T-Bank spenden',
    'donation_github': '💖 Auf GitHub sponsern',
    'donation_maybe_later': '✅ Vielleicht später',

    # Success messages
    'success_export_complete': 'Karte erfolgreich kompiliert! Datei gespeichert:',
    'success_mapping_saved': 'Zuordnung erfolgreich gespeichert',
    'success_mapping_loaded': 'Zuordnung erfolgreich geladen',

    # Tools tab (labels, placeholders, info)
    'mkgmap_path_label': 'Pfad zu mkgmap.jar:',
    'mkgmap_path_placeholder': 'mkgmap.jar auswählen oder herunterladen',
    'splitter_path_label': 'Pfad zu splitter.jar (optional):',
    'splitter_path_placeholder': 'splitter wird zum Zerlegen großer Karten benötigt (optional)',
    'java_path_label': 'Pfad zu Java:',
    'java_path_placeholder': 'Leer = java aus PATH; die Schaltfläche rechts erkennt es',
    'tools_info': 'Die QGIS-Regeln verbieten das Bündeln von mkgmap.jar mit dem Plugin. '
                  'Klicken Sie auf "mkgmap herunterladen" – das Plugin lädt die neueste '
                  'Version von mkgmap.org.uk (oder vom Yandex.Disk-Backup) herunter, oder '
                  'geben Sie mit "mkgmap hinzufügen" Ihre eigene Datei an.',
    'support_tip': 'Unterstützen Sie die Plugin-Entwicklung!',
    'author_tip': 'Informationen zum Plugin-Autor',

    # Tuning tab - group titles
    'map_params_group': 'Kartenparameter (mkgmap)',
    'generalization_group': 'Generalisierung',
    'performance_group': 'Leistung (Feineinstellung)',
    'logging_group': 'Protokollierung und Fehlersuche',

    # Tuning tab - options
    'code_page_label': 'Codepage der Beschriftungen:',
    'draw_priority_label': 'Zeichenpriorität (--draw-priority):',
    'draw_priority_tip': '25 ist Standard. Höher = die Karte wird über andere gezeichnet. '
                         'Für transparente Overlay-Karten mehr als 25 verwenden.',
    'opt_index': 'Adressindex für die Suche (--index)',
    'opt_add_pois': 'POIs aus Polygonen erstellen (--add-pois-to-areas)',
    'opt_lower_case': 'Kleinbuchstaben in Beschriftungen zulassen (--lower-case)',
    'opt_order_area': 'Kleine Polygone über große (--order-by-decreasing-area)',
    'reduce_density_label': 'Linienvereinfachung, m (--reduce-point-density):',
    'reduce_density_polygon_label': 'Polygonvereinfachung, m (--reduce-point-density-polygon):',
    'min_polygon_label': 'Min. Polygongröße (--min-size-polygon):',
    'min_polygon_tip': 'Kleinere Polygone werden entfernt. 8-15 empfohlen.',
    'java_heap_label': 'Java-Speicher, GB (-Xmx):',
    'java_heap_tip': 'mkgmap benötigt ~500 MB pro Thread. Für 8 Kerne 4 GB einstellen.',
    'max_jobs_label': 'Threads (--max-jobs):',
    'max_jobs_tip': '0 = mkgmap entscheidet anhand von Kernen und Speicher.',
    'opt_mkgmap_log': 'mkgmap.log-Datei im Ausgabeordner führen',
    'opt_verbose': 'Ausführliches Protokoll (INFO-Ebene)',
    'opt_keep_temp': 'Zwischendateien (MP, TYP) im Ausgabeordner behalten',
    'extra_args_label': 'Zusätzliche mkgmap-Argumente:',
    'extra_args_placeholder': 'z. B.: --precomp-sea=C:/sea.zip --generate-sea',
    'value_auto': 'auto',
    'value_auto_default': 'auto (2.6)',

    # Code pages
    'cp_1251': 'CP1251 (Kyrillisch)',
    'cp_1252': 'CP1252 (Latin-1, Westeuropa)',
    'cp_1250': 'CP1250 (Mitteleuropa)',
    'cp_1253': 'CP1253 (Griechisch)',
    'cp_1254': 'CP1254 (Türkisch)',
    'cp_1257': 'CP1257 (Baltisch)',
    'cp_65001': 'UTF-8 / Unicode (alle Sprachen)',
    'cp_1255': 'CP1255 (Hebräisch)',
    'cp_1256': 'CP1256 (Arabisch)',
    'cp_1258': 'CP1258 (Vietnamesisch)',
    'cp_874': 'CP874 (Thai)',
    'cp_932': 'CP932 (Japanisch, Shift-JIS)',
    'cp_936': 'CP936 (Vereinfachtes Chinesisch, GBK)',
    'cp_949': 'CP949 (Koreanisch)',
    'cp_950': 'CP950 (Traditionelles Chinesisch, Big5)',
    'cp_866': 'CP866 (Kyrillisch, DOS)',
    'cp_850': 'CP850 (Westeuropäisch, DOS)',
    'cp_852': 'CP852 (Mitteleuropäisch, DOS)',
    # TYP tab
    'typ_info': 'Eine TYP-Datei legt fest, wie Objekte auf dem Garmin-Gerät aussehen: '
                'Polygonfarben, Linienbreiten, Punktsymbole. Das Plugin kann eine TYP '
                'automatisch aus der aktuellen QGIS-Layer-Symbolik erzeugen – die Karte '
                'auf dem Navigationsgerät sieht dann aus wie in QGIS.',
    'typ_none': 'Standard-Garmin-Stil (ohne TYP)',
    'typ_generate': 'TYP aus QGIS-Stilen erzeugen (empfohlen)',
    'typ_file': 'Vorhandene TYP-/typ.txt-Datei verwenden:',
    'typ_file_placeholder': 'Pfad zu einer .typ- oder .txt-Datei',

    # Layers tab
    'layers_info': 'Wählen Sie Projektlayer zum Export in das Garmin-IMG-Format aus',

    # Export tab (placeholders, tooltips)
    'output_folder_placeholder': 'Ordner zum Speichern der IMG-Datei auswählen',
    'map_description_placeholder': 'Mit dem QGIS Garmin Export Plugin erstellte Karte',
    'family_id_tip': 'Kennung der Kartenfamilie. Muss unter den Karten auf dem Gerät eindeutig sein.',
    'map_id_tip': '8-stellige Kartenkachelnummer. Muss eindeutig sein.',
    'transparent_tip': 'Eine transparente Karte wird über andere Karten gezeichnet (z. B. über eine Basiskarte).',
    'routing_tip': 'NET/NOD-Daten schreiben (--route). Funktioniert, wenn die Daten ein Straßennetz enthalten.',

    # Styles tab
    'mapping_info': 'Konfigurieren Sie die Zuordnung zwischen QGIS-Layern und Garmin-Objekttypen',
    'mapping_placeholder': 'Die JSON-Stilzuordnung wird automatisch geladen...',

    # Levels tab
    'levels_info': 'Ebenen legen fest, bei welchem Maßstab Objekte auf dem Gerät sichtbar sind. '
                   'Ebene 0 (Auflösung 24) ist am detailliertesten, Ebene 3 (Auflösung 18) ist '
                   'die Übersicht. In der Stilzuordnung legt der Parameter "level" fest, bis zu '
                   'welcher Ebene ein Objekt sichtbar bleibt.',

    # Log widget
    'log_ready': 'Garmin Export Plugin geladen und bereit',
    'log_hint': 'Vorgangsprotokolle erscheinen hier...',
}
