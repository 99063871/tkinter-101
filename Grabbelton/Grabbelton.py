import string
import tkinter
import random

grabbelton = ["Dinosaurus", "Lego bouwset", "Snoepzak", "Playstation 6", "Poffertjes", "Berenvlees", "Stukje Pizza", "Vakantie ticket", "Peperkoek", "voetbal", "Laptop", "Fifa 12"]
grabbelAmount = 0
grabbelGrabAmount = 6
grabbelGrabAmountLeft = 6
window = tkinter.Tk()
window.title("Grabbelton")
labelAmount = tkinter.Label(text="U mag nog "+str(grabbelGrabAmountLeft)+" keer grabbelen")
labelAmount.pack()
def grabbelFunc():
    global grabbelAmount
    global grabbelGrabAmount
    global grabbelGrabAmountLeft
    grabbelGrabAmountLeft-=1
    
    if grabbelAmount < grabbelGrabAmount:
        labelAmount.configure(text="U mag nog "+str(grabbelGrabAmountLeft)+" keer grabbelen")
        item = random.choice(grabbelton)
        grabbelton.remove(item)
        label = tkinter.Label(text="Gefeliciteerd, je hebt een "+item+" gegrabbeld!")
        label.pack()
        grabbelAmount+=1
    else:
        label = tkinter.Label(text="Sorry, je mag niet meer grabbelen")
        button["state"] = "disabled"
        label.pack()

button = tkinter.Button(window, text ="Grabbelen", command = grabbelFunc)

button.pack()
window.mainloop()
