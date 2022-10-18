#include <stdio.h>

void main() {
    printf("\n - - - - - - MIN and MAX - - - - -\n");
    int m;
    int M;
    int isFirst = 1;

    printf("\nInsert numbers [0 for break]\n\n");
    int i = 1;
    while (1) {
        int n;
        printf("\tN %5d :  ", i);
        scanf("%d", &n);

        if (n == 0) break;
        else {
            if (isFirst == 1) {
                m = n;
                M = n;
                isFirst = 0;
            } else {
                if (n < m) m = n;
                if (n > M) M = n;
            }
        }

        i++;
    }

    if (isFirst == 1) {
        printf("\nWarning: Input is empty!\n\n");
    } else {
        printf("\nMIN = %d\nMAX = %d\n\n", m, M);
    }
}