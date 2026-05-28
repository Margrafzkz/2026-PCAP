'''
Disciplina : Pensamento computacional, algoritimos e programação (PCAP)
Projetto : jogo "adivinhe o numero"
Arquivo : adivinhe.py
Autor: Matheus Margraf
Data: 28.05.2026
'''

import random 

def jogar(maximo, chances):
    numero_secreto = random.randint(1, maximo)
acertou = False 

while chances > 0 and not acertou:
     palpite = int(input("Seu palpite (1 a " + str(maximo) + "): "))

if palpite == numero_secreto:
        print("Acertou ! O número era", numero_secreto)
        acertou = True
elif palpite < numero_secreto:
        print("Muito baixo ! Tente um valor maior.")
else:
        print ("Muito alto! Tente um valor menor.")

chances = chances - 1
print("Chances restantes:", chances)

if not acertou: 
     print("Suas chances acabaram! O número era", numero_secreto)

