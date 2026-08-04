'''
Projeto: Jogo "Pedra-Papel-Tesoura"
Arquivo: ppt.py
Autor: Matheus Margraf
Data: 2026.16.06
'''

import random 

def resultado(jogador, maquina):
    if jogador == maquina:
        return "empate"
    if jogador == "pedra" and maquina == "tesoura":
        return "jogador"
    if jogador == "papel" and maquina == "pedra":
        return "jogador"
    if jogador == "tesoura" and maquina == "papel":
        return "jogador"
    return 'maquina'


opcoes = ["pedra", "papel", "tesoura"]
pontos_jogador = 0 
pontos_maquina = 0 

for rodada in range(1, 6 ):
    print("--- Rodada", rodada, "---")
    jogada_maquina = random.choice(opcoes)
    entrada = input("Teste sua sorte‼️  (pedra, papel ou tesoura): ")
    jogada_jogador =  entrada.lower().strip()

    if jogada_jogador not in opcoes:
        print(" ❌ jogada inválida! Digite pedra, papel ou tesoura. ")
        pontos_maquina = pontos_maquina + 1 
    else:
        quem = resultado(jogada_jogador, jogada_maquina)
        if quem == "empate":
            print("🤝 Empate!")
        elif quem == "jogador":
            print("🎉 Você ganhou a rodada!")
            ponto_jogador = pontos_jogador + 1
        else:
            print("🎭 A máquina ganhou a rodada, ela jogou", jogada_maquina)
            pontos_maquina = pontos_maquina + 1    
    
       

print ("Placar final -> Você:", pontos_jogador, "| Máquina:", pontos_maquina)
         