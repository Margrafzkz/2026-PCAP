#==============================================
# Arquivo:    ppt.py
# Disciplina: 2026-PCAP
# Aula:       20
# Autor:      Margraf 
# Data:       2026.08.11
# Conceitos: Jogo com modulo, lista como tabela de nome, funcao com retorno, operador % para dar a volta 

#==============================================


# importa funcao radint da bliblioteca random, sorte um numero inteiro aleatorio em um intervalo definido 
from random import randint 

#importa as funcoes titulo e linha do arquivo telas.py
from telas import titulo, linha 

# importa a funcao ler-opcao do aquivo modulos.py
from modulos import ler_opcao 

#lista com pedra == 0 ,  papel == 1, tesoura == 2
JOGADAS = ["PEDRA","PAPEL", "TESOURA"]

def quem_vence(jogador, computador):
    if jogador == computador:
        return "empate"
    if jogador == (computador + 1) % 3:
        return "jogador"
    return "computador"


def mostrar_jogadadas():
    print('[0] Pedra')
    print('[1] Papel')
    print('[2] Tesoura')
    linha()

def jogar_ppt():
    titulo('PEDRA - PAPEL - TESOURA')

    pontos_jogador = 0 
    pontos_computador = 0

    while pontos_jogador < 2 and pontos_computador < 2:
        mostrar_jogadadas()

        jogador = int(ler_opcao("Sua jogada", ["0", "1", "2"]))
        computdor = randint(0, 2)

        print('Você Jogou '  +  JOGADAS [ jogador] + ".")
        print("Computador Jogou "  +  JOGADAS [ computdor] + '.')

        resultado = quem_vence(jogador, computdor)

        if resultado == 'empate':
            print("empate! Ninguém venceu!")
        elif resultado == "jogador":
            pontos_jogador += 1 
            print("Você venceu essa rodada!")
        elif resultado == "computador":
            pontos_computador += 1 
            print("computador venceu essa rodada!") 

        linha()
        print(f'Placar: Jogador  {pontos_jogador}  X  {pontos_computador} Computador')
        linha()

    if pontos_jogador > pontos_computador:
        titulo('YOU WIN!')
    else:
        titulo('YOU LOSE!')



            