# Yin and Yang
#
# You are no doubt familiar with the "Yin Yang" symbol which illustrates
# the concept of complementary forces combining to produce a unified
# whole.  (If not look it up online!)  Your challenge is to draw this
# symbol accurately using Turtle graphics.  To do do you will need
# to use the "circle", "beginfill" and "endfill" functions as well as
# the usual moving and drawing functions.  Note that:
#
# * You can set the pen colour and fill colour separately via the
#   "pencolor" and "fillcolor" functions.
#
# * The "circle" function takes an optional argument, "extent",
#   measured in degrees, which tells the turtle how much of the
#   circle it should walk, e.g., circle(45, extent = 180) causes
#   the turtle to walk only half of a circle of radius 45 pixels.
#
# This exercise seems hard at first because the "circle" function
# makes the turtle walk anti-clockwise by default but we need
# it to walk in both directions.  (Hint: A negative radius will
# make it walk clockwise!)
#
# NB: An important requirement for this exercise is that it must be
# easy to change the size of the symbol.  Below is a variable
# called "radius" which defines the radius of the overall symbol.
# Your code should use this value rather than "hardwiring" pixel
# measurements so that changing the value of "radius" will cause the
# whole symbol to re-scale accordingly.
#

# Import the turtle library
from turtle import *

# Create the drawing canvas and give it a name
setup()
title('Yin and Yang')

# Define the radius of the overall symbol - changing
# this value should change the whole symbol's size,
# while retaining its proper proportions
radius = 300

## DEVELOP YOUR SOLUTION HERE

speed('fast')

# Draws half a black circle
fillcolor('black')
begin_fill()
circle(radius, 180)
end_fill()
circle(radius, 180)

# half black semi 
begin_fill()
circle(radius / 2, -180)
end_fill()

# half white semi
fillcolor('white')
begin_fill()
circle((-abs(radius) / 2), -180)
end_fill()

# small white circle
penup()
setheading(270)
goto(-abs(radius) / 6, radius)
forward(radius / 2)
pendown()
color('white')
begin_fill()
circle(radius/6)
end_fill()

# Small black circle
penup()
goto(-abs(radius) / 6, radius * 1.5)
begin_fill()
color('black')
circle(radius/6)
end_fill()


# Exit gracefully
hideturtle()
done()
