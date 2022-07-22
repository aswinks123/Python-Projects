#Created by Aswin ks
#This program will generate random complex password according to user requirement

import random   #importing random module to use random function

#Creating valid data range
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case=upper_case.lower()
numbers="0123456789"
symbols="!@#$%^&*()><."

#Asking for user requirements
l = input("Enter the Length of password: ")
h = input("How many password to generate: ")
u = int(input("Do you want upper case characters-(1/0): "))
lo = int(input("Do you want lower case characters-(1/0): "))
nm = int(input("Do you want numbers-(1/0): "))
s = int(input("Do you want symbols-(1/0): "))



#First set all requirement as YES
upper, lower,num,symb=True,True,True,True

#Making changes as per user imputs
if u==0:
    upper=False
if lo==0:
    lower=False
if s==0:
    symb=False
if num==0:
    num=False

#total will have the final string
total=""
#Appending the data range to total as per user input
if upper:
    total+=upper_case

if lower:
    total+=lower_case

if num:
    total+=numbers

if symb:
    total+=symbols


length=int(l)
count=int(h)

#Generating the password
for i in range(count):
    passwd="".join(random.sample(total,length))
    print(passwd)

