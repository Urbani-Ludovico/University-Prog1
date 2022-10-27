#include <stdio.h>

int F1(int n, int k) {
    if (n == k)
        return k;
    else
        return k + F1(n, k + 1);
}

int F2(int a, int b) {
    int s = F1(a, 0);
    for (int i = a + 1; i <= b; i++) {
        s = 2 * s + i;
    }
    return s;
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

    if (n > 0 && a <= b) {
        printf("\nRESULT (N = %d):\n", n);
        printf("\tF1  ->  %d\n", F1(n, 0));
        printf("\tF2  ->  %d\n", F2(a, b));
    } else {
        printf("\nWarning: N must be equal or greater then 1 and A must be equal or less then B!\n");
    }
}