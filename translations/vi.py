# -*- coding: utf-8 -*-
"""
Vietnamese translations for Garmin Export Plugin
Bản dịch tiếng Việt cho plugin Garmin Export

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""

translations = {
    # Main interface
    'window_title': 'Xuất Garmin IMG - Bộ chuyển đổi dữ liệu vector',
    'no_vector_layers': 'Dự án không có lớp vector nào để xuất.\n\n'
                        'Hãy thêm các lớp vector vào dự án rồi thử lại.',

    # Tabs
    'tab_layers': 'Lớp',
    'tab_export': 'Xuất',
    'tab_tools': 'Công cụ',
    'tab_styles': 'Kiểu',
    'tab_typ': 'TYP',
    'tab_levels': 'Cấp độ',
    'tab_tuning': 'Tinh chỉnh',

    # Layer selection
    'select_layers': 'Chọn lớp để xuất',
    'select_all_layers': 'Chọn tất cả các lớp',
    'deselect_all_layers': 'Bỏ chọn tất cả',
    'refresh': 'Làm mới',
    'layers_list': 'Danh sách lớp của dự án:',

    # Export settings
    'output_files': 'Tệp đầu ra',
    'output_folder': 'Thư mục đầu ra:',
    'output_file_name': 'Tên tệp bản đồ:',
    'browse': 'Duyệt...',
    'map_settings': 'Cài đặt bản đồ',
    'family_id': 'Family ID:',
    'map_id': 'Map ID:',
    'map_name': 'Tên bản đồ:',
    'map_description': 'Mô tả:',
    'transparent': 'Bản đồ trong suốt',
    'routing': 'Hỗ trợ định tuyến',

    # Tools (mkgmap / splitter / java)
    'tools_mkgmap': 'Công cụ mkgmap',
    'add_mkgmap': 'Thêm mkgmap',
    'download_mkgmap': 'Tải mkgmap',
    'add_splitter': 'Thêm splitter',
    'download_splitter': 'Tải splitter',
    'detect_java': 'Tự động phát hiện',
    'select_mkgmap': 'Chọn tệp mkgmap.jar',
    'select_splitter': 'Chọn tệp splitter.jar',
    'select_java': 'Chọn tệp thực thi java',
    'jar_valid': 'tệp hợp lệ',
    'jar_invalid': 'Tệp không phải là mkgmap.jar hợp lệ',
    'java_not_found': 'Không tìm thấy Java. Vui lòng cài đặt Java (JRE 8+).',
    'downloading': 'Đang tải...',
    'download_in_progress': 'Đã có một quá trình tải đang diễn ra.',
    'download_failed': 'Tải tệp không thành công',
    'download_complete': 'Tải xong',

    # Style mapping
    'style_mapping': 'Ánh xạ kiểu JSON',
    'load_mapping': 'Tải',
    'save_mapping': 'Lưu',
    'edit_mapping': 'Sửa',
    'default_mapping': 'Mặc định',
    'mapping_title': 'Trình chỉnh sửa ánh xạ kiểu JSON',
    'mapping_description': 'Cấu hình ánh xạ giữa các lớp QGIS và loại đối tượng Garmin',
    'validate_json': 'Kiểm tra JSON',
    'json_valid': 'Cú pháp JSON hợp lệ!',
    'select_mapping_file': 'Chọn tệp ánh xạ JSON',
    'save_mapping_file': 'Lưu tệp ánh xạ JSON',

    # TYP styling
    'typ_styling': 'Tạo kiểu bản đồ (TYP)',
    'select_typ_file': 'Chọn tệp TYP',

    # Levels
    'export_levels': 'Cấp độ hiển thị bản đồ',
    'level_0': 'Cấp 0 (Chi tiết)',
    'level_1': 'Cấp 1 (Chính)',
    'level_2': 'Cấp 2 (Trung bình)',
    'level_3': 'Cấp 3 (Tổng quan)',

    # Control buttons
    'compile_map': 'Biên dịch bản đồ',
    'compiling': 'Đang biên dịch...',
    'cancel': 'Hủy',
    'clear_logs': 'Xóa nhật ký',
    'save': 'Lưu',
    'close': 'Đóng',
    'details': 'Chi tiết',

    # Progress / results
    'progress': 'Tiến trình',
    'logs': 'Nhật ký',
    'results': 'Kết quả',
    'layer': 'Lớp',
    'status': 'Trạng thái',
    'message': 'Thông báo',
    'geometry_type': 'Loại hình học',
    'garmin_type': 'Loại Garmin',
    'label_field': 'Trường nhãn',

    # Common
    'success': 'Thành công',
    'error': 'Lỗi',
    'warning': 'Cảnh báo',
    'info': 'Thông tin',
    'confirmation': 'Xác nhận',
    'critical_error': 'Lỗi nghiêm trọng',
    'select_output_folder': 'Chọn thư mục đầu ra cho tệp IMG',

    # Errors
    'error_no_layers': 'Chọn ít nhất một lớp để xuất',
    'error_no_output_folder': 'Chỉ định thư mục đầu ra',
    'error_output_folder_missing': 'Thư mục đầu ra không tồn tại',
    'error_no_mkgmap': 'Chỉ định đường dẫn tới mkgmap.jar hoặc tải nó '
                       'bằng nút "Tải mkgmap"',
    'error_invalid_mkgmap': 'Tệp được chỉ định không phải là mkgmap.jar hợp lệ',
    'error_java_not_found': 'Không tìm thấy Java trên hệ thống. Cài đặt Java (JRE 8+) '
                            'và đặt đường dẫn ở tab "Công cụ".',
    'error_typ_not_found': 'Không tìm thấy tệp TYP được chỉ định',
    'error_invalid_json': 'Định dạng ánh xạ JSON không hợp lệ',
    'error_mkgmap_execution': 'Lỗi thực thi mkgmap: {error}',
    'confirm_close': 'Đang biên dịch. Dừng và đóng?',

    # Author dialog
    'about_author': 'Về tác giả',
    'header_support': 'Ủng hộ',
    'header_about_author': 'Về tác giả',
    'version': 'Phiên bản',
    'author': 'Tác giả',
    'contact': 'Liên hệ',
    'year': 'Năm',
    'organization': 'Tổ chức',
    'plugin_description': 'Công cụ chuyên nghiệp để xuất dữ liệu QGIS '
                          'sang bản đồ Garmin IMG qua mkgmap',
    'multilingual_support': 'Tạo kiểu từ QGIS, tạo TYP, tinh chỉnh mkgmap, '
                            'giao diện đa ngôn ngữ',

    # Donation dialog
    'donation_title': '☕ Ủng hộ phát triển',
    'donation_window_title': '☕ Ủng hộ phát triển plugin',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 Garmin Export Plugin</b></p>
            <p>plugin này được phát triển và duy trì <b>miễn phí</b>!</p>
            <p>Sự ủng hộ của bạn giúp cập nhật và cải thiện plugin.</p>
            <p style="color: #7f8c8d; font-size: 13px;">Mỗi ly cà phê đều quý giá! ❤️</p>
        </div>''',
    'donation_kofi': '☕ Mời cà phê trên Ko-fi',
    'donation_tbank': '💳 Quyên góp qua T-Bank',
    'donation_github': '💖 Tài trợ trên GitHub',
    'donation_maybe_later': '✅ Để sau',

    # Success messages
    'success_export_complete': 'Biên dịch bản đồ thành công! Đã lưu tệp:',
    'success_mapping_saved': 'Đã lưu ánh xạ thành công',
    'success_mapping_loaded': 'Đã tải ánh xạ thành công',

    # Tools tab (labels, placeholders, info)
    'mkgmap_path_label': 'Đường dẫn tới mkgmap.jar:',
    'mkgmap_path_placeholder': 'Chọn hoặc tải mkgmap.jar',
    'splitter_path_label': 'Đường dẫn tới splitter.jar (tùy chọn):',
    'splitter_path_placeholder': 'splitter cần để cắt các bản đồ lớn (tùy chọn)',
    'java_path_label': 'Đường dẫn tới Java:',
    'java_path_placeholder': 'Trống = java từ PATH; nút bên phải sẽ tự phát hiện',
    'tools_info': 'Quy tắc của QGIS cấm đóng gói mkgmap.jar trong plugin. '
                  'Nhấn "Tải mkgmap" và plugin sẽ lấy phiên bản mới nhất '
                  'từ mkgmap.org.uk (hoặc từ bản sao lưu Yandex.Disk), hoặc '
                  'trỏ đến tệp của riêng bạn bằng "Thêm mkgmap".',
    'support_tip': 'Ủng hộ việc phát triển plugin!',
    'author_tip': 'Thông tin tác giả plugin',

    # Tuning tab - group titles
    'map_params_group': 'Tham số bản đồ (mkgmap)',
    'generalization_group': 'Tổng quát hóa',
    'performance_group': 'Hiệu năng (tinh chỉnh)',
    'logging_group': 'Ghi nhật ký và gỡ lỗi',

    # Tuning tab - options
    'code_page_label': 'Bảng mã của nhãn:',
    'draw_priority_label': 'Ưu tiên vẽ (--draw-priority):',
    'draw_priority_tip': '25 là mặc định. Cao hơn = bản đồ được vẽ đè lên bản đồ khác. '
                         'Với bản đồ phủ trong suốt hãy dùng lớn hơn 25.',
    'opt_index': 'Chỉ mục địa chỉ để tìm kiếm (--index)',
    'opt_add_pois': 'Tạo POI từ các đa giác (--add-pois-to-areas)',
    'opt_lower_case': 'Cho phép chữ thường trong nhãn (--lower-case)',
    'opt_order_area': 'Đa giác nhỏ nằm trên đa giác lớn (--order-by-decreasing-area)',
    'reduce_density_label': 'Đơn giản hóa đường, m (--reduce-point-density):',
    'reduce_density_polygon_label': 'Đơn giản hóa đa giác, m (--reduce-point-density-polygon):',
    'min_polygon_label': 'Kích thước đa giác tối thiểu (--min-size-polygon):',
    'min_polygon_tip': 'Các đa giác nhỏ hơn giá trị này sẽ bị xóa. Khuyến nghị 8-15.',
    'java_heap_label': 'Bộ nhớ Java, GB (-Xmx):',
    'java_heap_tip': 'mkgmap cần ~500 MB cho mỗi luồng. Với 8 lõi đặt 4 GB.',
    'max_jobs_label': 'Luồng (--max-jobs):',
    'max_jobs_tip': '0 = mkgmap tự quyết định dựa trên số lõi và bộ nhớ.',
    'opt_mkgmap_log': 'Giữ tệp mkgmap.log trong thư mục đầu ra',
    'opt_verbose': 'Nhật ký chi tiết (mức INFO)',
    'opt_keep_temp': 'Giữ các tệp trung gian (MP, TYP) trong thư mục đầu ra',
    'extra_args_label': 'Đối số mkgmap bổ sung:',
    'extra_args_placeholder': 'vd: --precomp-sea=C:/sea.zip --generate-sea',
    'value_auto': 'tự động',
    'value_auto_default': 'tự động (2.6)',

    # Code pages
    'cp_1251': 'CP1251 (Kirin)',
    'cp_1252': 'CP1252 (Latin-1, Tây Âu)',
    'cp_1250': 'CP1250 (Trung Âu)',
    'cp_1253': 'CP1253 (Hy Lạp)',
    'cp_1254': 'CP1254 (Thổ Nhĩ Kỳ)',
    'cp_1257': 'CP1257 (Baltic)',
    'cp_65001': 'UTF-8 / Unicode (tất cả ngôn ngữ)',
    'cp_1255': 'CP1255 (Do Thái)',
    'cp_1256': 'CP1256 (Ả Rập)',
    'cp_1258': 'CP1258 (Tiếng Việt)',
    'cp_874': 'CP874 (Thái)',
    'cp_932': 'CP932 (Nhật, Shift-JIS)',
    'cp_936': 'CP936 (Trung giản thể, GBK)',
    'cp_949': 'CP949 (Hàn)',
    'cp_950': 'CP950 (Trung phồn thể, Big5)',
    'cp_866': 'CP866 (Kirin, DOS)',
    'cp_850': 'CP850 (Tây Âu, DOS)',
    'cp_852': 'CP852 (Trung Âu, DOS)',

    # TYP tab
    'typ_info': 'Tệp TYP xác định cách các đối tượng hiển thị trên thiết bị Garmin: '
                'màu đa giác, độ rộng đường, biểu tượng điểm. Plugin có thể tạo '
                'TYP tự động từ ký hiệu lớp QGIS hiện tại - bản đồ trên thiết bị '
                'định vị sẽ trông giống như trong QGIS.',
    'typ_none': 'Kiểu Garmin tiêu chuẩn (không có TYP)',
    'typ_generate': 'Tạo TYP từ kiểu QGIS (khuyến nghị)',
    'typ_file': 'Dùng tệp TYP / typ.txt có sẵn:',
    'typ_file_placeholder': 'Đường dẫn tới tệp .typ hoặc .txt',

    # Layers tab
    'layers_info': 'Chọn các lớp của dự án để xuất sang định dạng Garmin IMG',

    # Export tab (placeholders, tooltips)
    'output_folder_placeholder': 'Chọn thư mục để lưu tệp IMG',
    'map_description_placeholder': 'Bản đồ được tạo bằng QGIS Garmin Export Plugin',
    'family_id_tip': 'Định danh họ bản đồ. Phải là duy nhất trong số các bản đồ trên thiết bị.',
    'map_id_tip': 'Số ô bản đồ gồm 8 chữ số. Phải là duy nhất.',
    'transparent_tip': 'Bản đồ trong suốt được vẽ đè lên bản đồ khác (vd: đè lên bản đồ nền).',
    'routing_tip': 'Ghi dữ liệu NET/NOD (--route). Hoạt động nếu dữ liệu chứa mạng lưới đường.',

    # Styles tab
    'mapping_info': 'Cấu hình sự tương ứng giữa các lớp QGIS và loại đối tượng Garmin',
    'mapping_placeholder': 'Ánh xạ kiểu JSON sẽ được tải tự động...',

    # Levels tab
    'levels_info': 'Các cấp độ xác định ở mức thu phóng nào các đối tượng hiển thị trên thiết bị. '
                   'Cấp 0 (độ phân giải 24) chi tiết nhất, cấp 3 (độ phân giải 18) là tổng quan. '
                   'Trong ánh xạ kiểu, tham số "level" đặt đối tượng hiển thị đến cấp độ nào.',

    # Log widget
    'log_ready': 'Garmin Export Plugin đã tải và sẵn sàng',
    'log_hint': 'Nhật ký thao tác sẽ hiển thị ở đây...',
}
