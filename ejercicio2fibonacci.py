x= int(input("ingresa un numero "))
a= 0
b=1
print(a)
print(b)
for i in range(2, x):
    resultado = a+b 
    a=b
    b=resultado
    print(resultado)
    
j=0
k=1
for i in range( x):
    result = j+k 
    j=k
    k=result
print("la suma de los numeros es:",result-1)

