numero = int(input("Ingrese un numero de 3 digitos"))
ultdig = numero %10
primdig = numero // 100
if ultdig == primdig:
    print("El primer y ultimo digito son iguales")
else:
    print("El primer y ultimo digito no son iguales")
