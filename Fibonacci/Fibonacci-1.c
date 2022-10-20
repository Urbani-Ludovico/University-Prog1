#include <stdio.h>

int Fbn(int i, int n, int n1, int n2) {
    if (i < n) {
        return Fbn(i+1, n, n2, n1+n2);
    } else {
        return n1 + n2;
    }
}

int main() {
    int n;
    printf("Fn -> Inserisci n :  ");
    scanf("%d", &n);

    if (n >= 0) {
        // If you want to use a normal for loop
        /*int N1 = 0;
        int N2 = 2;
        for (int i = 1; i < n; i++) {
            int tmp = N1 + N2;
            N1 = N2;
            N2 = tmp;
        }
        printf("\nResult = %d\n", N2);*/

        // Using recursive function
        if (n == 0) {
            printf("\nResult = %d\n", 0);
        } else if (n == 1) {
            printf("\nResult = %d\n", 1);
        } else {
            printf("\nResult = %d\n", Fbn(2, n, 0, 1));
        }
    } else {
        printf("\nWarning: N must be greather thank 0\n");
    }
}