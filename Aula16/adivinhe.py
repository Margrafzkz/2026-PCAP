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
         
       return acertou


niveis = [ 
     ["Fácil", 10, 3],
     ["Médio", 100, 5],
     ["Impossível", 1000, 10],
     ["Absurdo", 5000, 15],
   ]


print("Escolha o nível de dificuldade:")
print("1 - Fácil       (1 a 10, 3 chances)")
print("2 - Médio       (1 a 100, 5 chances)")
print("3 - Impossível  (1 a 1000, 10 chances)")
print("4 - Apenas se gosta de um desafio!   (1 a 5000, 15 chances)")
opcao = int(input("Digite 1, 2, 3 ou 4: "))


nivel = niveis[opcao - 1]


print("Você escolheu o nível:", nivel[0])
venceu = jogar(nivel[1], nivel[2])

if not venceu:
     print(" Fim de jogo! Se você e fraco tente um nível mais fácil! ")