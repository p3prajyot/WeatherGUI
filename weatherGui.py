from tkinter import *
import time
from fetchWeather import *
from weather import *

def getinfo():
    city_name=textfield.get()
    wea=fetch(city_name)
    label1=Label(canvas,text=wea.get_city_name())
    label1.pack()
    label2=Label(canvas,text=wea.get_temperature())
    label2.pack()
    label3=Label(canvas,text=wea.get_weather())
    label3.pack()



canvas=Tk()
canvas.title("Weather Forecasting")
canvas.geometry("600x500")

f=("poppins",20,"bold")
t=("poppins",17,"bold")

textfield=Entry(canvas, font=f)
textfield.pack(pady=20,padx=20)
textfield.focus()


button1=Button(canvas,text="search",width=10,bg="silver",activebackground="white",font="aerial",command=getinfo)
button1.pack()


canvas.mainloop()