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
window.geometry("300x200")
def numberCheck():
    if amount == 0:
        window.configure(bg="gray")
    elif amount >=1:
        window.configure(bg="green")
    elif amount <=1:
        window.configure(bg="red")
numberCheck()
buttonUp = tkinter.Button(text= "Up", command=commandUp, width=50, background="white", padx=100)
buttonUp.pack(

            fill='both',

            expand=True,

            pady=20,

            padx=20

        )

label = tkinter.Label(text=amount, width=50, background="white")
label.pack(

            fill='both',

            expand=True,

            pady=20,

            padx=20

        )

buttonDown = tkinter.Button(window, text= "Down", command=commandDown, width=50, background="white")
buttonDown.pack(

            fill='both',

            expand=True,

            pady=20,

            padx=20

        )

window.mainloop()