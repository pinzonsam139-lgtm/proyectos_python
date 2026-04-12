print("---Iniciando analisis---")
totalretiros=0
errordeingreso=0
historial=""
mostrar_saldo=0
errorderetiro=0
totalingreso=0
saldo = 0  # Inicializamos
while True:
    try:
        saldo = int(input("Ingresa el saldo inicial:"))
        if saldo > 0:
            break  # <--- Esto rompe el bucle solo si el saldo es válido
        else:
            print("No puedes ingresar saldo negativo o cero.")
    except ValueError:
        print("Vuelve a intentar. Tipo de dato inválido.")
while True:
    eleccion=int(input("Ingresa 1 para retirar dinero, 2 para mostrar saldo, 3 para añadir saldo,4 para salir:"))
    if eleccion==1:
        try:
            
            retiro=int(input("Ingresa la cantidad de dinero que deseas retirar:"))
        except ValueError:
            print("Error tipo de valor no valido.")
            errorderetiro+=1
        if retiro>saldo or retiro<=0:
            errorderetiro+=1
            print("No puedes retirar esta cantidad de dinero ya que supera el saldo.")
        else:
            saldo-=retiro
            totalretiros+=retiro
            print(f"Tu nuevo saldo es de:{saldo}")
    elif eleccion==2:
        print(f"Tu saldo es de:{saldo}")
        mostrar_saldo+=1
    elif eleccion==3:
        try:
            ingreso=int(input("Ingresa el dinero que deseas ingresar a tu cuenta:"))
        except ValueError:
            print("Error tipo de valor no valido.")
            errordeingreso+=1
        if ingreso<=0:
            print("Error el ingreso no puede ser menor o igual a 0.")
            errordeingreso+=1
        else:
            saldo+=ingreso
            totalingreso+=ingreso
            print(f"Tu nuevo saldo es de:{saldo}")
    elif eleccion==4:
        break
    else:
        print("opcion no valida, vuelve a intentar.")
with open("movimientos.txt", "w") as movimientos:
    movimientos.write("=== REPORTE DE ANÁLISIS ===\n")
    movimientos.write(f"Fecha: 05/04/2026\n")
    movimientos.write(f"El historial más reciente es:\n{historial}.")
    movimientos.write(f"Hubo {errordeingreso} errores de ingreso y {errorderetiro} errores de retiro.")
    movimientos.write(f"EL total de dinero retirado fue:{totalretiros}.")
    movimientos.write(f"El total de de dinero ingresado a tu cuenta fue de: {totalingreso}.")
    movimientos.write(f"Se mostro el saldo {mostrar_saldo}.")
nombre_excel = "movimientos.csv"
with open(nombre_excel, "w") as excel:
    # 2. Escribimos los encabezados (los títulos de las columnas)
    excel.write("Saldo;Saldo view;Error ingreso;Error retiro;Ingreso total;Total de retiros;\n")
    # 3. Escribimos los datos separados por punto y coma (;) 
    # Usamos punto y coma porque en Latinoamérica Excel lo prefiere así
    fila = f"{saldo};{mostrar_saldo};{errordeingreso};{errorderetiro};{totalretiros};{totalingreso}\n"
    excel.write(fila)
print(f"--- ¡Archivo {nombre_excel} generado con éxito! ---")