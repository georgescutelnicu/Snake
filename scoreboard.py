from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.sety(280)
        self.hideturtle()
        with open("data.txt", "r") as file:
            self.highscore = int(file.read())
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(arg=f"Your score is: {self.score} | Highscore: {self.highscore}", align="center", font=('Arial', 15, 'normal'))


    def increase_score(self):
        self.clear()
        self.write(arg=f"Your score is: {self.score} | Highscore: {self.highscore}", align="center", font=('Arial', 15, 'normal'))
        self.score += 1

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.refresh_score()
