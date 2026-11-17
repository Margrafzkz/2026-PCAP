/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 1168 - LED
 * Autor     : Margraf
 * LIAC      : N números, cada um como texto (podem ter vinte algarismos); para cada um, soma quantos leds cada algarismo acende num visor de sete segmentos
 */

#include <iostream>
#include <string>
using namespace std;

int main() {
    int leds_por_digito[10] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};
    
    int n;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        string numero;
        cin >> numero;
        
        int total_leds = 0;
        
        for (int j = 0; j < numero.length(); j++) {
            int digito = numero[j] - '0';
            total_leds += leds_por_digito[digito];
        }
        
        cout << total_leds << " leds" << endl;
    }
    
    return 0;
}