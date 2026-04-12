ventas = {
    "Andrés": [1200, 1500, 0, 1800, 2000, 0, 1700],
    "Laura":  [0, 0, 950, 1100, 1300],
    "Carlos": [3000, 2500, 0, 0, 4000, 3800]
}
for clave,lista in ventas.items():
    datos_0=0
    for dato in lista:
        if dato<=0:
            datos_0+=1
        else:
            total+=dato
        if total>0:
            divisor=len(lista)-datos_0
            prom=total/divisor
        else:
            exit()
             
             