ventas = {
    "Andrés": [1200, 1500, 0, 1800, 2000],
    "Laura": [0, 0, 950, 1100],
    "Carlos": [3000, 2500, 0, 0, 4000, 3800]
}
def resumen(ventas):
    texto=" "
    mayor=0
    for clave,lista in ventas.items():
        total=sum(lista)
        
        prom=total/len(lista)
        texto+=total
        texto+=prom
        if prom>mayor:
            mayor=prom
            
            mejor=clave

    return  texto
im=resumen(ventas)
print(im)