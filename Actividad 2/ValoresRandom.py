import random as rd
total_impares = 0
total_pares = 0

for x in range(500):

    num = rd.randint(0,100)
    if num%2 ==1:
        total_impares +=1
    else:
        total_pares +=1

print(f"La cantidad de valores pares generados son: {total_pares}")
print(f"La cantidad de valores pares generados son: {total_impares}")