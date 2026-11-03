/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1551 - Frase completa
 * Autor     : Margraf
 * LIAC      : Leia N frases, só com letras minúsculas e espaços. Para cada uma, conte quantas letras diferentes do alfabeto aparecem: 26 é "frase completa"; de 13 a 25, "frase quase completa"; menos de 13, "frase mal elaborada".
 */

 #include <iostream>
#include <string>
using namespace std;

int conta_letras(string frase) {
    int total = 0, i, tam = frase.size();
    char letra;
    bool achou;

    for (letra = 'a'; letra <= 'z'; letra++) {
        achou = false;
        for (i = 0; i < tam; i++) {
            if (frase[i] == letra) {
                achou = true;
            }
        }
        if (achou) {
            total++;
        }
    }
    return total;
}

int main() {
    int n, i, letras;
    string frase;

    cin >> n;
    cin.ignore();
    for (i = 0; i < n; i++) {
        getline(cin, frase);
        letras = conta_letras(frase);
        if (letras == 26) {
            cout << "frase completa" << endl;
        } else if (letras >= 13) {
            cout << "frase quase completa" << endl;
        } else {
            cout << "frase mal elaborada" << endl;
        }
    }

    return 0;
}