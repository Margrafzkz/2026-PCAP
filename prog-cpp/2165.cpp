/*
 * Disciplina: 2026-PCAP
 * Problema  : beecrowd 2165 - Twitting
 * Autor     : Margraf
 * LIAC      : Leia uma linha de texto. Se ela tem até 140 caracteres, mostre TWEET; se tem mais, mostre MUTE.
 */

 #include <iostream>
 #include <string>
 using namespace std;

 int main() {
    string texto;

    getline(cin, texto);
    if (texto.size() <= 140) {
        cout << "TWEET" << endl;
    } else {
        cout << "MUTE" << endl;
    } 

    return 0;
 }