import random
from turtle import Screen
from player import Player
from cars import Cars
from score import Score
import time

screen = Screen()
screen.setup(600,600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.up, "Up")

cars = Cars()
score = Score()

game_is_on = True
level = 0
while game_is_on:

    time.sleep(0.1)
    cars.create_cars()
    cars.move()
    screen.update()
    if player.ycor() > 300:
        player.goto(0, -280)
        cars.change_speed()
        score.create_text()
    for car in cars.list_of_cars:
        if player.distance(car) < 30:
            score.game_over()
            game_is_on = False

screen.exitonclick()