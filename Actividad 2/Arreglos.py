
sucursales = list(range(1, 26))
ventas = []
suma_ventas = 0

for i in range(25):
    venta = float(input(f"Ingrese las ventas de la sucursal {sucursales[i]}: "))
    ventas.append(venta)
    suma_ventas += venta

promedio = suma_ventas / 25

print(f"\nEl promedio de ventas es: {promedio:.2f}")

print("Sucursales con ventas mayores al promedio:")
for i in range(25):
    if ventas[i] > promedio:
        print(f"Sucursal {sucursales[i]} con ventas de: {ventas[i]:.2f}")
