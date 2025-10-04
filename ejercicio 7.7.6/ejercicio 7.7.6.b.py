#b) 
def multiplo_de_dos(limite): 
    multiplo=[] 
    for i in range(limite+1): 
        if i%2==0 : 
            multiplo.append(i)
    return multiplo

print(multiplo_de_dos(20))
