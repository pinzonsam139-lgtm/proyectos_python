print("Este programa evalúa la seguridad de la contraseña")

# Listas de referencia
numeros = "0123456789"
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
simbolos = "+-*/=&%$#!,':}{"

while True:
    contraseña = input("Ingresa tu contraseña: ")
    
    # Banderas (estado de cada tipo de carácter)
    tiene_numero = False
    tiene_letra = False
    tiene_simbolo = False

    # Recorremos cada carácter de la contraseña
    for caracter in contraseña:
        if caracter in numeros:
            tiene_numero = True
        elif caracter in letras:
            tiene_letra = True
        elif caracter in simbolos:
            tiene_simbolo = True

    # Longitud de la contraseña
    cantidad = len(contraseña)

    # Evaluación
    if cantidad < 8:
        print("Muy débil")
    else:
        if tiene_numero and tiene_letra and tiene_simbolo:
            print("Fuerte")
        elif tiene_numero and tiene_letra:
            print("Media")
        else:
            print("Débil")

    # Información adicional
    print(f"La contraseña tiene {cantidad} caracteres.")
    print(f"Contiene número: {tiene_numero}")
    print(f"Contiene letra: {tiene_letra}")
    print(f"Contiene símbolo: {tiene_simbolo}")

    # Continuar o salir
    continuar = input("¿Deseas probar otra contraseña? (si/no): ")
    if continuar.lower() != "si":
        break