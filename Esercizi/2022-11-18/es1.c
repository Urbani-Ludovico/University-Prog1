
#include <stdio.h>

int funcS(int a[], int n) {
    int s = 0;

    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0) {
            s = s + a[i];
        }
    }

    return s;
}

void main() {

    int a[10] = {0,1,2,3,4,5,6,7,8,9}; 
     
    printf("Res: %d\n", funcS(a, 10));
}