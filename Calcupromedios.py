nota_1= float(input("Ingrese la primera nota "))
nota_2= float(input("Ingrese la segunda nota "))
nota_3= float(input("Ingrese la tercer nota "))

promedio= (nota_1+nota_2+nota_3)/3

print(f"Su promedio final es: {promedio} ")

if promedio > 7:
     print("Aprobado")
elif promedio >= 4:
     print("Reprobado con derecho a recuperacion")
else:
     print("Reprobado sin derecho a recuperacion")
              
              
