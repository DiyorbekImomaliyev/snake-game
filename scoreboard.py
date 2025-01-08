from os import write
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.color("red")
        with open("data.txt") as prev:
            self.prev_score = prev.read()
        if self.high_score<int(self.prev_score):
            self.high_score = int(self.prev_score)
        self.update()


    def update(self):
        self.clear()
        self.goto(0, 250)
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align="center", move=True, font=("Arial", 24, "normal"))

    def reset(self):
        self.update()
        if self.high_score<int(self.prev_score):
            self.high_score = int(self.prev_score)
        elif self.score>self.high_score:
            self.high_score = self.score
        with open("data.txt", mode='w') as data:
            data.write(f"{self.high_score}")
        self.score = 0
        self.update()







