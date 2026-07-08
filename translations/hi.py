# -*- coding: utf-8 -*-
"""
Hindi translations for Garmin Export Plugin
Garmin Export प्लगइन के लिए हिन्दी अनुवाद

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""

translations = {
    # Main interface
    'window_title': 'Garmin IMG निर्यात - वेक्टर डेटा कनवर्टर',
    'no_vector_layers': 'परियोजना में निर्यात करने के लिए कोई वेक्टर लेयर नहीं है।\n\n'
                        'परियोजना में वेक्टर लेयर जोड़ें और पुनः प्रयास करें।',

    # Tabs
    'tab_layers': 'लेयर',
    'tab_export': 'निर्यात',
    'tab_tools': 'उपकरण',
    'tab_styles': 'शैलियाँ',
    'tab_typ': 'TYP',
    'tab_levels': 'स्तर',
    'tab_tuning': 'फ़ाइन-ट्यूनिंग',

    # Layer selection
    'select_layers': 'निर्यात के लिए लेयर चयन',
    'select_all_layers': 'सभी लेयर चुनें',
    'deselect_all_layers': 'चयन हटाएँ',
    'refresh': 'ताज़ा करें',
    'layers_list': 'परियोजना लेयर सूची:',

    # Export settings
    'output_files': 'आउटपुट फ़ाइलें',
    'output_folder': 'आउटपुट फ़ोल्डर:',
    'output_file_name': 'मानचित्र फ़ाइल का नाम:',
    'browse': 'ब्राउज़ करें...',
    'map_settings': 'मानचित्र सेटिंग्स',
    'family_id': 'Family ID:',
    'map_id': 'Map ID:',
    'map_name': 'मानचित्र नाम:',
    'map_description': 'विवरण:',
    'transparent': 'पारदर्शी मानचित्र',
    'routing': 'रूटिंग समर्थन',

    # Tools (mkgmap / splitter / java)
    'tools_mkgmap': 'mkgmap उपकरण',
    'add_mkgmap': 'mkgmap जोड़ें',
    'download_mkgmap': 'mkgmap डाउनलोड करें',
    'add_splitter': 'splitter जोड़ें',
    'download_splitter': 'splitter डाउनलोड करें',
    'detect_java': 'स्वतः पहचानें',
    'select_mkgmap': 'mkgmap.jar फ़ाइल चुनें',
    'select_splitter': 'splitter.jar फ़ाइल चुनें',
    'select_java': 'java निष्पादन योग्य फ़ाइल चुनें',
    'jar_valid': 'फ़ाइल मान्य है',
    'jar_invalid': 'फ़ाइल एक मान्य mkgmap.jar नहीं है',
    'java_not_found': 'Java नहीं मिला। कृपया Java (JRE 8+) स्थापित करें।',
    'downloading': 'डाउनलोड हो रहा है...',
    'download_in_progress': 'एक डाउनलोड पहले से चल रहा है।',
    'download_failed': 'फ़ाइल डाउनलोड करने में विफल',
    'download_complete': 'डाउनलोड पूर्ण',

    # Style mapping
    'style_mapping': 'JSON शैली मैपिंग',
    'load_mapping': 'लोड करें',
    'save_mapping': 'सहेजें',
    'edit_mapping': 'संपादित करें',
    'default_mapping': 'डिफ़ॉल्ट',
    'mapping_title': 'JSON शैली मैपिंग संपादक',
    'mapping_description': 'QGIS लेयर और Garmin ऑब्जेक्ट प्रकारों के बीच मैपिंग कॉन्फ़िगर करें',
    'validate_json': 'JSON सत्यापित करें',
    'json_valid': 'JSON वाक्यविन्यास मान्य है!',
    'select_mapping_file': 'JSON मैपिंग फ़ाइल चुनें',
    'save_mapping_file': 'JSON मैपिंग फ़ाइल सहेजें',

    # TYP styling
    'typ_styling': 'मानचित्र शैली (TYP)',
    'select_typ_file': 'TYP फ़ाइल चुनें',

    # Levels
    'export_levels': 'मानचित्र प्रदर्शन स्तर',
    'level_0': 'स्तर 0 (विस्तृत)',
    'level_1': 'स्तर 1 (मुख्य)',
    'level_2': 'स्तर 2 (मध्यम)',
    'level_3': 'स्तर 3 (अवलोकन)',

    # Control buttons
    'compile_map': 'मानचित्र संकलित करें',
    'compiling': 'संकलन हो रहा है...',
    'cancel': 'रद्द करें',
    'clear_logs': 'लॉग साफ़ करें',
    'save': 'सहेजें',
    'close': 'बंद करें',
    'details': 'विवरण',

    # Progress / results
    'progress': 'प्रगति',
    'logs': 'लॉग',
    'results': 'परिणाम',
    'layer': 'लेयर',
    'status': 'स्थिति',
    'message': 'संदेश',
    'geometry_type': 'ज्यामिति प्रकार',
    'garmin_type': 'Garmin प्रकार',
    'label_field': 'लेबल फ़ील्ड',

    # Common
    'success': 'सफलता',
    'error': 'त्रुटि',
    'warning': 'चेतावनी',
    'info': 'जानकारी',
    'confirmation': 'पुष्टिकरण',
    'critical_error': 'गंभीर त्रुटि',
    'select_output_folder': 'IMG फ़ाइल के लिए आउटपुट फ़ोल्डर चुनें',

    # Errors
    'error_no_layers': 'निर्यात के लिए कम से कम एक लेयर चुनें',
    'error_no_output_folder': 'आउटपुट फ़ोल्डर निर्दिष्ट करें',
    'error_output_folder_missing': 'आउटपुट फ़ोल्डर मौजूद नहीं है',
    'error_no_mkgmap': 'mkgmap.jar का पथ निर्दिष्ट करें या इसे '
                       '"mkgmap डाउनलोड करें" बटन से डाउनलोड करें',
    'error_invalid_mkgmap': 'निर्दिष्ट फ़ाइल एक मान्य mkgmap.jar नहीं है',
    'error_java_not_found': 'सिस्टम में Java नहीं मिला। Java (JRE 8+) स्थापित करें '
                            'और "उपकरण" टैब में पथ सेट करें।',
    'error_typ_not_found': 'निर्दिष्ट TYP फ़ाइल नहीं मिली',
    'error_invalid_json': 'अमान्य JSON मैपिंग प्रारूप',
    'error_mkgmap_execution': 'mkgmap निष्पादन त्रुटि: {error}',
    'confirm_close': 'संकलन जारी है। रोकें और बंद करें?',

    # Author dialog
    'about_author': 'लेखक के बारे में',
    'header_support': 'सहयोग',
    'header_about_author': 'लेखक के बारे में',
    'version': 'संस्करण',
    'author': 'लेखक',
    'contact': 'संपर्क',
    'year': 'वर्ष',
    'organization': 'संगठन',
    'plugin_description': 'mkgmap के माध्यम से QGIS डेटा को '
                          'Garmin IMG मानचित्रों में निर्यात करने का पेशेवर उपकरण',
    'multilingual_support': 'QGIS शैली, TYP निर्माण, mkgmap फ़ाइन-ट्यूनिंग, '
                            'बहुभाषी इंटरफ़ेस',

    # Donation dialog
    'donation_title': '☕ विकास का समर्थन करें',
    'donation_window_title': '☕ प्लगइन विकास का समर्थन करें',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 Garmin Export Plugin</b></p>
            <p>यह प्लगइन <b>मुफ़्त</b> में विकसित और अनुरक्षित किया जाता है!</p>
            <p>आपका समर्थन प्लगइन को अपडेट और बेहतर बनाने में मदद करता है।</p>
            <p style="color: #7f8c8d; font-size: 13px;">हर कॉफ़ी मायने रखती है! ❤️</p>
        </div>''',
    'donation_kofi': '☕ Ko-fi पर कॉफ़ी खरीदें',
    'donation_tbank': '💳 T-Bank के माध्यम से दान करें',
    'donation_github': '💖 GitHub पर प्रायोजित करें',
    'donation_maybe_later': '✅ शायद बाद में',

    # Success messages
    'success_export_complete': 'मानचित्र सफलतापूर्वक संकलित हुआ! फ़ाइल सहेजी गई:',
    'success_mapping_saved': 'मैपिंग सफलतापूर्वक सहेजी गई',
    'success_mapping_loaded': 'मैपिंग सफलतापूर्वक लोड हुई',

    # Tools tab (labels, placeholders, info)
    'mkgmap_path_label': 'mkgmap.jar का पथ:',
    'mkgmap_path_placeholder': 'mkgmap.jar चुनें या डाउनलोड करें',
    'splitter_path_label': 'splitter.jar का पथ (वैकल्पिक):',
    'splitter_path_placeholder': 'बड़े मानचित्रों को विभाजित करने के लिए splitter आवश्यक है (वैकल्पिक)',
    'java_path_label': 'Java का पथ:',
    'java_path_placeholder': 'खाली = PATH से java; दाईं ओर का बटन इसे खोज लेगा',
    'tools_info': 'QGIS नियम प्लगइन में mkgmap.jar शामिल करने पर रोक लगाते हैं। '
                  '"mkgmap डाउनलोड करें" पर क्लिक करें — प्लगइन नवीनतम संस्करण '
                  'mkgmap.org.uk से (या Yandex.Disk बैकअप से) प्राप्त करेगा, या '
                  '"mkgmap जोड़ें" बटन से अपनी फ़ाइल निर्दिष्ट करें।',
    'support_tip': 'प्लगइन विकास का समर्थन करें!',
    'author_tip': 'प्लगइन लेखक की जानकारी',

    # Tuning tab - group titles
    'map_params_group': 'मानचित्र पैरामीटर (mkgmap)',
    'generalization_group': 'सामान्यीकरण',
    'performance_group': 'प्रदर्शन (ट्यूनिंग)',
    'logging_group': 'लॉगिंग और डिबगिंग',

    # Tuning tab - options
    'code_page_label': 'लेबल कोड पेज:',
    'draw_priority_label': 'ड्रॉ प्राथमिकता (--draw-priority):',
    'draw_priority_tip': '25 मानक है। अधिक = मानचित्र अन्य के ऊपर बनाया जाता है। '
                         'पारदर्शी ओवरले मानचित्रों के लिए 25 से अधिक रखें।',
    'opt_index': 'खोज के लिए पता सूचकांक (--index)',
    'opt_add_pois': 'बहुभुजों से POI बनाएँ (--add-pois-to-areas)',
    'opt_lower_case': 'लेबल में छोटे अक्षर अनुमत करें (--lower-case)',
    'opt_order_area': 'छोटे बहुभुज बड़ों के ऊपर (--order-by-decreasing-area)',
    'reduce_density_label': 'रेखा सरलीकरण, मी (--reduce-point-density):',
    'reduce_density_polygon_label': 'बहुभुज सरलीकरण, मी (--reduce-point-density-polygon):',
    'min_polygon_label': 'न्यूनतम बहुभुज आकार (--min-size-polygon):',
    'min_polygon_tip': 'इससे छोटे बहुभुज हटा दिए जाते हैं। 8-15 अनुशंसित।',
    'java_heap_label': 'Java मेमोरी, GB (-Xmx):',
    'java_heap_tip': 'mkgmap को प्रति थ्रेड ~500 MB चाहिए। 8 कोर के लिए 4 GB रखें।',
    'max_jobs_label': 'थ्रेड (--max-jobs):',
    'max_jobs_tip': '0 = mkgmap कोर और मेमोरी के आधार पर तय करेगा।',
    'opt_mkgmap_log': 'आउटपुट फ़ोल्डर में mkgmap.log लॉग फ़ाइल रखें',
    'opt_verbose': 'विस्तृत लॉग (INFO स्तर)',
    'opt_keep_temp': 'मध्यवर्ती फ़ाइलें (MP, TYP) आउटपुट फ़ोल्डर में रखें',
    'extra_args_label': 'अतिरिक्त mkgmap तर्क:',
    'extra_args_placeholder': 'उदा.: --precomp-sea=C:/sea.zip --generate-sea',
    'value_auto': 'स्वतः',
    'value_auto_default': 'स्वतः (2.6)',

    # Code pages
    'cp_1251': 'CP1251 (सिरिलिक)',
    'cp_1252': 'CP1252 (Latin-1, पश्चिमी यूरोप)',
    'cp_1250': 'CP1250 (मध्य यूरोप)',
    'cp_1253': 'CP1253 (यूनानी)',
    'cp_1254': 'CP1254 (तुर्की)',
    'cp_1257': 'CP1257 (बाल्टिक)',
    'cp_65001': 'UTF-8 / Unicode (सभी भाषाएँ)',
    'cp_1255': 'CP1255 (हिब्रू)',
    'cp_1256': 'CP1256 (अरबी)',
    'cp_1258': 'CP1258 (वियतनामी)',
    'cp_874': 'CP874 (थाई)',
    'cp_932': 'CP932 (जापानी, Shift-JIS)',
    'cp_936': 'CP936 (सरलीकृत चीनी, GBK)',
    'cp_949': 'CP949 (कोरियाई)',
    'cp_950': 'CP950 (पारंपरिक चीनी, Big5)',
    'cp_866': 'CP866 (सिरिलिक, DOS)',
    'cp_850': 'CP850 (पश्चिमी यूरोप, DOS)',
    'cp_852': 'CP852 (मध्य यूरोप, DOS)',
    # TYP tab
    'typ_info': 'TYP फ़ाइल Garmin उपकरण पर वस्तुओं का रूप निर्धारित करती है: '
                'बहुभुज रंग, रेखा चौड़ाई, बिंदु चिह्न। प्लगइन वर्तमान QGIS लेयर '
                'प्रतीक विज्ञान से TYP स्वतः उत्पन्न कर सकता है — नेविगेटर पर मानचित्र '
                'QGIS जैसा दिखेगा।',
    'typ_none': 'मानक Garmin शैली (TYP के बिना)',
    'typ_generate': 'QGIS शैलियों से TYP उत्पन्न करें (अनुशंसित)',
    'typ_file': 'मौजूदा TYP / typ.txt फ़ाइल का उपयोग करें:',
    'typ_file_placeholder': '.typ या .txt फ़ाइल का पथ',

    # Layers tab
    'layers_info': 'Garmin IMG प्रारूप में निर्यात के लिए परियोजना लेयर चुनें',

    # Export tab (placeholders, tooltips)
    'output_folder_placeholder': 'IMG फ़ाइल सहेजने के लिए फ़ोल्डर चुनें',
    'map_description_placeholder': 'QGIS Garmin Export प्लगइन से बनाया गया मानचित्र',
    'family_id_tip': 'मानचित्र परिवार पहचानकर्ता। उपकरण के मानचित्रों में अद्वितीय होना चाहिए।',
    'map_id_tip': '8-अंकीय मानचित्र टाइल संख्या। अद्वितीय होनी चाहिए।',
    'transparent_tip': 'पारदर्शी मानचित्र अन्य मानचित्रों के ऊपर बनाया जाता है (उदा. आधार मानचित्र के ऊपर)।',
    'routing_tip': 'NET/NOD डेटा लिखें (--route)। तब काम करता है जब डेटा में सड़क नेटवर्क हो।',

    # Styles tab
    'mapping_info': 'QGIS लेयर और Garmin वस्तु प्रकारों के बीच पत्राचार कॉन्फ़िगर करें',
    'mapping_placeholder': 'JSON शैली मैपिंग स्वतः लोड होगी...',

    # Levels tab
    'levels_info': 'स्तर निर्धारित करते हैं कि किन पैमानों पर वस्तुएँ उपकरण पर दिखती हैं। '
                   'स्तर 0 (रिज़ॉल्यूशन 24) सबसे विस्तृत है, स्तर 3 (रिज़ॉल्यूशन 18) अवलोकन है। '
                   'शैली मैपिंग में "level" पैरामीटर निर्धारित करता है कि वस्तु किस स्तर तक दिखती है।',

    # Log widget
    'log_ready': 'Garmin Export Plugin लोड हो गया और तैयार है',
    'log_hint': 'संचालन लॉग यहाँ दिखाई देंगे...',
}
