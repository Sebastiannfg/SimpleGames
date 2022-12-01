# Simple Pong Game by Sebastian Grut, Following the tutorial https://www.youtube.com/watch?v=XGf2GcyHPhc&t=14s

# Overhaul of physics system, implementing angle and momentum based ball bouncing.
# Giving more creative freedom with what can be programmed.


#             ____  _____  _  _  ___    ____  __    __  __  ___
#            (  _ \(  _  )( \( )/ __)  (  _ \(  )  (  )(  )/ __)
#             )___/ )(_)(  )  (( (_-.   )___/ )(__  )(__)( \__ \
#            (__)  (_____)(_)\_)\___/  (__)  (____)(______)(___/


# Imports
import turtle
import random
import math

#Preferences
debug_mode = True

# Turtle environment setup + Screen setup
wn = turtle.Screen()
wn.title("Pong by Sebastian")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#Drawing the border
border_pencil = turtle.Turtle()
border_pencil.speed(0)
border_pencil.shape("square")
border_pencil.color("white")
border_pencil.shapesize(stretch_wid=0.1,stretch_len=0.1)
border_pencil.penup()
border_pencil.goto(-400,300)
border_pencil.pendown()
border_pencil.goto(400,300)
border_pencil.goto(400,-300)
border_pencil.goto(-400,-300)
border_pencil.goto(-400,300)
# -- All variables requiring definition before looping are defined here --

#Scores
score_a = 0
score_b = 0

#Velocities
a_vel = 0
b_vel = 0
ball_velocity = 0.7

#Paddle Power
paddle_a_power = False
paddle_b_power = False

# -- All Turtles are created and moved to their starting positions --

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.angle = (math.pi)/4

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
if debug_mode == True:
    pass
else:
    pen.write("Player A: 0 PlayerB: 0", align="center", font = ("Courier", 24, "normal"))
# -- Important infrastructure setup --

# Functions

#Paddle A Movement
def paddle_a_up():
    global a_vel
    a_vel += 0.3
def paddle_a_down():
    global a_vel
    a_vel -= 0.3

#Paddle B Movement
def paddle_b_up():
    global b_vel
    b_vel += 0.3
def paddle_b_down():
    global b_vel
    b_vel -= 0.3

#Power Mode
def paddle_a_power_strike():
    global paddle_a_power
    if paddle_a_power:
        paddle_a.color("white")
    else:
        paddle_a.color("orange")
    paddle_a_power = not paddle_a_power
def paddle_b_power_strike():
    global paddle_b_power
    if paddle_b_power:
        paddle_b.color("white")
    else:
        paddle_b.color("orange")
    paddle_b_power = not paddle_b_power

# Keyboard binding

wn.listen()

#Paddle a Movement
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")

#Paddle b Movement
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#Power
wn.onkeypress(paddle_a_power_strike, "e")
wn.onkeypress(paddle_b_power_strike, "p")

# -- Main game loop --
a=1
old_angle = ball.angle

def move_balls():
    global score_a, score_b, a, a_vel, b_vel, old_angle, ball_velocity, debug_mode, paddle_a_power, paddle_b_power
    # -- Physics Drivers --

    # Deceleration
    dec = 0.003

    a_vel = a_vel - a_vel*(dec)
    paddle_a.sety( paddle_a.ycor() + a_vel )

    b_vel = b_vel - b_vel * (dec)
    paddle_b.sety( paddle_b.ycor() + b_vel )

    # -- Main --
    wn.update()

    # Moving Ball
    if ball.angle > math.pi:
        ball.angle -= math.pi*2
    elif ball.angle <= -math.pi:
        ball.angle += math.pi*2

    ball.setx(ball.xcor() + ball_velocity*math.sin(ball.angle))
    ball.sety(ball.ycor() + ball_velocity*math.cos(ball.angle))
    # -- Section for Bouncing --

    # Border checking Paddles
    if paddle_a.ycor() > 250:
        a_vel = -a_vel
        paddle_a.sety(250)
    elif paddle_a.ycor() < -250:
        a_vel = -a_vel
        paddle_a.sety(-250)

    if paddle_b.ycor() > 250:
        b_vel = -b_vel
        paddle_b.sety(250)
    elif paddle_b.ycor() < -250:
        b_vel = -b_vel
        paddle_b.sety(-250)

    # Border checking Ball
    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.angle = -ball.angle + math.pi

    if ball.xcor() > 390:
        ball.goto(0,random.randint( -200,200))
        ball.angle = -math.pi * random.uniform(0.1, 0.9)
        score_a += 1
        pen.clear()
        ball_velocity = 0.7
        if debug_mode == False:# DEBUG CODE
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))
    elif ball.xcor() < -390:
        ball.goto(0, random.randint(-200,200))
        ball.angle = math.pi * random.uniform(0.1, 0.9)
        score_b += 1
        pen.clear()
        ball_velocity = 0.7
        if debug_mode == False: # DEBUG CODE
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))

    if old_angle != ball.angle:
        old_angle = ball.angle

        if debug_mode == True:
            pen.clear()
            pen.write("{}".format(ball.angle), align='center', font=('Courier', 24, 'bold'))
        else:
            pass

    # Paddle and ball collisions
    if (-340 < ball.xcor() < -330) and (paddle_a.ycor() - 60 < ball.ycor() < paddle_a.ycor() + 60):
        ball.setx(-330)
        ball.angle = -ball.angle
        if paddle_a_power == True:
            ball_velocity *= 2
        else:
            ball_velocity = 0.7
    elif (330 < ball.xcor() < 340) and (paddle_b.ycor() - 60 < ball.ycor() < paddle_b.ycor() + 60):
        ball.setx(330)
        ball.angle = -ball.angle
        if paddle_b_power == True:
            ball_velocity *= 2
        else:
            ball_velocity = 0.7


# -- Game Loop --
while True:
    move_balls()
    #wn.ontimer(move_balls, 1)