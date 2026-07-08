# -*- coding: utf-8 -*-
"""
Portuguese translations for Garmin Export Plugin
Traduções em português para o complemento Garmin Export

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025-2026
"""

translations = {
    # Main interface
    'window_title': 'Exportar para Garmin IMG - Conversor de dados vetoriais',
    'no_vector_layers': 'O projeto não tem camadas vetoriais para exportar.\n\n'
                        'Adicione camadas vetoriais ao projeto e tente novamente.',

    # Tabs
    'tab_layers': 'Camadas',
    'tab_export': 'Exportar',
    'tab_tools': 'Ferramentas',
    'tab_styles': 'Estilos',
    'tab_typ': 'TYP',
    'tab_levels': 'Níveis',
    'tab_tuning': 'Ajuste',

    # Layer selection
    'select_layers': 'Seleção de camadas para exportar',
    'select_all_layers': 'Selecionar todas as camadas',
    'deselect_all_layers': 'Desmarcar tudo',
    'refresh': 'Atualizar',
    'layers_list': 'Lista de camadas do projeto:',

    # Export settings
    'output_files': 'Arquivos de saída',
    'output_folder': 'Pasta de saída:',
    'output_file_name': 'Nome do arquivo do mapa:',
    'browse': 'Procurar...',
    'map_settings': 'Configurações do mapa',
    'family_id': 'Family ID:',
    'map_id': 'Map ID:',
    'map_name': 'Nome do mapa:',
    'map_description': 'Descrição:',
    'transparent': 'Mapa transparente',
    'routing': 'Suporte a roteamento',

    # Tools (mkgmap / splitter / java)
    'tools_mkgmap': 'Ferramentas mkgmap',
    'add_mkgmap': 'Adicionar mkgmap',
    'download_mkgmap': 'Baixar mkgmap',
    'add_splitter': 'Adicionar splitter',
    'download_splitter': 'Baixar splitter',
    'detect_java': 'Detecção automática',
    'select_mkgmap': 'Selecionar arquivo mkgmap.jar',
    'select_splitter': 'Selecionar arquivo splitter.jar',
    'select_java': 'Selecionar executável do java',
    'jar_valid': 'o arquivo é válido',
    'jar_invalid': 'O arquivo não é um mkgmap.jar válido',
    'java_not_found': 'Java não encontrado. Instale o Java (JRE 8+).',
    'downloading': 'Baixando...',
    'download_in_progress': 'Já há um download em andamento.',
    'download_failed': 'Falha ao baixar o arquivo',
    'download_complete': 'Download concluído',

    # Style mapping
    'style_mapping': 'Mapeamento de estilos JSON',
    'load_mapping': 'Carregar',
    'save_mapping': 'Salvar',
    'edit_mapping': 'Editar',
    'default_mapping': 'Padrão',
    'mapping_title': 'Editor de mapeamento de estilos JSON',
    'mapping_description': 'Configure a correspondência entre as camadas do QGIS e os tipos de objeto Garmin',
    'validate_json': 'Validar JSON',
    'json_valid': 'A sintaxe JSON é válida!',
    'select_mapping_file': 'Selecionar arquivo de mapeamento JSON',
    'save_mapping_file': 'Salvar arquivo de mapeamento JSON',

    # TYP styling
    'typ_styling': 'Estilo do mapa (TYP)',
    'select_typ_file': 'Selecionar arquivo TYP',

    # Levels
    'export_levels': 'Níveis de exibição do mapa',
    'level_0': 'Nível 0 (detalhado)',
    'level_1': 'Nível 1 (principal)',
    'level_2': 'Nível 2 (médio)',
    'level_3': 'Nível 3 (visão geral)',

    # Control buttons
    'compile_map': 'Compilar mapa',
    'compiling': 'Compilando...',
    'cancel': 'Cancelar',
    'clear_logs': 'Limpar registros',
    'save': 'Salvar',
    'close': 'Fechar',
    'details': 'Detalhes',

    # Progress / results
    'progress': 'Progresso',
    'logs': 'Registros',
    'results': 'Resultados',
    'layer': 'Camada',
    'status': 'Status',
    'message': 'Mensagem',
    'geometry_type': 'Tipo de geometria',
    'garmin_type': 'Tipo Garmin',
    'label_field': 'Campo de rótulo',

    # Common
    'success': 'Sucesso',
    'error': 'Erro',
    'warning': 'Aviso',
    'info': 'Informação',
    'confirmation': 'Confirmação',
    'critical_error': 'Erro crítico',
    'select_output_folder': 'Selecione a pasta de saída para o arquivo IMG',

    # Errors
    'error_no_layers': 'Selecione pelo menos uma camada para exportar',
    'error_no_output_folder': 'Especifique a pasta de saída',
    'error_output_folder_missing': 'A pasta de saída não existe',
    'error_no_mkgmap': 'Especifique o caminho para o mkgmap.jar ou baixe-o '
                       'com o botão "Baixar mkgmap"',
    'error_invalid_mkgmap': 'O arquivo especificado não é um mkgmap.jar válido',
    'error_java_not_found': 'Java não encontrado no sistema. Instale o Java (JRE 8+) '
                            'e defina o caminho na aba "Ferramentas".',
    'error_typ_not_found': 'O arquivo TYP especificado não foi encontrado',
    'error_invalid_json': 'Formato de mapeamento JSON inválido',
    'error_mkgmap_execution': 'Erro de execução do mkgmap: {error}',
    'confirm_close': 'Compilação em andamento. Parar e fechar?',

    # Author dialog
    'about_author': 'Sobre o autor',
    'header_support': 'Apoiar',
    'header_about_author': 'Sobre o autor',
    'version': 'Versão',
    'author': 'Autor',
    'contact': 'Contato',
    'year': 'Ano',
    'organization': 'Organização',
    'plugin_description': 'Ferramenta profissional para exportar dados do QGIS '
                          'para mapas Garmin IMG via mkgmap',
    'multilingual_support': 'Estilo do QGIS, geração de TYP, ajuste fino do mkgmap, '
                            'interface multilíngue',

    # Donation dialog
    'donation_title': '☕ Apoiar o desenvolvimento',
    'donation_window_title': '☕ Apoie o desenvolvimento do complemento',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 Garmin Export Plugin</b></p>
            <p>este complemento é desenvolvido e mantido <b>gratuitamente</b>!</p>
            <p>Seu apoio ajuda a atualizar e melhorar o complemento.</p>
            <p style="color: #7f8c8d; font-size: 13px;">Cada café conta! ❤️</p>
        </div>''',
    'donation_kofi': '☕ Pagar um café no Ko-fi',
    'donation_tbank': '💳 Doar via T-Bank',
    'donation_github': '💖 Patrocinar no GitHub',
    'donation_maybe_later': '✅ Talvez mais tarde',

    # Success messages
    'success_export_complete': 'Mapa compilado com sucesso! Arquivo salvo:',
    'success_mapping_saved': 'Mapeamento salvo com sucesso',
    'success_mapping_loaded': 'Mapeamento carregado com sucesso',

    # Tools tab (labels, placeholders, info)
    'mkgmap_path_label': 'Caminho para mkgmap.jar:',
    'mkgmap_path_placeholder': 'Selecione ou baixe o mkgmap.jar',
    'splitter_path_label': 'Caminho para splitter.jar (opcional):',
    'splitter_path_placeholder': 'splitter é necessário para dividir mapas grandes (opcional)',
    'java_path_label': 'Caminho para o Java:',
    'java_path_placeholder': 'Vazio = java do PATH; o botão à direita o detecta',
    'tools_info': 'As regras do QGIS proíbem incluir o mkgmap.jar no complemento. '
                  'Clique em "Baixar mkgmap" e o complemento obterá a versão mais recente '
                  'em mkgmap.org.uk (ou do backup no Yandex.Disk), ou indique seu próprio '
                  'arquivo com "Adicionar mkgmap".',
    'support_tip': 'Apoie o desenvolvimento do complemento!',
    'author_tip': 'Informações sobre o autor do complemento',

    # Tuning tab - group titles
    'map_params_group': 'Parâmetros do mapa (mkgmap)',
    'generalization_group': 'Generalização',
    'performance_group': 'Desempenho (ajuste)',
    'logging_group': 'Registro e depuração',

    # Tuning tab - options
    'code_page_label': 'Página de código dos rótulos:',
    'draw_priority_label': 'Prioridade de desenho (--draw-priority):',
    'draw_priority_tip': '25 é o padrão. Maior = o mapa é desenhado sobre os outros. '
                         'Para mapas de sobreposição transparentes, use mais de 25.',
    'opt_index': 'Índice de endereços para busca (--index)',
    'opt_add_pois': 'Criar POIs a partir de polígonos (--add-pois-to-areas)',
    'opt_lower_case': 'Permitir minúsculas nos rótulos (--lower-case)',
    'opt_order_area': 'Polígonos pequenos sobre os grandes (--order-by-decreasing-area)',
    'reduce_density_label': 'Simplificação de linhas, m (--reduce-point-density):',
    'reduce_density_polygon_label': 'Simplificação de polígonos, m (--reduce-point-density-polygon):',
    'min_polygon_label': 'Tamanho mín. do polígono (--min-size-polygon):',
    'min_polygon_tip': 'Polígonos menores que isso são removidos. 8-15 recomendado.',
    'java_heap_label': 'Memória do Java, GB (-Xmx):',
    'java_heap_tip': 'mkgmap precisa de ~500 MB por thread. Para 8 núcleos, defina 4 GB.',
    'max_jobs_label': 'Threads (--max-jobs):',
    'max_jobs_tip': '0 = mkgmap decide com base nos núcleos e na memória.',
    'opt_mkgmap_log': 'Manter um arquivo mkgmap.log na pasta de saída',
    'opt_verbose': 'Registro detalhado (nível INFO)',
    'opt_keep_temp': 'Manter arquivos intermediários (MP, TYP) na pasta de saída',
    'extra_args_label': 'Argumentos adicionais do mkgmap:',
    'extra_args_placeholder': 'ex.: --precomp-sea=C:/sea.zip --generate-sea',
    'value_auto': 'auto',
    'value_auto_default': 'auto (2.6)',

    # Code pages
    'cp_1251': 'CP1251 (cirílico)',
    'cp_1252': 'CP1252 (Latin-1, Europa Ocidental)',
    'cp_1250': 'CP1250 (Europa Central)',
    'cp_1253': 'CP1253 (grego)',
    'cp_1254': 'CP1254 (turco)',
    'cp_1257': 'CP1257 (báltico)',
    'cp_65001': 'UTF-8 / Unicode (todos os idiomas)',
    'cp_1255': 'CP1255 (hebraico)',
    'cp_1256': 'CP1256 (árabe)',
    'cp_1258': 'CP1258 (vietnamita)',
    'cp_874': 'CP874 (tailandês)',
    'cp_932': 'CP932 (japonês, Shift-JIS)',
    'cp_936': 'CP936 (chinês simplificado, GBK)',
    'cp_949': 'CP949 (coreano)',
    'cp_950': 'CP950 (chinês tradicional, Big5)',
    'cp_866': 'CP866 (cirílico, DOS)',
    'cp_850': 'CP850 (Europa Ocidental, DOS)',
    'cp_852': 'CP852 (Europa Central, DOS)',
    # TYP tab
    'typ_info': 'Um arquivo TYP define a aparência dos objetos no dispositivo Garmin: '
                'cores de polígonos, espessura de linhas, ícones de pontos. O complemento pode '
                'gerar um TYP automaticamente a partir da simbologia atual das camadas do QGIS '
                '— o mapa no navegador ficará como no QGIS.',
    'typ_none': 'Estilo padrão do Garmin (sem TYP)',
    'typ_generate': 'Gerar TYP a partir dos estilos do QGIS (recomendado)',
    'typ_file': 'Usar um arquivo TYP / typ.txt existente:',
    'typ_file_placeholder': 'Caminho para um arquivo .typ ou .txt',

    # Layers tab
    'layers_info': 'Selecione as camadas do projeto para exportar no formato Garmin IMG',

    # Export tab (placeholders, tooltips)
    'output_folder_placeholder': 'Selecione uma pasta para salvar o arquivo IMG',
    'map_description_placeholder': 'Mapa criado com o complemento QGIS Garmin Export',
    'family_id_tip': 'Identificador da família de mapas. Deve ser único entre os mapas do dispositivo.',
    'map_id_tip': 'Número de bloco do mapa de 8 dígitos. Deve ser único.',
    'transparent_tip': 'Um mapa transparente é desenhado sobre outros mapas (ex.: sobre um mapa base).',
    'routing_tip': 'Gravar dados NET/NOD (--route). Funciona se os dados contiverem uma rede viária.',

    # Styles tab
    'mapping_info': 'Configure a correspondência entre as camadas do QGIS e os tipos de objeto Garmin',
    'mapping_placeholder': 'O mapeamento de estilos JSON será carregado automaticamente...',

    # Levels tab
    'levels_info': 'Os níveis definem em que escalas os objetos ficam visíveis no dispositivo. '
                   'O nível 0 (resolução 24) é o mais detalhado, o nível 3 (resolução 18) é a '
                   'visão geral. No mapeamento de estilos, o parâmetro "level" define até que '
                   'nível um objeto permanece visível.',

    # Log widget
    'log_ready': 'Garmin Export Plugin carregado e pronto',
    'log_hint': 'Os registros de operações aparecerão aqui...',
}
