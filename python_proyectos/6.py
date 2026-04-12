notas = {
    "Andrés": [4.5, 3.8, 4.9, 5.0],
    "Laura":  [3.0, 2.5, 3.2, 3.8],
    "Carlos": [5.0, 4.8, 4.9, 5.0],
    "Sofía":  [2.0, 2.8, 3.0, 2.5]
}
analisis={
    "Andrés":[],
    "Laura":[],
    "Carlos":[],
    "Sofía":[]
}
def calificaciones(notas):
    
    for clave,lista in notas.items():
        total=sum(lista)
        analisis[clave].append("Total:")
        analisis[clave].append(total)
        maxi=max(lista)
        analisis[clave].append("Maximo:")
        analisis[clave].append(maxi)
        mini=min(lista)
        analisis[clave].append("Minimo:")
        analisis[clave].append(mini)
        prom=total/len(lista)
        analisis[clave].append("Promedio:")
        analisis[clave].append(prom)
        
        if prom>=3.0:
            analisis[clave].append("Aprobo:")
            analisis[clave].append(True)

        else:
            analisis[clave].append("Aprobo:")
            analisis[clave].append(False)
calificaciones(notas)
if __name__=="__main__":
    print(analisis)