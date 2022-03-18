# Change Calculator
#
# THE PROBLEM
#
# You need to calculate how much change is due when you go shopping.
# You have a $20 note and buy the following:
#   2 cartons of milk @ $2.50
#   5 Mars bars @ $1.20 each
#   1 pkt indigestion tablets @ $3.50
#
# Write an expression to calculate the change you should be given
# from $20, after buying those groceries.  Display the value of the
# change in a message to the screen.

total = 20

milk = 2.50*2
mars_bars = 1.20*5
tablets = 3.50

print(total - milk - mars_bars - tablets)

# HINTS:
# * You will need to use built-in mathematical operators: *, + and -
# * You may like to introduce variables to accumulate and store values
# * The Python function call "print(E)" will print the value of expression E

