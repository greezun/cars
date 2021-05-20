from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.score = 0
        self.goto(-220, 250)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f'Score {self.score}', move=False, align= 'center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game over.', move=False, align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.print_score()
