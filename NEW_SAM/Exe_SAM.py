from NEW_SAM_1 import Query

# Valores que vão sair do TWM e iniciar o processo de saneamento 
saneado = 'Não' #ou vazio
id_fatura = '62f783c8445a39954ec8e00e51fc0559' #precisa ver qual vem do TWM e comparar com qual indice do Raven
id_fatura2 = '62f783c8445a39954ec8e00e51fc0559'

# Coluna extraída do DocParser que é usada para sanear e subir para o Dash *Mas faltam as colunas azuis do consolidado
list_campos_parser =        ['dc_identificador_conta',
                             'dt_vencimento',
                             'vl_total',
                             'dc_razao_social',
                             'dc_identificador_pessoa_juridica',
                             'dc_razao_social_cliente',
                             'dc_identificador_pessoa_juridica_cliente',
                             'dc_endereco_cliente',
                             'dt_leitura_anterior',
                             'dt_leitura_atual',
                             'unidade_medida',
                             'dt_mes_referencia',
                             'vl_base_calculo_icms',
                             'vl_valor_icms',
                             'vl_aliquota_icms',
                             'vl_base_calculo_pis_pasep',
                             'vl_valor_pis_pasep',
                             'vl_aliquota_pis_pasep',
                             'vl_base_calculo_cofins',
                             'vl_aliquota_cofins',
                             'vl_valor_cofins',
                             'dc_classe',
                             'dc_subclasse',
                             'valores_faturados_auditoria Descricao',
                             'valores_faturados_auditoria Quantidade',
                             'valores_faturados_auditoria Tarifa Preco',
                             'valores_faturados_auditoria Valor',
                             'valores_faturados_auditoria Faturado',
                             'dc_modalidade_tarifaria',
                             'dc_grupo_tensao',
                             'dc_subgrupo_tensao',
                             'vl_tensao_nominal',
                             'vl_tensao_contratada',
                             'dc_limites_tensao',
                             'fator_carga Hora Ponta',
                             'fator_carga Hora Fora Ponta',
                             'energia_reativa Hfp/único',
                             'energia_reativa Hora Ponta',
                             'energia_reativa Reservado']

# Criando dicioário com valores vazios para todos os campos do parser
list_valor_parser = []
for i in range(len(list_campos_parser)):
    list_valor_parser.append(0)
dict_indice_e_valor = dict(zip(list_campos_parser, list_valor_parser))
    

Query_start = Query()
Query_start.setUp()




list_faturas_pendetes = [id_fatura, id_fatura2]


# Executando query para cada fatura pendente que veio do TWM e preenchendo dict com os valores parseados
for id_fatura in list_faturas_pendetes: 
    query_results = Query_start.query_where(id_fatura)
    
    
    dc_identificador_conta = query_results[0].dc_identificador_conta
    dt_vencimento = query_results[0].dt_vencimento
    vl_total = query_results[0].vl_total
    dc_razao_social = query_results[0].dc_razao_social
    dc_identificador_pessoa_juridica = query_results[0].dc_identificador_pessoa_juridica
    
    dict_indice_e_valor['dc_identificador_conta'] = dc_identificador_conta
    dict_indice_e_valor['dt_vencimento'] = dt_vencimento
    dict_indice_e_valor['vl_total'] = vl_total
    dict_indice_e_valor['dc_razao_social'] = dc_razao_social
    dict_indice_e_valor['dc_identificador_pessoa_juridica'] = dc_identificador_pessoa_juridica
    
    print('------------------------------')
    print('id_fatura', id_fatura)
    print(dict_indice_e_valor)
    print('------------------------------')






# Query_start.query_where_equals()
# Query_start.query_on_date_time_range()