
#include <stdio.h>
#include <stdlib.h>

void printA(int a[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d\n",a[i]);
    }
}

// - - - - - ES 1 - - - - -
int removeDup_Find(int a[], int n2, int x) {
    for (int i = 0; i < n2; i++) {
        if (a[i] == x) return 0;
    }
    return 1;
}

int * removeDup(int a[], int n) {
    // first element is the size of new the array
    int * a2 = (int *)malloc(sizeof(int) * (n + 1));
    int count = 1;

    for (int i=0; i < n; i++) {
        if (removeDup_Find(a, i, a[i])) {
            *(a2 + count) = a[i];
            count++;
        }
    }
    
    *a2 = count-1;
    return a2;
}

// - - - - - ES 2 - - - - - -

void K_order_swap(int * a, int i1, int i2) {
    int tmp = *(a + i1);
    *(a + i1) = *(a + i2);
    *(a + i2) = tmp;
}

void K_order(int a[], int n, int k) {
    int m = 0;
    int M = n-1;
    while (m <= M) {
        if (a[m] <= k) {
            m++;
        } else {
            K_order_swap(a, m, M);
            M--;
        }
    }
}

int K_order_check(int a[], int n) {
    for (int j = 0; j < n; j++) {
        int j_correct = 1;
        for (int i = 0; i < n; i++) {
            if (i <= j && a[i] >= j) j_correct = 0;
            if (i > j && a[i] <= j) j_correct = 0;
        }
        if (j_correct == 1) return j;
    }
    return -1;
}

// - - - - - ES 3 - - - - - -
int * sum_order(int a[], int n, int b[], int m) {
    int * c = (int *)malloc(sizeof(int) * (n+m));
    int n2 = 0;
    int m2 = 0;
    int c2 = 0;
    while (n2 < n || m2 < m) {
        if (n2 == n || (m2 != m && a[n2] >= b[m2])) {
            c[c2] = b[m2];
            m2++;
        } else {
            c[c2] = a[n2];
            n2++;
        } 
        c2++;
    }
    return c;
}

void main() {

    printf("\nES 1\n");
    int a[10] = {1,2,3,4,1,5,2,8,8,7};
    int * a2 = (int *)removeDup(a, 10);
    int removeSize = *a2;
    a2++;
    printA(a2, removeSize);


    printf("\nES 2\n");
    int b[10] = {5,1,6,2,4,8,3,5,7,2};
    K_order(b, 10, 5);
    printA(b, 10);

    int b1[5] = {1,1,1,6,6};
    int b2[5] = {1,5,2,3,5};
    printf("j(b1): %d\nj(b2): %d\n", K_order_check(b1, 5), K_order_check(b2, 5));


    printf("\nES 3\n");
    int c[4] = {1,2,3,4};
    int d[6] = {1,3,5,7,9,11};
    int * c2 = (int *)sum_order(c, 4, d, 6);
    printA(c2, 10);

}