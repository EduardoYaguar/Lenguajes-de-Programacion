#include <stdio.h>

int main() {
    int i = 0;
    int num =0;
    int sum =0;
    float promedio;

    printf("Ingrese 10 numeros enteros:\n");

    for (i = 0; i < 10; i++) {
        printf("Valor %d: ", i + 1);
        if (scanf("%d", &num) != 1) {
            printf("Ingrese solo numeros enteros.\n");
            return 1;
        }
        sum += num;
    }

    promedio = sum / 10.0;
    printf("El valor de la sumatoria es: %d\n", sum);
    printf("El promedio es: %.2f\n", promedio);

    return 0;
}
