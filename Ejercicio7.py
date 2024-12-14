###escribe un programa que invierta los digitos de un numero entero dado por el usuario
# y lo imprima en pantalla

numero = input("Ingrese un número: ")
numero_invertido = ""
for digito in numero:
    numero_invertido = digito + numero_invertido
print(f"El número invertido es: {numero_invertido}")