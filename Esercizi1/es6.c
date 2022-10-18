#include <stdio.h>

void main() {
    printf(" - - - - - POWER - - - - -\n");

    int a;
    printf("\nBase :  ");
    scanf("%d", &a);

    int b;
    printf("Power :  ");
    scanf("%d", &b);

    int res = a;

    if (b > 0) {
        for (int i = 1; i < b; i++) {
            res = res * a;
        }

        printf("\nRESULT :  %d ^ %d = %d\n\n", a, b, res);
    } else {
        printf("\nPower must be > 0!");
    }

}