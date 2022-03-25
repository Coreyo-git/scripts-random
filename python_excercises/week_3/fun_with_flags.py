#--------------------------------------------------------------------
#
# Fun With Flags
#
# In the lecture demonstration program "stars and stripes" we saw
# how function definitions allowed us to reuse code that drew a
# star and a rectangle (stripe) multiple times to create a copy of
# the United States flag.
#
# As a further example of the way functions allow us to reuse code,
# in this exercise we will import the flag_elements module into
# this program and create a different flag.  In the PDF document
# accompanying this file you will find several flags which can be
# constructed easily using the "star" and "stripe" functions already
# defined.  Choose one of these and try to draw it.
#

# First we import the two functions we need (make sure a copy of file
# flag_elements.py is in the same folder as this one)
from flag_elements import star, stripe

# Import the turtle graphics functions
from turtle import *

# Set up the drawing environment
setup(600, 400)

##### PUT YOUR CODE FOR DRAWING THE FLAG HERE
def draw_stripes():
    stripes = 13 # total amount of stripes
    
    speed('fastest')
    i = 0
    while i < stripes:
        i += 1
        color = ['red', 'white']
        if (i % 2):
            stripe(400, 10, color[0])
        else:
            stripe(400, 10, color[1])
        setheading(270)
        forward(10)
    penup()
    home()
    
def draw_stars():
    stars = 50 # total amount of stars
    #
    print()

draw_stripes()
stripe(160, 80, 'blue')
draw_stars()
# Exit gracefully
hideturtle()
done()

# 6 to 5
