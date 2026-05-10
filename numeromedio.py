num= int(input("Ingrese un numero de 4 cifras."))
num1= (num // 1000) 
num2= (num // 100) %10 
num3= (num // 10) %10
num4= num %10
suma= (num2+num3)

if num < 1000 or num > 9999:
    print("Error: El numero tiene que ser de 4 cifras")
elif num1 == num4:
    print("Extremos en equilibrio.")
elif suma %2 ==0:
    print("Nucleo estable.")
else:
    print("Tesoro inestable")

    
    
