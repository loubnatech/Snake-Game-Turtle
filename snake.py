from turtle import Turtle
class Snake:
    def __init__(self):
        self.turtles=[]
        self.position=((-40,0),(-20,0),(0,0))
        self.create_snake()
        self.head=self.turtles[-1]
    def create_snake(self):
        for i in range(len(self.position)):
            new_snake=Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(self.position[i])
            self.turtles.append(new_snake)
    def move_snake(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.head.fd(20)
    def extend(self):
        new_pieces=Turtle(shape="square")
        new_pieces.color("white")
        new_pieces.penup()
        new_pieces.goto(self.position[0])
        self.turtles.insert(0,new_pieces)
    def move_up(self):
        self.head.setheading(90)
    def move_down(self):
        self.head.setheading(270)
    def move_right(self):
        self.head.setheading(0)
    def move_left(self):
        self.head.setheading(180)

