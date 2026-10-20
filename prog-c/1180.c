/*
Disciplina  : 2026-PCAP
Problema    : beecrowd 1180
Autor       : Matheus Margraf
LIAC        : Leia N e depois N inteiros. Mostre o menor valor e a posição em que ele está, contando a partir de zero. 
*/

#include <stdio.h>

int posicao_do_menor(int v[], int n) {
    int i, pos = 0;

    for (i = 1; i < n; i++) {
        if(v[i] < v[pos]) {
            pos = i;
        }
    }
    return pos;
}

int main() {
    int v[1000], n, i, pos;

    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    pos = posicao_do_menor(v, n);

    printf("Menor valor: %d\n", v[pos]);
    printf("Posicao: %d\n", pos);

    return 0;
}