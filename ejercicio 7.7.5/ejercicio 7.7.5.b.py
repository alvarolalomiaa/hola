#b)
def sumatoria(lista): 
    suma=0
    for i in lista: 
        suma+=i
    promedio= suma/len(lista)
    print("La suma es: ", suma, " y el promedio es: ", promedio)

numeros=[2,3,4,1]

sumatoria(numeros)
