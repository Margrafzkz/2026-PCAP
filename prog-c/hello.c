/* Comentário de bloco
Progama: hello.c
data: 2026.09.22
autor: Margraf  
*/

// importa blibioteca padrão de entrada e saída 
#include <stdio.h>

// defino a função principal do tipo int
int main(){
    // printf == Saída --> Mostra na Tela ; 
    // "entre aspas == texto" ; comando se encerra     
    printf("Hello World!\n");

    // Receber 2 valores somar e mostrar o resultado 
    int num1=0, num2=0, soma=0;

    // recebe o primeiro valor 
    printf("Digite o primeiro número: ");
    scanf("%d", &num1);

    // recebe o segundo valor 
    printf("Digite o segundo número: ");
    scanf("%d", &num2);

    // realiza a soma dos dois valores 
    soma = num1 + num2;

    // Exibe o resultado da soma na tela
    printf("A soma de %d + %d é igual a %d\n", num1, num2, soma);

    // indica que chegou ao fim da função == retornando 0
    return 0;
}

/*
para compilar == 
gcc <nome-do-arquivo> -o nome-do-programa

para executar 
./nome-do-programa

*/