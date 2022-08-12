#Generate QR code for student and automate attendence report.uses Open CV for image recognition.
#Note: This project is a testing project and might contain errors.Feel free to clone and make changes accordingly!
#Created By Aswin KS



from tkinter.filedialog import asksaveasfilename
from datetime import date
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from tkinter import *
import qrcode
from tkinter import messagebox #for message box
from PIL import ImageTk, Image


#--------------Open CV------
def scan():
    cap=cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    with open('mydatafile.txt')as f:
        mydatalist=f.readlines()
    print(mydatalist)

    while True:
        success,img=cap.read()
        for barcode in decode(img):

            #print(barcode.data)
            mydata=barcode.data.decode('utf-8')
            print(mydata)

            if mydata+"\n" in mydatalist:
                myoutput='Authorized'
            else:
                myoutput='Un-Authorized!!!!'


            pts=np.array([barcode.polygon],np.int32)
            pts=pts.reshape((-1,1,2))
            cv2.polylines(img,[pts],True,(255,0,255),5)
            pts2=barcode.rect
            cv2.putText(img,myoutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)
            today = str(date.today())


            if myoutput=='Authorized':
                with open('attendence.txt') as f:
                    myatt = f.readlines()
                xx=mydata+":"+today+'\n'

                if xx in myatt:
                    print("Available!!!!!!!")
                else:
                        with open('attendence.txt', 'a+') as f:

                            f.write(mydata+":"+today)
                            f.write("\n")
            else:
                print("Unauthorized user tried to log in")

        cv2.imshow('Result',img)
        cv2.waitKey(1)
#--------------------------------------------------------------------------------------------------------------------
def attendence():#To print the Attendence data

    top = Toplevel(window)

    top.geometry("250x250")
    top.title("Attendence Window")
    my_text_box=Text(top, height=10, width=40)
    text_file = open("attendence.txt", "r")
    content = text_file.read()
    my_text_box.insert(END, content)
    text_file.close()
    my_text_box.grid(row=0,column=1)

#-------------------------------------------------------------------------------------------------------------------
def clear_fields(save): #clear text field

    save.pack_forget()

#-------------------------------------------------------------------------------------------------------------------

def saveimage(): #Save QR code
    file="qr-image.jpg"
    image = Image.open(file)
    photo = ImageTk.PhotoImage(image)
    a = image.filename = asksaveasfilename(initialdir="/",defaultextension='.jpg',title="Select file", filetypes=(
    ('JPEG', ('*.jpg', '*.jpeg', '*.jpe', '*.jfif')), ('PNG', '*.png'), ('BMP', ('*.bmp', '*.jdib')), ('GIF', '*.gif')))
    image.save(a)
    messagebox.showinfo(title="Saved", message="QR code saved Successfully")
#-------------------------------------------------------------------------------------------------------------------

def New_student():#To add a new student

    # inputbox for source
    source_input = Entry(width=40)
    source_input.grid(row=0, column=3)

    def QR_generator():
        x=(source_input.get())
        if x == "":  # If user didnt give an input then choose default value.
            messagebox.showinfo(title="No Data Provided", message="Enter the Data first!")
        else:
            img = qrcode.make(x)
            img.save("qr-image.jpg")

            messagebox.showinfo(title="QR Created", message="QR code Created Successfully")

            logo = PhotoImage(file="qr-image.jpg")

            canvas.create_image(290, 290, image=logo)
            canvas.grid(row=1, column=7)

            # button for saving image
            save_buttons = Button(text="Save Image", command=saveimage)
            save_buttons.grid(row=2, column=7)

            def addtodb():  #Add student to student authorized database
                xx=source_input.get()
                with open('mydatafile.txt', 'a+') as f:
                    f.write(xx)
                    f.write("\n")
                    messagebox.showinfo(title="Record Added", message="Student Added to Authorized Database")

            # button for adding to Student DB
            save_buttonz = Button(text="Add to DataBase", command=addtodb)
            save_buttonz.grid(row=4, column=7)


            def clean_screen():#To Hide the widget when clear button is clicked
                save_buttons.grid_forget()
                source_input.grid_forget()
                qr_button.grid_forget()
                clear_button.grid_forget()
                canvas.grid_forget()
                save_buttonz.grid_forget()
            clear_button = Button(window, text="Clear", command=clean_screen)
            clear_button.grid(row=0, column=5)

            # button for create QR code
    qr_button = Button(text="Create QR code",command=QR_generator)
    qr_button.grid(row=0, column=4)


#-----------------UI---------------------
window=Tk()

window.state("zoomed")
#Title bar
window.title("Attendence System using openCV and Barcode")

canvas=Canvas(height=500,width=500)
canvas.grid(row=5,column=5)


#button for scan

search_button=Button(text="Scan",command=scan)
search_button.grid(row=0,column=0)

view_attendence=Button(text="View Attendence",command=attendence)
view_attendence.grid(row=0,column=1)

search_button=Button(text="Register a student",command=New_student)
search_button.grid(row=0,column=2)

window.mainloop()





