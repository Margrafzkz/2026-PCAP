'''
Problema beecrowd | 1044
Data: 2026.04.16
Estudante: Matheus Margraf
'''
#Obejtivo : Verificar se dois inteiros são múltiplos entre si

# --- ANÁLISE ---
# Entrada: dois inteiros A e B na mesma linha separados por espaço
# Processamento: identificar maior ou menor, verificar se maior % menor == 0
# Sáida: "Sao multiplos" ou "nao sao multiplos"

A, B = input().split()
A = int(A)
B = int(B)

# indentifica maior e menor para aplicar o operador % corretamente
# (o resto sempre deve ser calculado dividindo o maior pelo menor)
if A > B:
    maior = A
    menor = B 
else: 
    maior = B
    menor = A

# Operador % (módulo): retorna o resto da divisão inteira
# se o resto for 0, o maior é multiplo do menor - são multiplos entre si
if maior % menor == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
