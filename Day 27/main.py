from tkinter import *

window = Tk()
window.title("Meow")
window.minsize(width=600, height=400)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"

#button
def action():
    my_label["text"] = input.get()

button = Button(text="Click me", command=action)
button.pack()


#input

input = Entry()
input.pack()


window.mainloop()
