import turtle
import random
import math
import os

#sets the size and color of the screen
wn = turtle.Screen()
wn.setup(600,600)
wn.bgcolor("blue")

circle = turtle.Turtle()
circle.color("black")
circle.shape("circle")
circle.penup()
def spawncircle():
  circle.setpos(random.randint(-275,275), random.randint(-275,275))
spawncircle()

e = turtle.Turtle()
e.color("pink")
e.shape("square")
e.penup()
def spawne():
  e.setpos(random.randint(-275,275), random.randint(-275,275))
e.setpos(-500,-500)
#pygame/turtle specific things

player = turtle.Turtle()
image = "/home/wyatt/Documents/GitHub/turtle/rocketship.gif"
wn.register_shape(image)
player.shape(image)
player.penup


#c





#assigns functions to keys
speed = 1
def turnright():
  player.right(30)
def turnleft():
  player.left(30)
def increasespeed():
  #sets variable outside of definition
  global speed
  speed += random.randint(1,3)
def decreasespeed():
  #sets variable outside of definition
  global speed
  speed -= random.randint(1,3)
#gets input
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")

lives = 3
points = 0
turn = 0


while True:
  distance = math.sqrt(math.pow(player.xcor()-circle.xcor(),2) + math.pow(player.ycor()-circle.ycor(),2))
  distancee = math.sqrt(math.pow(player.xcor()-e.xcor(),2) + math.pow(player.ycor()-e.ycor(),2))
  if turn == 0:
    spawne()
    turn =  50
  else:
    turn -= .1
  player.forward(speed)
  if player.xcor() > 275 or player.xcor() < -275:
    player.setpos(0,0)
    lives -= 1
  elif player.ycor() > 275 or player.ycor() < -275:
    player.setpos(0,0)
    lives -= 1
  if lives <= 0:
    player.hideturtle()
    print ("Your score was" + str(points))
    break
  else:
    pass
  if distance < 25:
    circle.hideturtle()
    spawncircle()
    circle.showturtle()
    points += 1
    print (points)
  if distancee < 25:
      e.hideturtle()
      spawne()
      e.showturtle()
      lives -= 1
      print (points)
      player.setpos(0,0)

delay = input("Press Enter to finish")
#exits program on input
