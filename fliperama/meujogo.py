#==============================================
# Arquivo:     mina.py
# Disciplina: 2026-PCAP
# Autor:      Matheus Margraf
# Projeto:    Jogo Autoral - Mina Terrestre
#==============================================

import random
from telas import titulo, linha
from modulos import ler_opcao

def jogar_mina():
    titulo("MINA TERRESTRE")
    print("Existe 1 mina escondida entre as posições 1 e 5.")
    print("Sua missão é encontrar todas as áreas seguras!\n")

    # A máquina sorteia qual posição (1 a 5) tem a mina
    mina = str(random.randint(1, 5))
    
    posicoes_livres = ['1', '2', '3', '4', '5']
    pontos = 0

    while len(posicoes_livres) > 1:
        print("Posições disponíveis: " + " ".join(posicoes_livres))
        escolha = ler_opcao("Escolha uma posição seguro", posicoes_livres)

        if escolha == mina:
            linha()
            print("💥 BOOM! Você pisou na mina terrestre!")
            print("GAME OVER. Pontuação final: " + str(pontos) + " pontos.")
            linha()
            return

        # Remove a posição segura escolhida para não repetir
        posicoes_livres.remove(escolha)
        pontos += 10
        print("✅ Posição " + escolha + " segura! (+10 pontos)\n")

    # Se sobrou apenas a posição que continha a mina, o jogador venceu!
    linha()
    print("🏆 PARABÉNS! Você desarmou o campo minado!")
    print("Pontuação máxima: " + str(pontos) + " pontos!")
    linha()