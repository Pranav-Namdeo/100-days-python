import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

number_of_cars = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
car = CarManager()

screen.listen()
screen.onkey(tim.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    # Detect collision with car
    for c in car.all_cars:
        if c.distance(tim) < 20:
            game_is_on = False



screen.exitonclick()
