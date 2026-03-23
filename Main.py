import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from Funcoes.Funcoes_analises import analisar_coluna,analisar_correlação_spearman
from Funcoes.Funcoes_tratar import tratar,remover_duplicados

df = pd.read_csv(r'Dataset\german_credit_data.csv',index_col=0)
df_sem_duplicados = remover_duplicados(df)
df_tratado = tratar(df_sem_duplicados)

if __name__ == "__main__":
    
    for coluna in df_tratado.columns:
        analisar_coluna(df_tratado, coluna)
    
    analisar_correlação_spearman(df_tratado, 'Credit amount_normalizado', 'Risk_num')   