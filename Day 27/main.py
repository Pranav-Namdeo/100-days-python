import tkinter

window = tkinter.Tk()
window.title("Meow")
window.minsize(width=600, height=400)

#Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()



window.mainloop()
