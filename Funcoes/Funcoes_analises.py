import pandas as pd
from Funcoes.Funcoes_csv import gerar_csv_contagem
from Funcoes.Funcoes_medidas import calcular_quartis, media, mediana, moda

def analisar_coluna(df, column):

    #gerar_csv_contagem(df, column)
    
    print(f"------------------{column.upper()}------------------")
    
    print(f"Moda: {moda(df, column)}")

    if pd.api.types.is_numeric_dtype(df[column]):
        print(f"Média: {media(df, column):.2f}") 
        print(f"Mediana: {mediana(df, column)}")
    
    if column in ['Age', 'Credit amount', 'Duration']:
        print("QUARTIS:")
        quartis = calcular_quartis(df, column)
        for quartil, valor in quartis.items():
            print(f"{quartil}: {valor}")
            
    print("========================================\n")

