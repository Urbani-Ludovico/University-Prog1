#include <stdio.h>

double An(int n) {
    if (n == 1) {
        printf("N = 1 -> 0.5\n");
        return (double)0.5;
    }
    else {
        double v = (An(n-1) + 1) / 2.0;
        printf("N = %-6d -> %.30e\n", n, v);
        return v;
    }
}

void main () {
    int n;
    printf("Inserisci N :  ");
    scanf("%d", &n);

    if (n >= 1) {
        printf("\nRESULT:\n\tN = %d  ->  %.30e\n", n, An(n));
    } else {
        printf("\nWarning: N must be equal or greater than 1!\n");
    }
}