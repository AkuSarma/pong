"""
Author = Aku Sarma
github = https://github.com/AkuSarma

"""

import turtle 

wn = turtle.Screen()
wn.title("Pong by @AkuSarma")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer


# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# bot paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 8
ball.dy = 8

#paddle movement
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

# score
score_a = 0
score_b = 0

# scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Human : 0   Bot : 0", align="center",
          font=("courier", 24, "normal"))


# bot
def bot():
    if ball.xcor() > 0 and ball.dx == 8:
        paddle_b.goto(350, ball.ycor())
    else:
        pass


while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)

    ball.sety(ball.ycor() + ball.dy)

    bot()

    # border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Human : {score_a}   Bot : {score_b} ",
                  align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dy *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Human : {score_a}   Bot : {score_b} ",
                  align="center", font=("courier", 24, "normal"))

    # paddle and ball collision
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor()+40 > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor()+40 > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    # Maximum score is 15 but you can increase it here
    if score_a >= 15:
        break
    elif score_b >= 15:
        break
    else:
        continue

turtle.done()
