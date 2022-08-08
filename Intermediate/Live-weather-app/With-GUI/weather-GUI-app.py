#create a GUI weather app using api. We are using openweathermap Api to fetch weather info. find more detials @ https://openweathermap.org/
#Created by Aswin Ks

from tkinter import *
import requests
from tkinter import messagebox


#--------------------------Method to fetch weather details from Open weather api--------------------------------------
def fetch_weather():


    api_key='705f27d5f8729c3f9553535ecfb11f34' #you can get this api key from the https://openweathermap.org/ websites api section.create an account and use your api key.
    user_input=place_entry.get()

    if user_input =="":   #if user didnt enter any data
        messagebox.showinfo(title="Data Missing", message="Please enter the City Name")

    else:#if user entered data

        weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")
        if int(weather_data.json()['cod'])==404: #checking whether entered city exist . 404 means not exist
            messagebox.showinfo(title="Data Missing", message="Invalid City Name!")
        else: #if not 404

            lname = weather_data.json()['name']
            weather_condition = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])
            temp=temp,"C"

            #Pringing the output of the fetched result
            output_label_place = Label(text="City: ")
            output_label_place.grid(row=1, column=1)
            place_labeloutput = Label(text=lname)
            place_labeloutput.grid(row=1, column=2)

            output_label_weather = Label(text="Weather Condition: ")
            output_label_weather.grid(row=2, column=1)
            weather_condition = Label(text=weather_condition)
            weather_condition.grid(row=2, column=2)


            output_label_temperature = Label(text="Temperature: ")
            output_label_temperature.grid(row=3, column=1)
            temperature=Label(text=temp)
            temperature.grid(row=3,column=2)



#--------------------------------------------UI setup---------------------------------------------------------------

window=Tk()

#Title bar
window.title("Aswin's Weather App")

window.config(padx=50,pady=50)
canvas=Canvas(height=200,width=300)

#image
logo=PhotoImage(file="logow.png")
canvas.create_image(80,80,image=logo)
canvas.grid(row=8,column=3)


#label
place_label1=Label(text="Enter City Name")
place_label1.grid(row=0,column=1)

#inputbox
place_entry=Entry(width=35)
place_entry.grid(row=0,column=2)

#button
search_button=Button(text="Search",command=fetch_weather)
search_button.grid(row=0,column=3)


#for printing about
def print_about():
    messagebox.showinfo(title="About", message="Created by Aswin KS. Find More @ https://github.com/aswinks1995")


#button
about_button=Button(text="About",command=print_about)
about_button.grid(row=1,column=3)



window.mainloop()