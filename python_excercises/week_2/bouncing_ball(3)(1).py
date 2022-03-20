## Bouncing Ball
##
## Just as printing "Hello World" is the standard first
## example completed in a new programming language, games
## packages are usually introduced with a "Bouncing Ball"
## demonstration in which a ball bounces around
## the screen.  Turtle graphics is not designed for
## creating games, but we can still produce a convincing
## bouncing ball simulation.
##
## The incomplete program below creates a black window and
## makes the cursor look like a beachball.  (Make sure the
## file 'beachball.gif' is in the same folder as this
## program.)
##
## Your job is to make the ball bounce realistically around
## the walls.  Use the following strategy.
##
## 1. Set up the window size to a known value so that you
##    know the maximum x and y coordinates (i.e., where the
##    borders are)
## 2. Lift the pen, because we don't want to leave a trail
## 3. For each of a large range of "bounces":
##    a. Choose a random position on the top border
##    b. Move the cursor to that position
##    c. Choose a random position on the left border
##    d. Move the cursor to that position
##    e. Choose a random position on the bottom border
##    f. Move the cursor to that position
##    g. Choose a random position on the right border
##    h. Move the cursor to that position
##
## Experiment with different ways of choosing the random
## positions to get the most realistic bouncing effect.
## (We found that it's best to keep the ball away from
## the corners.)

# 360 - Right
# 325 - Bottom Right
# 270 - Bottom
# 225 - Bottom Left
# 180 - Left
# 135 - Top Left
# 90 - Top
# 45 - Top Right

# 0 and 360 = right 

# 0 - 90 = top to right          
# 90 - 180 = left to top 
# 180 - 270 = left to bottom
# 270 - 360 = bottom to right

# Import the functions required
from turtle import *
from random import randint
from math import sqrt, acos, degrees, atan, tan

turn_degree = 0
startx = xcor()
starty = ycor()

def draw_border():
    color("white")
    penup()
    goto(0,0)
    pendown()
    goto(600, 0)
    goto(600, 600)
    goto(0, 600)
    goto(0,0)
    penup()
            
# Set up the playing field
def start():
    
    setup()
    title('Bouncing Ball')
    bgcolor('black')
    screensize(600, 600)
    draw_border()
    goto(300, 300) # start in middle
    pendown()
    # Create the ball's image from a file
    register_shape('beachball(3).gif')
    shape('beachball(3).gif') # make the turtle look like a ball
    
    # Set the drawing speed, if necessary
    speed('fastest')
    right(randint(0,360)) # randomizes initial direction
    
# Tracks position and borders for ball colission
def watch_border(xcord, ycord): 
    global lastHit
    global startx
    global starty
    match xcord:
        case xcord if xcord <= 50: # if the ball hits the left
            if lastHit != 1:
                lastHit = 1
                calc_rebound("left")
                
        case xcord if xcord >= 550: # if the ball hits the right
            if lastHit != 2:
                lastHit = 2
                calc_rebound("right")
                
    match ycord:
        case ycord if ycord <= 50: # if the ball hits the bottom
            if lastHit != 3:
                lastHit = 3
                calc_rebound("bottom")
                
        case ycord if ycord >= 550: # if the ball hits the top
            if lastHit != 4:
                lastHit = 4
                calc_rebound("top")
    startx = xcor()
    starty = ycor()
    
       
# Maps a reflection using trying to make   
# Thought I could calculate a right angle triangle from distance between start and hit
# Then double the x or y axis and calculate where it would redirect via angle
# Was either wrong in my assumption I could do that or just couldn't figure it out :P
# Still passes the exercise though 
def calc_distance(x1, y1, x2, y2):
    dist = sqrt(((x2 - x1) **2) + ((y2 - y1)**2)) 
    c = sqrt((dist * dist) + (dist * dist))
    calc_angle(dist, dist, c)

def calc_angle(A, B, C):
    global turn_degree
    turn_degree = degrees(acos((A * A + B * B - C * C)/(2.0 * A * B)* 2))
    print("Side A:", int(A), "| Side B:", int(B), "| Side C:", (C), "| Degrees:", turn_degree)

# Calculates the rebound of the ball
def calc_rebound(wall):
    global turn_degree
    calc_distance(startx, starty, xcor(), ycor())
    
    match wall:
        case "left":
            if starty > ycor():
                left(turn_degree)
                print("-------------------------------------")     
            else:
                right(turn_degree)
                print("-------------------------------------")
                
        case "right":
            if starty > ycor():
                right(turn_degree)
                print("-------------------------------------")
            else:
                left(turn_degree)
                print("-------------------------------------")
                
        case "bottom":
            if startx > xcor():
                right(turn_degree)
                print("-------------------------------------")
            else:
                left(turn_degree)
                print("-------------------------------------")
                
        case "top":
            if startx > xcor():
                left(turn_degree)
                print("-------------------------------------")
            else:
                right(turn_degree)
                print("-------------------------------------")
    

lastHit = 0

start()

# Main game loop
while True:
    forward(2)
    watch_border(xcor(), ycor())

# Exit gracefully
done()

