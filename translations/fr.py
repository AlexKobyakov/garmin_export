# -*- coding: utf-8 -*-
"""
French translations for Garmin Export Plugin
Traductions françaises pour l'extension Garmin Export

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
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

    # Tools tab (labels, placeholders, info)
    'mkgmap_path_label': 'Chemin vers mkgmap.jar :',
    'mkgmap_path_placeholder': 'Sélectionnez ou téléchargez mkgmap.jar',
    'splitter_path_label': 'Chemin vers splitter.jar (facultatif) :',
    'splitter_path_placeholder': 'splitter est nécessaire pour découper les grandes cartes (facultatif)',
    'java_path_label': 'Chemin vers Java :',
    'java_path_placeholder': 'Vide = java depuis le PATH ; le bouton à droite le détecte',
    'tools_info': 'Les règles de QGIS interdisent d\'inclure mkgmap.jar dans l\'extension. '
                  'Cliquez sur « Télécharger mkgmap » et l\'extension récupérera la dernière '
                  'version depuis mkgmap.org.uk (ou depuis la sauvegarde Yandex.Disk), ou '
                  'indiquez votre propre fichier avec « Ajouter mkgmap ».',
    'support_tip': 'Soutenez le développement de l\'extension !',
    'author_tip': 'Informations sur l\'auteur de l\'extension',

    # Tuning tab - group titles
    'map_params_group': 'Paramètres de la carte (mkgmap)',
    'generalization_group': 'Généralisation',
    'performance_group': 'Performance (réglages)',
    'logging_group': 'Journalisation et débogage',

    # Tuning tab - options
    'code_page_label': 'Page de codes des étiquettes :',
    'draw_priority_label': 'Priorité de dessin (--draw-priority) :',
    'draw_priority_tip': '25 est la valeur standard. Plus élevé = la carte est dessinée par-dessus '
                         'les autres. Pour les cartes de superposition transparentes, utilisez plus de 25.',
    'opt_index': 'Index d\'adresses pour la recherche (--index)',
    'opt_add_pois': 'Créer des POI à partir des polygones (--add-pois-to-areas)',
    'opt_lower_case': 'Autoriser les minuscules dans les étiquettes (--lower-case)',
    'opt_order_area': 'Petits polygones au-dessus des grands (--order-by-decreasing-area)',
    'reduce_density_label': 'Simplification des lignes, m (--reduce-point-density) :',
    'reduce_density_polygon_label': 'Simplification des polygones, m (--reduce-point-density-polygon) :',
    'min_polygon_label': 'Taille min. de polygone (--min-size-polygon) :',
    'min_polygon_tip': 'Les polygones plus petits sont supprimés. 8-15 recommandé.',
    'java_heap_label': 'Mémoire Java, Go (-Xmx) :',
    'java_heap_tip': 'mkgmap nécessite ~500 Mo par thread. Pour 8 cœurs, mettez 4 Go.',
    'max_jobs_label': 'Threads (--max-jobs) :',
    'max_jobs_tip': '0 = mkgmap décide selon les cœurs et la mémoire.',
    'opt_mkgmap_log': 'Tenir un fichier mkgmap.log dans le dossier de sortie',
    'opt_verbose': 'Journal détaillé (niveau INFO)',
    'opt_keep_temp': 'Conserver les fichiers intermédiaires (MP, TYP) dans le dossier de sortie',
    'extra_args_label': 'Arguments mkgmap supplémentaires :',
    'extra_args_placeholder': 'ex. : --precomp-sea=C:/sea.zip --generate-sea',
    'value_auto': 'auto',
    'value_auto_default': 'auto (2.6)',

    # Code pages
    'cp_1251': 'CP1251 (cyrillique)',
    'cp_1252': 'CP1252 (Latin-1, Europe de l\'Ouest)',
    'cp_1250': 'CP1250 (Europe centrale)',
    'cp_1253': 'CP1253 (grec)',
    'cp_1254': 'CP1254 (turc)',
    'cp_1257': 'CP1257 (balte)',
    'cp_65001': 'UTF-8 / Unicode (toutes les langues)',
    'cp_1255': 'CP1255 (hébreu)',
    'cp_1256': 'CP1256 (arabe)',
    'cp_1258': 'CP1258 (vietnamien)',
    'cp_874': 'CP874 (thaï)',
    'cp_932': 'CP932 (japonais, Shift-JIS)',
    'cp_936': 'CP936 (chinois simplifié, GBK)',
    'cp_949': 'CP949 (coréen)',
    'cp_950': 'CP950 (chinois traditionnel, Big5)',
    'cp_866': 'CP866 (cyrillique, DOS)',
    'cp_850': "CP850 (Europe de l'Ouest, DOS)",
    'cp_852': 'CP852 (Europe centrale, DOS)',
    # TYP tab
    'typ_info': 'Un fichier TYP définit l\'apparence des objets sur l\'appareil Garmin : '
                'couleurs des polygones, épaisseur des lignes, icônes des points. L\'extension '
                'peut générer un TYP automatiquement à partir de la symbologie actuelle des '
                'couches QGIS — la carte sur le GPS ressemblera à celle de QGIS.',
    'typ_none': 'Style Garmin standard (sans TYP)',
    'typ_generate': 'Générer un TYP à partir des styles QGIS (recommandé)',
    'typ_file': 'Utiliser un fichier TYP / typ.txt existant :',
    'typ_file_placeholder': 'Chemin vers un fichier .typ ou .txt',

    # Layers tab
    'layers_info': 'Sélectionnez les couches du projet à exporter au format Garmin IMG',

    # Export tab (placeholders, tooltips)
    'output_folder_placeholder': 'Sélectionnez un dossier pour enregistrer le fichier IMG',
    'map_description_placeholder': 'Carte créée avec l\'extension QGIS Garmin Export',
    'family_id_tip': 'Identifiant de la famille de cartes. Doit être unique parmi les cartes de l\'appareil.',
    'map_id_tip': 'Numéro de tuile de carte à 8 chiffres. Doit être unique.',
    'transparent_tip': 'Une carte transparente est dessinée par-dessus d\'autres cartes (ex. : par-dessus un fond de carte).',
    'routing_tip': 'Écrire les données NET/NOD (--route). Fonctionne si les données contiennent un réseau routier.',

    # Styles tab
    'mapping_info': 'Configurez la correspondance entre les couches QGIS et les types d\'objets Garmin',
    'mapping_placeholder': 'La correspondance de styles JSON sera chargée automatiquement...',

    # Levels tab
    'levels_info': 'Les niveaux définissent à quelles échelles les objets sont visibles sur l\'appareil. '
                   'Le niveau 0 (résolution 24) est le plus détaillé, le niveau 3 (résolution 18) est la '
                   'vue d\'ensemble. Dans la correspondance de styles, le paramètre « level » définit '
                   'jusqu\'à quel niveau un objet reste visible.',

    # Log widget
    'log_ready': 'Garmin Export Plugin chargé et prêt',
    'log_hint': 'Les journaux des opérations apparaîtront ici...',
}
