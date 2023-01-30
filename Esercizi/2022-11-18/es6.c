
#include <stdio.h>

int card_Si(float a[], int n, int i) {
    int c = 0;
    for (int j = 0; j < n; j++) {
        if (a[j] <= a[i]) c++;
    }
    return c;
}

float my_fun(float a[], int n, int k) {
    for (int i = 0; i < n; i++) {
        if (k == card_Si(a, n, i)) return a[i];
    }
    return 0;
}

void main() {

    float a[10] = {0,1,2,3,4,5,6,7,8,9};

    printf("Res: %f\n", my_fun(a, 10, 8));
}