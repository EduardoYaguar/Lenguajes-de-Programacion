#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int total_pares = 0;
    int total_impares = 0;
    int num = 0;

    
    srand(time(0));

    for (int i = 0; i < 500; i++) {
        num = rand() % 101; 
        if (num % 2 == 0) {
            total_pares++;
        } else {
            total_impares++;
        }
    }

    printf("La cantidad de valores pares generados son: %d\n", total_pares);
    printf("La cantidad de valores impares generados son: %d\n", total_impares);

    return 0;
}
