#include <stdio.h>
#include <math.h>

float Distanza(float p1x, float p2x, float p1y, float p2y) {
    return sqrt(
        powf(p1x - p2x, 2) + powf(p1y - p2y, 2)
    );
}

void main() {
    float p1x, p2x, p1y, p2y;

    printf("Punto P1:\n\tP1 -> X :  ");
    scanf("%f", &p1x);
    printf("\tP1 -> Y :  ");
    scanf("%f", &p1y);

    printf("\nPunto P2:\n\tP2 -> X :  ");
    scanf("%f", &p2x);
    printf("\tP2 -> Y :  ");
    scanf("%f", &p2y);

    printf("\nDistanza Euclidea = %f", 
        Distanza(p1x, p2x, p1y, p2y)
    );
}