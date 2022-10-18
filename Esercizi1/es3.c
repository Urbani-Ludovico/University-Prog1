#include <stdio.h>

void main() {
    printf("\n - - - - - CONTADINO RUSSO - - - - - \n\n");

    int n1;
    printf("First number :  ");
    scanf("%d", &n1);

    int n2;
    printf("Second number :  ");
    scanf("%d", &n2);

    int res = 0;

    printf("\nPROBLEM :  %d x %d = ?\n\n", n1, n2);
    printf("\t             n1 | n2\n");
    printf("\t     ---------- | ----------\n");
    while (n1 > 0) {
        printf("\t%15d | %-15d", n1, n2);
        if (n1 % 2 != 0) {
            res = res + n2;
            printf("  <--");
        }
        printf("\n");
        n1 = n1 / 2;
        n2 = n2 * 2;
    }
    printf("\nRESULT :  %d", res);
}