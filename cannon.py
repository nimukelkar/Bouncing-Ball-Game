from random import *
from turtle import *
from base import vector

# Here we are setting the location of the cannon in the lower left corner with (-200,-200)
# Speed of cannonball is stationary with (0,0) - it depends on where user taps

ball=vector(-200,-200)
speed=vector(0,0)
targets=[]


# This function simply returns true if cannon ball is inside the screen.
def inside(xy):
    return -200<xy.x<200 and -200<xy.y<200

# Respond to the screen tap. Speed of cannonball gets a higher value when x or y value of tap is big

def tap(x,y):
# As long as there is no ball already inside the play screen
    if not inside(ball):
        ball.x=-199
        ball.y=-199
# Sets the ball speed according to the tap. The +200 ensures speed is positive
        speed.x=(x+200)/25
        speed.y=(y+200)/25


# This function draws the present position of cannon ball and targets at the instant called.
def draw():
    clear()
# At the present position of the targets, draw the target i.e. the blue balloon
    for target in targets:
        goto(target.x,target.y)
        dot(20,'blue')
# At the present position of the cannon ball, draw the cannon ball provided it is inside the screen
    if inside(ball):
        goto(ball.x,ball.y)
        dot(6,'red')
# keeps screen updated when tracer is off
    update()


# This is for movement of ball and target
def move():

# Creating a target at a random y position on right of screen and appending to list of targets
# target is actually a current (x,y) position so targets is a list of tuples
    if randrange(40)==0:
        y=randrange(-150,150)
        target=vector(200,y)
        targets.append(target)

    for target in targets:
# At every update target position being decreased by 0.5 (i.e. moving to left)
        target.x-=0.5
    if inside(ball):
# At every update cannon ball y velocity being decreased by 0.35, x velocity unchanged
        speed.y-=0.35
# Ball being translated
        ball.move(speed)


# Will recompute target list depending on if ball has hit target or not
    dupe=targets.copy()
    targets.clear()

    for target in dupe:
# If distance between ball and target is < 13, destroy target else append it to the list
        if abs(target-ball)>13:
            targets.append(target)
    draw()

# If target is not inside the screen boundary, game will be over
    for target in targets:
        if not inside(target):
            return
    ontimer(move,50)

setup(420,420,370,0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

