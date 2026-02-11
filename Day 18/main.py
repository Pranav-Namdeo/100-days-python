from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")

shape_data = [
    {"angle" : "3", "color" :"red"},
    {"angle" : "4", "color" :"blue"},
    {"angle" : "5", "color" :"green"},
    {"angle" : "6", "color" :"yellow"},
    {"angle" : "7", "color" :"purple"},
    {"angle" : "8", "color" :"orange"},
    {"angle" : "9", "color" :"pink"},
    {"angle" : "10", "color" :"brown"}
]

for shape in shape_data:
    timmy.color(shape["color"])
    for _ in range(0, int(shape["angle"])):
        timmy.forward(100)
        timmy.right(float(360/float(shape["angle"])))


screen = Screen()
screen.exitonclick()
