# ================================ MEDIDAS DE CENTRALIZAÇÃO ========================================

def media(df, column):
    return df[column].mean()

def mediana(df, column):
    return df[column].median()

def moda(df, column):    
    return df[column].mode()[0]

def Valores_Na_Null(df, column):
    return df[column].isna().sum()
