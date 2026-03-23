import pandas as pd
from Funcoes.Funcoes_csv import gerar_csv_contagem
from Funcoes.Funcoes_medidas import calcular_amplitude, calcular_correlacao_spearman, calcular_desvio_padrao, calcular_quartis, calcular_variancia, media, mediana, moda

# ================================ ANALISES GERAIS ========================================

def analisar_coluna(df, column):

    #gerar_csv_contagem(df, column)
    
    print(f"------------------{column.upper()}------------------")
    
    print(f"Moda: {moda(df, column)}")

    if pd.api.types.is_numeric_dtype(df[column]):
        print(f"Média: {media(df, column):.2f}") 
        print(f"Mediana: {mediana(df, column)}")
    
    if column in ['Age', 'Credit amount', 'Duration']:

        print("\n--- MEDIDAS DE POSIÇÃO ---\n")
        
        q = calcular_quartis(df, column)
        print(f"Quartis: Q1: {q['Q1']} | Q2: {q['Q2']} | Q3: {q['Q3']}")
        
        print("\n--- MEDIDAS DE DISPERSÃO ---\n")
        
        dp = calcular_desvio_padrao(df, column)
        var = calcular_variancia(df, column)
        amp = calcular_amplitude(df, column)
        
        print(f"Desvio Padrão: {dp:.2f}")
        print(f"Variância: {var:.2f}")
        print(f"Amplitude Total: {amp}")
        
    print("========================================\n")

# ================================ ANALISAR CORRELAÇÃO DE SPEARMAN ========================================

def analisar_correlação_spearman(df, col1, col2):
    
    correlacao = calcular_correlacao_spearman(df, col1, col2)

    print("\n" + "="*50)
    print(f"ANÁLISE DE CORRELAÇÃO (Spearman)")
    print(f"Relação entre Valor do Crédito e Risco: {correlacao:.4f}")
    print("="*50 + "\n")

    if correlacao > 0:
        print("INTERPRETAÇÃO: Existe uma correlação positiva. Quanto MAIOR o crédito, MAIOR o risco.")
    else:
        print("INTERPRETAÇÃO: Não há evidência de que o valor alto aumente o risco nesta base.")


# =================================== HIPOTESES ===========================================