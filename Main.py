import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from Funcoes.Funcoes_analises import analisar_coluna,analisar_correlação_spearman
from Funcoes.Funcoes_tratar import tratar,remover_duplicados

df = pd.read_csv(r'Dataset\german_credit_data.csv',index_col=0)
df_sem_duplicados = remover_duplicados(df)
df_tratado = tratar(df_sem_duplicados)

if __name__ == "__main__":
    
    #=====================================================================================================================================

    #ANALISE GERAL DAS COLUNAS
    
    for coluna in df_tratado.columns:
        analisar_coluna(df_tratado, coluna)
    
    #=====================================================================================================================================

    #ANALISE DA HIPOTESE 1
  
    sns.boxplot(
        x='Risk', 
        y='Credit amount', 
        data=df_tratado, 
        palette='Set2', 
        hue='Risk',     
        legend=False     
    )

    print("\n--- RESULTADO HIPÓTESE 1 ---")
    plt.title('O valor do crédito solicitado influencia a taxa de inadimplência?')

    plt.xlabel('Classificação de Risco')
    plt.ylabel('Valor do Crédito (Original)')

    plt.show()

    analisar_correlação_spearman(df_tratado, 'Credit amount_normalizado', 'Risk_num')   

    #=====================================================================================================================================

    #ANALISE DA HIPOTESE 2

    sns.boxplot(
        x='Risk', 
        y='Age', 
        data=df_tratado, 
        palette='muted', 
        hue='Risk',       
        legend=False      
    )

    print("\n--- RESULTADO HIPÓTESE 2 ---")
    plt.title('Existe uma relação entre a idade do cliente e o risco de crédito?')
    plt.xlabel('Classificação de Risco')
    plt.ylabel('Idade')

    plt.show()

    analisar_correlação_spearman(df_tratado, 'Age', 'Risk_num') 

    #=====================================================================================================================================

    #ANALISE DA HIPOTESE 3

    plt.figure(figsize=(12, 6))
    sns.countplot(x='Purpose', hue='Risk', data=df_tratado)

    plt.title('Hipótese 3: Qual o propósito de empréstimo que apresenta o maior risco médio?')

    plt.xticks(rotation=45)
    plt.title('Distribuição de Risco por Categoria de Uso do Crédito')

    plt.show()

    #=====================================================================================================================================

    #ANALISE DA HIPOTESE 4

    df_tratado['Categoria da duração'] = df_tratado['Duration'].apply(
        lambda x: 'Curta (<12m)' if x < 12 else 'Longa (>=12m)'
    )

    df_baixo_saldo = df_tratado[df_tratado['Checking account'] == 'little'].copy()

    analise_h4 = df_baixo_saldo.groupby('Categoria da duração')['Risk_num'].mean() * 100

    print("\n--- RESULTADO HIPÓTESE 4 ---")
    print(f"Taxa de Inadimplência (Saldo Baixo + Duração Curta): {analise_h4['Curta (<12m)']:.2f}%")
    print(f"Taxa de Inadimplência (Saldo Baixo + Duração Longa): {analise_h4['Longa (>=12m)']:.2f}%")

    grafico_hipotese_4 = sns.catplot(
        data=df_tratado, 
        x="Checking account", 
        hue="Risk", 
        col="Categoria da duração", 
        kind="count", 
        palette="viridis"
    )

    grafico_hipotese_4.set_axis_labels("Saldo em Conta", "Quantidade de Clientes")
    grafico_hipotese_4.set_titles("Duração do Empréstimo: {col_name}")

    plt.show()
    #=====================================================================================================================================

    #ANALISE DA HIPOTESE 5

    media_credito = df_tratado['Credit amount'].mean()

    df_tratado['Faixa de Valor'] = df_tratado['Credit amount'].apply(
        lambda x: 'Acima da Média' if x > media_credito else 'Abaixo da Média'
    )

    df_moradia = df_tratado[df_tratado['Housing'] == 'own'].copy()

    analise_h5 = df_moradia.groupby('Faixa de Valor')['Risk_num'].mean() * 100

    print("\n--- RESULTADO HIPÓTESE 5 (Clientes com Casa Própria) ---")
    print(f"Média Global de Crédito: {media_credito:.2f}")
    print(f"Taxa de Risco - Pedidos Abaixo da Média: {analise_h5['Abaixo da Média']:.2f}%")
    print(f"Taxa de Risco - Pedidos Acima da Média: {analise_h5['Acima da Média']:.2f}%")

    grafico_hipotese_5 = sns.catplot(
        data=df_moradia, 
        x="Risk", 
        col="Faixa de Valor", 
        kind="count", 
        palette="magma",
        hue="Risk",
        legend=False
    )

    grafico_hipotese_5.set_axis_labels("Classificação de Risco", "Quantidade de Clientes")
    grafico_hipotese_5.set_titles("Crédito: {col_name}")

    plt.show()

    #=====================================================================================================================================