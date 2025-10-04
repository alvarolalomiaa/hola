#a) 
def mayores_menores_iguales(lista, k):  
    lista1=[]
    lista2=[]
    lista3=[]
    for i in lista: 
        if i<k : 
            lista1.append(i)
        if i>k: 
            lista2.append(i)
        if i==k: 
            lista3.append(i)
    
    print( lista1 , lista2 , lista3) 


numeros=[2,5,7,3,4,9,10,11]

mayores_menores_iguales(numeros, 4)
