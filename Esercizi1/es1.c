#include <stdio.h>

void main() {
  int n;
  printf("Numero intero :  ");
  scanf("%d", &n);

  if (n > 0) {
    printf("\nQuadrati perfetti:\n");
    for (int i = 1; i <= n; i++) {
      printf("\t%d  =>  %d\n", i, i*i);
    }
  } else {
    printf("\nToo small number!\n\n");
  }
}