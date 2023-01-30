

#include <stdio.h>

float my_fun(float a[], float b[], int n) {
    int s = 0;

    for (int i = 0; i < n; i++) {
        s = s + a[i] * b[i];
    }

    return s;
}

void main() {

    float a[10] = {0,1,2,3,4,5,6,7,8,9};
    float b[10] = {0,1,2,3,4,5,6,7,8,9};

    printf("Res: %f\n", my_fun(a, b, 10));
}