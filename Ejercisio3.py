print("Ejercicio #3")
nombre = input(" ingrese su nombre")
salario = int (input(" ingrese su salario"))
edad = int(input("Ingrese la edad de la persona"))

if edad<=16:
    print ("No tiene edad para trabajar")
elif edad <=50:
    t = salario * 0.05
    tl = salario + t
    print ("Su salario:", salario)
    print("Su aumento es de:", t)
    print ("Su total es:", tl)
    
elif edad <=60:
    t2 = salario * 0.10
    tr2 = salario + t2
    print ("Su salario:", salario)
    print("Su aumento es de:", t2)
    print ("Su aumento es:", tr2)
    
    
else:
    t3 = salario * 0.15
    tt3 = salario + t3
    print ("Su salario:", salario)
    print("Su aumento es de:", t3)
    print ("Su aumento es:", tt3)


print("Ejercicio #2")
def mayor (a,b):
        if (a>b):
              return a
        if (a>b):
               return b
print(mayor(12,6))


print("Ejercicio #3")
nombre = input(" ingrese su nombre")
salario = int (input(" ingrese su salario"))
edad = int(input("Ingrese la edad de la persona"))

if edad<=16:
    print ("No tiene edad para trabajar")
elif edad <=50:
    t = salario * 0.05
    tl = salario + t
    print ("Su salario:", salario)
    print("Su aumento es de:", t)
    print ("Su total es:", tl)
    
elif edad <=60:
    t2 = salario * 0.10
    tr2 = salario + t2
    print ("Su salario:", salario)
    print("Su aumento es de:", t2)
    print ("Su aumento es:", tr2)
    
    
else:
    t3 = salario * 0.15
    tt3 = salario + t3
    print ("Su salario:", salario)
    print("Su aumento es de:", t3)
    print ("Su aumento es:", tt3)


 
