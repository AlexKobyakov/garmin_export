# -*- coding: utf-8 -*-
"""
Indonesian translations for Garmin Export Plugin
Terjemahan bahasa Indonesia untuk plugin Garmin Export

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""

translations = {
    # Main interface
    'window_title': 'Ekspor Garmin IMG - Pengonversi Data Vektor',
    'no_vector_layers': 'Proyek tidak memiliki layer vektor untuk diekspor.\n\n'
                        'Tambahkan layer vektor ke proyek dan coba lagi.',

    # Tabs
    'tab_layers': 'Layer',
    'tab_export': 'Ekspor',
    'tab_tools': 'Alat',
    'tab_styles': 'Gaya',
    'tab_typ': 'TYP',
    'tab_levels': 'Tingkat',
    'tab_tuning': 'Penyetelan',

    # Layer selection
    'select_layers': 'Pemilihan Layer untuk Ekspor',
    'select_all_layers': 'Pilih Semua Layer',
    'deselect_all_layers': 'Batalkan Pilihan',
    'refresh': 'Segarkan',
    'layers_list': 'Daftar Layer Proyek:',

    # Export settings
    'output_files': 'Berkas Keluaran',
    'output_folder': 'Folder Keluaran:',
    'output_file_name': 'Nama Berkas Peta:',
    'browse': 'Telusuri...',
    'map_settings': 'Pengaturan Peta',
    'family_id': 'Family ID:',
    'map_id': 'Map ID:',
    'map_name': 'Nama Peta:',
    'map_description': 'Deskripsi:',
    'transparent': 'Peta Transparan',
    'routing': 'Dukungan Perutean',

    # Tools (mkgmap / splitter / java)
    'tools_mkgmap': 'Alat mkgmap',
    'add_mkgmap': 'Tambah mkgmap',
    'download_mkgmap': 'Unduh mkgmap',
    'add_splitter': 'Tambah splitter',
    'download_splitter': 'Unduh splitter',
    'detect_java': 'Deteksi otomatis',
    'select_mkgmap': 'Pilih berkas mkgmap.jar',
    'select_splitter': 'Pilih berkas splitter.jar',
    'select_java': 'Pilih berkas java yang dapat dieksekusi',
    'jar_valid': 'berkas valid',
    'jar_invalid': 'Berkas bukan mkgmap.jar yang valid',
    'java_not_found': 'Java tidak ditemukan. Silakan pasang Java (JRE 8+).',
    'downloading': 'Mengunduh...',
    'download_in_progress': 'Unduhan sedang berlangsung.',
    'download_failed': 'Gagal mengunduh berkas',
    'download_complete': 'Unduhan selesai',

    # Style mapping
    'style_mapping': 'Pemetaan Gaya JSON',
    'load_mapping': 'Muat',
    'save_mapping': 'Simpan',
    'edit_mapping': 'Ubah',
    'default_mapping': 'Bawaan',
    'mapping_title': 'Editor Pemetaan Gaya JSON',
    'mapping_description': 'Atur pemetaan antara layer QGIS dan tipe objek Garmin',
    'validate_json': 'Validasi JSON',
    'json_valid': 'Sintaks JSON valid!',
    'select_mapping_file': 'Pilih berkas pemetaan JSON',
    'save_mapping_file': 'Simpan berkas pemetaan JSON',

    # TYP styling
    'typ_styling': 'Penggayaan Peta (TYP)',
    'select_typ_file': 'Pilih berkas TYP',

    # Levels
    'export_levels': 'Tingkat Tampilan Peta',
    'level_0': 'Tingkat 0 (Terperinci)',
    'level_1': 'Tingkat 1 (Utama)',
    'level_2': 'Tingkat 2 (Sedang)',
    'level_3': 'Tingkat 3 (Ikhtisar)',

    # Control buttons
    'compile_map': 'Kompilasi Peta',
    'compiling': 'Mengompilasi...',
    'cancel': 'Batal',
    'clear_logs': 'Bersihkan Log',
    'save': 'Simpan',
    'close': 'Tutup',
    'details': 'Rincian',

    # Progress / results
    'progress': 'Kemajuan',
    'logs': 'Log',
    'results': 'Hasil',
    'layer': 'Layer',
    'status': 'Status',
    'message': 'Pesan',
    'geometry_type': 'Tipe Geometri',
    'garmin_type': 'Tipe Garmin',
    'label_field': 'Bidang Label',

    # Common
    'success': 'Berhasil',
    'error': 'Kesalahan',
    'warning': 'Peringatan',
    'info': 'Informasi',
    'confirmation': 'Konfirmasi',
    'critical_error': 'Kesalahan Kritis',
    'select_output_folder': 'Pilih folder keluaran untuk berkas IMG',

    # Errors
    'error_no_layers': 'Pilih setidaknya satu layer untuk diekspor',
    'error_no_output_folder': 'Tentukan folder keluaran',
    'error_output_folder_missing': 'Folder keluaran tidak ada',
    'error_no_mkgmap': 'Tentukan jalur ke mkgmap.jar atau unduh '
                       'dengan tombol "Unduh mkgmap"',
    'error_invalid_mkgmap': 'Berkas yang ditentukan bukan mkgmap.jar yang valid',
    'error_java_not_found': 'Java tidak ditemukan di sistem. Pasang Java (JRE 8+) '
                            'dan atur jalurnya pada tab "Alat".',
    'error_typ_not_found': 'Berkas TYP yang ditentukan tidak ditemukan',
    'error_invalid_json': 'Format pemetaan JSON tidak valid',
    'error_mkgmap_execution': 'Kesalahan eksekusi mkgmap: {error}',
    'confirm_close': 'Kompilasi sedang berlangsung. Hentikan dan tutup?',

    # Author dialog
    'about_author': 'Tentang Penulis',
    'header_support': 'Dukung',
    'header_about_author': 'Tentang Penulis',
    'version': 'Versi',
    'author': 'Penulis',
    'contact': 'Kontak',
    'year': 'Tahun',
    'organization': 'Organisasi',
    'plugin_description': 'Alat profesional untuk mengekspor data QGIS '
                          'ke peta Garmin IMG melalui mkgmap',
    'multilingual_support': 'Penggayaan QGIS, pembuatan TYP, penyetelan mkgmap, '
                            'antarmuka multibahasa',

    # Donation dialog
    'donation_title': '☕ Dukung Pengembangan',
    'donation_window_title': '☕ Dukung Pengembangan Plugin',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 Garmin Export Plugin</b></p>
            <p>plugin ini dikembangkan dan dipelihara <b>secara gratis</b>!</p>
            <p>Dukungan Anda membantu memperbarui dan meningkatkan plugin.</p>
            <p style="color: #7f8c8d; font-size: 13px;">Setiap cangkir kopi berarti! ❤️</p>
        </div>''',
    'donation_kofi': '☕ Belikan Kopi di Ko-fi',
    'donation_tbank': '💳 Donasi via T-Bank',
    'donation_github': '💖 Sponsori di GitHub',
    'donation_maybe_later': '✅ Mungkin Nanti',

    # Success messages
    'success_export_complete': 'Peta berhasil dikompilasi! Berkas disimpan:',
    'success_mapping_saved': 'Pemetaan berhasil disimpan',
    'success_mapping_loaded': 'Pemetaan berhasil dimuat',

    # Tools tab (labels, placeholders, info)
    'mkgmap_path_label': 'Jalur ke mkgmap.jar:',
    'mkgmap_path_placeholder': 'Pilih atau unduh mkgmap.jar',
    'splitter_path_label': 'Jalur ke splitter.jar (opsional):',
    'splitter_path_placeholder': 'splitter diperlukan untuk memotong peta besar (opsional)',
    'java_path_label': 'Jalur ke Java:',
    'java_path_placeholder': 'Kosong = java dari PATH; tombol di kanan mendeteksinya',
    'tools_info': 'Aturan QGIS melarang menyertakan mkgmap.jar di dalam plugin. '
                  'Klik "Unduh mkgmap" dan plugin akan mengambil versi terbaru '
                  'dari mkgmap.org.uk (atau dari cadangan Yandex.Disk), atau '
                  'tunjuk berkas Anda sendiri dengan "Tambah mkgmap".',
    'support_tip': 'Dukung pengembangan plugin!',
    'author_tip': 'Informasi penulis plugin',

    # Tuning tab - group titles
    'map_params_group': 'Parameter peta (mkgmap)',
    'generalization_group': 'Generalisasi',
    'performance_group': 'Kinerja (penyetelan)',
    'logging_group': 'Pencatatan dan debug',

    # Tuning tab - options
    'code_page_label': 'Code page label:',
    'draw_priority_label': 'Prioritas gambar (--draw-priority):',
    'draw_priority_tip': '25 adalah standar. Lebih tinggi = peta digambar di atas yang lain. '
                         'Untuk peta tumpang-tindih transparan gunakan lebih dari 25.',
    'opt_index': 'Indeks alamat untuk pencarian (--index)',
    'opt_add_pois': 'Buat POI dari poligon (--add-pois-to-areas)',
    'opt_lower_case': 'Izinkan huruf kecil pada label (--lower-case)',
    'opt_order_area': 'Poligon kecil di atas yang besar (--order-by-decreasing-area)',
    'reduce_density_label': 'Penyederhanaan garis, m (--reduce-point-density):',
    'reduce_density_polygon_label': 'Penyederhanaan poligon, m (--reduce-point-density-polygon):',
    'min_polygon_label': 'Ukuran min. poligon (--min-size-polygon):',
    'min_polygon_tip': 'Poligon lebih kecil dari ini akan dihapus. 8-15 disarankan.',
    'java_heap_label': 'Memori Java, GB (-Xmx):',
    'java_heap_tip': 'mkgmap butuh ~500 MB per thread. Untuk 8 inti atur 4 GB.',
    'max_jobs_label': 'Thread (--max-jobs):',
    'max_jobs_tip': '0 = mkgmap memutuskan berdasarkan inti dan memori.',
    'opt_mkgmap_log': 'Simpan berkas mkgmap.log di folder keluaran',
    'opt_verbose': 'Log terperinci (tingkat INFO)',
    'opt_keep_temp': 'Simpan berkas antara (MP, TYP) di folder keluaran',
    'extra_args_label': 'Argumen mkgmap tambahan:',
    'extra_args_placeholder': 'mis.: --precomp-sea=C:/sea.zip --generate-sea',
    'value_auto': 'otomatis',
    'value_auto_default': 'otomatis (2.6)',

    # Code pages
    'cp_1251': 'CP1251 (Kiril)',
    'cp_1252': 'CP1252 (Latin-1, Eropa Barat)',
    'cp_1250': 'CP1250 (Eropa Tengah)',
    'cp_1253': 'CP1253 (Yunani)',
    'cp_1254': 'CP1254 (Turki)',
    'cp_1257': 'CP1257 (Baltik)',
    'cp_65001': 'UTF-8 / Unicode (semua bahasa)',
    'cp_1255': 'CP1255 (Ibrani)',
    'cp_1256': 'CP1256 (Arab)',
    'cp_1258': 'CP1258 (Vietnam)',
    'cp_874': 'CP874 (Thai)',
    'cp_932': 'CP932 (Jepang, Shift-JIS)',
    'cp_936': 'CP936 (Tionghoa Sederhana, GBK)',
    'cp_949': 'CP949 (Korea)',
    'cp_950': 'CP950 (Tionghoa Tradisional, Big5)',
    'cp_866': 'CP866 (Kiril, DOS)',
    'cp_850': 'CP850 (Eropa Barat, DOS)',
    'cp_852': 'CP852 (Eropa Tengah, DOS)',

    # TYP tab
    'typ_info': 'Berkas TYP menentukan tampilan objek pada perangkat Garmin: '
                'warna poligon, lebar garis, ikon titik. Plugin dapat membuat '
                'TYP secara otomatis dari simbologi layer QGIS saat ini - peta '
                'di navigator akan tampak seperti di QGIS.',
    'typ_none': 'Gaya Garmin standar (tanpa TYP)',
    'typ_generate': 'Buat TYP dari gaya QGIS (disarankan)',
    'typ_file': 'Gunakan berkas TYP / typ.txt yang ada:',
    'typ_file_placeholder': 'Jalur ke berkas .typ atau .txt',

    # Layers tab
    'layers_info': 'Pilih layer proyek untuk diekspor ke format Garmin IMG',

    # Export tab (placeholders, tooltips)
    'output_folder_placeholder': 'Pilih folder untuk menyimpan berkas IMG',
    'map_description_placeholder': 'Peta dibuat dengan QGIS Garmin Export Plugin',
    'family_id_tip': 'Pengidentifikasi keluarga peta. Harus unik di antara peta pada perangkat.',
    'map_id_tip': 'Nomor ubin peta 8 digit. Harus unik.',
    'transparent_tip': 'Peta transparan digambar di atas peta lain (mis. di atas peta dasar).',
    'routing_tip': 'Tulis data NET/NOD (--route). Berfungsi jika data berisi jaringan jalan.',

    # Styles tab
    'mapping_info': 'Atur korespondensi antara layer QGIS dan tipe objek Garmin',
    'mapping_placeholder': 'Pemetaan gaya JSON akan dimuat secara otomatis...',

    # Levels tab
    'levels_info': 'Tingkat menentukan pada zoom berapa objek terlihat di perangkat. '
                   'Tingkat 0 (resolusi 24) paling terperinci, tingkat 3 (resolusi 18) '
                   'adalah ikhtisar. Dalam pemetaan gaya, parameter "level" menentukan '
                   'sampai tingkat mana objek tetap terlihat.',

    # Log widget
    'log_ready': 'Garmin Export Plugin dimuat dan siap',
    'log_hint': 'Log operasi akan muncul di sini...',
    'extracting': 'Mengekstrak...',
}
