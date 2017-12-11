## Simple Banking Pgm
import random
from bank import existing

def acc_create(a,b,c,d,e,f):
    #acc=random.getrandbits(30)
    acc1={"Name":a,"Age":b,"Gender":c,"address":d,"Phone":e,"Avail_Amount":f}
    return acc1
##    acc1={acc:{"Name":a,"Age":b,"Gender":c,"address":d,"Phone":e,"Avail_Amount":f}}
##    return acc1



global t1
t1={}
while True:
    
    g=(int(input("Press \n'1' New Customer: \n'2' Existing customer:\n")))
    if g == 1:
        a=(input("Enter the Accoubt holders Name:"))
        b=(int(input("Enter the Accoubt holders Age:")))
        c=(input("Enter the Accoubt holders Gender:"))
        d=(input("Enter the Accoubt holders Address:"))
        e=(int(input("Enter the Accoubt holders Phone:")))
        f=(int(input("Enter the Amount to be add:")))
        
        t=acc_create(a,b,c,d,e,f)
        t1[random.getrandbits(30)]=t
        
        print(t1)
           
    
    if g == 2:
        ac=int(input("enter your account number"))
        
        r=(ac in t1)
        if r==True:
            print(t1[ac])
            existing.existing_acc(t1,ac)
        if r==False:
            print("You entered a invalid Account number \nPlease enter a valid account number Next time")
            
    cho=input("Enter C for continue  X for exit")
    print("-------------------------------------")
    if cho=="c":
        pass
    else:
        break  
    
        

    
