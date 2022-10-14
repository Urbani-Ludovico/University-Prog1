#include <stdio.h>

void main() {
  int cnt = 0;
  int sum = 0;
  int last = -1;

  printf("\nInsert inputs [0 for end]\n\n");
  
  while (last != 0) {
    printf("\tInput %d :  ", cnt + 1);
    scanf("%d", &last);

    if (last > 0) {
      sum = sum + last;
      cnt++;
    }
  }
  printf("\nAverage = %f\n\n", (float)sum / cnt);
}