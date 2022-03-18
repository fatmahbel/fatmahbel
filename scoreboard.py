from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")



# screen.title("score")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        # self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



# screen.exitonclick()

