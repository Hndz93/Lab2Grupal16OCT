#funcion multiplicar

def mult (x):
	numero=int(input("ingrese nunero a multiplicar"))
	for i in range (1,11):
		tabla=i*numero
		print(numero,"x",i,"=",tabla)
		
x=input("ingrese numero")
print(mult(x))


