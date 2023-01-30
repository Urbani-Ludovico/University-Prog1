
#include <stdio.h>

int my_fun(int a[], int * b, int n) {
    int b_count = 0;
    for (int i = 0; i < n; i++) {
        int t = 0;
        for (int j = 0; j < n; j++) {
            if (i != j && a[j] != 0 && a[i] != 0 && (a[i] % a[j] == 0)) {
                t = 1;
            }
        }
        if (t == 0) {
            *(b + b_count) = a[i];
            b_count++;
        }
    }
    return b_count;
}

void main() {

    int a[10] = {0,1,2,3,4,5,6,7,8,9};
    int b[10] = {0,0,0,0,0,0,0,0,0,0};
    
    int els = my_fun(a, b, 10);

    for (int i = 0; i < els; i++) {
        printf("%d\n", b[i]);
    }
}