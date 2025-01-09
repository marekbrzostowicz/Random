import random
from turtle import Turtle

random_color = ["yellow", "red", "green", "black", "blue", "pink", "brown"]
class Cars (Turtle):

    def __init__(self):
        super().__init__()
        self.car = None
        self.list_of_cars = []
        self.hideturtle()
        self.speed = -10



    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle("square")
            car.color(random.choice(random_color))
            car.shapesize(1,3)
            car.penup()
            car.goto(300, random.randint(-230, 270))
            self.list_of_cars.append(car)

    def move(self):
        for car in self.list_of_cars:
            car.forward(self.speed)
            if car.xcor() < -280:
                car.clear()
                car.hideturtle()
                self.list_of_cars.remove(car)



    def change_speed(self):
        self.speed *= 1.5



