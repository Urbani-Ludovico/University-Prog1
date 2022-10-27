#include <stdio.h>

int F1(int n, int k) {
    if (k == n)
        return 1;

    return 2 * F1(n, k+1);
}

float F2(float a, int b) {
    if (a > b/2)
        return -b;

    float res = 1;
    for (int i=(int)a; i <= b/2; i++) {
        res = res * (F1(i, 0) / a);
    }
    return res - b;
}

void main () {
    int n;
    printf("Inserisci N :  ");
    scanf("%d", &n);

    int a;
    printf("Inserisci A :  ");
    scanf("%d", &a);

    int b;
    printf("Inserisci B :  ");
    scanf("%d", &b);

    if (n >= 0 && a <= b) {
        printf("\nRESULT (N = %d):\n", n);
        printf("\tF1  ->  %i\n", F1(n, 0));
        printf("\tF2  ->  %f\n", F2(a, b));
    } else {
        printf("\nWarning: N must be equal or greater then 0 and A must be equal or less then B!\n");
    }
}