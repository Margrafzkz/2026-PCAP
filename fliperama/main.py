#==============================================
# Arquivo:    main.py
# Disciplina: 2026-PCAP
# Aula:       20
# Autor:      Margraf 
# Data:       2026.08.04
# Conceitos: 
#==============================================

# imporatar funções d arquivos (módulos)
from telas import titulo, linha
from adivinhe import jogar_adivinhe
from modulos import ler_opcao

NOME_DO_DONO = "MARGRAF"
OPCOES = ['0', '1']
while True:
    titulo( "FLIPERAMA DO " + NOME_DO_DONO)
    print('1 - jogo adivinhe o número')
    print('0 - sair do fliperama')
    linha()
    opcao = ler_opcao('Escolha uma opção', OPCOES)

    if opcao == '0':
        print('Até a próxima!')
        break
    elif opcao == '1':
        jogar_adivinhe()
    else:
        print('Opção invalida! Tente novamente.')    