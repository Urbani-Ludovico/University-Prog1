#include <stdio.h>

// Function for evaluating SUCCESSIONE using recursive mode, from a value given by user.
int Succ_Rec(a) {
    if (a > 0)
        return 2 * Succ(a-1) + 3;
    else
        return 1;
}

// Function for evaluating SUCCESSIONE using iterative mode, from a value given by user.
int Succ_Iter(a) {
    int res = 1;
    for (int i = 1; i <= a; i++) {
        res = 2 * res + 3;
    }
    return res;
}

// Function for evaluating QUANTITÀ using recursive mode, from a value given by user.
int Quant_Rec(a) {

}


void main() {
    /*int n;
    printf("Inserisci N :  ");
    scanf("%d", &n);*/
}