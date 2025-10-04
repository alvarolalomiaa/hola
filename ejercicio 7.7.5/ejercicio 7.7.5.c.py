#c) 
def factorial(lista): 
    import math
    lista1=[]
    for i in lista: 
        i=math.factorial(i)
        lista1.append(i)
    
    print(lista1) 
                    
num_p=[5,2,4]
        
factorial(num_p)
