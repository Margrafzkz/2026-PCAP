# Fliperama em C (MeuApp v3.0)

## O que e
Trata-se de um sistema de fliperama em C onde os jogadores criam o seu perfil, jogam à adivinhação e o programa guarda o progresso num ficheiro.

## Como compilar e rodar
gcc -Wall fliperama.c -o fliperama
./fliperama

## Arquivos
- fliperama.c: ah pasta main do fliperama
- jogadores.csv: guarda informação dos jogadores registrados

## Python x C: o que mudou
| O que | No jogadores.py (linha) | No fliperama.c (linha) |
|---|---|---|
| guardar um jogador | jogadores.append(novo) (l. 29) | strcpy(apelidos[qtd], novo) (l. 76) |
| comparar apelidos | == (l. 64) | strcmp(...) == 0 (l. 53) |
| abrir sem arquivo | open(ARQUIVO, 'r') (l. 132) | fopen == NULL (l. 138) |

## O que o C me obrigou a decidir
O Python gerenciava o tamanho das listas de forma dinâmica com o `.append()`, enquanto no C precisei definir manualmente o tamanho limite do vetor e usar a função `strcpy` para manipular strings em posições pré-alocadas de memória.

## Autoavaliacao
| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura, compilacao e Git | B | README.md e histórico de commits do Git |
| 2. Cadastro: menu, funcoes e vetores | A | fliperama.c (l. 53, l. 76) |
| 3. Jogo e partidas | B | fliperama.c (l. 164) |
| 4. Persistencia | B | fliperama.c (l. 125, l. 135, l. 138) |
| 5. Documentacao e comparacao | A | README.md (seção Python x C) |