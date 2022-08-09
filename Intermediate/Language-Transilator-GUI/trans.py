#Program to tanslate languages.This uses google translate module to do the transilation
#Created by Aswin KS


import googletrans
from tkinter import *  #for creating GUI
from tkinter import messagebox #for message box
from googletrans import Translator 
from numpy import common_type
import pyperclip #for copy to clipboard


#-----Method to translate--------------------
def transilate():
    dest.delete(0,END)
    translator = Translator()

    input=source_input.get()
    print(input)
    destination=menu.get()
    result = translator.translate(input,dest=destination)
    dest.insert(0,result.text)

#-----Method to Copy text to clipboard--------------------
def copyclip():  
    op=dest.get()
    pyperclip.copy(op)   #To copy password to clipboard 
    messagebox.showinfo(title="Data Copied", message="Data Copied to Clipboard")


#--------------------------------------------UI setup---------------------------------------------------------------
window=Tk()

#Title bar
window.title("Aswin's Transilator")
window.resizable(0,0)  #to remove maximise button
window.config(padx=50,pady=50)
canvas=Canvas(height=200,width=300)

#image
logo=PhotoImage(file="D:\\Devops\\Python-Begineer\Real-world-Projects\\Language-Transilator\\trans.png") #chnage the path accordingly
canvas.create_image(80,80,image=logo)
canvas.grid(row=4,column=3)



# Create Dropdown menu
choices = { 'English','Hindi','Gujarati','Spanish','German','malayalam'}
menu= StringVar()
menu.set("Select source Language")
drop1 = OptionMenu(window,menu,*choices) 
drop1.grid(row=0,column=1)

#label for source
source=Label(text="Enter the source text: ")
source.grid(row=1,column=1)



#inputbox for source
source_input=Entry(width=70)
source_input.grid(row=1,column=2)



# Create Dropdown menu
menu= StringVar()
menu.set("Select Destination Language")
drop2 = OptionMenu(window,menu,*choices) 
drop2.grid(row=2,column=1)




#Inputbox for Dest
dest=Entry(width=70)
dest.grid(row=2,column=2)


#button for transilate calling transilate method()
search_button=Button(text="Translate",command=transilate)
search_button.grid(row=1,column=3)

#button for copy calling copyclip method()
copy_button=Button(text="Copy",command=copyclip)
copy_button.grid(row=2,column=3)

#method for printing about
def print_about():
    messagebox.showinfo(title="About", message="Created by Aswin KS. Find More @ https://github.com/aswinks1995")


#button for About
about_button=Button(text="About",command=print_about)
about_button.grid(row=4,column=1)

window.mainloop()


