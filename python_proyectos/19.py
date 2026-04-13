"""1. Agregar estudiante
2. Agregar nota a estudiante
3. Mostrar estudiantes y notas
4. Mostrar promedio de cada estudiante
5. Mostrar el mejor estudiante
6. Salir"""
estudiantes={}

while True:
    try:
        fin_rango = int(input("Ingresa la nota maxima: "))
        if fin_rango > 0:
            ok = input(f"Deseas que la nota maxima sea {fin_rango}? (si/no): ")
            if ok.lower() == "si":
                break
        else:
            print("Debe ser mayor que 0")
    except ValueError:
        print("Dato invalido")
    
while True:
    print("A continuacion ingresa 1 de estas opciones de forma numerica")
    print("1. Agregar estudiante,2. Agregar nota a estudiante,3. Mostrar estudiantes y notas,4. Mostrar promedio de cada estudiante,5. Mostrar el mejor estudiante,6. Salir")
    try:
        eleccion=int(input("De las opciones anteriores ingresa:"))
    except ValueError:
        print("Vuelve a intentar tipo de dato invalido")
        continue
    if eleccion==1:
        name=input("Ingresa el nombre del estudiante:")
        estudiantes[name]=[]
        print("Base de datos actualizada")
        print(estudiantes)
    elif eleccion==2:
        name=input("Ingresa el nombre del estudiante:")
        if name in estudiantes:
            try:
                nota=int(input("Ingresa la nota a agregar:"))
                
            
                if nota<0 or nota>fin_rango:
                    print("Esta nota no se pudo agregar esta fuera del rango")
                elif nota>=0 and nota<=fin_rango:    
                    estudiantes[name].append(nota)
                    print("nota agregada")
                    print(estudiantes)
            except ValueError:
                print("Vuelve a intentar dato invalido")    
                continue    
    elif eleccion==3:
        print(estudiantes)
    elif eleccion==4:
        for nombre,lista in  estudiantes.items():
            if len(lista) > 0:
                total=sum(lista)  
                cantidad=len(lista)
                
                prom=total/cantidad
                print(f"El promedio de:{nombre},fue de:{prom:.2f}")
            else:
                print(f"Insuficientes datos por parte de {nombre}")
    elif eleccion==5:
        mayor=-1
        menor=5498236
        for nombre,lista in  estudiantes.items():
            if len(lista) > 0:
                total=sum(lista)  
                cantidad=len(lista)
                prom=total/cantidad
                if prom>mayor:
                    mayor=prom
                    name_mayor=nombre
                if prom<menor:
                    menor=prom
                    name_menor=nombre
        print(f"El mejor estudiante fue:{name_mayor} con {mayor:.2f}")
        print(f"El  estudiante con el peor promedio fue:{name_menor} con {menor:.2f}")