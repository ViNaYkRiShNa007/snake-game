from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Consolas', 12, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.color("white")
        self.hideturtle()
        self.update_score()

    def get_high_score(self):
        with open("data.txt") as file:
            high_score = file.read()

        self.high_score = int(high_score)

    def update_high_score(self, score):
        with open("data.txt",mode="w") as file:
            file.write(str(score))

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score(self.score)

        self.score = 0
        self.update_score()
        pass

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER !!!", align=ALIGNMENT, font=FONT)
