from tkinter import *

window = Tk()
window.title("Meow")
window.minsize(width=600, height=400)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"

#button

button = Button(text="Click me")
button.pack()





window.mainloop()
