# ================================ REMOVER DUPLICADOS ========================================
def remover_duplicados(df):
    qtd_antes = len(df)
    df = df.drop_duplicates()
    qtd_depois = len(df)
    
    if qtd_antes > qtd_depois:
        print(f"Foram removidos {qtd_antes - qtd_depois} registros duplicados.\n")
    else:
        print("Não foram encontrados dados duplicados.\n")
        
    return df

# ================================ TRATAR ========================================

def tratar(df):

    for column in df.columns:
        
        if column in ['Saving accounts', 'Checking account']:

            if Valores_Na_Null(df, column) > 0:
                
                print(f"Foram identificados {Valores_Na_Null(df, column)} valores NaN na coluna '{column}'.")
                df[column] = tratar_NaN(df, column)

        if column == 'Job':
            print("Convertendo tipos de dados: Mapeando coluna JOB...")
            df[column] = converter_job_para_string(df[column])

    return df

# ================================ TRATAMENTO NaN ========================================

def Valores_Na_Null(df, column):
    return df[column].isna().sum()

def tratar_NaN(df, column):
    print(f"TRATANDO {column}...\n")
    # fillna direto na coluna
    coluna_tratada = df[column].fillna('No account')
    print(f"Coluna '{column}' tratada com 'No account'!\n")
    return coluna_tratada

# ================================ TRATAMENTO Coluna Job ========================================

def converter_job_para_string(coluna_job):
    mapeamento_job = {
        0: 'unskilled and non-resident',
        1: 'unskilled and resident',
        2: 'skilled',
        3: 'highly skilled'
    }

    return coluna_job.map(mapeamento_job)