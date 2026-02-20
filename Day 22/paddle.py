from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.penup()
        self.teleport(position[0], position[1])

    def go_up(self):
        y = self.ycor()
        y += 50
        self.sety(y)

    def go_down(self):
        y = self.ycor()
        y -= 50
        self.sety(y)
