number1=int(input("ingresa numero 1:"))
number2=int(input("ingresa numero 2:"))
try:
    
    resultado=number1/number2
    print(resultado)
except ZeroDivisionError:
    print("eror division")