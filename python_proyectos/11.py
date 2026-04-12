productos={}
dinero_caja=0
while True:
    print("Ingresa 1 para agregar un producto,2 para mostrar inventario,3 para vender un producto,4 para mostrar Producto con mayor valor en inventario,5 eliminar producto,6 para salir")
    eleccion=int(input("Escoje una de las acciones anteriores:"))
    if eleccion==1:
        name=input("Ingresa el nombre del producto:")
        price=int(input("Ingresa el precio del producto:"))
        stock_cantidad=int(input("Ingresa la cantidad en stock:"))
        if price>0 and stock_cantidad>0:
            productos[name]={"precio":price,"stock":stock_cantidad}
        else:
            print("Error hay cantidades negativas")
    elif eleccion==2:
        print(productos)
    elif eleccion==3:
        buscar=input("Ingresa el nombre del producto:")
        cantidad=int(input("Ingresa la cantidad de unidades que deseas llevar:"))
        if buscar in productos.keys():
            print("producto encontrado")
            if cantidad>0:
                if productos[buscar]["stock"]>=cantidad:
                    new_stock=productos[buscar]["stock"]-cantidad
                    productos[buscar][new_stock]
                    producto={buscar:{"precio":price,"stock":new_stock}}
