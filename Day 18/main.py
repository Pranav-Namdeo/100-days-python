from turtle import Turtle, Screen
import random
timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(5)
timmy.speed("fastest")
colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Brown", "Black", "Gray", "Cyan", "Magenta", "Lime", "Maroon", "Navy", "Olive", "Teal", "Coral", "Turquoise", "Indigo", "Violet", "Gold", "Silver", "Beige", "Lavender", "Salmon", "Chocolate", "Crimson", "DarkBlue", "DarkGreen"]
directions = [0, 90, 180, 270]

for x in range(1000):
    timmy.color(random.choice(colors))
    timmy.setheading(random.choice(directions))
    timmy.forward(20)



screen = Screen()
screen.exitonclick()
