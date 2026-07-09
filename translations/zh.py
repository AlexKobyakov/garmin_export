# -*- coding: utf-8 -*-
"""
Chinese (Simplified) translations for Garmin Export Plugin
Garmin Export 插件简体中文翻译

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
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

    # Tools tab (labels, placeholders, info)
    'mkgmap_path_label': 'mkgmap.jar 路径：',
    'mkgmap_path_placeholder': '选择或下载 mkgmap.jar',
    'splitter_path_label': 'splitter.jar 路径（可选）：',
    'splitter_path_placeholder': 'splitter 用于切分大型地图（可选）',
    'java_path_label': 'Java 路径：',
    'java_path_placeholder': '留空 = 使用 PATH 中的 java；右侧按钮可自动检测',
    'tools_info': 'QGIS 规则禁止在插件中捆绑 mkgmap.jar。'
                  '点击“下载 mkgmap”，插件将从 mkgmap.org.uk 获取最新版本'
                  '（或从 Yandex.Disk 备份获取），'
                  '或使用“添加 mkgmap”指定您自己的文件。',
    'support_tip': '支持插件开发！',
    'author_tip': '插件作者信息',

    # Tuning tab - group titles
    'map_params_group': '地图参数（mkgmap）',
    'generalization_group': '概化',
    'performance_group': '性能（调优）',
    'logging_group': '日志与调试',

    # Tuning tab - options
    'code_page_label': '标注代码页：',
    'draw_priority_label': '绘制优先级（--draw-priority）：',
    'draw_priority_tip': '25 为标准值。值越大，地图越绘制在其他地图之上。'
                         '对于透明叠加地图请设置为大于 25。',
    'opt_index': '用于搜索的地址索引（--index）',
    'opt_add_pois': '从多边形创建 POI（--add-pois-to-areas）',
    'opt_lower_case': '允许标注使用小写字母（--lower-case）',
    'opt_order_area': '小多边形置于大多边形之上（--order-by-decreasing-area）',
    'reduce_density_label': '线简化，米（--reduce-point-density）：',
    'reduce_density_polygon_label': '多边形简化，米（--reduce-point-density-polygon）：',
    'min_polygon_label': '最小多边形尺寸（--min-size-polygon）：',
    'min_polygon_tip': '小于此尺寸的多边形将被删除。建议 8-15。',
    'java_heap_label': 'Java 内存，GB（-Xmx）：',
    'java_heap_tip': 'mkgmap 每个线程需要约 500 MB。8 核请设置 4 GB。',
    'max_jobs_label': '线程数（--max-jobs）：',
    'max_jobs_tip': '0 = mkgmap 根据核心数和内存自动决定。',
    'opt_mkgmap_log': '在输出文件夹中保留 mkgmap.log 日志文件',
    'opt_verbose': '详细日志（INFO 级别）',
    'opt_keep_temp': '在输出文件夹中保留中间文件（MP、TYP）',
    'extra_args_label': 'mkgmap 附加参数：',
    'extra_args_placeholder': '例如：--precomp-sea=C:/sea.zip --generate-sea',
    'value_auto': '自动',
    'value_auto_default': '自动 (2.6)',

    # Code pages
    'cp_1251': 'CP1251（西里尔文）',
    'cp_1252': 'CP1252（Latin-1，西欧）',
    'cp_1250': 'CP1250（中欧）',
    'cp_1253': 'CP1253（希腊文）',
    'cp_1254': 'CP1254（土耳其文）',
    'cp_1257': 'CP1257（波罗的海文）',
    'cp_65001': 'UTF-8 / Unicode（所有语言）',
    'cp_1255': 'CP1255（希伯来文）',
    'cp_1256': 'CP1256（阿拉伯文）',
    'cp_1258': 'CP1258（越南文）',
    'cp_874': 'CP874（泰文）',
    'cp_932': 'CP932（日文，Shift-JIS）',
    'cp_936': 'CP936（简体中文，GBK）',
    'cp_949': 'CP949（韩文）',
    'cp_950': 'CP950（繁体中文，Big5）',
    'cp_866': 'CP866（西里尔文，DOS）',
    'cp_850': 'CP850（西欧，DOS）',
    'cp_852': 'CP852（中欧，DOS）',
    # TYP tab
    'typ_info': 'TYP 文件定义对象在 Garmin 设备上的外观：'
                '多边形颜色、线宽、点图标。插件可以根据当前 QGIS 图层符号'
                '自动生成 TYP —— 导航仪上的地图将与 QGIS 中一致。',
    'typ_none': 'Garmin 标准样式（无 TYP）',
    'typ_generate': '从 QGIS 样式生成 TYP（推荐）',
    'typ_file': '使用现有的 TYP / typ.txt 文件：',
    'typ_file_placeholder': '.typ 或 .txt 文件的路径',

    # Layers tab
    'layers_info': '选择要导出为 Garmin IMG 格式的项目图层',

    # Export tab (placeholders, tooltips)
    'output_folder_placeholder': '选择保存 IMG 文件的文件夹',
    'map_description_placeholder': '由 QGIS Garmin Export 插件创建的地图',
    'family_id_tip': '地图族标识符。在设备的各地图中必须唯一。',
    'map_id_tip': '8 位地图分块编号。必须唯一。',
    'transparent_tip': '透明地图绘制在其他地图之上（例如底图之上）。',
    'routing_tip': '写入 NET/NOD 数据（--route）。当数据包含道路网络时有效。',

    # Styles tab
    'mapping_info': '配置 QGIS 图层与 Garmin 对象类型之间的对应关系',
    'mapping_placeholder': 'JSON 样式映射将自动加载……',

    # Levels tab
    'levels_info': '级别决定对象在设备上以何种缩放显示。'
                   '级别 0（分辨率 24）最详细，级别 3（分辨率 18）为概览。'
                   '在样式映射中，“level”参数设置对象可见到哪个级别。',

    # Log widget
    'log_ready': 'Garmin Export Plugin 已加载并就绪',
    'log_hint': '操作日志将显示在此处……',
    'extracting': '正在解压……',
}
