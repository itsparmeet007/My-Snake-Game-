from turtle import Turtle
import time
#creating constants
ALIGNMENT = "center"
FONT = ("Lucide console", 24, "bold")
score = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score :{self.score} ",align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.color("red")

        for size in range(10,40,2): #from small to big transition
            self.clear()
            self.write("GAME OVER",align=ALIGNMENT,font=("Console",size, "bold"))
            time.sleep(0.05)

    def increase_score(self):
        self.score += 100
        self.clear()
        self.update_score()


