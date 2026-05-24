#NO ES NECESARIO DECLARAR VARIABLES EN PYTHON
#SE CREAN LISTAS VACIAS
nombres=[ ]
apellidos=[ ]
lista_precios=[ ]
lista_cantidades=[ ]
lista_total=[ ]

#SE PIDE LA CANTIDAD DE VENTAS
cant_ventas= int(input("Ingrese la cantidad de ventas que se van a registrar.\n"))

#CONTADOR ANTES DE INICIAR BUCLE "WHILE"
contador = 0

#INICIAMOS BUCLE "WHILE"
while contador < cant_ventas:
    #SE PIDE LOS DATOS QUE SE VAN A REGISTRAR
    nombre= input("Ingrese su nombre.\n")
    apellido= input("Ingrese su apellido.\n")
    cantidad_entradas= int(input("Ingrese la cantidad de entradas compradas.\n"))
    precio_entradas= float(input("Ingrese el precio unitario de las entradas.\n"))
    
    #SE AÑADE LA INFORMACION A LAS LISTAS
    nombres.append(nombre)
    apellidos.append(apellido)
    lista_cantidades.append(cantidad_entradas)
    lista_precios.append(precio_entradas)
    
    #SE CALCULA EL SUBTOTAL ANTES DE APLICAR DESCUENTO
    subtotal= cantidad_entradas * precio_entradas

    #REFERENCIAS PORCENTAJES DE DESCUENTOS
    #1 ENTRADA = 10%
    #2 O 3 ENTRADAS = 20%
    #4 O 5 ENTRADAS = 30%
    #6 O MAS ENTRADAS = 40%
    if cantidad_entradas == 1:
        porcentaje= 0.10
    else:
        if cantidad_entradas == 2 or cantidad_entradas == 3:
            porcentaje= 0.20
        else:
            if cantidad_entradas == 4 or cantidad_entradas == 5:
                porcentaje= 0.30
            else:
                if cantidad_entradas >= 6:
                    porcentaje= 0.40
                else:
                    porcentaje= 0.0
                    
    #SE CALCULA EL MONTO DEL DESCUENTO Y EL MONTO A PAGAR
    monto_descuento= subtotal * porcentaje
    total_cliente= subtotal - monto_descuento

    #SE AÑADE EL TOTAL DE CADA CLIENTE
    lista_total.append(total_cliente)

    #EL CONTADOR SUMA 1
    contador += 1        #AQUI TERMINA EL BUCLE "WHILE"
    
#SE USA "suma_totales" PARA IR GUARDANDO EL DINERO DE LAS VENTAS
suma_totales= 0

#SE INICIA BUCLE "FOR"
#LA LISTA COMIENZA DESDE LA POSICION 0 POR DEFECTO, ENTONCES NO SE AÑADE NADA
for i in range(cant_ventas):
    print(f"Cliente:\n Nombre: {nombres[i]} {apellidos[i]}\n Cantidad de entradas: {lista_cantidades[i]}\n Precio Unitario: ${lista_precios[i]}\n Total a pagar: {lista_total[i]:.2f}\n")

    #SE SUMA EL DINERO REAL DE LAS VENTAS
    suma_totales += lista_total[i]

#SE CALCULA EL PROMEDIO DE VENTAS REALIZADAS
#SE CALCULA EL MAYOR Y MENOS MONTO
promedio= suma_totales/cant_ventas
mayor_monto= max(lista_total)
menor_monto= min(lista_total)

#SE MUESTRAN LOS RESULTADOS
#SE USA :.2f PARA OBTENER UNICAMENTE DOS DECIMALES
print(f"El promedio de ventas realizadas es: {promedio:.2f}.")
print(f"La venta de mayor monto es {mayor_monto:.2f}.")
print(f"La venta de menor monto es {menor_monto:.2f}.")


    
                    
    

