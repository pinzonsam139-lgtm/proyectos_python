edades = [12, 18, 25, 40, 67, 90, 15, 30]
def verificar(edades):
    total=sum(edades)
    menores=0
    adultos=0
    mayores=0
    if len(edades)>0:
        prom=total/len(edades)
    else:
        return "lista invalida "    
    for edad in edades:
        if edad<0:
            return "edad negativa error"
            break
        elif edad<18:
            menores+=1
        elif edad>=18 and edad<65:
            adultos+=1
        elif edad>=65:
            mayores+=1
        
    minima=min(edades)        
    maxima=max(edades)
    return f"La edad mínima es {minima}, la edad máxima es {maxima} y el promedio de edad es {prom:.2f}.\n En la lista dada hay: {menores} menores de edad,{adultos} adultos y {mayores} mayores de edad"
resumen=verificar(edades)
print(resumen)