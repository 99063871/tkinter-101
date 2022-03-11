from ctypes import sizeof
import tkinter

amount = 0

def commandUp():
    global amount
    amount+=1
    label.configure(text=amount)
    numberCheck()

def commandDown():
    global amount
    amount-=1
    label.configure(text=amount)
    numberCheck()


window = tkinter.Tk()
def numberCheck():
    if amount == 0:
        window.configure(bg="gray")
    elif amount >=1:
        window.configure(bg="green")
    elif amount <=1:
        window.configure(bg="red")
numberCheck()
buttonUp = tkinter.Button(text= "Up", command=commandUp, width=50)
buttonUp.pack(ipadx=10, ipady=10, expand=True)

label = tkinter.Label(text=amount, width=50)
label.pack(ipadx=10, ipady=10, expand=True)

buttonDown = tkinter.Button(text= "Down", command=commandDown, width=50)
buttonDown.pack(ipadx=10, ipady=10, expand=True)


window.mainloop()