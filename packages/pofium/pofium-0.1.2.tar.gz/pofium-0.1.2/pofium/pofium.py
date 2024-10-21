import pandas as pd
import numpy as np
import re
from ftplib import FTP
import os
import zipfile
import shutil
from platformdirs import user_cache_dir

def get_default_path():
    # Get the user cache directory for your application
    cache_dir = user_cache_dir("pofium")
    return os.path.join(cache_dir, 'dados_pof')

def get_dict_path():
    cache_dir = user_cache_dir("pofium")
    return os.path.join(cache_dir, 'dict_pof')

def download_file():
    # Criar uma pasta chamada 'dados_pof' no diretório de trabalho atual
    file_path = get_default_path()
    
    # Verificar se a pasta já existe, senão criar
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    
    ftp = FTP('ftp.ibge.gov.br', timeout=600)
    ftp.login()
    
    # Caminho do arquivo no FTP
    ftp_path_pof = 'Orcamentos_Familiares/Pesquisa_de_Orcamentos_Familiares_2017_2018/Microdados/Dados_20230713.zip'
    
    # Caminho completo para salvar o arquivo baixado
    local_file_path = os.path.join(file_path, 'pof.zip')
    
    # Abrir o arquivo local e baixar o arquivo do FTP
    with open(local_file_path, 'wb') as pof:
        ftp.retrbinary(f'RETR {ftp_path_pof}', pof.write)

def download_inst():
    # Criar uma pasta chamada 'dados_pof' no diretório de trabalho atual
    file_path = get_default_path()
    
    # Verificar se a pasta já existe, senão criar
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    
    ftp = FTP('ftp.ibge.gov.br', timeout=600)
    ftp.login()
    
    # Caminho do arquivo no FTP
    ftp_path_pof = 'Orcamentos_Familiares/Pesquisa_de_Orcamentos_Familiares_2017_2018/Microdados/Programas_de_Leitura_20230713.zip'
    
    # Caminho completo para salvar o arquivo baixado
    local_file_path = os.path.join(file_path, 'inst.zip')
    
    # Abrir o arquivo local e baixar o arquivo do FTP
    with open(local_file_path, 'wb') as inst:
        ftp.retrbinary(f'RETR {ftp_path_pof}', inst.write)

def download_dict():
    # Criar uma pasta chamada 'dados_pof' no diretório de trabalho atual
    file_path = get_dict_path()
    
    # Verificar se a pasta já existe, senão criar
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    
    ftp = FTP('ftp.ibge.gov.br', timeout=600)
    ftp.login()
    
    # Caminho do arquivo no FTP
    ftp_path_pof = 'Orcamentos_Familiares/Pesquisa_de_Orcamentos_Familiares_2017_2018/Microdados/Documentacao_20230713.zip'
    
    # Caminho completo para salvar o arquivo baixado
    local_file_path = os.path.join(file_path, 'dict.zip')
    
    # Abrir o arquivo local e baixar o arquivo do FTP
    with open(local_file_path, 'wb') as dicts:
        ftp.retrbinary(f'RETR {ftp_path_pof}', dicts.write)

def unzip():
    file_path = get_default_path()
    files = os.listdir(file_path)
    for file in files:
        local_zip_file_path = os.path.join(file_path, file)
        if '.zip' in local_zip_file_path:
            with zipfile.ZipFile(local_zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(file_path)

    dict_path = get_dict_path()
    files_dict = os.listdir(dict_path)
    for file in files_dict:
        local_zip_dict_path = os.path.join(dict_path, file)
        if '.zip' in local_zip_dict_path:
            with zipfile.ZipFile(local_zip_dict_path, 'r') as zip_ref:
                zip_ref.extractall(dict_path)    

def inst_df():
    file_path = get_default_path()
    inst = open(file_path + "/SAS/Leitura dos Microdados - SAS.txt", "r")
    inst = inst.read()
    # Regex para capturar todos os blocos entre /* e */
    pattern_t = re.compile(r'/\*([\s\S]*?)\*/')

    # Encontrar todas as ocorrências
    matches_t = pattern_t.findall(inst)

    titles = []
    # Exibir os resultados
    for match in matches_t[1:]:
        titles.append(match)
    # Regex para capturar todos os blocos entre /* e */
    pattern_vars = re.compile(r'INPUT\n([\s\S]*?)\nrun;')

    # Encontrar todas as ocorrências
    matches_vars = pattern_vars.findall(inst)

    var_text = []
    # Exibir os resultados
    for match in matches_vars:
        var_text.append(match)
    pattern_cod = re.compile(r'@\d+\s+(\w+)')
    var_cod = []

    for tab in var_text:
        var_cod.append(pattern_cod.findall(tab))
    pattern_n = re.compile(r'@\d+\s+\w+\s+(\$?\d+)\.')
    var_n = []

    for tab in var_text:
        var_n.append(pattern_n.findall(tab))

    df = pd.DataFrame([pd.Series(titles), pd.Series(var_n), pd.Series(var_cod)]).T
    df = df.explode([1,2])
    df.columns = ['tab', 'n', 'cod']
    df = df.reset_index(drop=True)
    df['tab'] = df['tab'].str.replace('REGISTRO -', '')
    df['str'] = np.where(df['n'].astype(str).str.contains('$', regex=False), 'str', 'float')
    df['n'] = df['n'].str.replace('$', '', regex= False).astype(int)
    df.loc[df['cod'].isin(['COD_UPA', 'NUM_DOM', 'NUM_UC', 'COD_INFORMANTE']), 'str'] = 'str'
    df = df.reset_index()

    name_keys = list(df['tab'].sort_values().drop_duplicates())
    name_dict = {}
    file_names = [
        "ALUGUEL_ESTIMADO.txt",
        "CADERNETA_COLETIVA.txt",
        "CARACTERISTICAS_DIETA.txt",
        "CONDICOES_VIDA.txt",
        "CONSUMO_ALIMENTAR.txt",
        "DESPESA_COLETIVA.txt",
        "DESPESA_INDIVIDUAL.txt",
        "DOMICILIO.txt",
        "INVENTARIO.txt",
        "MORADOR.txt",
        "MORADOR_QUALI_VIDA.txt",
        "OUTROS_RENDIMENTOS.txt",
        "RENDIMENTO_TRABALHO.txt",
        "RESTRICAO_PRODUTOS_SERVICOS_SAUDE.txt",
        "SERVICO_NAO_MONETARIO_POF2.txt",
        "SERVICO_NAO_MONETARIO_POF4.txt"
    ]

    for i, x in enumerate(name_keys):
        name_dict[x] = file_names[i]

    df = df.drop(columns=['index'])
    df['files'] = df['tab'].map(name_dict)
    return df
    
def carrega_tabela(d = None, save = None):
    file_path = get_default_path()
    inst = inst_df()
    file_names = [
        "ALUGUEL_ESTIMADO.txt",
        "CADERNETA_COLETIVA.txt",
        "CARACTERISTICAS_DIETA.txt",
        "CONDICOES_VIDA.txt",
        "CONSUMO_ALIMENTAR.txt",
        "DESPESA_COLETIVA.txt",
        "DESPESA_INDIVIDUAL.txt",
        "DOMICILIO.txt",
        "INVENTARIO.txt",
        "MORADOR.txt",
        "MORADOR_QUALI_VIDA.txt",
        "OUTROS_RENDIMENTOS.txt",
        "RENDIMENTO_TRABALHO.txt",
        "RESTRICAO_PRODUTOS_SERVICOS_SAUDE.txt",
        "SERVICO_NAO_MONETARIO_POF2.txt",
        "SERVICO_NAO_MONETARIO_POF4.txt"
    ]
    serie_files = pd.Series(file_names)

    if d is None:
        print('Escolha o número da tabela que deseja abrir:')
        print(serie_files)

    elif d not in list(serie_files.index):
        print('Número da tabela inválido.')
        print('Escolha o número da tabela que deseja abrir:')
        print(serie_files)

    else:
        chosen_file = serie_files[d]
        c_widths = inst[inst['files']==chosen_file]['n']
        c_cods = inst[inst['files']==chosen_file]['cod']
        dict_dtypes = dict(zip(
            (list(inst[inst['files']==chosen_file]['cod'])),
            (list(inst[inst['files']==chosen_file]['str'])) 
            ))
        dict_dtypes
        df = pd.read_fwf(
                            file_path + '/' + chosen_file,
                            widths=c_widths,
                            names=c_cods,
                            na_values=" ",
                            dtype = dict_dtypes)
        
        if 'NUM_DOM' in df.columns:
            df['COD_DOM'] = df['COD_UPA'] + df['NUM_DOM'].str.zfill(2)

        if 'NUM_UC' in df.columns:
            df['COD_UC'] = df['COD_UPA'] + df['NUM_DOM'].str.zfill(2) + df['NUM_UC']

        if 'COD_INFORMANTE' in df.columns:
            df['COD_PESSOA'] = df['COD_UPA'] + df['NUM_DOM'].str.zfill(2) + df['NUM_UC'] + df['COD_INFORMANTE'].str.zfill(2)
            
        if save:
            pof_name = chosen_file.replace('.txt', '.parquet')
            df.to_parquet(pof_name)
        
        return df
                
def salva_parquets():
    file_names = [
        "ALUGUEL_ESTIMADO.txt",
        "CADERNETA_COLETIVA.txt",
        "CARACTERISTICAS_DIETA.txt",
        "CONDICOES_VIDA.txt",
        "CONSUMO_ALIMENTAR.txt",
        "DESPESA_COLETIVA.txt",
        "DESPESA_INDIVIDUAL.txt",
        "DOMICILIO.txt",
        "INVENTARIO.txt",
        "MORADOR.txt",
        "MORADOR_QUALI_VIDA.txt",
        "OUTROS_RENDIMENTOS.txt",
        "RENDIMENTO_TRABALHO.txt",
        "RESTRICAO_PRODUTOS_SERVICOS_SAUDE.txt",
        "SERVICO_NAO_MONETARIO_POF2.txt",
        "SERVICO_NAO_MONETARIO_POF4.txt"
    ]
    serie_files = pd.Series(file_names)
    serie_files = serie_files.str.replace('.txt', '')
    for i in serie_files.index:
        print('Criando o DataFrame: ' + serie_files[i] + ' ...')
        carrega_tabela(i, save=True)
        print('DataFrame: ' + serie_files[i] + ' salvo como .parquet')

def consulta_var(cod=None, desc=None, d=None):
    file_path = get_dict_path()
    try:
        df = pd.ExcelFile(file_path + r'\Dicionários de váriaveis.xls')
    except:
        print('Arquivo .xls do dicionário não encontrado. Rode pofium.download()')
        return None
    series_dicts = pd.Series(sorted(df.sheet_names))

    if (d is None) or (d not in list(series_dicts.index)):
        print("Informe o número de acordo com a tabela que deseja consultar:")
        print(series_dicts)

    else:
            chosen_table = series_dicts[d]
            dict_df = df.parse(chosen_table, header=3)
            dict_df = dict_df.dropna(subset=['Código da variável', 'Descrição', 'Categorias'], how='all')
            dict_df = dict_df[['Código da variável', 'Descrição']]
            dict_df = dict_df.dropna()
            
            # Busca por código da variável
            if cod and not desc:
                dict_query = dict_df[dict_df['Código da variável'].str.contains(cod, case=False)]
                return dict_query
            
            # Busca por descrição
            if desc and not cod:
                dict_query = dict_df[dict_df['Descrição'].str.contains(desc, case=False)]  # Corrigido
                return dict_query
            
            # Verificação se ambos os parâmetros estão ausentes ou ambos presentes
            else:
                print("Informe exatamente um dos parâmetros de busca:")
                print("- cod = Código da Variável; ou")
                print("- desc = Descrição")

def descreva_var(cod=None, d=None):
    file_path = get_dict_path()
    try:
        df = pd.ExcelFile(file_path + r'\Dicionários de váriaveis.xls')
    except:
        print('Arquivo .xls do dicionário não encontrado. Rode pofium.download()')
        return None
    series_dicts = pd.Series(sorted(df.sheet_names))

    if (d is None) or (d not in list(series_dicts.index)):
        print("Informe o número de acordo com a tabela que deseja consultar:")
        print(series_dicts)

    else:
           
            if not cod:
                print("Informe também o código da variável para consultar as categorias. Ex: cod = 'V0403'")
            
            else:               
                chosen_table = series_dicts[d]
                dict_df = df.parse(chosen_table, header=3)
                dict_df = dict_df.dropna(subset=['Código da variável', 'Descrição', 'Categorias'], how='all')
                dict_df = dict_df[['Código da variável', 'Categorias']]
                dict_df['Código da variável'] = dict_df['Código da variável'].ffill()
                cod_query = cod.upper()
                dict_query = dict_df[dict_df['Código da variável']==cod_query]
                
                if len(dict_query) > 0:
                    print('Variável consultada: ' + cod_query )
                    print('Resultado:')
                    print(dict_query['Categorias'].reset_index(drop=True))
                
                else:
                    print('Variável consultada: ' + cod_query )
                    print('Não encontrada. Verifique se a tabela designada é a correta.')

def delete_pof():
    file_path = get_default_path()
    # Verifica se a pasta existe
    if os.path.exists(file_path):
        # Remove a pasta e todos os arquivos dentro dela
        shutil.rmtree(file_path)

def download():
    print('-  Download da base de dados iniciado')
    download_file()
    print('-  Download da base de dados finalizado')
    download_inst()
    download_dict()
    print('-  Download de arquivos auxiliares finalizado')
    print('-  Carregando base de dados em DataFrames Pandas')
    unzip()
    salva_parquets()
    print('-  Todos os arquivos foram salvos no diretório de trabalho')
    delete_pof()
    print('-  Procedimento finalizado')
