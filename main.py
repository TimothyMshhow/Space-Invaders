from turtle import Turtle, Screen
from ship import Ship
from invaders import Invader
from scoreboard import Scoreboard, LifeScore, WaveNumber
import time


screen = Screen()
screen.setup(width=800, height=800)
screen.bgpic("images/space.gif")
screen.title("Space Invaders")
screen.tracer(0)
screen.listen()
screen.register_shape("images/ship3.gif")
screen.register_shape("images/alien.gif")

ship = Ship()
ship.shape("images/ship3.gif")
projectiles = []
scoreboard = Scoreboard()
life_score = LifeScore()
wave_number = WaveNumber()

COLLISION_THRESHOLD = 20
invaders = []

screen.onkey(ship.go_left, key="Left")
screen.onkey(ship.go_right, key="Right")
screen.onkeypress(ship.go_left, key="Left")
screen.onkeypress(ship.go_right, key="Right")
screen.onkey(ship.shoot, key="space")


game_is_on = True


def create_invaders():
    invader_x = -235
    invader_y = 300
    for r in range(5):
        for c in range(4):
            invader = Invader((invader_x, invader_y))
            invader.shape("images/alien.gif")
            invaders.append(invader)
            invader_x += 150
        invader_x = -235
        invader_y -= 60


left_edge_reached = False

invaders_projectiles = [projectile for invader in invaders for projectile in invader.projectiles]

create_invaders()

while game_is_on:
    screen.update()
    time.sleep(0.1)


    leftmost_invader = min(invaders, key=lambda x: x.xcor()).xcor()
    rightmost_invader = max(invaders, key=lambda x: x.xcor()).xcor()

    for invader in invaders:
        invader.move()
        invader.shoot()

        if invader.projectiles and invader.projectiles[-1] not in invaders_projectiles:
            invaders_projectiles.append(invader.projectiles[-1])

    for projectile in invaders_projectiles:
        invader.enemy_projectiles_move(projectile)

    if leftmost_invader == -350:
        for invader in invaders:
            invader.move_right()

    if rightmost_invader == 350:
        for invader in invaders:
            invader.move_left()

    if ship.projectiles:
        for projectile in ship.projectiles:
            ship.projectile_move(projectile)

        # collision detection
    for invader in invaders:
        for projectile in ship.projectiles:
            if invader.distance(projectile) < 30:
                if projectile in ship.projectiles:
                    invader.hideturtle()
                    invaders.remove(invader)
                    scoreboard.score_up()
                    ship.projectiles.remove(projectile)
                    projectile.hideturtle()

    # Collision detection between the ship and invaders' projectiles
    for projectile in invaders_projectiles:
        if ship.distance(projectile) < COLLISION_THRESHOLD:
            life_score.lose_life()

    if life_score.life == 0:
        wave_number.game_over()
        break

    if not invaders:
        create_invaders()
        wave_number.next_wave()
        invader.increase_shooting_speed()


screen.exitonclick()
