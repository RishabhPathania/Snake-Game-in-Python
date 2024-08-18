from turtle import Turtle
# from food import Big_food
ALIGNMENT='center'
FONT=('Times New Roman',20,'bold')
# big_food=Big_food()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open(r'C:\Users\KIIT\OneDrive\Desktop\PYTHON COURSES\Python_Boot_camp\21.Snake_game\data.txt',mode='r') as data:
            self.highscore=int(data.read())
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.hideturtle()
    def update_score(self):
        self.clear()
        self.write(arg=f'Score = {self.score}, High Score = {self.highscore}' ,align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open(r'C:\Users\KIIT\OneDrive\Desktop\PYTHON COURSES\Python_Boot_camp\21.Snake_game\data.txt',mode='w') as data:
                data.write(f"{self.highscore}")
        self.score=0 
        self.update_score()
    
    # def gameover(self):
    #     self.goto(0,0)
    #     self.write(arg='Game Over...',align=ALIGNMENT,font=FONT)
        
        
        
    def increase_score(self):
        self.score +=1
        self.update_score()
        # if self.score %5==0:
        #     self.big_food()

        
        