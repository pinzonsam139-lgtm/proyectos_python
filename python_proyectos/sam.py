lista=[1,2,10,11,7]
def analisis(lista):
    total=sum(lista)
    mayores=0
    for elemento in lista:
        if elemento>=10:
            mayores+=1
    if len(lista)>0:
        promedio=total/len(lista)
    return f" De la lista dada hubo {mayores} elementos mayores o iguales a 10.\n Ademas el total fue de: {total}, el promedio fue de: {promedio:.2f}"
datos=analisis(lista)
print(datos)