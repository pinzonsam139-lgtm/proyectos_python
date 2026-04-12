estudiantes = {
    "Andrés": {
        "matematicas": [4.5, 3.8, 5.0],
        "python": [5.0, 4.9, 4.8],
        "historia": [3.5, 4.0, 4.2]
    },
    "Laura": {
        "matematicas": [2.5, 3.0, 2.8],
        "python": [3.5, 3.8, 4.0],
        "historia": [4.5, 4.8, 4.9]
    },
    "Carlos": {
        "matematicas": [5.0, 4.9, 4.8],
        "python": [4.0, 4.2, 4.1],
        "historia": [2.0, 2.5, 3.0]
    }
}

mejor_promedio = 0
mejor_estudiante = ""

for nombre, materias in estudiantes.items():
    print("Estudiante:", nombre)
    
    total_general = 0
    contador_materias = 0
    
    for materia, notas in materias.items():
        suma = sum(notas)
        promedio = suma / len(notas)
        
        print("   ", materia, ":", round(promedio, 2))
        
        total_general += promedio
        contador_materias += 1
    
    promedio_general = total_general / contador_materias
    print("Promedio general:", round(promedio_general, 2))
    print()
    
    if promedio_general > mejor_promedio:
        mejor_promedio = promedio_general
        mejor_estudiante = nombre

print("El mejor estudiante es:", mejor_estudiante)
print("Con promedio:", round(mejor_promedio, 2))