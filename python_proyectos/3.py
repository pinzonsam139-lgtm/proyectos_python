numeros = [12, 5, 8, 7, 20, 3, 10]
def numbers(numeros):
    total_par=0
    pares=0
    total_impar=0
    impares=0
    if len(numeros)==0:
        return "lista vacia "
    else:
        for number in numeros:
            if number==0:
                return "numero menor a cero" 
        for number in numeros:     
            if number%2==0:
                pares+=1
                total_par+=number
            else:
                impares+=1    
                total_impar+=number
        total=sum(numeros) 
        prom=total/len(numeros)
        minimo=min(numeros)         
        maxi=max(numeros)  
    return f"En la lista dada hubo {pares} numeros pares y la suma de numeros pares fue de: {total_par}\n Ademas hubo {impares} cuya suma total fue de: {total_impar}\n El promedio fue de {prom:.2f}\n El numero mayor fue {maxi} y el numero menor fue:{minimo}\n "
if __name__ == "__main__":
    print(analizar_numeros(numeros))




