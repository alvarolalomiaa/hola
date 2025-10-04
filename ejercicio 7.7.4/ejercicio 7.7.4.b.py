#b) 
def producto(v1,v2): 
    (a,b)=v1
    (c,d)=v2
    result= (a*c),(b*d)

    if result==(0,0) : 
        print("Los vectores, ", v1, v2 ,"son ortogonales")
    if result!= (0,0) : 
        print("Los vectores, ", v1, v2 ,"no son ortogonales")

producto((1,0),(0,1))
