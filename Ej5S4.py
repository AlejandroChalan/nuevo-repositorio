numero=int(input("Ingrese un numero."))
ult= numero %10
penult= (numero // 10) %10
suma= ult+penult
if suma %2 == 0:
    print(f"La suma de los dos ultimos digitos es: {suma}, y es par.")
else:
    print(f"La suma de los dos ultimos digitos es: {suma}, y es impar.")
    

