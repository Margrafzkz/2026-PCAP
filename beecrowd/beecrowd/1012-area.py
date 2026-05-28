'''
Problema: beecrowd | 1012
Data: 2026.04.07
Estudantes: Matheus Margraf
'''

# Objetivo: Efetuar 5 calculos usando de 3 entradas 

# --- ANÁLISE (LIAC) ---
# Entrada:  3 valores na mesma linha 
# Processamento: calcular de acordo com a formula definida
# Saída: exibir 5 resultados com quatro digitos atras da virgula (:.4f)

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

# definir pi
PI = 3.14159

Y = A + B

# definir as formulas
TRI = A * C /2
CIR = PI * C **2
TRA = Y * C /2  
QUA = B**2
RET = B * A

# Exbir a resposta com 3 digitos apos o ponto decimal
print(f"TRIANGULO: {TRI:.3f}")
print(f"CIRCULO: {CIR:.3f}")
print(f"TRAPEZIO: {TRA:.3f}")
print(f"QUADRADO: {QUA:.3f}")
print(f"RETANGULO: {RET:.3f}")