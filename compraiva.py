cant_siva= float(input("¿Cual es la cantidad total sin iva?"))
iva= float(input("¿Que porcentaje de IVA paga?"))
porc_iva= (iva*cant_siva)/100
total_compra= porc_iva+ cant_siva
print(f"La cantidad a pagar incluyendo el IVA es: {total_compra} ")


