#include <stdio.h>

int main() {
    int sucursales[25];
    float ventas[25];
    float suma_ventas = 0, promedio;

    for (int i = 0; i < 25; i++) {
        sucursales[i] = i + 1;
        printf("Ingrese las ventas de la sucursal %d: ", sucursales[i]);
        scanf("%f", &ventas[i]);
        suma_ventas += ventas[i];
    }

    promedio = suma_ventas / 25;

    printf("\nEl promedio de ventas es: %.2f\n", promedio);

    printf("Sucursales con ventas mayores al promedio:\n");
    for (int i = 0; i < 25; i++) {
        if (ventas[i] > promedio) {
            printf("Sucursal %d con ventas de: %.2f\n", sucursales[i], ventas[i]);
        }
    }

    return 0;
}
