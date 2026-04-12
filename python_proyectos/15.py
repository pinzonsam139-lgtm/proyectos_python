print("Este programa evalua la seguridad de la contraseña")
numbers=["1","2","3","4","5","6","7","8","9","10"]
simbolos=["+","-","*","/","=","&","%","$","#","!",",","'",":","}","{"]
letras = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
imbolo=0
nums=0
let=0
for number in numbers:
    nums+=1
for letra in letras:
    let+=1
for simbolo in simbolos:
    imbolo+=1

while True:
    contraseña=input("Ingresa tu contraseña:")
    cantidad=len(contraseña)
  
    if cantidad<8:
        print("Muy débil")
    elif cantidad>=8:
        if  number in contraseña and letra in contraseña and simbolo in contraseña:
            print("Fuerte")
        elif number in contraseña and letra in contraseña and not simbolo in contraseña:
            print("Media")
        elif number in contraseña and not letra in contraseña and not simbolo:
            print("Debil")
    print(f"Hay {let} letras en el analizador.")
    print(f"Hay {imbolo} simbolos en el anlizador.")
    print(f"Usamos {nums} numeros en el analisis.")
    continuar=input("ingresa (si/no) deseas continuar con el programa y probar otra contraseña:")
    if continuar.lower()=="si":
        pass
    else:
        break