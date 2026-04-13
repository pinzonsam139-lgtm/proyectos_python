# Lista de niveles medidos
niveles = [40, 75, 30, 90, 10]
contaminado=0
limpio=0
try:
    nivel=int(input("Ingresa el nuevo nivel medido:"))
except ValueError:
    print("Error tipo de dato invalido.")
niveles.append(nivel)
for medicion in niveles:
    if medicion > 50:
        contaminado+=1
    else:
        limpio+=1
with open("Niveles.txt","a") as Niveles:
    Niveles.write(f"De la siguiente lista:{niveles}\n")
    Niveles.write(f"Hubo {limpio} datos los cuales arrojaron aire limpio y {contaminado} dieron resultados de contaminacion\n")
    print("Archivo creado correctamente.")