# -*- coding: utf-8 -*-
"""
Hindi translations for Garmin Export Plugin
Garmin Export प्लगइन के लिए हिन्दी अनुवाद

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
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
}
