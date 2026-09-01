#==============================================
# Arquivo:    main.py
# Disciplina: 2026-PCAP
# Aula:       20
# Autor:      Margraf 
# Data:       2026.08.04
# Conceitos: 
#==============================================

# importar funções d arquivos (módulos)
from telas import titulo, linha
from adivinhe import jogar_adivinhe
from ppt import jogar_ppt
from modulos import ler_opcao
from placar import salvar_placar, carregar_placar
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores, buscar
from par_impar2 import jogar_par_ou_impar
from mina import jogar_mina

def mostrar_placar():
    titulo("PLACAR")
    for i in range(len(NOMES_DOS_JOGOS)):
        print(NOMES_DOS_JOGOS[i] + ': ' + str(vezes_jogado[i]) + 'x')



NOME_DO_DONO = "MARGRAF"
OPCOES = ['0', '1', '2', '3', '4', '5']
NOMES_DOS_JOGOS = ['Advinhe o Numero', "Pedra, Papel e Tesoura", "Par ou Impar", "Mina Terrestre"]
vezes_jogado = carregar_placar()
jogadores = carregar_jogadores()

while True:
    titulo( "FLIPERAMA DO " + NOME_DO_DONO)
    print('1 - jogo adivinhe o número')
    print('2 - Pedra, Papel e Tesoura')
    print('3 - Par ou Impar')
    print('4 - Mina Terrestre')
    print('5 - Gerenciar Jogadores')
    print('0 - sair do fliperama')
    linha()
    opcao = ler_opcao('Escolha uma opção', OPCOES)

    if opcao == '0':
        mostrar_placar()
        salvar_placar(vezes_jogado)
        salvar_jogadores(jogadores)
        titulo(" Ate a proxima!")
        break
    if opcao == '5':
        menu_jogadores(jogadores)
    else:
        apelido = input('Quem vai jogar (apelido): ').strip().lower()
        i = buscar(jogadores, apelido)

        if i != -1:
            jogadores[i][2] = str(int(jogadores[i][2]) + 1)

        indice = int(opcao) - 1 
        vezes_jogado[indice] = vezes_jogado[indice] + 1   
         
        if opcao == '1':
           jogar_adivinhe()
        elif opcao == '2':
             jogar_ppt()
        elif opcao == '3':
            jogar_par_ou_impar()
        elif opcao == '4':
            jogar_mina()