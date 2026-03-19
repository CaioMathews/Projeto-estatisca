import pandas as pd
import os

df = pd.read_csv('Dataset\german_credit_data.csv')

print(df.head())


def media(df, column):
    return df[column].mean()

def mediana(df, column):
    return df[column].median()

def moda(df, column):    
    return df[column].mode()[0]

def Valores_Na_Null(df, column):
    return df[column].isna().sum()

def menores_de_idade(df, column):
    return df[df[column] < 18].shape[0]

def criar_csv_idades_unicas_e_quantidade(df, column):

    df_contagem = df[column].value_counts().reset_index()
    df_contagem.columns = [column, 'Quantidade']
    
    df_contagem = df_contagem.sort_values(by=column).reset_index(drop=True)
    
    df_contagem.to_csv('idades_unicas_e_quantidade.csv', index=False)
    return df_contagem

if not os.path.exists('idades_unicas_e_quantidade.csv'):
    criar_csv_idades_unicas_e_quantidade(df, 'Age')


print("------------------IDADES------------------")
print("Media:", media(df, 'Age'))
print("Mediana:", mediana(df, 'Age'))   
print("Moda:", moda(df, 'Age'))
print("Valores NaN:", Valores_Na_Null(df, 'Age'))
print("Menores de idade:", menores_de_idade(df, 'Age'))



print("========================================\n")
print("------------------SEXO------------------")
print("Moda:", moda(df, 'Sex'))
print("========================================\n")
