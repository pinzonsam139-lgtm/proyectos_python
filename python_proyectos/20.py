print("--- Iniciando Análisis ---")

lineas=[]
with open("datos.txt", "r") as archivo:
    for linea in archivo:
        try:
            lineal=int(linea.strip())
            lineas.append(lineal)
        except ValueError:
            
            pass
par=0
impar=0
positivo=0
menoria=0
try:
    mayor=lineas[0]
    menor=lineas[0]
except IndexError:
    print("Hay 0 Datos o son invalidos")
    exit()
cantidad=len(lineas)       
for l in lineas:
    if l%2==0:
        par+=1
    else:
        impar+=1 
    if l>0:
        positivo+=1
    elif l<0:
        menoria+=1
    if l>mayor:
        mayor=l
    if l<menor:
        menor=l
    
if cantidad<1:
    print("No hay suficientes datos para analizar.") 
    exit()
else:
    suma=sum(lineas)
    rango=mayor-menor
    prom=suma/cantidad    
    info=""
    info+=f"El total fue:{suma}.\n El numero mayor fue:{mayor}.\n El numero menor fue:{menor}.\n Hubo {par} números pares y {impar} números impares.\n El promedio fue:{prom:.2f},hubo {menoria} números negativos y {positivo} números positivos." 
print(info)
with open("reporte.txt", "w") as reporte:
    reporte.write("=== REPORTE DE ANÁLISIS ===\n")
    reporte.write(f"Fecha: 04/04/2026\n")
    reporte.write(f"El resultado del analisis es:\n{info}")
    reporte.write(f"El rango es de:{rango}")
# ... (Todo tu código de procesamiento anterior se mantiene igual)

# 1. Definimos el nombre del archivo con extensión .csv
nombre_excel = "reporte_final.csv"

with open(nombre_excel, "w") as excel:
    # 2. Escribimos los encabezados (los títulos de las columnas)
    excel.write("Suma;Mayor;Menor;Promedio;Pares;Impares;Positivos;Negativos;Rango\n")
    
    # 3. Escribimos los datos separados por punto y coma (;) 
    # Usamos punto y coma porque en Latinoamérica Excel lo prefiere así
    fila = f"{suma};{mayor};{menor};{prom:.2f};{par};{impar};{positivo};{menoria};{rango}\n"
    excel.write(fila)

print(f"--- ¡Archivo {nombre_excel} generado con éxito! ---")