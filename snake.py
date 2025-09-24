from turtle import Turtle

class Snake:
    def __init__(self, length=5, position=(0, 0)):  # shorter snake for visibility
        self.segment = []
        for i in range(length):
            seg = Turtle("square")
            seg.color("white")
            seg.penup()
            seg.goto(position[0] - i*20, position[1])
            self.segment.append(seg)
        self.head = self.segment[0]
        self.alive = True

    def movement(self):
        # Move body segments
        for i in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[i-1].xcor()
            new_y = self.segment[i-1].ycor()
            self.segment[i].goto(new_x, new_y)

        # Move head forward
        self.head.forward(10)  # faster movement for visibility

        # Check collision with body
        for segment in self.segment[1:]:
            if self.head.distance(segment) < 10:
                print("Game Over!")
                self.alive = False

        # Check collision with walls
        if abs(self.head.xcor()) > 380 or abs(self.head.ycor()) > 280:
            print("Hit the wall! Game Over!")
            self.alive = False

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
