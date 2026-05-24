# EJERCICIO 1: PRESENTACIÓN
nombre= "Alejandro Chalan"
edad= 23
print(f"Hola mi nombre es {nombre} y tengo {edad} anios.")


# EJERCICIO 2: CONVERSOR
dias= edad*365
print(f"23 anios equivalen a {dias} dias.")


# EJERCICIO 3: CONDICIONAL SENCILLO IF/ELSE
if edad >= 18:
    print("Eres mayor de edad, entonces puedes pasar.")
else:
    print("Eres menor de edad. ¡Lo siento!")
    
    
# EJERCICIO 4: CONDICIONAL IF/ELIF
color= input("Ingrese un color que se vincule con un semaforo. ").lower()
if color == "verde":
    print("¡Adelante.!")
elif color == "amarillo":
    print("¡Precaución, detente!")
elif color == "rojo":
    print("!No se puede pasar!")
else:
    print("Color no válido")


# EJERCICIO 5: CALCULADORA CONVERSION
cant_entradas= int(input("Ingrese la cantidad de entradas que desea comprar. "))
total= cant_entradas*5
print(f"El precio total de sus entradas es de {total} dólares")


# EJERCICIO 6: BUCLE FOR
num_for= int(input("Ingrese un número sin decimales. "))
for i in range(1, num_for+1):
    print(i)
    

# EJERCICIO 7: BUCLE WHILE
palabra= " "
while palabra != "salir":
    palabra= input("Escribe algo o escriba `salir` para terminar. ")
    
print("Bucle terminado con éxito.")


# EJERCICIO 8: WHILE+OPERACION
total_puntos= 0
while total_puntos < 50:
    print(f"Llevas {total_puntos} puntos")
    puntos= int(input("¿Cuántos puntos quieres sumar?"))
    total_puntos += puntos

print(f"Felicidades, llegaste a la meta con {total_puntos} puntos.")git


    
    
