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








def clear_fields(save):

    save.pack_forget()





def saveimage():
    file="qr-image.jpg"
    image = Image.open(file)
    photo = ImageTk.PhotoImage(image)
    a = image.filename = asksaveasfilename(initialdir="/",defaultextension='.jpg',title="Select file", filetypes=(
    ('JPEG', ('*.jpg', '*.jpeg', '*.jpe', '*.jfif')), ('PNG', '*.png'), ('BMP', ('*.bmp', '*.jdib')), ('GIF', '*.gif')))
    image.save(a)
    messagebox.showinfo(title="Saved", message="QR code saved Successfully")


def New_student():
    # label for source
    source = Label(text="Enter unique code for Student")
    source.grid(row=0, column=3)

    # inputbox for source
    source_input = Entry(width=40)
    source_input.grid(row=1, column=3)


    def QR_generator():
        x=(source_input.get())
        if x == "":  # If user didnt give an input then choose default value.
            messagebox.showinfo(title="No Data Provided", message="Enter the Data first!")
        else:
            img = qrcode.make(x)
            img.save("qr-image.jpg")

            messagebox.showinfo(title="QR Created", message="QR code Created Successfully")


            #logo = PhotoImage(file="qr-image.jpg")  # chnage the path accordingly
            logo = PhotoImage(file="qr-image.jpg")

            canvas.create_image(290, 290, image=logo)
            canvas.grid(row=3, column=3)
            # button for create QR code
            save_button = Button(text="Save Image", command=saveimage)
            save_button.grid(row=3, column=5)

            clear_button = Button(window,text="Clear", command=lambda:clear_button.pack_forget())
            clear_button.grid(row=1, column=7)









            # button for create QR code
    qr_button = Button(text="Create QR code",command=QR_generator)
    qr_button.grid(row=1, column=4)









#-----------------UI---------------------
window=Tk()

#Title bar
window.title("Attendence System using openCV and Barcode")
#window.resizable(0,0)  #to remove maximise button
window.config(padx=100,pady=100)
canvas=Canvas(height=500,width=500)



#button for scan

search_button=Button(text="Scan",command=scan)
search_button.grid(row=1,column=1)

search_button=Button(text="Register a student",command=New_student)
search_button.grid(row=1,column=2)














window.mainloop()





with open('attendence.txt') as f:
    lines = f.readlines()


print(lines)
xx='https://github.com/aswinks1995'
x=xx+'\n'
if x in lines:
    print("Available")
else:
    with open('attendence.txt', 'a+') as f:
        f.write(xx+'\n')
        f.write("\n")
        print("Newly added")
