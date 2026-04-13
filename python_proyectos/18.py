"""Pida al usuario ingresar números uno por uno.
Termine cuando el usuario escriba "salir".
Al final muestre:
Cantidad total de números ingresados
Número mayor
Número menor
Promedio"""
lista=[]
def analisis(lista):
    par=0
    impar=0
    cantidad=len(lista)
    if cantidad<1:
        return "No ingresaste ningun número."
    maximo=max(lista)
    minimo=min(lista)
    total=sum(lista)
    for number in lista:
        if number%2==0:
            par+=1
        else:
            impar+=1
    
    prom=total/cantidad
    return f"De los {cantidad} números ingresados, el número mayor fue: {maximo} y el menor fue: {minimo}\n El promedio fue de: {prom:.2f}\n Hubo {par} números pares y {impar} números impares"
while True:    
    number=input("Ingresa el número o ingresa salir para salir:")
    if number.lower()=="salir":
        print(analisis(lista))
        break
    try:
        numero=int(number)
        lista.append(numero)
    except ValueError:
        print("tipo de dato incorrecto, para salir ingresa salir")
    else:
        continue   