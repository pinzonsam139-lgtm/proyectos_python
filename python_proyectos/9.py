notas = [45, 82, 33, 90, 55, 70, 40]

# Escribe tu lógica aquí:

def analisis(notas):
    aprobado=0
    reprobado=0
    total_aprobado=0
    invalida=0
    for nota in notas:
        if nota<0 or nota>100:
            invalida+=1
        elif nota>=60:
            aprobado+=1
            total_aprobado+=nota
            
        elif nota<60:
            reprobado+=1
    prom=total_aprobado/aprobado
    print(f"De la lista dada hubo {aprobado} estudiantes aprobados,{reprobado} estudiantes reprobados,y hubo {invalida} notas invalidas")
    print(f"La suma de los aprobados es de: {total_aprobado}")
    print(f"Y el promedio de los aprobados es de: {prom:.2f}")
analisis(notas)