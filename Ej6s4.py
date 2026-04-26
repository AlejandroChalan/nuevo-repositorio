numero=int(input("Ingrese un numero."))
ult= numero %10
penult= (numero // 10) %10
if ult == penult:
    print("Sus dos ultimos digitos son iguales")
else:
    print("Sus dos ultimos digitos no son iguales")
