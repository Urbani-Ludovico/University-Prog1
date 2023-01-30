
#include <stdio.h>

void my_fun(int * a, int n) {
    int s = 0;
    for (int i = 0; i < n; i++) {
        s = s + i + 1;
        *(a + i) = s;
    }
}

void main() {

    int a[10];
    my_fun(&(a[0]), 10);

    for (int i = 0; i < 10; i++) {
        printf("%i\n", a[i]);
    }
}