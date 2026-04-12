saldo=1000
pines=[128385,565566,5555]
Historial=""
intentos=3
while True and intentos>0:
    try:
        pin=int(input("Ingresa tu pin:"))
    except ValueError:
        print("Vuelve a intentar tienes que ingresar un valor de tipo entero ej:1")
    if pin in pines:
        pass
    else:
        intentos-=1
        print(f"Vuelve a intenta te quedan {intentos}.")
        continue
    try:
        eleccion=int(input("Ingresa 1 para consultar saldo,2 para depositar dinero,3 para retirar dinero,4 para salir:"))
    except ValueError:
        print("Vuelve a intentar tienes que ingresar un valor de tipo entero ej:1")
    if eleccion==1:
        print(f"Tu saldo es de:{saldo}")
        Historial+="Se realizo consulta de saldo.\n"
    elif eleccion==2:
        try:
            deposito=int(input("Ingresa la cantidad de dinero a depositar:"))
        except ValueError:
            print("Vuelve a intentar tienes que ingresar un valor de tipo entero ej:1")
        if deposito<=0:
            print("Tu deposito no se pudo realizar")
            Historial+="Hubo un intento fallido de deposito.\n"
        else:
            saldo+=deposito
            Historial+=f"Se deposito {deposito}\n"
    elif eleccion==3:
        try:
            retiro=int(input("Ingresa la cantidad de dinero a retirar:"))
        except ValueError:
            print("Vuelve a intentar tienes que ingresar un valor de tipo entero ej:1")
        if retiro<0 or retiro>saldo:
            print("Cantidad insuficiente o cantidad negativa")
            Historial+="Se realizo un intento fallido de retiro.\n"
        else:
            saldo-=retiro
            Historial+=f"Se realizo un retiro de {retiro}.\n"
            if retiro>500:
                Historial+=f"Se realizo un gasto grande por {retiro}.\n"
            elif retiro<500:
                Historial+=f"Se realizo un gasto pequeño por {retiro}.\n"
    elif eleccion==4:
        print("Gracias por usar este programa")
        print("Tu historial fue el siguiente:")
        print(Historial)
        break
    else:
        print("Vuelve a intentar opcion no existente.")