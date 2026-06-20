from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

front_card = PhotoImage(file="D:/Code/100 days python/day 31/images/card_front.png")
canvas.create_image(400, 263, image=front_card)
canvas.grid(row=0, column=0, rowspan=3 ,columnspan=2)

back_card = PhotoImage(file="D:/Code/100 days python/day 31/images/card_back.png")

right_img = PhotoImage(file="D:/Code/100 days python/day 31/images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(row=3, column=1)

wrong_img = PhotoImage(file="D:/Code/100 days python/day 31/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=3, column=0)

title_label = Label(text="Title", font=("Ariel", 40, "italic"), bg="#ffffff", fg="black")
title_label.grid(row=0, column=0, columnspan=2)

word_label = Label(text="Word", font=("Ariel", 60, "bold"), bg="#ffffff", fg="black")
word_label.grid(row=1, column=0, columnspan=2)


window.mainloop()
