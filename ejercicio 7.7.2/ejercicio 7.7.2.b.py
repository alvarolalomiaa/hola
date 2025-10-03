#b)
def encajar_ficha(ficha1, ficha2): 
    if  ficha1[0]==ficha2[0] or ficha1[0]==ficha2[1] or ficha1[1]==ficha2[0] or ficha1[1]==ficha2[1]:
        return "las fichas encajan"
    else: 
        return "las fichas no encajan"
    
cadena_a= '3-4' 
cadena_b= '5-4'

print(encajar_ficha(cadena_a, cadena_b))
print(encajar_ficha((3,4) , (5,4)))
print(encajar_ficha((2,3) , (5,7)))
