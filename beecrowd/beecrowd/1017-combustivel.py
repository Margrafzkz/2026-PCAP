'''
Problema: beecrowd | 1017
Data: 2026.04.23
Estudante: Matheus Margraf
'''

# Objetivo: sabendo que o automovel faz 12KM/L, devemos colocar 2 informações o tempo de viagem e a velocidade media do veiculo e dar o resultado com 3 casas decimais 

# --- ANÁLISE (LIAC) ---
# Entrada: o tempo de viagem e a velocidade media do veiculo
# Processamento: multiplicar o tempo de viagem por velocidade media
# Saída: imprimir a quantidade de litros 
 
# Lê o tempo de viagem 
T = int(input())

# lê a velocidade media do veiculo 
V = int(input())

# calcula o total da viagem em km
K = T * V

# calcula o total de combustivel gasto
TOTAL = K / 12

# exibe o resultado com 3 casas decimais 
print(f"{TOTAL:.3f}")