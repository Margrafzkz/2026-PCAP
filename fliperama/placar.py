#==============================================
# Arquivo:     placar.py
# Disciplina: 2026-PCAP
# Autor:      Margraf 
#==============================================

from os.path import exists

ARQUIVO = "placar.csv"
NOMES = ["Advinhe o numero", "Pedra-Papel-Tesoura", "Par ou Impar", "Mina Terrestre"]


def salvar_placar(vezes):
    arquivo = open(ARQUIVO, 'w')
    for i in range(len(NOMES)):
        arquivo.write(NOMES[i] + "," + str(vezes[i]) + '\n')
    arquivo.close()    


def carregar_placar():
    if not exists(ARQUIVO):
        return [0, 0, 0, 0]

    arquivo = open(ARQUIVO, 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    vezes = []
    for linha in linhas:
        campos = linha.strip().split(',')
        if len(campos) == 2:
            vezes.append(int(campos[1]))

    
    while len(vezes) < len(NOMES):
        vezes.append(0)

    return vezes