from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 190)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def Lscore(self):
        self.l_score += 1
        self.update()

    def Rscore(self):
        self.r_score += 1
        self.update()
