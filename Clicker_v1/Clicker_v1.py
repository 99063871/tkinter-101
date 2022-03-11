import tkinter

amount = 0

def commandUp():
    global amount
    amount+=1
    label.configure(text=amount)

def commandDown():
    global amount
    amount-=1
    label.configure(text=amount)

window = tkinter.Tk()
window.geometry("250x100")
buttonUp = tkinter.Button(text= "Up", padx=100, command=commandUp)
buttonUp.pack()

label = tkinter.Label(text=amount, padx=100)
label.pack()

buttonDown = tkinter.Button(text= "Down", padx=100, command=commandDown)
buttonDown.pack()


window.mainloop()