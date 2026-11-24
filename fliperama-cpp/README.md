# Fliperama em C++ (MeuApp v4.0)

## O que e
Um aplicativo de console de fliperama com menu validado, cadastro e exclusão dinâmica de jogadores e o jogo "Adivinhe o Número" com contagem de partidas e salvamento imediato em arquivo.


## Como compilar e rodar
g++ -Wall fliperama.cpp -o fliperama
./fliperama

## Arquivos
- fliperama.cpp: Código-fonte completo do programa contendo o menu, o jogo, o cadastro/exclusão de jogadores e a manipulação de arquivos.
- jogadores.csv: Arquivo de persistência onde cada linha armazena o apelido do jogador (coluna 1) e sua quantidade de partidas jogadas (coluna 2), separados por vírgula.

## C x C++: o que mudou
| O que | No fliperama.c (linha) | No fliperama.cpp (linha) |
|---|---|---|
| guardar um jogador | strcpy(apelidos[qtd], novo) (l. 74) | apelidos.push_back(novo) (l. 98) |
| comparar apelidos | strcmp(...) == 0 (l. 50) | == (l. 55) |
| a funcao que cadastra | int cadastrar(..., int qtd) (l. 57) | void cadastrar(... &apelidos, ...) (l. 87) |
| abrir arquivo para salvar | FILE *arquivo = fopen(..., "w") (l. 117) | ofstream arquivo(ARQUIVO) (l. 63) |
| abrir arquivo para carregar | FILE *arquivo = fopen(..., "r") (l. 127) | ifstream arquivo(ARQUIVO) (l. 72) |
| limite de cadastro | if (qtd >= CAPACIDADE) (l. 62) | Não existe (vector cresce dinamicamente) |

## O que o C++ decidiu por mim
Em C, eu precisava gerenciar manualmente a capacidade máxima dos vetores (`CAPACIDADE 50`) e o tamanho das strings (`TAM_APELIDO 20`); em C++, o `std::vector` e o `std::string` gerenciam a alocação de memória e o crescimento dinâmico automaticamente através do `.push_back()` e `.size()`.
Além disso, a função `cadastrar` deixou de devolver `int` porque o `vector` agora é passado por referência (`&`) e guarda o próprio tamanho internamente (`.size()`), dispensando o retorno manual de uma variável `qtd` atualizada para o `main`.

## Autoavaliacao
| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura, compilacao e Git | B | fliperama.cpp (l. 1-17) e histórico do Git |
| 2. Cadastro: vectors e referencia | B | fliperama.cpp (l. 87-102, 104-121, 123-133) |
| 3. Jogo e partidas | B | fliperama.cpp (l. 135-166) |
| 4. Persistencia | B | fliperama.cpp (l. 62-85, 100, 119, 165, 198) |
| 5. Documentacao e comparacao | B | fliperama.cpp (l. 1-6) e README.md |