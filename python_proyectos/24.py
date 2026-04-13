total=0

while True:
    
    try:
        name=input("Ingresa el nombre de tu gasto:")
    except EOFError:
        print("Error causado por no ingresar datos")
    
    try:
        valor=int(input("Ingresa el valor de tu gasto:"))
        total+=valor
    except ValueError:
        print("Tipo de dato invalido")
        continue
    
    try:
        stop=input("ingresa s para salir:")
    except EOFError:
        print("Error causado por no ingresar datos.")

    with open("Gastos.txt","a") as Gastos:
        Gastos.write(f"Se gasto {valor} en:{name}.\n")
    
    if stop.lower()=="s":
        break

with open("Gastos.txt","a") as Gastos:
    Gastos.write(f"El total gastado fue de:{total}")
