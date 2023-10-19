from turtle import Turtle
MOVE = False
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}", MOVE, ALIGNMENT, FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", MOVE, ALIGNMENT, FONT)