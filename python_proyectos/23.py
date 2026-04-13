Resumen="===Historial===\n"
Resumen+="Cualquier problema llamar +57 3012172368"
productos={
    "manzana":20,"pera":31,"lulo":10}
while True:
    try:
        options=int(input("Ingresa 1 para añadir producto nuevo,2 para actualizar cantidad,3 mostrar cantidad total,4 para salir:"))
    except ValueError:
        print("Tipo de dato invalido.")
        continue
    if options==1:
        try:
            name=input("Ingresa el nombre del nuevo producto:")
        except EOFError:
            print("Error no ingresaste ningun dato.")
            continue
        try:
            cantidad=int(input("Ingresa la cantidad a ingresar del nuevo producto:"))
        except ValueError:
            print("Tipo de dato invalido.")
            continue
        if not name in productos:
            try:
                productos[name]=cantidad
            except KeyError:
                print("No hemos podido encontrar tu producto.")
                continue
            Resumen+="Se agrego un nuevo producto.\n"
        else:
            Resumen+="Se intento agregar un producto ya existente.\n"
            print("El producto ya se encuentra registrado")
    elif options==2:
        cambio=input("Ingresa el nombre del producto:")
        if cambio in productos.keys():
            try:
                valor=int(input("Ingresa la nueva cantidad que queda del producto"))
            except ValueError:
                print("Tipo de dato invalido")
                continue
        productos[cambio] = valor
        print("Registro actualizado")
        print(productos)
    elif options==3:
        if productos:
            total = sum(productos.values())
            prom=total/len(productos.values())
            Resumen+=f"El total fue:{total} y el promedio fue de: {prom}"
        else:
            print("No hay productos registrados.")
    elif options==4:
        break
    try:
        with open("Historial.txt","a") as Historial:
            Historial.write(Resumen)
    except Exception as e:
        print(f"No se pudo guardar el archivo: {e}")
print("Documento txt creado con exito revisa en la carpeta que tienes guardado el programa.")