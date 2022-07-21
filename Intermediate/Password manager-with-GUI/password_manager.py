#Create a password generator with GUI
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#----------------SAVE PASSWORD TO FILE----------

def save():
    websites=website_entry.get()
    emails=email_entry.get()
    passwords=passwd_entry.get()
    if len(websites)==0 or len(passwords)==0:
        messagebox.showinfo(title="Data Missing",message="Please fill all fields")
    else:
        is_ok=messagebox.askokcancel(title=websites,message=f"Verify the Details :\nEmail:{emails}\nPassword: {passwords}\nDo you want to Save?")
        if is_ok:
            with open("data.txt","a")as data_file:
                data_file.write(f"{websites} | {emails} | {passwords}\n")
                website_entry.delete(0,END)
                email_entry.delete(0,END)
                passwd_entry.delete(0,END)


#-----------------Generate auto password-------------
#Creating valid data range
def password_generate():
    passwd_entry.delete(0, END)
    upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case=upper_case.lower()
    numbers="0123456789"
    symbols="!@#$%^&*()><."
    total=upper_case+lower_case+numbers+symbols
    passwd="".join(random.sample(total,14))
    passwd_entry.insert(0,passwd)
    pyperclip.copy(passwd)   #To copy password to clipboard







#------------UI SETUP---------------
from tkinter import *

window=Tk()
window.title("Password manager")

window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)

canvas.grid(row=0,column=1)



#Labels
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)
creator_label=Label(text="Created by Aswin ks")
creator_label.grid(row=9,column=0)
github_label=Label(text="More projects @ https://github.com/aswinks1995")
github_label.grid(row=10,column=0)
#Entries(text fields)
website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"test@gmail.com")
passwd_entry=Entry(width=35)
passwd_entry.grid(row=3,column=1,columnspan=2)


#Buttons
generate_password_button=Button(text="Generate Password",command=password_generate)
generate_password_button.grid(row=4,column=2,columnspan=2)
add_button=Button(text="Add",command=save)

add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()