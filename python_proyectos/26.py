print("Revisando prioridad: Andrés siempre va primero")
total_recursos=1000
clan_part=0
faltante=0
while True:
    try:
        name_clan=input("Ingresa el nombre del clan")
    except EOFError:
        print("no ingresaste datos vuelve a intentar")
    try:
        recurso=int(input("Ingresa la cantidad de recurso que tienes:"))
    
    except ValueError:
        print("Error tipo de dato invalido.")
    try:
        integrantes=int(input("Ingresa la cantidad de integrantes de tu clan:"))
    except ValueError:
        print("Error tipo de dato invalido.")
    try:
        name=input("Ingresa tu nombre:")
    except EOFError:
        print("No ingresaste datos vuelve a intentar")
    try:
        costo=int(input("Ingresa el costo de la mejora a realizar:"))
    except ValueError:
        print("Tipo de dato invalido")
    if integrantes>0 and costo>0 and name!="":
        clan_part=total_recursos/integrantes
        total=clan_part+recurso
        faltante=costo-total
        break
    else:
        print("Falta informacion.")
        print("Vuelve a intentar")
print(f"Hola {name},la cantidad de recursos faltantes es:{faltante}.")
with open("Historial_juego.txt","a") as Historial_juego:
    Historial_juego.write(f"Ingreso el usuario {name}.\n")
    Historial_juego.write(f"Del clan: {name_clan}.\n")
    Historial_juego.write(f"Con {integrantes} integrantes.\n")
    Historial_juego.write(f"Tiene un faltante de: {faltante}.\n")