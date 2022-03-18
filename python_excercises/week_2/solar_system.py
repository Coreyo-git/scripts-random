#---------------------------------------------------------------------
#
# Solar system
#
# Space is big. Really big. For we mere mortals it's often hard to
# visualise the immensity of the objects in the heavens.  In this
# exercise we'll try to get an understanding of the relative sizes
# of some of the planets in our solar system, by drawing dots
# representing them all to the same scale.
#
# Below are two lists containing data about some planets in our
# solar system.  Your task is to draw a dot of the suggested colour
# and diameter for each of the planets using Turtle's
# "dot" method.  In between drawing each dot you should move
# the cursor to a different location on the screen so that the
# dots are not all on top of one another.
#
# Optionally, you can also choose to write the planet's name next
# to it, using Turtle's "write" method.  You can change the colour
# of the text displayed using Turtle's "color" method.  To change
# the font size, e.g., to 12, call the "write" method with the
# argument "font=('Arial', 12)", where 'Arial' is the font name.
#
# Importantly, you should not "hardwire" the colours and diameters
# in your code.  You should instead refer to the appropriate list
# element by its index, so that your program can draw different
# planets simply by changing the data in the lists.

from turtle import *

# Lists of data your code should refer to
name = ['Mars', 'Earth', 'Neptune', 'Venus', 'Jupiter']
diameter = [13.6, 25.6, 97.2, 24.2, 285.6] # each pixel represents 500km
colour = ['red', 'light blue', 'light grey', 'yellow', 'tan']
locations = [[150, -150], [-150, -150], [150, 150], [180,-180], [-150, -100]]

# Create a canvas representing the vast emptiness of space
setup()
title('Some planets in our solar system')
bgcolor('black')
penup() # we can draw dots with the pen up

##### Put your code for drawing the planets here
for i in range(5):
    goto(locations[i])
    setheading(90)
    forward(diameter[i] - 100)
    color(colour[i])
    dot(diameter[i])
    forward(diameter[i] + 5)
    write(name[i])

# Exit gracefully
hideturtle()
done()

