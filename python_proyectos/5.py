estudiantes = {
    "Andrés": [1, 1, 1, 0, 1, 1],
    "Laura":  [1, 0, 0, 1, 1, 0],
    "Carlos": [1, 1, 1, 1, 1, 1],
    "Sofía":  [0, 0, 1, 0, 1, 0]
}
def asistencia(estudiantes):
    texto=f"El estudiante "
    mayor=0
    for clave,lista in estudiantes.items():
        no_asistio=0
        
        asistio=0
        for asistencias in lista:
            
            if asistencias==0:
                no_asistio+=1
            elif asistencias==1:
                
                asistio+=1
        conf=asistio/len(lista)  
        porcentaje=conf*100     
        if porcentaje>mayor:
            mayor=porcentaje
            name=clave    
        texto+=f"{clave}\n"
        texto+=f"No asistio {no_asistio} dias.\n"
        texto+=f" Asistio {asistio} dias.\n"           
        texto+=f".El estudiante tuvo un porcentaje de: {porcentaje:.2f}.\n"
    texto+=f"El estudiante con mayor porcentaje fue: {name} con porcentaje de: {mayor:.2f}.\n"
    texto+="Finalizando programa!!!."
    return texto
analisis=asistencia(estudiantes)
if __name__=="__main__":    
    print(analisis)    