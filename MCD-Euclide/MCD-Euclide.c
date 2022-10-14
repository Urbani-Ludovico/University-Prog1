#include <stdio.h>

void main() {
  int x;
  printf("\nPrimo numero :  ");
  scanf("%d", &x);

  int y;
  printf("Secondo numero :  ");
  scanf("%d", &y);

  while (x != y) {
    if (x > y)
      x = x - y;
    else
      y = y - x;
  }

  printf("\nMCD = %d\n\n", x);
}