
#include <stdio.h>

int my_fun(float a[], float b[], int n, int m) {
    float s_B = 0;

    for (int i = 0; i < m; i++) {
        s_B = s_B + b[i];
    }

    for (int i = 0; i < n; i++) {
        if (a[i] == s_B) return 0;
    }

    return 1;
}

void main() {

    float a[10] = {0,1,2,3,4,5,6,7,8,9};
    float b[8] = {0,1,2,3,4,5,6,7};

    printf("Res False: %i\n", my_fun(a, b, 10, 8));

    a[1] = 28;
    printf("Res True: %i\n", my_fun(a, b, 10, 8));
}