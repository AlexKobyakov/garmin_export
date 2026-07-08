# -*- coding: utf-8 -*-
"""
Arabic translations for Garmin Export Plugin
الترجمة العربية لإضافة Garmin Export

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
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

    # Tools tab (labels, placeholders, info)
    'mkgmap_path_label': 'مسار mkgmap.jar:',
    'mkgmap_path_placeholder': 'اختر أو نزّل mkgmap.jar',
    'splitter_path_label': 'مسار splitter.jar (اختياري):',
    'splitter_path_placeholder': 'يلزم splitter لتقسيم الخرائط الكبيرة (اختياري)',
    'java_path_label': 'مسار Java:',
    'java_path_placeholder': 'فارغ = java من PATH؛ الزر على اليمين يكتشفه',
    'tools_info': 'تمنع قواعد QGIS تضمين mkgmap.jar داخل الإضافة. '
                  'انقر على "تنزيل mkgmap" لتحصل الإضافة على أحدث إصدار من '
                  'mkgmap.org.uk (أو من نسخة Yandex.Disk الاحتياطية)، أو حدّد ملفك '
                  'الخاص باستخدام "إضافة mkgmap".',
    'support_tip': 'ادعم تطوير الإضافة!',
    'author_tip': 'معلومات عن مؤلّف الإضافة',

    # Tuning tab - group titles
    'map_params_group': 'معاملات الخريطة (mkgmap)',
    'generalization_group': 'التعميم',
    'performance_group': 'الأداء (الضبط)',
    'logging_group': 'التسجيل والتصحيح',

    # Tuning tab - options
    'code_page_label': 'صفحة ترميز التسميات:',
    'draw_priority_label': 'أولوية الرسم (--draw-priority):',
    'draw_priority_tip': '25 هو المعيار. أعلى = تُرسم الخريطة فوق غيرها. '
                         'للخرائط الشفافة التراكبية استخدم أكثر من 25.',
    'opt_index': 'فهرس العناوين للبحث (--index)',
    'opt_add_pois': 'إنشاء نقاط اهتمام من المضلّعات (--add-pois-to-areas)',
    'opt_lower_case': 'السماح بالأحرف الصغيرة في التسميات (--lower-case)',
    'opt_order_area': 'المضلّعات الصغيرة فوق الكبيرة (--order-by-decreasing-area)',
    'reduce_density_label': 'تبسيط الخطوط، م (--reduce-point-density):',
    'reduce_density_polygon_label': 'تبسيط المضلّعات، م (--reduce-point-density-polygon):',
    'min_polygon_label': 'أدنى حجم للمضلّع (--min-size-polygon):',
    'min_polygon_tip': 'تُحذف المضلّعات الأصغر من ذلك. يُوصى بـ 8-15.',
    'java_heap_label': 'ذاكرة Java، غيغابايت (-Xmx):',
    'java_heap_tip': 'يحتاج mkgmap إلى ~500 ميغابايت لكل خيط. لـ 8 أنوية اضبط 4 غيغابايت.',
    'max_jobs_label': 'الخيوط (--max-jobs):',
    'max_jobs_tip': '0 = يقرّر mkgmap بناءً على الأنوية والذاكرة.',
    'opt_mkgmap_log': 'الاحتفاظ بملف mkgmap.log في مجلد الإخراج',
    'opt_verbose': 'سجل مفصّل (مستوى INFO)',
    'opt_keep_temp': 'الاحتفاظ بالملفات الوسيطة (MP، TYP) في مجلد الإخراج',
    'extra_args_label': 'وسائط mkgmap إضافية:',
    'extra_args_placeholder': 'مثال: --precomp-sea=C:/sea.zip --generate-sea',
    'value_auto': 'تلقائي',
    'value_auto_default': 'تلقائي (2.6)',

    # Code pages
    'cp_1251': 'CP1251 (السيريلية)',
    'cp_1252': 'CP1252 (Latin-1، أوروبا الغربية)',
    'cp_1250': 'CP1250 (أوروبا الوسطى)',
    'cp_1253': 'CP1253 (اليونانية)',
    'cp_1254': 'CP1254 (التركية)',
    'cp_1257': 'CP1257 (البلطيقية)',
    'cp_65001': 'UTF-8 / Unicode (كل اللغات)',
    'cp_1255': 'CP1255 (العبرية)',
    'cp_1256': 'CP1256 (العربية)',
    'cp_1258': 'CP1258 (الفيتنامية)',
    'cp_874': 'CP874 (التايلاندية)',
    'cp_932': 'CP932 (اليابانية، Shift-JIS)',
    'cp_936': 'CP936 (الصينية المبسّطة، GBK)',
    'cp_949': 'CP949 (الكورية)',
    'cp_950': 'CP950 (الصينية التقليدية، Big5)',
    'cp_866': 'CP866 (السيريلية، DOS)',
    'cp_850': 'CP850 (أوروبا الغربية، DOS)',
    'cp_852': 'CP852 (أوروبا الوسطى، DOS)',
    # TYP tab
    'typ_info': 'يحدّد ملف TYP مظهر العناصر على جهاز Garmin: '
                'ألوان المضلّعات، وسمك الخطوط، ورموز النقاط. يمكن للإضافة إنشاء ملف TYP '
                'تلقائيًا من رموز طبقات QGIS الحالية — ستبدو الخريطة على الملاح كما في QGIS.',
    'typ_none': 'نمط Garmin القياسي (بدون TYP)',
    'typ_generate': 'إنشاء TYP من أنماط QGIS (مُوصى به)',
    'typ_file': 'استخدام ملف TYP / typ.txt موجود:',
    'typ_file_placeholder': 'مسار ملف ‎.typ أو ‎.txt',

    # Layers tab
    'layers_info': 'اختر طبقات المشروع للتصدير إلى تنسيق Garmin IMG',

    # Export tab (placeholders, tooltips)
    'output_folder_placeholder': 'اختر مجلدًا لحفظ ملف IMG',
    'map_description_placeholder': 'خريطة أُنشئت بإضافة QGIS Garmin Export',
    'family_id_tip': 'معرّف عائلة الخريطة. يجب أن يكون فريدًا بين الخرائط على الجهاز.',
    'map_id_tip': 'رقم بلاطة الخريطة المكوّن من 8 أرقام. يجب أن يكون فريدًا.',
    'transparent_tip': 'تُرسم الخريطة الشفافة فوق الخرائط الأخرى (مثلًا فوق خريطة أساس).',
    'routing_tip': 'كتابة بيانات NET/NOD (--route). تعمل إذا احتوت البيانات على شبكة طرق.',

    # Styles tab
    'mapping_info': 'اضبط المطابقة بين طبقات QGIS وأنواع كائنات Garmin',
    'mapping_placeholder': 'سيتم تحميل تعيين الأنماط بصيغة JSON تلقائيًا...',

    # Levels tab
    'levels_info': 'تحدّد المستويات المقاييس التي تظهر عندها العناصر على الجهاز. '
                   'المستوى 0 (الدقة 24) هو الأكثر تفصيلًا، والمستوى 3 (الدقة 18) هو العام. '
                   'في تعيين الأنماط، يحدّد المعامل "level" إلى أي مستوى يبقى الكائن ظاهرًا.',

    # Log widget
    'log_ready': 'تم تحميل Garmin Export Plugin وهو جاهز',
    'log_hint': 'ستظهر سجلات العمليات هنا...',
}
