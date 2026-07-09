# -*- coding: utf-8 -*-
"""
Thai translations for Garmin Export Plugin
คำแปลภาษาไทยสำหรับปลั๊กอิน Garmin Export

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""

translations = {
    # Main interface
    'window_title': 'ส่งออก Garmin IMG - ตัวแปลงข้อมูลเวกเตอร์',
    'no_vector_layers': 'โปรเจกต์ไม่มีชั้นข้อมูลเวกเตอร์ให้ส่งออก\n\n'
                        'เพิ่มชั้นข้อมูลเวกเตอร์ลงในโปรเจกต์แล้วลองอีกครั้ง',

    # Tabs
    'tab_layers': 'ชั้นข้อมูล',
    'tab_export': 'ส่งออก',
    'tab_tools': 'เครื่องมือ',
    'tab_styles': 'สไตล์',
    'tab_levels': 'ระดับ',
    'tab_typ': 'TYP',
    'tab_tuning': 'การปรับแต่ง',

    # Layer selection
    'select_layers': 'เลือกชั้นข้อมูลเพื่อส่งออก',
    'select_all_layers': 'เลือกชั้นข้อมูลทั้งหมด',
    'deselect_all_layers': 'ยกเลิกการเลือก',
    'refresh': 'รีเฟรช',
    'layers_list': 'รายการชั้นข้อมูลของโปรเจกต์:',

    # Export settings
    'output_files': 'ไฟล์ผลลัพธ์',
    'output_folder': 'โฟลเดอร์ผลลัพธ์:',
    'output_file_name': 'ชื่อไฟล์แผนที่:',
    'browse': 'เรียกดู...',
    'map_settings': 'การตั้งค่าแผนที่',
    'family_id': 'Family ID:',
    'map_id': 'Map ID:',
    'map_name': 'ชื่อแผนที่:',
    'map_description': 'คำอธิบาย:',
    'transparent': 'แผนที่โปร่งใส',
    'routing': 'รองรับการนำทางเส้นทาง',

    # Tools (mkgmap / splitter / java)
    'tools_mkgmap': 'เครื่องมือ mkgmap',
    'add_mkgmap': 'เพิ่ม mkgmap',
    'download_mkgmap': 'ดาวน์โหลด mkgmap',
    'add_splitter': 'เพิ่ม splitter',
    'download_splitter': 'ดาวน์โหลด splitter',
    'detect_java': 'ตรวจหาอัตโนมัติ',
    'select_mkgmap': 'เลือกไฟล์ mkgmap.jar',
    'select_splitter': 'เลือกไฟล์ splitter.jar',
    'select_java': 'เลือกไฟล์ปฏิบัติการ java',
    'jar_valid': 'ไฟล์ถูกต้อง',
    'jar_invalid': 'ไฟล์ไม่ใช่ mkgmap.jar ที่ถูกต้อง',
    'java_not_found': 'ไม่พบ Java โปรดติดตั้ง Java (JRE 8+)',
    'downloading': 'กำลังดาวน์โหลด...',
    'download_in_progress': 'มีการดาวน์โหลดกำลังดำเนินอยู่แล้ว',
    'download_failed': 'ดาวน์โหลดไฟล์ไม่สำเร็จ',
    'download_complete': 'ดาวน์โหลดเสร็จสมบูรณ์',

    # Style mapping
    'style_mapping': 'การแมปสไตล์ JSON',
    'load_mapping': 'โหลด',
    'save_mapping': 'บันทึก',
    'edit_mapping': 'แก้ไข',
    'default_mapping': 'ค่าเริ่มต้น',
    'mapping_title': 'ตัวแก้ไขการแมปสไตล์ JSON',
    'mapping_description': 'กำหนดการแมประหว่างชั้นข้อมูล QGIS กับชนิดวัตถุ Garmin',
    'validate_json': 'ตรวจสอบ JSON',
    'json_valid': 'ไวยากรณ์ JSON ถูกต้อง!',
    'select_mapping_file': 'เลือกไฟล์แมป JSON',
    'save_mapping_file': 'บันทึกไฟล์แมป JSON',

    # TYP styling
    'typ_styling': 'การจัดสไตล์แผนที่ (TYP)',
    'select_typ_file': 'เลือกไฟล์ TYP',

    # Levels
    'export_levels': 'ระดับการแสดงแผนที่',
    'level_0': 'ระดับ 0 (ละเอียด)',
    'level_1': 'ระดับ 1 (หลัก)',
    'level_2': 'ระดับ 2 (กลาง)',
    'level_3': 'ระดับ 3 (ภาพรวม)',

    # Control buttons
    'compile_map': 'คอมไพล์แผนที่',
    'compiling': 'กำลังคอมไพล์...',
    'cancel': 'ยกเลิก',
    'clear_logs': 'ล้างบันทึก',
    'save': 'บันทึก',
    'close': 'ปิด',
    'details': 'รายละเอียด',

    # Progress / results
    'progress': 'ความคืบหน้า',
    'logs': 'บันทึก',
    'results': 'ผลลัพธ์',
    'layer': 'ชั้นข้อมูล',
    'status': 'สถานะ',
    'message': 'ข้อความ',
    'geometry_type': 'ชนิดเรขาคณิต',
    'garmin_type': 'ชนิด Garmin',
    'label_field': 'ฟิลด์ป้ายกำกับ',

    # Common
    'success': 'สำเร็จ',
    'error': 'ข้อผิดพลาด',
    'warning': 'คำเตือน',
    'info': 'ข้อมูล',
    'confirmation': 'การยืนยัน',
    'critical_error': 'ข้อผิดพลาดร้ายแรง',
    'select_output_folder': 'เลือกโฟลเดอร์ผลลัพธ์สำหรับไฟล์ IMG',

    # Errors
    'error_no_layers': 'เลือกชั้นข้อมูลอย่างน้อยหนึ่งชั้นเพื่อส่งออก',
    'error_no_output_folder': 'ระบุโฟลเดอร์ผลลัพธ์',
    'error_output_folder_missing': 'ไม่มีโฟลเดอร์ผลลัพธ์',
    'error_no_mkgmap': 'ระบุพาธไปยัง mkgmap.jar หรือดาวน์โหลด '
                       'ด้วยปุ่ม "ดาวน์โหลด mkgmap"',
    'error_invalid_mkgmap': 'ไฟล์ที่ระบุไม่ใช่ mkgmap.jar ที่ถูกต้อง',
    'error_java_not_found': 'ไม่พบ Java ในระบบ ติดตั้ง Java (JRE 8+) '
                            'และกำหนดพาธในแท็บ "เครื่องมือ"',
    'error_typ_not_found': 'ไม่พบไฟล์ TYP ที่ระบุ',
    'error_invalid_json': 'รูปแบบการแมป JSON ไม่ถูกต้อง',
    'error_mkgmap_execution': 'ข้อผิดพลาดในการเรียกใช้ mkgmap: {error}',
    'confirm_close': 'กำลังคอมไพล์อยู่ ต้องการหยุดและปิดหรือไม่?',

    # Author dialog
    'about_author': 'เกี่ยวกับผู้พัฒนา',
    'header_support': 'สนับสนุน',
    'header_about_author': 'เกี่ยวกับผู้พัฒนา',
    'version': 'เวอร์ชัน',
    'author': 'ผู้พัฒนา',
    'contact': 'ติดต่อ',
    'year': 'ปี',
    'organization': 'องค์กร',
    'plugin_description': 'เครื่องมือระดับมืออาชีพสำหรับส่งออกข้อมูล QGIS '
                          'ไปยังแผนที่ Garmin IMG ผ่าน mkgmap',
    'multilingual_support': 'จัดสไตล์จาก QGIS, สร้าง TYP, ปรับแต่ง mkgmap, '
                            'ส่วนติดต่อหลายภาษา',

    # Donation dialog
    'donation_title': '☕ สนับสนุนการพัฒนา',
    'donation_window_title': '☕ สนับสนุนการพัฒนาปลั๊กอิน',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 Garmin Export Plugin</b></p>
            <p>ปลั๊กอินนี้พัฒนาและดูแล<b>โดยไม่มีค่าใช้จ่าย</b>!</p>
            <p>การสนับสนุนของคุณช่วยอัปเดตและปรับปรุงปลั๊กอิน</p>
            <p style="color: #7f8c8d; font-size: 13px;">กาแฟทุกแก้วมีความหมาย! ❤️</p>
        </div>''',
    'donation_kofi': '☕ เลี้ยงกาแฟบน Ko-fi',
    'donation_tbank': '💳 บริจาคผ่าน T-Bank',
    'donation_github': '💖 สนับสนุนบน GitHub',
    'donation_maybe_later': '✅ ไว้ภายหลัง',

    # Success messages
    'success_export_complete': 'คอมไพล์แผนที่สำเร็จ! บันทึกไฟล์แล้ว:',
    'success_mapping_saved': 'บันทึกการแมปสำเร็จ',
    'success_mapping_loaded': 'โหลดการแมปสำเร็จ',

    # Tools tab (labels, placeholders, info)
    'mkgmap_path_label': 'พาธไปยัง mkgmap.jar:',
    'mkgmap_path_placeholder': 'เลือกหรือดาวน์โหลด mkgmap.jar',
    'splitter_path_label': 'พาธไปยัง splitter.jar (ไม่บังคับ):',
    'splitter_path_placeholder': 'splitter จำเป็นสำหรับการตัดแผนที่ขนาดใหญ่ (ไม่บังคับ)',
    'java_path_label': 'พาธไปยัง Java:',
    'java_path_placeholder': 'ว่าง = java จาก PATH; ปุ่มทางขวาจะตรวจหาให้',
    'tools_info': 'กฎของ QGIS ห้ามรวม mkgmap.jar ไว้ในปลั๊กอิน '
                  'คลิก "ดาวน์โหลด mkgmap" แล้วปลั๊กอินจะดึงเวอร์ชันล่าสุด '
                  'จาก mkgmap.org.uk (หรือจากสำรอง Yandex.Disk) หรือ '
                  'ระบุไฟล์ของคุณเองด้วย "เพิ่ม mkgmap"',
    'support_tip': 'สนับสนุนการพัฒนาปลั๊กอิน!',
    'author_tip': 'ข้อมูลผู้พัฒนาปลั๊กอิน',

    # Tuning tab - group titles
    'map_params_group': 'พารามิเตอร์แผนที่ (mkgmap)',
    'generalization_group': 'การทำให้ทั่วไป',
    'performance_group': 'ประสิทธิภาพ (การปรับแต่ง)',
    'logging_group': 'การบันทึกและดีบัก',

    # Tuning tab - options
    'code_page_label': 'โค้ดเพจของป้ายกำกับ:',
    'draw_priority_label': 'ลำดับการวาด (--draw-priority):',
    'draw_priority_tip': '25 คือค่ามาตรฐาน สูงกว่า = แผนที่ถูกวาดทับแผนที่อื่น '
                         'สำหรับแผนที่ซ้อนโปร่งใสให้ใช้มากกว่า 25',
    'opt_index': 'ดัชนีที่อยู่สำหรับการค้นหา (--index)',
    'opt_add_pois': 'สร้าง POI จากรูปหลายเหลี่ยม (--add-pois-to-areas)',
    'opt_lower_case': 'อนุญาตตัวพิมพ์เล็กในป้ายกำกับ (--lower-case)',
    'opt_order_area': 'รูปหลายเหลี่ยมเล็กอยู่เหนือรูปใหญ่ (--order-by-decreasing-area)',
    'reduce_density_label': 'การลดทอนเส้น, ม. (--reduce-point-density):',
    'reduce_density_polygon_label': 'การลดทอนรูปหลายเหลี่ยม, ม. (--reduce-point-density-polygon):',
    'min_polygon_label': 'ขนาดรูปหลายเหลี่ยมต่ำสุด (--min-size-polygon):',
    'min_polygon_tip': 'รูปหลายเหลี่ยมที่เล็กกว่านี้จะถูกลบ แนะนำ 8-15',
    'java_heap_label': 'หน่วยความจำ Java, GB (-Xmx):',
    'java_heap_tip': 'mkgmap ต้องการ ~500 MB ต่อเธรด สำหรับ 8 คอร์ให้ตั้ง 4 GB',
    'max_jobs_label': 'เธรด (--max-jobs):',
    'max_jobs_tip': '0 = mkgmap ตัดสินใจตามคอร์และหน่วยความจำ',
    'opt_mkgmap_log': 'เก็บไฟล์ mkgmap.log ในโฟลเดอร์ผลลัพธ์',
    'opt_verbose': 'บันทึกแบบละเอียด (ระดับ INFO)',
    'opt_keep_temp': 'เก็บไฟล์ตัวกลาง (MP, TYP) ในโฟลเดอร์ผลลัพธ์',
    'extra_args_label': 'อาร์กิวเมนต์ mkgmap เพิ่มเติม:',
    'extra_args_placeholder': 'เช่น: --precomp-sea=C:/sea.zip --generate-sea',
    'value_auto': 'อัตโนมัติ',
    'value_auto_default': 'อัตโนมัติ (2.6)',

    # Code pages
    'cp_1251': 'CP1251 (ซีริลลิก)',
    'cp_1252': 'CP1252 (Latin-1, ยุโรปตะวันตก)',
    'cp_1250': 'CP1250 (ยุโรปกลาง)',
    'cp_1253': 'CP1253 (กรีก)',
    'cp_1254': 'CP1254 (ตุรกี)',
    'cp_1257': 'CP1257 (บอลติก)',
    'cp_65001': 'UTF-8 / Unicode (ทุกภาษา)',
    'cp_1255': 'CP1255 (ฮีบรู)',
    'cp_1256': 'CP1256 (อาหรับ)',
    'cp_1258': 'CP1258 (เวียดนาม)',
    'cp_874': 'CP874 (ไทย)',
    'cp_932': 'CP932 (ญี่ปุ่น, Shift-JIS)',
    'cp_936': 'CP936 (จีนตัวย่อ, GBK)',
    'cp_949': 'CP949 (เกาหลี)',
    'cp_950': 'CP950 (จีนตัวเต็ม, Big5)',
    'cp_866': 'CP866 (ซีริลลิก, DOS)',
    'cp_850': 'CP850 (ยุโรปตะวันตก, DOS)',
    'cp_852': 'CP852 (ยุโรปกลาง, DOS)',

    # TYP tab
    'typ_info': 'ไฟล์ TYP กำหนดลักษณะของวัตถุบนอุปกรณ์ Garmin: '
                'สีรูปหลายเหลี่ยม ความหนาเส้น ไอคอนจุด ปลั๊กอินสามารถสร้าง '
                'TYP อัตโนมัติจากสัญลักษณ์ของชั้นข้อมูล QGIS ปัจจุบัน - แผนที่ '
                'บนอุปกรณ์นำทางจะดูเหมือนใน QGIS',
    'typ_none': 'สไตล์ Garmin มาตรฐาน (ไม่มี TYP)',
    'typ_generate': 'สร้าง TYP จากสไตล์ QGIS (แนะนำ)',
    'typ_file': 'ใช้ไฟล์ TYP / typ.txt ที่มีอยู่:',
    'typ_file_placeholder': 'พาธไปยังไฟล์ .typ หรือ .txt',

    # Layers tab
    'layers_info': 'เลือกชั้นข้อมูลของโปรเจกต์เพื่อส่งออกเป็นรูปแบบ Garmin IMG',

    # Export tab (placeholders, tooltips)
    'output_folder_placeholder': 'เลือกโฟลเดอร์เพื่อบันทึกไฟล์ IMG',
    'map_description_placeholder': 'แผนที่สร้างด้วย QGIS Garmin Export Plugin',
    'family_id_tip': 'ตัวระบุตระกูลแผนที่ ต้องไม่ซ้ำกันในบรรดาแผนที่บนอุปกรณ์',
    'map_id_tip': 'หมายเลขไทล์แผนที่ 8 หลัก ต้องไม่ซ้ำกัน',
    'transparent_tip': 'แผนที่โปร่งใสจะวาดทับแผนที่อื่น (เช่น ทับแผนที่ฐาน)',
    'routing_tip': 'เขียนข้อมูล NET/NOD (--route) ใช้งานได้หากข้อมูลมีโครงข่ายถนน',

    # Styles tab
    'mapping_info': 'กำหนดความสอดคล้องระหว่างชั้นข้อมูล QGIS กับชนิดวัตถุ Garmin',
    'mapping_placeholder': 'การแมปสไตล์ JSON จะถูกโหลดโดยอัตโนมัติ...',

    # Levels tab
    'levels_info': 'ระดับกำหนดว่าที่ระดับการซูมใดวัตถุจะปรากฏบนอุปกรณ์ '
                   'ระดับ 0 (ความละเอียด 24) ละเอียดที่สุด ระดับ 3 (ความละเอียด 18) '
                   'เป็นภาพรวม ในการแมปสไตล์ พารามิเตอร์ "level" กำหนดว่าวัตถุ '
                   'จะมองเห็นได้จนถึงระดับใด',

    # Log widget
    'log_ready': 'Garmin Export Plugin โหลดแล้วและพร้อมใช้งาน',
    'log_hint': 'บันทึกการทำงานจะปรากฏที่นี่...',
    'extracting': 'กำลังแตกไฟล์...',
}
