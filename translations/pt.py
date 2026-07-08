# -*- coding: utf-8 -*-
"""
Portuguese translations for Garmin Export Plugin
Traduções em português para o complemento Garmin Export

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
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
}
