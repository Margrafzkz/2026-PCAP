/*
Disciplina  : 2026-PCAP
Problema    : beecrowd 1179
Autor       : Matheus Margraf
LIAC        : Leia quinze inteiros. Os pares vão para um vetor de cinco posições, os ímpares para outro. Cada vez que um dos dois enche, mostre-o (posição e valor) e esvazie-o. No fim, mostre o que sobrou: primeiro os ímpares, depois os pares. 
*/

#include <stdio.h>

void mostrar(int v[], int qtd, int eh_par) {
    int i;

    for (i = 0; i < qtd; i++) {
        if (eh_par) {
            printf("par[%d] = %d\n", i, v[i]);
        } else {
            printf("impar[%d] = %d\n", i, v[i]);
        }
    }
}

int main() {
    int par[5], impar[5];
    int qtd_par = 0, qtd_impar = 0, i, x;

    for (i = 0; i < 15; i++) {
        scanf("%d", &x);
        if (x % 2 == 0) {
            par[qtd_par] = x;
            qtd_par = qtd_par + 1;
            if (qtd_par == 5) {
                mostrar(par, qtd_par, 1);
                qtd_par = 0;
            }
        } else {
            impar[qtd_impar] = x;
            qtd_impar = qtd_impar + 1;
            if (qtd_impar == 5) {
                mostrar(impar, qtd_impar, 0);
                qtd_impar = 0;
            }
        }
    }

    mostrar(impar, qtd_impar, 0);
    mostrar(par, qtd_par, 1);

    return 0;
}