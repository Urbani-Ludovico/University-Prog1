#include <stdio.h>

void main() {
    int n;
    printf("Insert n [>0]: ");
    scanf("%d", &n);

    int k;
    printf("Insert k: ");
    scanf("%d", &k);

    if (n > 0){
        int res = 0;
        for (int i = 1; i <= n; i++) {
            int k2 = 1;
            for (int i2 = 1; i2 <= i; i2++) {
                k2 = k2 * k;
            }
            res = res + k2;
        }

        printf("Result = %d\n", res);
    } else {
        printf("Warning: n must be greater than 0\n");
    }
}