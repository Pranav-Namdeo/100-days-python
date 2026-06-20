from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
data = {}

try:
    x_data = pandas.read_csv("D:/Code/100 days python/day 31/data/to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("D:/Code/100 days python/day 31/data/french_words.csv")
    data = original_data.to_dict(orient="records")
else:
    data = x_data.to_dict(orient="records")

def flip_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(data)
    canvas.itemconfig(card_title, text="French", fill="#000000")
    canvas.itemconfig(card_word, text=random_word["French"], fill="#000000")
    canvas.itemconfig(card_background, image=front_card)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="#ffffff")
    canvas.itemconfig(card_word, text=random_word["English"], fill="#ffffff")
    canvas.itemconfig(card_background, image=back_card)

def remove_word():
    data.remove(random_word)
    to_learn = pandas.DataFrame(data)
    to_learn.to_csv("D:/Code/100 days python/day 31/data/to_learn.csv", index=False)
    flip_word()

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

front_card = PhotoImage(file="D:/Code/100 days python/day 31/images/card_front.png")
card_background = canvas.create_image(400, 263, image=front_card)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

back_card = PhotoImage(file="D:/Code/100 days python/day 31/images/card_back.png")

right_img = PhotoImage(file="D:/Code/100 days python/day 31/images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=remove_word)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="D:/Code/100 days python/day 31/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=flip_word)
wrong_button.grid(row=1, column=0)

flip_word()



window.mainloop()
