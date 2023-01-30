
#include <stdio.h>

// 0 = True
// 1 = False
int my_fun(float a[], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i!=j && a[i] == a[j]) return 1;
        }
    }
    return 0;
}

void main() {

    float a[10] = {0,1,2,3,4,5,6,7,8,9}; 
     
    printf("Res True: %d\n", my_fun(a, 10));

    a[1] = 2;
     
    printf("Res False: %d\n", my_fun(a, 10));
}