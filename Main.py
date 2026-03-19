import pandas as pd
import os

pasta_aux = 'csv_auxiliares'
if not os.path.exists(pasta_aux):
    os.makedirs(pasta_aux)

df = pd.read_csv(r'Dataset\german_credit_data.csv')

# ================================ FUNÇÃO PADRÃO PARA CSV ========================================

def gerar_csv_contagem(df, column):
    caminho_arquivo = os.path.join(pasta_aux, f'{column}.csv')
    
    if not os.path.exists(caminho_arquivo):
        df_contagem = df[column].value_counts().reset_index()
        df_contagem.columns = [column, 'Quantidade']
        df_contagem = df_contagem.sort_values(by=column).reset_index(drop=True)
        
        df_contagem.to_csv(caminho_arquivo, index=False)
        print(f"Arquivo {column}.csv criado com sucesso!")
    else:
        print(f"Arquivo {column}.csv já existe. Pulando geração.")

# ================================ MEDIDAS DE CENTRALIZAÇÃO ========================================

def media(df, column):
    return df[column].mean()

def mediana(df, column):
    return df[column].median()

def moda(df, column):    
    return df[column].mode()[0]

def Valores_Na_Null(df, column):
    return df[column].isna().sum()

# ================================ IDADES ========================================

def menores_de_idade(df, column):
    return df[df[column] < 18].shape[0]

gerar_csv_contagem(df, 'Age')

print("------------------IDADES------------------")
print(f"Media: {media(df, 'Age')}")
print(f"Mediana: {mediana(df, 'Age')}")   
print(f"Moda: {moda(df, 'Age')}")
print(f"Valores NaN: {Valores_Na_Null(df, 'Age')}")
print(f"Menores de idade: {menores_de_idade(df, 'Age')}")

print("========================================\n")
# ================================ SEXO ========================================

gerar_csv_contagem(df, 'Sex')

print("------------------SEXO------------------")
print(f"Moda: {moda(df, 'Sex')}")
print(f"Valores NaN: {Valores_Na_Null(df, 'Sex')}")

print("========================================\n") 

# ================================ JOB ========================================
