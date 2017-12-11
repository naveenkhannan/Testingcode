def existing_acc(t1,ac):
   x=int(input("\n Enter \n 1 for balance check \n 2: for withdrw \n 3:Deposit\n"))
   if x==1:
      print("Your balance is:",t1[ac]["Avail_Amount"])
   if x==2:
      withdraw=int(input("enter the amount to be withdrawn"))
      if withdraw<t1[ac]["Avail_Amount"]:
         print("amount withdrawn is:",withdraw)
         temp=t1[ac]["Avail_Amount"]-withdraw
         t1[ac]["Avail_Amount"]=temp
         print("your Available amount",t1[ac]["Avail_Amount"])
      else:
         print("enter lesser amount")
   if x==3:
      deposit=int(input("Please enter amount ot be deposit:"))
      print("Your balance is:",t1[ac]["Avail_Amount"])
      temp=t1[ac]["Avail_Amount"]+deposit
      t1[ac]["Avail_Amount"]=temp
      print("your Available balance after deposit is",t1[ac]["Avail_Amount"])
      
            
               
