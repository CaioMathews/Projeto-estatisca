import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from Funcoes.Funcoes_analises import analisar_coluna, analisa_NaN

df = pd.read_csv(r'Dataset\german_credit_data.csv',index_col=0)

if __name__ == "__main__":
    
    for coluna in df.columns:
        analisar_coluna(df, coluna)
    
    analisa_NaN(df)


