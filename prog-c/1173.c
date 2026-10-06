/*
Disciplina  : 2026-PCAP
Problema    : beecrowd 1175 
Autor       : Matheus Margraf
LIAC        :Leia um inteiro e guarde em N[0]. Preencha as posições de 1 a 9 com o dobro da posição anterior. Mostre o vetor. 
*/

#include <stdio.h>

int main() {
    int n[10], i;

    scanf("%d", &n[0]);

    for (i = 1; i < 10; i++) {
        n[i] = n[i - 1] * 2;
    }

    for (i = 0; i < 10; i++) {
        printf("N[%d] = %d\n", i, n[i]);
    } 
    
    
    return 0;
}