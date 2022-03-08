import tkinter
import random

grabbelton = ["Dinosaurus", "Lego", "Snoep", "Playstation 6", "Poffertjes", "Berenvlees", "Stukje Pizza", "Ik", "Peperkoek"]

top = tkinter.Tk()

def helloCallBack():
    hello = random.choice(grabbelton)
    label = tkinter.Label(text=hello)
    label.pack()

button = tkinter.Button(top, text ="Grabbel", command = helloCallBack)

button.pack()
top.mainloop()

