#include <stdio.h>

void main() {
    float n;
    printf("Inserire x: ");
    scanf("%f", &n);

    if (n >= 0) {
        printf("%f è positivo\nValore assoluto: %f\n", n, n);
    } else {
        printf("%f è negativo\nValore assoluto: %f\n", n, -n);
    }
}