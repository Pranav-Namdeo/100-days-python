from turtle import Turtle, Screen


screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


paddle_a = Turtle("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_a.penup()
paddle_a.teleport(350, 0)

def go_up():
    y = paddle_a.ycor()
    y += 50
    paddle_a.sety(y)

def go_down():
    y = paddle_a.ycor()
    y -= 50
    paddle_a.sety(y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
