numero=int(input("Ingrese un numero."))
ult_digito= numero %10
if ult_digito %2 ==0:
    print(f"El ultimo numero de su cifra es: {ult_digito}, y es par.")
else:
    print(f"El ultimo numero de su cifra es: {ult_digito}, y es impar")
    
