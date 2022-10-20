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
            // If k > n-k then number betwheen k and n-k , shud be factors and divisors. So we can exclude this numbers.
            // Not using three IF, we can add && ... in each cond block
            if (i > n - k && i > k) // n! / (n-k)! => exclude all factors < n-k && factors that should be revoved by k!
                res = res * i;
            if (i <= k && i <= n - k) // 1/k! complete (n k) removing k! (excluded factors that should be added by n!)
                res = res / i;
        }

        printf("Result = %d\n", res);
    } else {
        printf("Result = 0\n");
    }
}