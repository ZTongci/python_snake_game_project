from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        for number in range(3):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            x = t.pos()[0]
            t.goto(x - number * 20, 0)
            self.segments.append(t)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_number].goto(self.segments[seg_number - 1].xcor(), self.segments[seg_number - 1].ycor())
        self.segments[0].forward(20)

    def hit_body(self):
        for seg in self.segments[1:]:
            if self.segments[0].distance(seg) < 19:
                return True


    def increase_snake(self):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        x = t.pos()[0]
        t.goto(self.segments[1].pos()[0], self.segments[1].pos()[1])
        self.segments.insert(1, t)

    def reset(self):
        for seg in self.segments:
            seg.goto(10000, 10000)
        self.segments = []
        for number in range(3):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            x = t.pos()[0]
            t.goto(x - number * 20, 0)
            self.segments.append(t)
