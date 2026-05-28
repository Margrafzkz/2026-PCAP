'''
Problema: beecrowd | 1009
Data: 2026.04.09
Estudante: Matheus Margraf
'''
# Objetivo: Ler nome, salário fixo e total de vendas; calcular e exibir o total a receber

# --- ANÁLISE (LIAC) ---
# Entrada: nome (texto), salário fixo (float), total de vendas efetuadas (float)
# Processamento: comissão = vendas * 0.15 - total = salário fixo + comissão
# Saída: exibir no formato exato "TOTAL = R$ valor" com 2 casa decimais 

# input() sem conversão - retorna nome como texto (str)
n = input()

# float(input()) - lê valores monetários (podem ter casas decimais)
s = float(input()) # salário fixo
v = float(input()) # total de vendas efetuadas no mês

# O vendedor ganhar 15% de comissão sobre total de vendas 
c = v * 0.15

# Total a receber = salário fixo + comissão
st = s + c

# :.2f dentro da f-string - formata o número com exatamente 2 casas decimais 
print(f"TOTAL = R$ {st:.2f}")