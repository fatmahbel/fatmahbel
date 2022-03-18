from turtle import Turtle
X_POSITION = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.all_square_t = []
        self.create_snake()
        self.head = self.all_square_t[0]

    def create_snake(self):
        for square_turtle in range(0, 3):
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(x=X_POSITION[square_turtle], y=0)
            self.all_square_t.append(turtle)


    def move(self):
        for turtle_num in range(len(self.all_square_t) - 1, 0, -1):
            new_x = self.all_square_t[turtle_num - 1].xcor()
            new_y = self.all_square_t[turtle_num - 1].ycor()
            self.all_square_t[turtle_num].goto(new_x, new_y)
        self.all_square_t[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.head.setheading != DOWN:
          self.head.setheading(UP)
    def down(self):
        if self.head.setheading != UP:
           self.head.setheading(DOWN)
    def left(self):
        if self.head.setheading != RIGHT:
           self.head.setheading(LEFT)
    def right(self):
        if self.head.setheading != LEFT:
            self.head.setheading(RIGHT)





