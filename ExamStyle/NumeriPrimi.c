#include <stdio.h>

int Iter(int n) {
    for (int i=2; i < n; i++) {
        if (n % i == 0)
            return 0;
    }
    return 1;
}

int Rec(int n, int k) {
    if (n == 1)
        return 1;
    else if (k == n)
        return 1;
    else if (n % k == 0)
        return 0;
    else
        return Rec(n, k+1);
}

void main () {
    int n;
    printf("Inserisci N :  ");
    scanf("%d", &n);

    if (n > 0) {
        printf("\nRESULT (N = %d):\n", n);
        printf("\tIterative  ->  %s\n", Iter(n) ? "PRIMO" : "NON PRIMO");
        printf("\tRecursive  ->  %s\n", Rec(n, 2) ? "PRIMO" : "NON PRIMO");
    } else {
        printf("\nWarning: N must be equal or greater than 1!\n");
    }

    printf("\nPrimi da 1 a 100:\n");
    int tot = 0;
    float distanze = 0;
    int prec = -1;
    for (int i = 1; i <= 100; i++) {
        if (Iter(i) == 1) {
            tot++;
            if (prec != -1){
                distanze = distanze + (i - prec);
            }
            prec = i;
        }
    }
    printf("\tTot numeri = %d\n\tMedia distanze = %f", tot, distanze / (tot - 1));
}