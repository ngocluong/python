from turtle import Turtle

MOVE_DISTANCE = 20
INIT_LENGTH = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        for i in range(INIT_LENGTH):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(-(20 * i), 0)
            self.segments.append(segment)

    def move(self):
        for segm in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segm - 1].xcor()
            new_y = self.segments[segm - 1].ycor()
            self.segments[segm].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(new_x, new_y)
        self.segments.append(segment)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def reset(self):
        for segm in self.segments:
            segm.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]