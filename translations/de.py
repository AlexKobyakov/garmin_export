# -*- coding: utf-8 -*-
"""
German translations for Garmin Export Plugin
Deutsche Übersetzungen für das Garmin-Export-Plugin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
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
}
