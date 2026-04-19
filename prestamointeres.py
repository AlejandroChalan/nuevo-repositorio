total_prestamo= float(input("Ingrese la cantidad total de su prestamo "))
porcentaje_interes= float(input("Ingrese el porcentaje de su interes mensual"))
mes_sin_interes= total_prestamo/12
interes_mes= (total_prestamo*porcentaje_interes)/100
mes_total= mes_sin_interes+interes_mes
print(f"Su interes mensual es de: {interes_mes}")
print(f"Su mensualidad a pagar incluyendo el interes mensual es de: {mes_total}")


