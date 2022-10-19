#include <stdio.h>

void main() {
    int n;
    printf("Insert n [>0]: ");
    scanf("%d", &n);

    int k;
    printf("Insert k: ");
    scanf("%d", &k);

    if (n >= k){
        int res = 1;
        for (int i = n; i > 0; i--) {
            if (i > n - k) // n! / (n-k)! => exclude all factors < n-k
                res = res * i;
            if (i <= k) // 1/k! complete (n k) removing k!
                res = res / i;
        }

        printf("Result = %d\n", res);
    } else {
        printf("Result = 0\n");
    }
}