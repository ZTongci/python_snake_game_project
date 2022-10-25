from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score_storage.txt") as score_storage:
            self.hight_score = int(score_storage.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Your score: {self.score},Your hightest score: {self.hight_score}", True, align="center", font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.penup()
        self.goto(0, 270)
        if self.hight_score < self.score:
            with open("score_storage.txt", mode="w") as score_storage:
                score_storage.write(f"{self.score}")
        with open("score_storage.txt") as score_storage:
            self.hight_score = int(score_storage.read())
        self.write(f"Your score: {self.score},Your hightest score: {self.hight_score}", True, align="center", font=('Arial', 24, 'normal'))

    def reset(self):
        self.clear()
        self.penup()
        self.goto(0, 270)
        if self.hight_score < self.score:
            with open("score_storage.txt", mode="w") as score_storage:
                score_storage.write(f"{self.score}")
        self.score = 0
        with open("score_storage.txt") as score_storage:
            self.hight_score = int(score_storage.read())
        self.write(f"Your score: {self.score},Your hightest score: {self.hight_score}", True, align="center", font=('Arial', 24, 'normal'))

