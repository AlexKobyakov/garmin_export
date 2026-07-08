# -*- coding: utf-8 -*-
"""
French translations for Garmin Export Plugin
Traductions françaises pour l'extension Garmin Export

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

translations = {
    # Main interface
    'window_title': 'Export Garmin IMG - Convertisseur de données vectorielles',
    'no_vector_layers': 'Le projet ne contient aucune couche vectorielle à exporter.\n\n'
                        'Ajoutez des couches vectorielles au projet et réessayez.',

    # Tabs
    'tab_layers': 'Couches',
    'tab_export': 'Export',
    'tab_tools': 'Outils',
    'tab_styles': 'Styles',
    'tab_typ': 'TYP',
    'tab_levels': 'Niveaux',
    'tab_tuning': 'Réglages',

    # Layer selection
    'select_layers': 'Sélection des couches à exporter',
    'select_all_layers': 'Tout sélectionner',
    'deselect_all_layers': 'Tout désélectionner',
    'refresh': 'Actualiser',
    'layers_list': 'Liste des couches du projet :',

    # Export settings
    'output_files': 'Fichiers de sortie',
    'output_folder': 'Dossier de sortie :',
    'output_file_name': 'Nom du fichier de carte :',
    'browse': 'Parcourir...',
    'map_settings': 'Paramètres de la carte',
    'family_id': 'Family ID :',
    'map_id': 'Map ID :',
    'map_name': 'Nom de la carte :',
    'map_description': 'Description :',
    'transparent': 'Carte transparente',
    'routing': 'Prise en charge du routage',

    # Tools (mkgmap / splitter / java)
    'tools_mkgmap': 'Outils mkgmap',
    'add_mkgmap': 'Ajouter mkgmap',
    'download_mkgmap': 'Télécharger mkgmap',
    'add_splitter': 'Ajouter splitter',
    'download_splitter': 'Télécharger splitter',
    'detect_java': 'Détection automatique',
    'select_mkgmap': 'Sélectionner le fichier mkgmap.jar',
    'select_splitter': 'Sélectionner le fichier splitter.jar',
    'select_java': 'Sélectionner l\'exécutable java',
    'jar_valid': 'le fichier est valide',
    'jar_invalid': 'Le fichier n\'est pas un mkgmap.jar valide',
    'java_not_found': 'Java introuvable. Veuillez installer Java (JRE 8+).',
    'downloading': 'Téléchargement...',
    'download_in_progress': 'Un téléchargement est déjà en cours.',
    'download_failed': 'Échec du téléchargement du fichier',
    'download_complete': 'Téléchargement terminé',

    # Style mapping
    'style_mapping': 'Correspondance de styles JSON',
    'load_mapping': 'Charger',
    'save_mapping': 'Enregistrer',
    'edit_mapping': 'Modifier',
    'default_mapping': 'Par défaut',
    'mapping_title': 'Éditeur de correspondance de styles JSON',
    'mapping_description': 'Configurez la correspondance entre les couches QGIS et les types d\'objets Garmin',
    'validate_json': 'Valider le JSON',
    'json_valid': 'La syntaxe JSON est valide !',
    'select_mapping_file': 'Sélectionner le fichier de correspondance JSON',
    'save_mapping_file': 'Enregistrer le fichier de correspondance JSON',

    # TYP styling
    'typ_styling': 'Style de la carte (TYP)',
    'select_typ_file': 'Sélectionner le fichier TYP',

    # Levels
    'export_levels': 'Niveaux d\'affichage de la carte',
    'level_0': 'Niveau 0 (détaillé)',
    'level_1': 'Niveau 1 (principal)',
    'level_2': 'Niveau 2 (moyen)',
    'level_3': 'Niveau 3 (vue d\'ensemble)',

    # Control buttons
    'compile_map': 'Compiler la carte',
    'compiling': 'Compilation...',
    'cancel': 'Annuler',
    'clear_logs': 'Effacer les journaux',
    'save': 'Enregistrer',
    'close': 'Fermer',
    'details': 'Détails',

    # Progress / results
    'progress': 'Progression',
    'logs': 'Journaux',
    'results': 'Résultats',
    'layer': 'Couche',
    'status': 'État',
    'message': 'Message',
    'geometry_type': 'Type de géométrie',
    'garmin_type': 'Type Garmin',
    'label_field': 'Champ d\'étiquette',

    # Common
    'success': 'Succès',
    'error': 'Erreur',
    'warning': 'Avertissement',
    'info': 'Information',
    'confirmation': 'Confirmation',
    'critical_error': 'Erreur critique',
    'select_output_folder': 'Sélectionnez le dossier de sortie pour le fichier IMG',

    # Errors
    'error_no_layers': 'Sélectionnez au moins une couche à exporter',
    'error_no_output_folder': 'Indiquez un dossier de sortie',
    'error_output_folder_missing': 'Le dossier de sortie n\'existe pas',
    'error_no_mkgmap': 'Indiquez le chemin vers mkgmap.jar ou téléchargez-le '
                       'avec le bouton « Télécharger mkgmap »',
    'error_invalid_mkgmap': 'Le fichier indiqué n\'est pas un mkgmap.jar valide',
    'error_java_not_found': 'Java introuvable sur le système. Installez Java (JRE 8+) '
                            'et définissez le chemin dans l\'onglet « Outils ».',
    'error_typ_not_found': 'Le fichier TYP indiqué est introuvable',
    'error_invalid_json': 'Format de correspondance JSON non valide',
    'error_mkgmap_execution': 'Erreur d\'exécution de mkgmap : {error}',
    'confirm_close': 'Compilation en cours. Arrêter et fermer ?',

    # Author dialog
    'about_author': 'À propos de l\'auteur',
    'header_support': 'Soutenir',
    'header_about_author': 'À propos de l\'auteur',
    'version': 'Version',
    'author': 'Auteur',
    'contact': 'Contact',
    'year': 'Année',
    'organization': 'Organisation',
    'plugin_description': 'Outil professionnel pour exporter les données QGIS '
                          'vers des cartes Garmin IMG via mkgmap',
    'multilingual_support': 'Style depuis QGIS, génération de TYP, réglage fin de mkgmap, '
                            'interface multilingue',

    # Donation dialog
    'donation_title': '☕ Soutenir le développement',
    'donation_window_title': '☕ Soutenez le développement de l\'extension',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 Garmin Export Plugin</b></p>
            <p>cette extension est développée et maintenue <b>gratuitement</b> !</p>
            <p>Votre soutien aide à mettre à jour et à améliorer l\'extension.</p>
            <p style="color: #7f8c8d; font-size: 13px;">Chaque café compte ! ❤️</p>
        </div>''',
    'donation_kofi': '☕ Offrir un café sur Ko-fi',
    'donation_tbank': '💳 Faire un don via T-Bank',
    'donation_github': '💖 Sponsoriser sur GitHub',
    'donation_maybe_later': '✅ Peut-être plus tard',

    # Success messages
    'success_export_complete': 'Carte compilée avec succès ! Fichier enregistré :',
    'success_mapping_saved': 'Correspondance enregistrée avec succès',
    'success_mapping_loaded': 'Correspondance chargée avec succès',
}
