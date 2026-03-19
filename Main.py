import pandas as pd
import os

pasta_aux = 'csv_auxiliares'
if not os.path.exists(pasta_aux):
    os.makedirs(pasta_aux)

df = pd.read_csv(r'Dataset\german_credit_data.csv',index_col=0)

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
gerar_csv_contagem(df, 'Job')

print("------------------JOB------------------")
print(f"Moda: {moda(df, 'Job')}")
print(f"Valores NaN: {Valores_Na_Null(df, 'Job')}")

print("========================================\n") 


# ================================ HOUSING ========================================
gerar_csv_contagem(df, 'Housing')

print("------------------HOUSING------------------")
print(f"Moda: {moda(df, 'Housing')}")
print(f"Valores NaN: {Valores_Na_Null(df, 'Housing')}")

print("========================================\n") 

# ================================ SAVING ACCOUNT ========================================
gerar_csv_contagem(df, 'Saving accounts')

print("------------------SAVING ACCOUNT------------------")
print(f"Moda: {moda(df, 'Saving accounts')}")
print(f"Valores NaN: {Valores_Na_Null(df, 'Saving accounts')}")

print("========================================\n")

# ================================ CHECKING ACCOUNT ========================================
gerar_csv_contagem(df, 'Checking account')

print("------------------CHECKING ACCOUNT------------------")
print(f"Moda: {moda(df, 'Checking account')}")
print(f"Valores NaN: {Valores_Na_Null(df, 'Checking account')}")

print("========================================\n")

# ================================ CREDIT AMOUNT ========================================
gerar_csv_contagem(df, 'Credit amount')

print("------------------CREDIT AMOUNT------------------")
print(f"Média: {media(df, 'Credit amount')}")
print(f"Mediana: {mediana(df, 'Credit amount')}")
print(f"Moda: {moda(df, 'Credit amount')}")
print(f"Valores NaN: {Valores_Na_Null(df, 'Credit amount')}")

print("========================================\n")


# ================================ DURATION ========================================

gerar_csv_contagem(df, 'Duration')

print("------------------DURATION------------------")
print(f"Média: {media(df, 'Duration')}")
print(f"Mediana: {mediana(df, 'Duration')}")
print(f"Moda: {moda(df, 'Duration')}")
print(f"Valores NaN: {Valores_Na_Null(df, 'Duration')}")

print("========================================\n")


# ================================ PURPOSE ========================================

gerar_csv_contagem(df, 'Purpose')

print("------------------PURPOSE------------------")
print(f"Moda: {moda(df, 'Purpose')}")
print(f"Valores NaN: {Valores_Na_Null(df, 'Purpose')}")

print("========================================\n")

# ================================ FIM ========================================