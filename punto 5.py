
cot= 0

while cot<= 5 :
    cot+=1
    dni= float(input("ingrese su dni: "))
    serv= int(input("tipo de servicio: ")) 

    if serv == 1 : 
        monto=30*750
        print("usted debe pagar: ", monto)
        print("DNI: ", dni)
        print("Servicio elegido: ", serv)   

    if  serv== 2 : 
        monto=50*1100
        print( "usted debe pagar: " ,monto) 
        print("DNI: ", dni)
        print("Servicio elegido: ", serv)

    if  serv==3:  
        porc=   (1500*0.05)
        monto= 100* ((1500) - (porc))
        print("usted debe pagar: ", monto)
        print("DNI: ", dni)
        print("Servicio elegido: ", serv)
    

        
    
