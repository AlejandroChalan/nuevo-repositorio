num= int(input("Ingrese un numero. "))
for i in range(1,11):
    x= num * i                  #podemos hacer la multiplicacion dentro
    print(f"{num} x {i} = {x}") #de las f-strings.


## Ejemplo corregido.
num= int(input("Ingrese un numero. "))
for i in range(1,11):                  #Asi se ve mas limpio visualmente
    print(f"{num} x {i} = {num*1}")    #y ahorramos una linea de codigo.

    
    
