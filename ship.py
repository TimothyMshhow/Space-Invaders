from turtle import Turtle
import winsound

STARTING_POSITION = (0, -350)


class Ship(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("triangle")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.color('#F06535')
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.projectiles = []

    def go_left(self):
        if self.xcor() != -350:
            new_x = self.xcor() - 15
            self.goto(x=new_x, y=self.ycor())

    def go_right(self):
        if self.xcor() != 350:
            new_x = self.xcor() + 15
            self.goto(x=new_x, y=self.ycor())

    def shoot(self):
        projectile = Turtle('circle')
        projectile.penup()
        projectile.color("white")
        projectile.setheading(90)
        projectile.goto(self.xcor(), self.ycor() + 50)
        projectile.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.shoot_sound_play()
        self.projectile_move(projectile)
        self.projectiles.append(projectile)

    def shoot_sound_play(self):
        winsound.PlaySound("shoot.wav", winsound.SND_ASYNC)

    def projectile_move(self, projectile):
        new_y = projectile.ycor() + 20
        projectile.goto(projectile.xcor(), new_y)

