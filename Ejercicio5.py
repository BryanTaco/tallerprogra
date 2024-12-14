#escribe un programa que convierte un numero decimal dado por el usuario
#a su equivalente en el sistema octal

numero_decimal=int(input("ingrese un numero decimal:"))
if(numero_decimal < 0):
    print("ingrese un numero positivo decimal:")
else:
    numero = numero_decimal
    octal = 0
    posicion = 1 #asignamos el peso decimal adecuado para cada digito del numero octal
while(numero > 0):
    resto = numero%8 #nos da los digitos individuales del numero en 8
    octal += resto * posicion #+= o *= almacena en la misma variable, el valor que tenía la variable más la cantidad que se muestra
    numero = numero // 8
    posicion *= 10 #se incrementa la posicion para colocar los digitos en el lugar correcto
    break
print(f"el numero {numero_decimal} en base decimal es {octal} en base octal:")
