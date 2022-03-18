######################################################################
#
# Millions and billions
#

seconds_per_minute = 60

minutes_per_hour = 60

hours_per_day = 24

minutes_per_day = minutes_per_hour * hours_per_day

days_per_year = 365 # ignoring leap years

# Your challenge, part one: Below write code for calculating
# how many days there are in a million seconds and print the
# result to the screen.  Use floating point arithmetic to do
# the calculation and round off your answer to a whole number
# before printing it.

seconds_per_day = hours_per_day * minutes_per_hour * seconds_per_minute

# Rounded down as it seemed more realistic to round up when the unit is a days value
print("There are "+ str(int(1000000 / seconds_per_day)) + " days in 1 million seconds")


# Your challenge, part two: Below write code for calculating
# how many years there are in a billion seconds and print the
# result to the screen.  Use floating point arithmetic to do
# the calculation and round off your answer to a whole number
# before printing it.

seconds_per_year = days_per_year * hours_per_day * minutes_per_hour * seconds_per_minute
print("There are "+ str(int(1000000000 / seconds_per_year)) + " years in 1 billion seconds")

# Not sure what was meant by "Use Floating point arithmetic"