#Create QR code from text or URL
#Created by : Aswin ks

import qrcode
from PIL import Image

#Asking for data
x=input("Enter the URL or text to convert to QR code: ")
if x == "": #If user didnt give an inout then choose default value.
    #Optional session: This will create the QR code with default URL!

    x="https://github.com/aswinks1995"
    print("No data provided. Using default URl to create QRcode!")
    img = qrcode.make(x)
    img.save("qr-image.jpg")
    print("QR-code saved!")
   #-----------------------------------------------------------------

else:#If user provide input then create qr code with user's input
    img = qrcode.make(x)

    img.save("qr-image.jpg")
    print("QR-code saved!")