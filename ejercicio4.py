### Ejercicio 4 

### Escribe un programa que determine si un numero dado por el usuario es un numero perfecto
# Un numero perfecto es un numero entero positivo que es igual a la suma de sus divisores propios positivos (excluyendo el propio numero) 
# Por ejemplo, 28 es un numero perfecto porque 1 + 2 + 4


def es_perfecto(n):
    suma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n

numero = int(input("Ingrese un numero: "))
if es_perfecto(numero):
    print(f"El numero {numero} es perfecto")
else:
    print(f"El numero {numero} no es perfecto")