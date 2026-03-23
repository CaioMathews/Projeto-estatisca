import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from Funcoes.Funcoes_analises import analisar_coluna,analisar_correlação_spearman
from Funcoes.Funcoes_tratar import tratar,remover_duplicados

df = pd.read_csv(r'Dataset\german_credit_data.csv',index_col=0)
df_sem_duplicados = remover_duplicados(df)
df_tratado = tratar(df_sem_duplicados)

if __name__ == "__main__":
    
    #ANALISE GERAL DAS COLUNAS
    
    for coluna in df_tratado.columns:
        analisar_coluna(df_tratado, coluna)
    
    #ANALISE DA HIPOTESE 1


    sns.boxplot(x='Risk', y='Credit amount', data=df_tratado, palette='Set2')

    plt.title('Hipótese 1: O valor do crédito solicitado influencia a taxa de inadimplência?')

    plt.xlabel('Classificação de Risco')
    plt.ylabel('Valor do Crédito (Original)')

    plt.show()

    analisar_correlação_spearman(df_tratado, 'Credit amount_normalizado', 'Risk_num')   

    #ANALISE DA HIPOTESE 2

    sns.boxplot(x='Risk', y='Age', data=df_tratado, palette='Pastel1')

    plt.title('Hipótese 2: Existe uma relação entre a idade do cliente e o risco de crédito?')

    plt.xlabel('Classificação de Risco')
    plt.ylabel('Idade')

    plt.show()

    analisar_correlação_spearman(df_tratado, 'Age', 'Risk_num') 

    #ANALISE DA HIPOTESE 3

    plt.figure(figsize=(12, 6))
    sns.countplot(x='Purpose', hue='Risk', data=df_tratado)

    plt.title('Hipótese 3: Qual o propósito de empréstimo que apresenta o maior risco médio?')

    plt.xticks(rotation=45)
    plt.title('Distribuição de Risco por Categoria de Uso do Crédito')

    plt.show()
