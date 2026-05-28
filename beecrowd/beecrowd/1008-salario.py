'''
Problema: beecrowd | 1008
Data: 2026.04.09
Estudantes: Matheus Margraf
'''
# Objetivo: receber as horas trabalhadas de um funcionario e o valor que recebe por horas e calcular o salário deste funcionario

# --- ANÁLISE (LIAC) ---
# Entrada: a numeração do funcionario (N), quantidade de horas (H), e o valor que recebe por hora (V)
# Processamento multiplicar as horas pelo valor de horas 
# Saída: exibir a numeração do funcionario e abaixo o salario ja multiplicado

# Entradas descritas na LIAC
N = int(input())
H = int(input())
V = float(input())

# Calcular o salário multiplicando H por V 
SAL = H * V 

# Saída - mostra o numero com 2 casa decimais (:.2f)
print (f"NUMBER = {N}")
print (f"SALARY = U$ {SAL:.2f}")