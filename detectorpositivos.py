#El programa debe decir si exactamente uno de los dos números es positivo.
#Condicion: Uno es positivo y el otro no. ((+,+)(-,-))= no valido.

primn= int(input("Ingrese un numero entero."))
segn= int(input("Ingrese un numero entero."))
if primn > 0 and segn <= 0:
    print(f"Su numero positivo es: {primn}.")
elif primn <= 0 and segn <= 0:
    print("Resultado no valido")
elif primn > 0 and segn > 0:
    print("Resultado no valido")
else:
    print(f"Su resultado positivo es: {segn}.")
    
        

    

    

    
