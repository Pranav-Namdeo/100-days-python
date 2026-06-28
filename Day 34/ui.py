from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score : 0", background=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Meow", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="D:/Code/100 days python/day 34/images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="D:/Code/100 days python/day 34/images/false.png")
        self.false_button = Button(image=false_image)
        self.false_button.grid(row=2, column=1)


        self.window.mainloop()
