from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/wather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(data["main"]["temp"]-273.15))



win = Tk()
win.title("Raushan's Weather app")
win.config(bg = "blue")
win.geometry("500 * 500")

name_label = Label(win, text =  "Raushan's Weather app",
                   font=("Time New Romn", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()

list_name = ["Kathmandu","Janakpur","Pokhara"]
com = ttk.combobox(win, text =  "Raushan's Weather app",values=list_name,
                   font=("Time New Romn", 30, "bold"))

com.place(x=25, y=50, height=50, width=450) 

done_button = Button(win, text="Done",
                     font=("Time New Roman",20,"bold"))
done_button.place(y=190,height=50,width=100,x=200)

w_label = Label(win, text="Weather climate",
                 font=("Time New Roman",20))
w_label.place(x=25,y=260,height=50,width=210)
w_label1 = Label(win, text="t",
                 font=("Time New Roman",20))
w_label1.place(x=25,y=260,height=50,width=210)

wb_label = Label(win,text="Weather Description",
                 font=("Time New Roman",17))
wb_label.place(x=25,y=330,height=50,width=210)
wb_label1 = Label(win,text="",
                  font=("Time New Roman",17))
wb_label1.place(x=25,y=330,height=50,width=210)
temp_label = Label(win,text="Temperature",
                   font=("Time New Romn", 20))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1 = Label(win,text="",
                   font=("Time New Romn", 20))
temp_label1.place(x=25,y=400,height=50,width=210)
win.mainloop()