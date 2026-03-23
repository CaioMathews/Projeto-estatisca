import pandas as pd

# ================================ MEDIDAS DE CENTRALIZAÇÃO ========================================

def media(df, column):
    return df[column].mean()

def mediana(df, column):
    return df[column].median()

def moda(df, column):    
    return df[column].mode()[0]

# ================================ MEDIDAS DE POSIÇÃO ======================================== 
def calcular_quartis(df, column):
    
    q = df[column].quantile([0.25, 0.5, 0.75])
    
    return {
        'Q1': q[0.25],
        'Q2': q[0.50],
        'Q3': q[0.75]
    }


# ================================ MEDIDAS DE DISPERSÃO ======================================== 

def calcular_desvio_padrao(df, column):
    return df[column].std()

def calcular_variancia(df, column):
    return df[column].var()

def calcular_amplitude(df, column):
    return df[column].max() - df[column].min()