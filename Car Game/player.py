from turtle import Turtle

class Player (Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.right(270)
        self.goto(0,-280)

    def up(self):
        self.forward(10)