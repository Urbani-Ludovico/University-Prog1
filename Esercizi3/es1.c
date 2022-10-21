#include <stdio.h>

int GetMin(int n1, int n2, int n3) {
    if (n1 <= n2 && n1 <= n3)
        return n1;
    else if (n2 <= n3 & n2 <= n1)
        return n2;
    return n3;
}

void Output(int x, int y, int w) {
    printf("\t( %d, %d, %d)    ->    MIN = %d\n", x, y, w, GetMin(x, y, w));
}

void main() {
    int x, y, w;

    printf("Inserisci X :  ");
    scanf("%d", &x);

    printf("Inserisci Y :  ");
    scanf("%d", &y);

    printf("Inserisci W :  ");
    scanf("%d", &w);

    printf("\nRESULT:\n");
    Output(x, y, w);

    if (x > 1 || y > 1) {
        printf("\nTESTS:\n");
        
        for (int i = 1; i <= x || i <= y; i++) {
            Output(x, y, i);
        }
    } else {
        printf("\nWarning: For exec tests, X or Y must be greater than 1!\n");
    }
}