import random
number=random.randint(1,20)
print("Bienvenido a este programa \nEste es un juego el cual consiste en adivinar un numero te daremos pistas")
intentos=0
while True:
    
    try :
        intento=int(input("Ingresa el numero que crees que es(pista:es un numero de 1 al 20):"))
        intentos+=1
    except ValueError :
        print("Debes ingresar un número válido.")
        intento=int(input("Ingresa el numero que crees que es(pista:es un numero de 1 al 20):"))


    
    if intento==number:
        print(f"Felicitaciones el número era {number}🎉🎊")
        print(f"Usaste {intentos} intentos para adivinar el número.")
        eleccion=input("Deseas jugar otra vez(si/no):")
        if eleccion.lower()=="si":
            number = random.randint(1,20)
            intentos=0
            print("¡Nueva partida!\nAdivina el número nuevamente.")
        else:    
            print("Gracias por usar este programa.")
            break
    elif intento<number:
        print("El número que intentas adivinar es un número mayor🧨🎃")
    elif intento>number:
        print("El número que intentas adivinar es un número menor🧨🎃")
