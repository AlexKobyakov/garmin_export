# -*- coding: utf-8 -*-
"""
Chinese (Simplified) translations for Garmin Export Plugin
Garmin Export 插件简体中文翻译

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

translations = {
    # Main interface
    'window_title': '导出到 Garmin IMG - 矢量数据转换器',
    'no_vector_layers': '项目中没有可导出的矢量图层。\n\n'
                        '请向项目添加矢量图层后重试。',

    # Tabs
    'tab_layers': '图层',
    'tab_export': '导出',
    'tab_tools': '工具',
    'tab_styles': '样式',
    'tab_typ': 'TYP',
    'tab_levels': '级别',
    'tab_tuning': '调优',

    # Layer selection
    'select_layers': '选择要导出的图层',
    'select_all_layers': '全选图层',
    'deselect_all_layers': '取消全选',
    'refresh': '刷新',
    'layers_list': '项目图层列表：',

    # Export settings
    'output_files': '输出文件',
    'output_folder': '输出文件夹：',
    'output_file_name': '地图文件名：',
    'browse': '浏览...',
    'map_settings': '地图设置',
    'family_id': 'Family ID：',
    'map_id': 'Map ID：',
    'map_name': '地图名称：',
    'map_description': '描述：',
    'transparent': '透明地图',
    'routing': '支持路线规划',

    # Tools (mkgmap / splitter / java)
    'tools_mkgmap': 'mkgmap 工具',
    'add_mkgmap': '添加 mkgmap',
    'download_mkgmap': '下载 mkgmap',
    'add_splitter': '添加 splitter',
    'download_splitter': '下载 splitter',
    'detect_java': '自动检测',
    'select_mkgmap': '选择 mkgmap.jar 文件',
    'select_splitter': '选择 splitter.jar 文件',
    'select_java': '选择 java 可执行文件',
    'jar_valid': '文件有效',
    'jar_invalid': '文件不是有效的 mkgmap.jar',
    'java_not_found': '未找到 Java。请安装 Java（JRE 8+）。',
    'downloading': '正在下载...',
    'download_in_progress': '已有下载正在进行中。',
    'download_failed': '文件下载失败',
    'download_complete': '下载完成',

    # Style mapping
    'style_mapping': 'JSON 样式映射',
    'load_mapping': '加载',
    'save_mapping': '保存',
    'edit_mapping': '编辑',
    'default_mapping': '默认',
    'mapping_title': 'JSON 样式映射编辑器',
    'mapping_description': '配置 QGIS 图层与 Garmin 对象类型之间的映射',
    'validate_json': '验证 JSON',
    'json_valid': 'JSON 语法有效！',
    'select_mapping_file': '选择 JSON 映射文件',
    'save_mapping_file': '保存 JSON 映射文件',

    # TYP styling
    'typ_styling': '地图样式（TYP）',
    'select_typ_file': '选择 TYP 文件',

    # Levels
    'export_levels': '地图显示级别',
    'level_0': '级别 0（详细）',
    'level_1': '级别 1（主要）',
    'level_2': '级别 2（中等）',
    'level_3': '级别 3（概览）',

    # Control buttons
    'compile_map': '编译地图',
    'compiling': '正在编译...',
    'cancel': '取消',
    'clear_logs': '清除日志',
    'save': '保存',
    'close': '关闭',
    'details': '详情',

    # Progress / results
    'progress': '进度',
    'logs': '日志',
    'results': '结果',
    'layer': '图层',
    'status': '状态',
    'message': '消息',
    'geometry_type': '几何类型',
    'garmin_type': 'Garmin 类型',
    'label_field': '标注字段',

    # Common
    'success': '成功',
    'error': '错误',
    'warning': '警告',
    'info': '信息',
    'confirmation': '确认',
    'critical_error': '严重错误',
    'select_output_folder': '选择 IMG 文件的输出文件夹',

    # Errors
    'error_no_layers': '请至少选择一个要导出的图层',
    'error_no_output_folder': '请指定输出文件夹',
    'error_output_folder_missing': '输出文件夹不存在',
    'error_no_mkgmap': '请指定 mkgmap.jar 的路径，或使用'
                       '“下载 mkgmap”按钮下载它',
    'error_invalid_mkgmap': '指定的文件不是有效的 mkgmap.jar',
    'error_java_not_found': '系统中未找到 Java。请安装 Java（JRE 8+）'
                            '并在“工具”选项卡中设置路径。',
    'error_typ_not_found': '未找到指定的 TYP 文件',
    'error_invalid_json': 'JSON 映射格式无效',
    'error_mkgmap_execution': 'mkgmap 执行错误：{error}',
    'confirm_close': '正在编译。是否停止并关闭？',

    # Author dialog
    'about_author': '关于作者',
    'header_support': '支持',
    'header_about_author': '关于作者',
    'version': '版本',
    'author': '作者',
    'contact': '联系方式',
    'year': '年份',
    'organization': '组织',
    'plugin_description': '通过 mkgmap 将 QGIS 数据导出为 '
                          'Garmin IMG 地图的专业工具',
    'multilingual_support': 'QGIS 样式、TYP 生成、mkgmap 精细调优、'
                            '多语言界面',

    # Donation dialog
    'donation_title': '☕ 支持开发',
    'donation_window_title': '☕ 支持插件开发',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 Garmin Export Plugin</b></p>
            <p>此插件<b>免费</b>开发和维护！</p>
            <p>您的支持有助于更新和改进插件。</p>
            <p style="color: #7f8c8d; font-size: 13px;">每一杯咖啡都很重要！❤️</p>
        </div>''',
    'donation_kofi': '☕ 在 Ko-fi 上请喝咖啡',
    'donation_tbank': '💳 通过 T-Bank 捐赠',
    'donation_github': '💖 在 GitHub 上赞助',
    'donation_maybe_later': '✅ 以后再说',

    # Success messages
    'success_export_complete': '地图编译成功！文件已保存：',
    'success_mapping_saved': '映射保存成功',
    'success_mapping_loaded': '映射加载成功',
}
