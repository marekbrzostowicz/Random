from turtle import Turtle

class Score (Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 1
        self.create_text()
        self.hideturtle()



    def create_text(self):
        self.goto(-240, 250)
        self.clear()
        self.write(f"Level {self.score}", False, "Center", ('Courier', 20, 'normal'))
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, "Center", ('Courier', 20, 'normal'))
