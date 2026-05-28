'''
Problema: beecrowd | 1035
Data: 2026.04.23
Estudante: Matheus Margraf
'''

# Objetivo: ler 4 valores inteiros A,B,C e D, se B for maior q C e se D fpr maior doq A, e a soma de C com D for maior q a soma de A com B e se C e D, ambos, forem positivos e se a variavel A for par sair valores aceitos se não valores nao aceitos 


# --- ANÁLISE (LIAC) ---
# Entrada: 4 valores inteiros 
# Processamento: ver se B e maior doq C e se D for maior doq A, e a soma de C com D for maior q a soma de A e B e se C e D
# Saída: valores aceitos ou valores não aceitos 

A, B, C, D = map(int, input().split())

if (B>C) and (D>C) and (C+D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")