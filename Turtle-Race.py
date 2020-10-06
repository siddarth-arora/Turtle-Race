import turtle
import random 

wn = turtle.Screen()
wn.title("TURTLE RACE")                #Sets the title of the turtle window

s1 = 0     # Speed of the turtles
s2 = 0
s3 = 0
d1 = 0     # Distance covered by the turtles
d2 = 0
d3 = 0
bob = turtle.Turtle()
bob.pu()
bob.setpos(-100, 45)
bob.speed(10)
r_1 = turtle.Turtle()     # Defines the Turtles Racers
r_1.pu()
r_1.shape("turtle")
r_1.color("blue")
r_1.setpos(-100, 30)
r_2 = turtle.Turtle()
r_2.pu()
r_2.shape("turtle")
r_2.color("green")
r_2.setpos(-100, 0)
r_3 = turtle.Turtle()
r_3.pu()
r_3.shape("turtle")
r_3.color("yellow")
r_3.setpos(-100, -30)


for n in range(4):                     # Building of the race track
  bob.write(n, align = "center")
  for i in range(15):
    bob.pu()
    bob.fd(10)
    bob.pd()
    bob.fd(10)
  bob.pu()
  bob.backward(300)
  bob.rt(90)
  bob.fd(30)
  bob.lt(90)
bob.setpos(200, 45)
bob.rt(90)
bob.pensize(5)
for m in range(3):
  if m%2 == 0 :
    bob.pd()
    bob.color("black")
    bob.fd(30)
  else:
    bob.pd()
    bob.color("blue")
    bob.fd(30)
bob.hideturtle()
r_1.pd()
r_2.pd()
r_3.pd()

while d1 <= 300 and d2 <= 300 and d3 <= 300:    # Race time -the race will continue until any of the one racers complete a distance of 300 pixels
  s1 = random.randint(1, 10)                    # Sets the pixels each racer has to move forward as a random integer between 1 - 10
  s2 = random.randint(1, 10)
  s3 = random.randint(1, 10)
  r_1.fd(s1)
  r_2.fd(s2)
  r_3.fd(s3)
  d1 += s1                                       # The pixels moved keeps on adding to the total distance travelled by each turtle
  d2 += s2
  d3 += s3

if d1 > d2 and d1 > d3:                        # The turtle which covers the maximum distance WINS
  won = "BLUE" 
elif d2 > d1 and d2 > d3:
  won = "GREEN"
elif d3 > d1 and d3 > d2:
  won = "YELLOW"
else:                                           # A special case in which the distance travelled by any 2 or 3 turtles are equal and it's a TIE
  won = "A TIE"

bob.pu()
bob.setpos(-55, 65)
bob.lt(90)
bob.write("THE WINNER IS " + won, font=("Verdana", 15, "normal"))     # Describes the winner of the turtle race on the basis of its color




wn.exitonclick()            # Prevents the window from closing by it self