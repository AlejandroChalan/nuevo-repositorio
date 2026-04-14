valor_dolar = float(input("¿A cuanto está el valor del dolar hoy?"))
cantidad_dolar = int(input("¿Cuantos dolares desea cambiar?"))
moneda_local = valor_dolar * cantidad_dolar
print(f"La cantidad que usted va a recibir es de {moneda_local}")
if moneda_local >= 1000:
    print("Tienes mucho dinero!")
else:
    print("Procesando el cambio, espere por favor")

