import tkinter

colors = ['black', 'purple', 'red', 'orange', 'yellow', 'white']
size = ['300x300', '250x250', '200x200', '150x150', '100x100', '50x50']

window = tkinter.Tk()
window.title("My First Window")
def countdown(count): 
    if count > 0:
        window.geometry(size[count-1])
        print(count)
        window.after(2000, countdown, count-1)
        window.configure(background=colors[count-1])
    elif count == 0:
        window.destroy()
        print("BOOM!")
 
countdown(6)

window.mainloop()