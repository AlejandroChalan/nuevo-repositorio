gasto_hijo1= float(input("¿Cuanto gasta en su primer hijo?"))
gasto_hijo2= float(input("¿Cuanto gasta en su segundo hijo?"))
gasto_hijo3= float(input("¿Cuanto gasta en su tercer hijo?"))
total= gasto_hijo1+gasto_hijo2+gasto_hijo3
print(f"El gasto total de sus 3 hijos es:{total}")

if total > 500:
    print(f"Su gasto de {total} es demasiado")
else:
    print(f"Su gasto de {total} es adecuado")
    

    
