#include <stdio.h>
#include <math.h>

double An1_p (double p, int n) {
    if (n == 1) {
        //printf("N = %-6d ->    %.30e\n", n, p);
        return p;
    } else {
        double p2 = An1_p(p, n-1);
        double v = (double)0.5 * (p2 + p / p2);
        //printf("N = %-6d ->    %.30e\n", n, v);
        return v;
    }
}

void main () {
    double p;
    printf("Inserisci P (double) :  ");
    scanf("%lf", &p);

    int n;
    printf("Inserisci N (int) :  ");
    scanf("%d", &n);

    if (n >= 1) {
        printf("\nRESULT:\n\tA(n+1,p)  =  %.30e\n\tsqrt(p)   =  %.30e", An1_p(p, n+1), sqrt(p));
    } else {
        printf("\nWarning: N must be equal or greater than 1!\n");
    }
}