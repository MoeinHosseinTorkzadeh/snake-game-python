from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt",mode="r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0,270)
        self.color('white')
        self.write(f"Score: {self.score}\t\tHigh Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt","w") as file:
                file.write(str(self.score))
                self.high_score = self.score
                self.clear()
                self.new_record()
        self.score = 0


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def new_record(self):
        self.goto(0,0)
        self.color("green")
        self.write("New Record",align=ALIGNMENT,font=FONT)

