total=0
cantidad=int(input("ingresa la cantidad de vacas a analizar:"))
if cantidad>0:
    for i in range(1,cantidad+1):
        milk=float(input(f"ingresa la cantidad de litros de leche producidos por la vaca n{i} de la forma 1.0:"))
        total+=milk
else:
    print("cantidad incorrecta")        
    exit()
def conversion(total):
    precio=total*1900
    prom=total/cantidad
    return f"el precio de tus {total:.2f} litros de leche es de: {precio:.2f} ademas el promedio fue de: {prom:.2f} "
analisis=conversion(total)
print(analisis)

with open(nombre_excel, "w") as excel:
    # 1. Añadimos "Rango" al título
    excel.write("Suma;Mayor;Menor;Promedio;Pares;Impares;Positivos;Negativos;Rango\n")
    
    # 2. Añadimos {rango} al final de la fila
    fila = f"{suma};{mayor};{menor};{prom:.2f};{par};{impar};{positivo};{menoria};{rango}\n"
    excel.write(fila)