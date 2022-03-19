##  Jackson Pollock's Final Masterpiece
##
##  20th century "artists" such as Jackson Pollock achieved fame
##  by stumbling drunkenly around a canvas on the floor
##  dribbling paint out of tins. (We're not being rude - he openly
##  admitted to being drunk when creating his paintings.) However,
##  today we can achieve the same effect without getting our hands
##  dirty or taking a swig by using Python!
##  
##  Using Turtle graphics develop a program to draw many blobs 
##  (dots) of random colour, size and location on the screen.
##  The blobs should be connected by lines of "paint" of
##  various widths as if paint had been dribbled from one
##  blob to the next.  The "paint" should not go off the edge
##  of the "canvas".  Use the following solution strategy.
##
##    1. Set up the blank canvas of a known size
##    2. Ensure the pen is down
##    3. For each "blob" in a large range:
##       a. Select a random pen colour
##       b. Pick a random pen width
##       c. Go to a random location on the screen
##          (drawing as you go)
##       d. Draw a blob (dot)
##    4. Exit the program gracefully
##
##  Hint: Although you could select colours from a list of
##  names, you can get a wider range of colours, by noting
##  that Turtle's "color" function can accept three numbers
##  as arguments, representing red-green-blue pixel densities.
##  These numbers are floating point values between 0.0 and 1.0.
##  Also note that the "random" module's "uniform" function
##  produces a random floating point number.
##
##  Hint: This exercise is actually very similar to the
##  previous "Starry, Starry Night" one, so you can develop
##  your solution as an extension of that.


# Import the functions required
from turtle import *
from random import uniform, randint

## DEVELOP YOUR PROGRAM HERE

# dot random size, position and color
# Connected by lines of paint of random widths 
# None to go off edge
setup()
title("Pollock Painting")
screensize(400, 400)
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

# Checks current x coord and moves back towards middle
def cord_boundary_check(xcor, ycor):
    match xcor:
        case xcor if xcor <= 100:
            #print("x below 100")
            setheading(0)
        case xcor if xcor >= 300:
            #print("x above 300")
            setheading(180)
    match ycor:
        case ycor if ycor <= 100:
            #print("y below 100")
            setheading(90)
        case ycor if ycor >= 300:
            #print("y above 300")
            setheading(270)
        
# draws a curved line by slightly turning
# ups the line width as it progresses
def draw_curved_line():
    for line in range(20,30):
        forward(randint(5,10))
        if randint(0,1) == 1:
            right(randint(2,20))
        else:
            left(randint(2,20))
        # Randomly ups or downs the pen size 50/50 chance 
        if randint(0,1) == 1:
            pensize(pensize() + 1)
        else:
            # if the pen size is atleast greater than 1
            if pensize() > 1: 
                pensize(pensize() - 1)

# Randomly creates a dollop of paint 10-20 times
for dollop in range(randint(80, 150)):
    # Randomly selects a color
    color(colors[randint(0,5)])
    pensize(randint(2,8))
    speed('fastest')
    draw_curved_line()  
    cord_boundary_check(xcor(), ycor())        
        
    dot(randint(10,40))
    
    if xcor() > 380 or ycor() > 380:
        print(xcor(), ycor())
    
    #right(randint(40, 300))

# Exit gracefully
hideturtle()
done()
