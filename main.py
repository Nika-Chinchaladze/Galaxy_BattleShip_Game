from turtle import Screen
from time import sleep
from Left_Ship import LeftWarShip
from Right_Ship import RightWarShip
from Left_Bullet import LeftBullets
from Right_Bullet import RightBullets
from Track_life import LifeTracker
from Winner_class import Winner
BULLET_DISTANCE = 50

# prepare screen:
screen = Screen()
screen.title("Space War")
screen.setup(width=736, height=460)
screen.bgpic("space.gif")
screen.addshape("left_ship.gif")
screen.addshape("right_ship.gif")
screen.tracer(0)

# create space warships:
left_ship = LeftWarShip()
right_ship = RightWarShip()

# create bullets:
left_bullet = LeftBullets()
right_bullet = RightBullets()

# create life tracker:
left_tracker = LifeTracker()
right_tracker = LifeTracker()
winner = Winner()
specification = LifeTracker()
specification.draw_border()

play_again = True
while play_again:

    # listen keyboard:
    screen.listen()
    screen.onkey(right_ship.move_up, "Up")
    screen.onkey(right_ship.move_down, "Down")
    screen.onkey(right_ship.move_forward, "Left")
    screen.onkey(right_ship.move_backward, "Right")
    screen.onkey(left_ship.move_up, "w")
    screen.onkey(left_ship.move_down, "s")
    screen.onkey(left_ship.move_forward, "d")
    screen.onkey(left_ship.move_backward, "a")

    play = True
    variable = 1
    while play:
        sleep(0.1)
        screen.update()
        if variable % 10 == 0:
            left_bullet.create_bullet(left_ship.xcor()+BULLET_DISTANCE, left_ship.ycor())
            right_bullet.create_bullet(right_ship.xcor()-BULLET_DISTANCE, right_ship.ycor())
        left_bullet.launch_bullet()
        right_bullet.launch_bullet()

        # right ship life:
        for l_blt in left_bullet.bullet_list:
            if right_ship.distance(l_blt) < BULLET_DISTANCE:
                l_blt.setposition(-500, 500)
                right_tracker.right_life -= 1
        # left ship life:
        for r_blt in right_bullet.bullet_list:
            if left_ship.distance(r_blt) < BULLET_DISTANCE:
                r_blt.setposition(500, 500)
                left_tracker.left_life -= 1

        left_tracker.write_left_life()
        right_tracker.write_right_life()

        # check winner:
        if left_tracker.left_life <= 0:
            winner.declare_winner("RED SHIP")
            play = False
        elif right_tracker.right_life <= 0:
            winner.declare_winner("GREEN SHIP")
            play = False

        # increase variable:
        variable += 1

    will = screen.textinput(title="end/continue", prompt="Do You Want to Try Again? Yes/No ").lower()
    if will == "no":
        play_again = False
    else:
        left_tracker.left_life = 15
        right_tracker.right_life = 15
        winner.clear()


screen.exitonclick()
