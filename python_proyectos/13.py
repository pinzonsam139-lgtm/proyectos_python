print("Este programa realiza un analisis completo de todos los numeros a ingresar ")
lista=[]
while True :


    try:
        number=int(input("Ingresa en numero:"))
        lista.append(number)
    except ValueError:
        print("Error al ingresar se esperaba un dato tipo entero.")
    salir=input("ingresa s para salir o cualquier letra para continuar:")
    if salir.lower() == "s":
        break

cantidad_numbers=len(lista)

if len(lista)>0:
    total=sum(lista)
    prom=total/len(lista)
    maximo=max(lista)
    minimo=min(lista)
 
    print(f"La cantidad de datos ingresados es: {cantidad_numbers}.")
    print(f"La suma total de los datos ingresados es de: {total}.")
    print(f"El promedio fue de: {prom:.2f}.")
    print(f"El numero mayor ingresad0 fue: {maximo}.")
    print(f"El numero minimo ingresado fue: {minimo}.")
