from turtle import Turtle
from random import randint

class Invader(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("gold")
        self.shape("circle")
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.penup()
        self.goto(position)
        self.setheading(180)
        self.projectiles = []
        self.shooting_speed = 1

    def move(self):
        self.forward(5)

    def move_left(self):
        self.setheading(180)

    def move_right(self):
        self.setheading(0)

    def shoot(self):
        random_chance = randint(0, 100)
        if random_chance == 1:
            projectile = Turtle('square')
            projectile.penup()
            projectile.color("gold")
            projectile.setheading(180)
            projectile.goto(self.xcor(), self.ycor() - 50)
            projectile.shapesize(stretch_wid=0.5, stretch_len=0.5)
            self.enemy_projectiles_move(projectile)
            self.projectiles.append(projectile)

    def enemy_projectiles_move(self, projectile):
        if projectile.ycor() > 300:  # Reset projectile if it goes off-screen
            projectile.goto(projectile.xcor(), -300)
        else:
            new_y = projectile.ycor() - (10 * self.shooting_speed)
            projectile.goto(projectile.xcor(), new_y)

    def increase_shooting_speed(self):
        self.shooting_speed *= 2
