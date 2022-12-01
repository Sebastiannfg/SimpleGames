#Simple Pong Game by Sebastian Grut, Following the tutorial https://www.youtube.com/watch?v=XGf2GcyHPhc&t=14s


import turtle


wn = turtle.Screen()
wn.title("Pong by Sebastian")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

#velocity and acceleration
a_vel = 0
b_vel = 0

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
ball.dx = 0.7
ball.dy = 0.7

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 PlayerB: 0", align="center", font = ("Courier", 24, "normal"))

# Functions
def paddle_a_up():
    global a_vel
    a_vel += 0.3

def paddle_a_down():
    global a_vel
    a_vel -= 0.3

def paddle_b_up():
    global b_vel
    b_vel += 0.3

def paddle_b_down():
    global b_vel
    b_vel -= 0.3

# Keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

# Main game loop
a=1

def move_balls():
    global score_a, score_b, a, a_vel, b_vel


    #Deceleration
    dec = 0.003

    a_vel = a_vel - a_vel*(dec)
    y_a = paddle_a.ycor() + a_vel
    paddle_a.sety(y_a)

    b_vel = b_vel - b_vel * (dec)
    y_b = paddle_b.ycor() + b_vel
    paddle_b.sety(y_b)

    # Border checking
    if paddle_a.ycor() > 250:

        a_vel = -a_vel
        paddle_a.sety(250)

    if paddle_a.ycor() < -250:

        a_vel = -a_vel
        paddle_a.sety(-250)

    if paddle_b.ycor() > 250:

        b_vel = -b_vel
        paddle_b.sety(250)

    if paddle_b.ycor() < -250:

        b_vel = -b_vel
        paddle_b.sety(-250)

    #Main
    wn.update()

    # Moving Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Paddle moves


    # Border checking
    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))

    # Paddle and ball collisions
    if (330 < ball.xcor() < 340) and (paddle_b.ycor() - 60 < ball.ycor() < paddle_b.ycor() + 60):
        ball.setx(330)
        ball.dx *= -1

    elif (-340 < ball.xcor() < -330) and (paddle_a.ycor() - 60 < ball.ycor() < paddle_a.ycor() + 60):
        ball.setx(-330)
        ball.dx *= -1

while True:
    move_balls()
    wn.ontimer(move_balls, 1)
