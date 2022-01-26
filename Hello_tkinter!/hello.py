import tkinter

window = tkinter.Tk()
window.title("Hello")
window.geometry("200x150")
window.configure(background="blue")

box = tkinter.Label(
    window,
    text="Hello\ntkinter!",
    font=("arial", 20),
    bg="red",
    fg="black"
)
box.pack(
    ipadx=20,
    ipady=20,
    expand=True
)
window.mainloop()