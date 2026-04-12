temperaturas=[10,15,25,26,27,28,10]
def verificador(temperaturas):
    calurosos=0
    if len(temperaturas)>0:
        total=sum(temperaturas)
    else: 
        return "lista invalida"
        
    prom=total/len(temperaturas)
    for temp in temperaturas:
        if temp>=25:
            calurosos+=1
    maxi=max(temperaturas)  
    mini=min(temperaturas)  
    return f"De la lista dada hubo {calurosos} dias calurosos,la temperatura maxima es {maxi} y la temperatura minima es {mini}, el promedio fue de:{prom:.2f}"
dates=verificador(temperaturas)    
print(dates)
