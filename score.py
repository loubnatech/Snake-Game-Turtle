from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore=self.get_highscore()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.display_score()
    def get_highscore(self):
        with open("highscore.txt","r") as file:
            return int(file.read())
    def save_highscore(self):
        with open("highscore.txt","w") as file:
            file.write(str(self.highscore))
   
    
    
    def display_score(self):
        self.write(f"Score: {self.score}    HighScore:{self.highscore}",align="center",font=("arial",15,"normal"))
    def score_raise(self):
        self.score+=1
        self.clear()
        self.display_score()
    def game_over(self):
        self.clear()
        if self.score>self.highscore:
            self.highscore=self.score
            self.save_highscore()
          
        self.screen.bgcolor("crimson")
        self.goto(0,0)
        self.write(f"{'-'*10}Game over{'-'*10}\n Score :{self.score}\n\n Highscore:{self.highscore}",align="center",font=("arial",24,"normal"))