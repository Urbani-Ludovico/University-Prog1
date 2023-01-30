
#include <stdio.h>


int my_fun(float a[], int n, int k) {
    for (int i = 0; i < n-2; i++) {
        if (k == a[i] + a[i+1] + a[i+2]) return 0;
    }
    return 1;
}

void main() {

    float a[10] = {0,1,2,3,4,5,6,7,8,9};

    printf("Res True: %d\n", my_fun(a, 10, 9));
    printf("Res False: %d\n", my_fun(a, 10, 8));
}