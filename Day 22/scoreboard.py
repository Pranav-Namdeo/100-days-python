from turtle import Turtle

L = 0
R = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(L, align= "center", font= ("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(R, align= "center", font= ("Courier", 80, "normal"))

    def update_L(self):
        global L
        L += 1
        self.update_scoreboard()

    def update_R(self):
        global R
        R += 1
        self.update_scoreboard()
