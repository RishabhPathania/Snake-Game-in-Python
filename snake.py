from turtle import Turtle
STARTING=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.all_turtles=[]
        self.create_snake()
        self.head=self.all_turtles[0]
    def create_snake(self):
        for i in STARTING:
            self.add_segment(i)
    def add_segment(self,i):
        new_segments=Turtle('square')
        new_segments.color('white')
        new_segments.penup()
        new_segments.goto(i)
        self.all_turtles.append(new_segments)
    def reset(self):
        for segments in self.all_turtles:
            segments.goto(1000,1000)
        self.all_turtles.clear()
        self.create_snake()
        self.head=self.all_turtles[0]
        
    def extend(self):
        self.add_segment(self.all_turtles[-1].position())
            
    def move(self):
        for i in range(len(self.all_turtles)-1,0,-1):
            new_x=self.all_turtles[i-1].xcor()
            new_y=self.all_turtles[i-1].ycor()
            self.all_turtles[i].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    


