#include <stdio.h>

int main() {
  int x;
  printf("\nPrimo numero :  ");
  int n = scanf("%d", &x);

  int y;
  printf("Secondo numero :  ");
  n = scanf("%d", &y);

  while (x != y) {
    if (x > y)
      x = x - y;
    else
      y = y - x;
  }

  printf("\nMCD = %d\n\n", x);
  
  return 0;
}