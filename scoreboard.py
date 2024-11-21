from turtle import Turtle
import time


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-320, y=350)
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Courier", 20, "normal"))

    def score_up(self):
        self.score += 1
        self.update_scoreboard()


class LifeScore(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.life = 3
        self.update_life()
        self.last_lost_time = 0

    def update_life(self):
        self.clear()
        self.goto(x=320, y=350)
        self.write(arg=f"Life: {self.life}", move=False, align="center", font=("Courier", 20, "normal"))

    def lose_life(self):
        current_time = time.time()
        if current_time - self.last_lost_time >= 3:
            self.life -= 1
            self.update_life()
            self.last_lost_time = current_time
        else:
            pass


class WaveNumber(Turtle):
    def __init__(self):
        super().__init__()
        self.color("gold")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.wave = 1
        self.update_wave()

    def update_wave(self):
        self.clear()
        self.goto(x=0, y=350)
        self.write(arg=f"Wave: {self.wave}", move=False, align="center", font=("Courier", 20, "normal"))

    def next_wave(self):
        self.clear()
        self.wave += 1
        self.update_wave()

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(arg=f"Game Over! You survived {self.wave - 1} waves of alien invaders!", move=False, align="center",
                   font=("Courier", 15, "normal"))



