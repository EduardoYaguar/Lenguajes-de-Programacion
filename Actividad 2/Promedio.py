print("Ingrese 10 numeros enteros")
try:
    total_sum = 0
    for i in range(10):
        num = int(input(f"Valor {i+1}: "))
        total_sum += num
    print(f"El valor de la sumatoria es: {total_sum}")
    print(f"El promedio es: {total_sum / 10}")

except ValueError:
    print("Ingrese solo números enteros.")
