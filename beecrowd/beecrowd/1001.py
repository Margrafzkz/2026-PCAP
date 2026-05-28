'''
Problema 1001 do BeeCrowd 
Matheus Margraf
2026.03.31
'''
# Objetivo: somar dois valores inseridos

 # --- ANÁLISE (LIAC) ---

# Entrada: valor 1 e valor 2
# Processamento: soma dos dois valores
# Saída: tem o Print que e uma saida  

# int() converte para o texto para um valor inteiro
# input() Lê o valor digitado
# int(input()) le e converte em uma unica instrução 
A = int(input(""))
B = int(input(""))

# Seguir as variaveis X, A e B a risca 
X = A + B 

# f-string: insere o valor de X dentro do texto {}
# atenção: espaço antes de depois do = é obrigatorio conforme o enunciado 
print (f"X = {A+B}")
