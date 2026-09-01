# ════════════════════════════════════════════════════════════
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Par ou Ímpar"
# Arquivo    : par_impar.py
# Autor      : Matheus Margraf
# Data       : 30/06/2026
# ════════════════════════════════════════════════════════════

import random
from telas import titulo, linha

# Verifica quem venceu a rodada.
def quem_venceu(soma, aposta):
    if soma % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"

    if resultado == aposta:
        return "Jogador"
    else:
        return "Máquina"


def jogar():
    maquina = random.randint(0, 5)

    # Lê e valida o número do jogador.
    while True:
        try:
            jogador = int(input("☝️  Escolha um número (0-5): "))
            if 0 <= jogador <= 5:
                break
            print("Número inválido! Digite entre 0 e 5. ❌")
        except ValueError:
            print("Por favor, digite apenas números inteiros! ❌")

    # Lê e valida a aposta.
    while True:
        aposta = input("☝️ Par ou Ímpar? ").lower().strip()

        if aposta == "ímpar":
            aposta = "impar"

        if aposta == "par" or aposta == "impar":
            break

        print("Digite apenas 'par' ou 'ímpar'.")

    soma = jogador + maquina
    vencedor = quem_venceu(soma, aposta)

    linha()
    print(" 🎰 RESULTADO ")
    print("Seu número:", jogador)
    print("Número da máquina:", maquina)
    print("Soma:", soma)

    if soma % 2 == 0:
        print("Resultado: PAR")
    else:
        print("Resultado: ÍMPAR")

    print("Vencedor da rodada:", vencedor)
    linha()

    return vencedor


def jogar_par_ou_impar():
    jogador = 0
    maquina = 0

    titulo("PAR OU ÍMPAR (Melhor de 5)")

    # O jogo termina quando alguém vencer 3 rodadas.
    while jogador < 3 and maquina < 3:
        vencedor = jogar()

        if vencedor == "Jogador":
            jogador += 1
        else:
            maquina += 1

        print("Placar atual:", jogador, "x", maquina)
        linha()

    titulo("FIM DE JOGO")

    if jogador == 3:
        print("🏆 Parabéns! Você Ganhou")
    else:
        print("🎭 A máquina venceu, você perdeu!")
    
    linha()