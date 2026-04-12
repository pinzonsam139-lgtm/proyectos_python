username=input("Ingresa tu  nombre de usuario a analizar:")
points=0
longitud=len(username)
numeros=["1","2","3","4","5","6","7","8","9"]
simbolos=["+","-","*","/","=","&","%","$","#","!",",","'",":","}","{","_","."]
letras = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
if username[1] in numeros:
    points-=5
elif username[1] in simbolos:
    points-=5

if longitud>=10:
    points+=20
elif longitud>=5:
    points+=10
tiene_simbolo=False
tiene_letra=False
tiene_numero=False  
for caracter in username:
    if caracter in numeros:
        tiene_numero = True
    elif caracter in letras:
        tiene_letra = True
    elif caracter in simbolos:
        tiene_simbolo = True
if tiene_letra:
    points+=20
if tiene_numero:
    points+=15
if tiene_simbolo:
    points+=15
if "user" in username or "admin" in username or "1234" in username:
    points-=30
if " " in username:
    points-=10
if points>=0 and points<=39:
    print("Malo")
elif points>=40 and points<=69:
    print("Aceptable")
elif points>=70 and points<=100:
    print("Bueno")