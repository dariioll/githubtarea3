num1=input("Digite primer numero: ")
num2=input("Digite segudno numero: ")
num3=input("Digite tercer numero: ")

#if num1>num2:
#    print("UNODOS{} mayor que : {} y {}".format(num1,num2,num3))    
#else:
#    if(num1>num3):
#        print("UNOTRES {} mayor que : {} y {}".format(num1,num2,num3))  

print("ORUEBA CON AND")

print("PUEBA NUMERO 1")
if(num1>=num2 and num1>=num3):
    if(num2>=num3):
        print("{}, {}, {}".format(num1,num2,num3)) 
    else:
        print("{}, {}, {}".format(num1,num3,num2))  
        print("PREUBA NUMERO 2")
else:    
    if( num2>=num3):
        if(num1>=num3):
            print("{}, {}, {}".format(num2,num1,num3)) 
        else:
            print("{}, {}, {}".format(num2,num1,num2))  
            print("prueba 3 numero")
    else:
        if(num1>=num2):
            print("{},{},{}".format(num3,num1,num2))
        else:
            print("{},{},{}".format(num3,num2,num1))
