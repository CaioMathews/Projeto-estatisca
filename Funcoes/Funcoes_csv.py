import os

pasta_aux = 'csv_auxiliares'
if not os.path.exists(pasta_aux):
    os.makedirs(pasta_aux)

# ================================ FUNÇÃO PARA GERAR CSV DOS VALORES NaN ========================================

def gerar_csv_nan(df):

    if not os.path.exists(os.path.join(pasta_aux, 'relatorio_nan.csv')):    
        if df['Checking account'].isnull().any() or df['Saving accounts'].isnull().any():
            
            filtro_nan = df['Checking account'].isnull() | df['Saving accounts'].isnull()
            
            df_nan = df[filtro_nan]
            
            caminho_nan = os.path.join(pasta_aux, 'relatorio_nan.csv')
            df_nan.to_csv(caminho_nan)
            print(f"Arquivo relatorio_nan.csv criado com sucesso!\n")
            print(f"Total de linhas: {df_nan.shape[0]}\n")
    else:
        print(f"Arquivo relatorio_nan.csv já existe. Pulando geração.\n")
    

# ================================ FUNÇÃO PADRÃO PARA CSV ========================================

def gerar_csv_contagem(df, column):
    caminho_arquivo = os.path.join(pasta_aux, f'{column}.csv')
    
    if not os.path.exists(caminho_arquivo):
        df_contagem = df[column].value_counts(dropna=False).reset_index()
        df_contagem.columns = [column, 'Quantidade']
        
        df_contagem = df_contagem.sort_values(by=column, na_position='last').reset_index(drop=True)
        
        df_contagem.to_csv(caminho_arquivo, index=False)
        print(f"Arquivo {column}.csv criado com sucesso!\n")
    else:
        print(f"Arquivo {column}.csv já existe. Pulando geração.\n")



