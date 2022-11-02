#include <stdio.h>

float Power(float k, int n) {
    if (n == 0)
        return 1;
    else
        return k * Power(k, n - 1);
}

float F1(int n, float k) {
    if (n >= 1) {
        return (n * Power(k, n + 1)) / Power(3, n) + F1(n-1, k);
    } else
        return 0;
}

void main () {
    int n;
    printf("Inserisci N :  ");
    scanf("%d", &n);

    float k;
    printf("Inserisci N :  ");
    scanf("%f", &k);


    if (n >= 1) {
        printf("\nRESULT (N = %d, K = %f):\n", n, k);
        printf("\tF1  ->  %f\n", F1(n, k));
    } else {
        printf("\nWarning: N must be equal or greater then 1!\n");
    }
}