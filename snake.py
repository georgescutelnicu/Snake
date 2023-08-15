from turtle import Turtle

COORD = [(0, 0), (-20, 0), (-40, 0)]

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]
        self.snake_head.color("white")

    def create_snake(self):
        for position in COORD:
            self.add_segment(position)

    def reset_snake(self):
        for i in self.segments:
            i.goto(2000, 2000)
        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color("green")
        self.segments.append(new_segment)

    def snake_extend(self):
        self.add_segment(self.segments[-1].position())


    def move_snake(self):
        for segment in range (len(self.segments)-1, 0, -1):
            x = self.segments[segment-1].xcor()
            y = self.segments[segment-1].ycor()
            self.segments[segment].goto(x, y)
        self.snake_head.forward(20)


    def move_up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)
    def move_down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)
    def move_left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)
    def move_right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)