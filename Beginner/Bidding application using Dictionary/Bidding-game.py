#Bidding Game using Dictionary
#Created by : Aswin ks

import os
print("This program gets bids from participants and finally displays one with highest bid")

bidtable={}  #to store name and amount
item=input("Enter the Bid item:\n")
option=True #for while loop
maxamount=0 #counter for max bid amount
maxuser="" #counter for max bid user.this will be used in below loop



while option==True: #continuous execution until option become false

    name=input("Enter your Name: \n")
    amount=input("Enter your Bid Amount: \n")
    bidtable[name]=amount


    x=input("Any one else for Bidding?(y/n): ").lower()
    if x=='y':
        os.system('cls')
    else:
        for key in bidtable:
            vals=int(bidtable[key])
            if  vals>maxamount:  #comparing
                maxamount=vals  #replacing the new max amount value
                maxuser=key

        
        option=False


print(f"{item} sold to {maxuser} with  Bid amount: {maxamount}")  #displaying
print("Congratulations")



