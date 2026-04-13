counter=0
idea="registro_ideas.csv"
print("Diario")
with open("ideas.txt","a") as ideas:

    ideas.write("=== Lluvia de  ideas===\n")
while True:
    try:
        think=input("Ingresa una nota o idea rapida para salir pon s:")
    except EOFError:
        print("Tipo de dato invalido")
    if think.lower()=="s":
        break
    else:
        counter+=1
        with open("ideas.txt", "a") as ideas:
            ideas.write(think+"\n")     
        with open(idea,"a") as f_csv:
            f_csv.write(f"{counter};{counter};{counter}\n")
            fila=(f"{think};{think};{think}")
            f_csv.write(f"{fila}")