import pandas as pd
from Funcoes.Funcoes_csv import gerar_csv_contagem, gerar_csv_nan
from Funcoes.Funcoes_medidas import media, mediana, moda, Valores_Na_Null

def analisar_coluna(df, column):

    gerar_csv_contagem(df, column)
    
    print(f"------------------{column.upper()}------------------")
    
    print(f"Valores NaN: {Valores_Na_Null(df, column)}")
    print(f"Moda: {moda(df, column)}")

    if pd.api.types.is_numeric_dtype(df[column]):
        print(f"Média: {media(df, column):.2f}") 
        print(f"Mediana: {mediana(df, column)}")
        
    
    print("========================================\n")

def analisa_NaN(df):
    gerar_csv_nan(df)