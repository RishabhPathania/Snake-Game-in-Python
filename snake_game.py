import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

    
screen=t.Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('The Snake Game')
screen.tracer(0)
snake=Snake()
food=Food()
score=Scoreboard()
screen.listen()
screen.onkey(key='Up',fun=snake.up)
screen.onkey(key='Down',fun=snake.down)
screen.onkey(key='Left',fun=snake.left)
screen.onkey(key='Right',fun=snake.right)


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.eat()
        snake.extend()
        score.increase_score()
    if snake.head.xcor()>285 or snake.head.xcor()<-285 or snake.head.ycor()>285 or snake.head.ycor()<-285:
        score.reset()
        snake.reset()
    for turtles in snake.all_turtles[1:]:
        if snake.head.distance(turtles)<8 :
            score.reset()
            snake.reset()
        

screen.exitonclick()