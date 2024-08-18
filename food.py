from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=.5,stretch_wid=.5)
        self.color('blue')
        self.speed('fastest')
        self.eat()
        
    def eat(self):    
        self.goto(random.randint(-280,280),random.randint(-280,280))
        
# class Big_food(Food):
#     def __init__(self):
#         super().__init__()
#         self.shapesize(stretch_len=1,stretch_wid=1)
#         self.color('red')
    