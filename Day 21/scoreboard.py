from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")

class scoreboard(Turtle):
    def __init__ (self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
