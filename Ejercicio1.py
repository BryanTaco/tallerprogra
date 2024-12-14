### Ejercicio tabla de multiplicar personalizada
### Escribe un programa que le pida al usuario un numero entero positivo. Luego, solicita al usuario un rango inicial y final para la tabla de multiplicar.
### El programa debe imprimir la tabla de multiplicar del número entero solicitado por el usuario,
### dentro del rango especificado por el usuario.

 
num = int(input("Ingrese un número entero positivo: "))
rango_inicial = int(input("Ingrese el rango inicial: "))
rango_final = int(input("Ingrese el rango final: "))

if num > 0:

    for i in range(rango_inicial, rango_final + 1):
        print(f"{num} x {i} = {num * i}")
    else:
        print("Tabla de multiplicar")
else:
    print("El número ingresado no es positivo")


