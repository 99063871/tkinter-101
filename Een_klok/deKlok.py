import tkinter
from time import strftime
from turtle import bgcolor

window = tkinter.Tk()
window.title('Clock')
window.configure(bg='light blue')
def time():
    string = strftime('%H:%M:%S')
    label.config(text = string)
    label.after(1000, time)
label = tkinter.Label(window, 
            font = ('calibri', 100))
label.configure(bg='light blue')
label.pack(anchor = 'center')

time()
 
tkinter.mainloop()