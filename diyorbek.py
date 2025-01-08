from turtle import Turtle
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

class Snake:
    def __init__(self):
        self.segs = []
        self.position = 0

        self.create_snake()
    def create_snake(self):
        for _ in range(3):
            self.add_segment()
    def reset(self):
        for each in self.segs:
            each.goto(1000,1000)
        self.segs.clear()
        self.create_snake()


    def add_segment(self):
        segment = Turtle(shape="square")
        segment.color("red")
        segment.penup()
        segment.goto(self.position, y=0)
        self.position -= 20
        self.segs.append(segment)

    def extend(self):
        tail = self.segs[-1]
        new_segment = Turtle(shape="square")
        new_segment.color("red")
        new_segment.penup()
        new_segment.goto(tail.xcor(), tail.ycor())
        self.segs.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segs) - 1, 0, -1):
            self.segs[seg_num].goto(self.segs[seg_num - 1].xcor(), self.segs[seg_num - 1].ycor())
        self.segs[0].forward(20)

    def up(self):
        if self.segs[0].heading() != DOWN:
            self.segs[0].setheading(UP)

    def right(self):
        if self.segs[0].heading() != LEFT:
            self.segs[0].setheading(RIGHT)

    def down(self):
        if self.segs[0].heading() != UP:
            self.segs[0].setheading(DOWN)

    def left(self):
        if self.segs[0].heading() != RIGHT:
            self.segs[0].setheading(LEFT)
