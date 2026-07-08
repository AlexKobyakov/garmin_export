# -*- coding: utf-8 -*-
"""
Arabic translations for Garmin Export Plugin
الترجمة العربية لإضافة Garmin Export

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

translations = {
    # Main interface
    'window_title': 'التصدير إلى Garmin IMG - محوّل البيانات المتّجهة',
    'no_vector_layers': 'لا يحتوي المشروع على طبقات متّجهة للتصدير.\n\n'
                        'أضف طبقات متّجهة إلى المشروع وحاول مرة أخرى.',

    # Tabs
    'tab_layers': 'الطبقات',
    'tab_export': 'التصدير',
    'tab_tools': 'الأدوات',
    'tab_styles': 'الأنماط',
    'tab_typ': 'TYP',
    'tab_levels': 'المستويات',
    'tab_tuning': 'الضبط الدقيق',

    # Layer selection
    'select_layers': 'اختيار الطبقات للتصدير',
    'select_all_layers': 'تحديد كل الطبقات',
    'deselect_all_layers': 'إلغاء التحديد',
    'refresh': 'تحديث',
    'layers_list': 'قائمة طبقات المشروع:',

    # Export settings
    'output_files': 'ملفات الإخراج',
    'output_folder': 'مجلد الإخراج:',
    'output_file_name': 'اسم ملف الخريطة:',
    'browse': 'استعراض...',
    'map_settings': 'إعدادات الخريطة',
    'family_id': 'معرّف العائلة (Family ID):',
    'map_id': 'معرّف الخريطة (Map ID):',
    'map_name': 'اسم الخريطة:',
    'map_description': 'الوصف:',
    'transparent': 'خريطة شفافة',
    'routing': 'دعم توجيه المسارات',

    # Tools (mkgmap / splitter / java)
    'tools_mkgmap': 'أدوات mkgmap',
    'add_mkgmap': 'إضافة mkgmap',
    'download_mkgmap': 'تنزيل mkgmap',
    'add_splitter': 'إضافة splitter',
    'download_splitter': 'تنزيل splitter',
    'detect_java': 'كشف تلقائي',
    'select_mkgmap': 'اختر ملف mkgmap.jar',
    'select_splitter': 'اختر ملف splitter.jar',
    'select_java': 'اختر ملف java القابل للتنفيذ',
    'jar_valid': 'الملف صالح',
    'jar_invalid': 'الملف ليس ملف mkgmap.jar صالحًا',
    'java_not_found': 'لم يتم العثور على Java. يرجى تثبيت Java (JRE 8+).',
    'downloading': 'جارٍ التنزيل...',
    'download_in_progress': 'هناك عملية تنزيل جارية بالفعل.',
    'download_failed': 'فشل تنزيل الملف',
    'download_complete': 'اكتمل التنزيل',

    # Style mapping
    'style_mapping': 'تعيين الأنماط بصيغة JSON',
    'load_mapping': 'تحميل',
    'save_mapping': 'حفظ',
    'edit_mapping': 'تحرير',
    'default_mapping': 'الافتراضي',
    'mapping_title': 'محرّر تعيين الأنماط بصيغة JSON',
    'mapping_description': 'اضبط المطابقة بين طبقات QGIS وأنواع كائنات Garmin',
    'validate_json': 'التحقق من JSON',
    'json_valid': 'صيغة JSON صحيحة!',
    'select_mapping_file': 'اختر ملف تعيين JSON',
    'save_mapping_file': 'حفظ ملف تعيين JSON',

    # TYP styling
    'typ_styling': 'تنسيق الخريطة (TYP)',
    'select_typ_file': 'اختر ملف TYP',

    # Levels
    'export_levels': 'مستويات عرض الخريطة',
    'level_0': 'المستوى 0 (مفصّل)',
    'level_1': 'المستوى 1 (رئيسي)',
    'level_2': 'المستوى 2 (متوسط)',
    'level_3': 'المستوى 3 (عام)',

    # Control buttons
    'compile_map': 'ترجمة الخريطة',
    'compiling': 'جارٍ الترجمة...',
    'cancel': 'إلغاء',
    'clear_logs': 'مسح السجلات',
    'save': 'حفظ',
    'close': 'إغلاق',
    'details': 'التفاصيل',

    # Progress / results
    'progress': 'التقدّم',
    'logs': 'السجلات',
    'results': 'النتائج',
    'layer': 'الطبقة',
    'status': 'الحالة',
    'message': 'الرسالة',
    'geometry_type': 'نوع الهندسة',
    'garmin_type': 'نوع Garmin',
    'label_field': 'حقل التسمية',

    # Common
    'success': 'نجاح',
    'error': 'خطأ',
    'warning': 'تحذير',
    'info': 'معلومات',
    'confirmation': 'تأكيد',
    'critical_error': 'خطأ حرج',
    'select_output_folder': 'اختر مجلد الإخراج لملف IMG',

    # Errors
    'error_no_layers': 'اختر طبقة واحدة على الأقل للتصدير',
    'error_no_output_folder': 'حدّد مجلد الإخراج',
    'error_output_folder_missing': 'مجلد الإخراج غير موجود',
    'error_no_mkgmap': 'حدّد مسار mkgmap.jar أو نزّله '
                       'باستخدام زر "تنزيل mkgmap"',
    'error_invalid_mkgmap': 'الملف المحدّد ليس ملف mkgmap.jar صالحًا',
    'error_java_not_found': 'لم يتم العثور على Java في النظام. ثبّت Java (JRE 8+) '
                            'وحدّد المسار في علامة التبويب "الأدوات".',
    'error_typ_not_found': 'لم يتم العثور على ملف TYP المحدّد',
    'error_invalid_json': 'تنسيق تعيين JSON غير صالح',
    'error_mkgmap_execution': 'خطأ في تنفيذ mkgmap: {error}',
    'confirm_close': 'الترجمة قيد التنفيذ. هل تريد الإيقاف والإغلاق؟',

    # Author dialog
    'about_author': 'عن المؤلّف',
    'header_support': 'الدعم',
    'header_about_author': 'عن المؤلّف',
    'version': 'الإصدار',
    'author': 'المؤلّف',
    'contact': 'التواصل',
    'year': 'السنة',
    'organization': 'المؤسّسة',
    'plugin_description': 'أداة احترافية لتصدير بيانات QGIS '
                          'إلى خرائط Garmin IMG عبر mkgmap',
    'multilingual_support': 'التنسيق من QGIS، وإنشاء TYP، والضبط الدقيق لـ mkgmap، '
                            'وواجهة متعدّدة اللغات',

    # Donation dialog
    'donation_title': '☕ ادعم التطوير',
    'donation_window_title': '☕ ادعم تطوير الإضافة',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 Garmin Export Plugin</b></p>
            <p>يتم تطوير هذه الإضافة وصيانتها <b>مجانًا</b>!</p>
            <p>دعمك يساعد على تحديث الإضافة وتحسينها.</p>
            <p style="color: #7f8c8d; font-size: 13px;">كل فنجان قهوة يُحدث فرقًا! ❤️</p>
        </div>''',
    'donation_kofi': '☕ اشترِ قهوة على Ko-fi',
    'donation_tbank': '💳 تبرّع عبر T-Bank',
    'donation_github': '💖 ارعَ المشروع على GitHub',
    'donation_maybe_later': '✅ ربما لاحقًا',

    # Success messages
    'success_export_complete': 'تمت ترجمة الخريطة بنجاح! تم حفظ الملف:',
    'success_mapping_saved': 'تم حفظ التعيين بنجاح',
    'success_mapping_loaded': 'تم تحميل التعيين بنجاح',
}
