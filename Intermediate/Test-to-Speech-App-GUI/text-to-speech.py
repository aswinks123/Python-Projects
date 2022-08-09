#program to convert text to speech.
#Created By : Aswin KS

from tkinter import *
from tkinter import scrolledtext
from turtle import bgcolor
import pyttsx3
from tkinter import messagebox #for message box

#Module to do text to speech operation
def speak():  
    txt_speech=pyttsx3.init()
    txt_speech.setProperty('rate', 150)
    text=source_input.get()
    txt_speech.say(text,)
    txt_speech.runAndWait()

#Module to clear text field
def clean():
     source_input.delete(0,END)

#method for printing about
def print_about():
    messagebox.showinfo(title="About", message="Created by Aswin KS. Find More @ https://github.com/aswinks1995")


#--------------------------------------------UI setup---------------------------------------------------------------

window=Tk()
window.title("Aswin's Text to Speech Engine")
window.resizable(0,0)  #to remove maximise button
window.config(padx=50,pady=50)
canvas=Canvas(height=200,width=300)

#label for source input box
source=Label(text="Enter the Text ")
source.grid(row=0,column=2)


#inputbox for source
source_input=Entry(width=70)
source_input.grid(row=1,column=2)

#button for Speak
search_button=Button(text="Speak",command=speak)
search_button.grid(row=1,column=3)

#button for Clear
search_button=Button(text="Clear",command=clean)
search_button.grid(row=1,column=4)


#button for About
about_button=Button(text="About",command=print_about)
about_button.grid(row=1,column=5)

window.mainloop()  #Ending 