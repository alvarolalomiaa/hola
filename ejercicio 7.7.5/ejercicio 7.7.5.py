#a) 
def primos(lista): 
    lista1=[]
    for i in lista: 
        if i%2== 0 : 
            lista1.append(i)
    
    print(lista1) 
                    
num_p=[3,9,8,4,2,10,9]
        
primos(num_p)
