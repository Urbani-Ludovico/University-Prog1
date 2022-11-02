#include <stdio.h>

void Print_Reverse(int num) {
    if (num < 10 && num > -10)
        printf("%d", num);
    else {
        if (num < 0) {
            printf("-");
            num = 0-num;
        }
        while (num != 0) {
            int n2 = num / 10;
            printf("%d", num - n2*10);
            num = n2;
        }
    }
}

int Reverse(int num) {
    if (num < 10 && num > -10)
        return num;
    else {
        int rev = 0;
        while (num != 0) {
            int n2 = num / 10;
            rev = rev * 10 + (num - n2*10);
            num = n2;
        }
        return rev;
    }
}

void main() {
    int n;
    printf("Inserisci N :  ");
    scanf("%d", &n);

    printf("%d\n", Reverse(n));
    Print_Reverse(n);
}