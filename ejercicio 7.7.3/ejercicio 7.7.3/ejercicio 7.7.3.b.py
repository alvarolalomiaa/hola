#b) 
def posiciones(tupla_nombres, inicio , fin): 
    
    tupla_nombres=tuple(tupla_nombres) 
    sub_tupla=tupla_nombres[inicio:fin+1]
    for i in sub_tupla: 
        print("Estimado",i, ", vote por mi")

tupla1= ('Alvaro', 'Santiago', 'Andres', 'Marcos', 'Nico', 'Matias')

posiciones(tupla1, 1, 4) 
