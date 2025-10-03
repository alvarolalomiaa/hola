def lista(tupla_elementos): 
    n = len(tupla_elementos)
    
    if n<2: 
        return "de menor a mayor"
    
    for i in range(n - 1): 
        if tupla_elementos[i] > tupla_elementos[i + 1]: 
            return "de mayor a menor"
    return "de menor a mayor"

tupla1=(5,10,20)
tupla2=(1,20,23,50)

print(f"la tupla {tupla1} esta ordenada {lista(tupla1)}")
print(f"la tupla {tupla2} esta ordenada {lista(tupla2)} ")











