##EJERCICIO DE NUMERO PRIMOS EN UN RANGO

numero_inicial = int(input("Por favor, ingresa el numero inicial: "))
numero_final = int(input("Por favor, ingresa el numero final: "))



if numero_inicial < 1 or numero_final < 1 or numero_inicial > numero_final:
    print("Por favor, asegúrate de que ambos números sean enteros positivos y que el número inicial sea menor final.")
else:
    print(f"Los números primos entre {numero_inicial} y {numero_final}")
    for num in range(numero_inicial, numero_final + 1):
        if num < 2:
            continue
        es_primo = True  
        for i in range(2, num):  
            if num % i == 0:
                es_primo = False  
                break
        if es_primo:
            print(num)