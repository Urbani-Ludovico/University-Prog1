#include <stdio.h>

float P(float n) {
    return n * n;
}

float F1(float n) {
    if (n == 0)
        return 1;

    return 1 / (P(2 * n + 1)) + F1(n - 1);
}

void main () {
    int n;
    printf("Inserisci N :  ");
    scanf("%d", &n);

    if (n > 0) {
        printf("\nRESULT (N = %d):\n", n);
        printf("\tF1  ->  %f\n", F1(n));
    } else {
        printf("\nWarning: N must be greater then 0!\n");
    }
}