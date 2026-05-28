'''
Problema: beecrowd | 1002
Data: 2026.04.07
Estudante: Matheus Margraf
'''
# Objetivo: Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

# --- ANÁLISE (LIAC) ---
# Entrada: definição de R
# Processamento: Calculo de area 
# Saída: Exibir o resultado do caulculo

# float() converte o texto para numero decimal
R = float(input())

# Defina pi conforme o enunciado indica
pi = 3.14159

# Definir a formula para caulcar o o valor da Area usando o R (raio)
AREA = pi * R ** 2

# :.3f - formata o numero com exatamente 3 casas decimais 
print(f"A={AREA:.4f}")