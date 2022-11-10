#include <stdio.h>

int conta(int n)
{
    int conta = 1;
    while (n > 10)
    {
        n = n / 10;
        conta = conta * 10;
    }
    return conta;
}

int scambia(int n)
{
    if (n < 10)
        return n;
    else
        return (n % 10) * conta(n) + scambia(n / 10);
}
int main()
{
    int n;
    printf("inserisci un numero: \n");
    scanf("%d", &n);
    if (n > 0)
    {
        int s_n;
        s_n = scambia(n);
        printf("il valore trovato è %d\n", s_n);
    }
    else
    {
        printf("inserire n maggiore di zero\n");
    }
}