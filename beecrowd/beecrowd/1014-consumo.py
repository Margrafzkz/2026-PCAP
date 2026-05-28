'''
Problema 1014 Beecrowd
Data : 2026.04.16
Estudante: Matheus Margraf
'''
# Objetivo: calcular o consumo médio de um automóvel em km/l

# --- ANÁLISE --- 
# Entrada:int(input() (inteiro, em km) e float(input()) (float, em litros
# Processamento: consumo = km/L
# Saída: consumo com 3 casas decimais seguido de "km/l"

# Lê a distância total percorrida em km (tipo inteiro)
X = int(input())

# lê o total de combustivel gasto em litros (tipos pontos flutuantes)
Y = float(input())

# Calcula o consumo medio
consumo = X / Y 

# exibe o resultado com 3 casas decimais e na unidade km/l
print(f"{consumo:.3f} km/l")