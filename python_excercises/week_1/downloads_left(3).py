# Music download credits
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, denoting the cost in cents for downloading one
# music track, your original budget in dollars, and the number of tracks
# already downloaded:

        #was 120?? lol not sure if that's acceptible..
track_cost = 1.2 # cost in cents for downloading one track
budget = 50 # dollars
total_budget = 50 # dollars
num_downloaded = 15 # number of tracks already downloaded

# Write expressions to calculate how many more tracks you can afford
# to download and print that value to the screen.
#
# A problem solving strategy:
# 1. Calculate the amount spent so far by
#    multiplying the number downloaded by the track cost
# 2. Calculate the balance left by
#    deducting the amount spent so far from the budget
# 3. Divide the balance left by the track cost to a whole number
# 4. Print the number of tracks left
#
# Be careful to allow for the fact that one of the given values
# is expressed in cents and the other is in dollars, i.e., the
# units associated with the values are different.

#Budget after initial 15 tracks bought
budget = budget - track_cost * num_downloaded

print("The amount spent on the initial 15 tracks: $" + str(num_downloaded * track_cost))
print("Budget left over from buying " + str(num_downloaded) + " tracks: $" + str(int(budget)))
print("The amount of tracks affordable: " + str(int(budget / track_cost))) #int rounds down
print("The amount of tracks bought totals to: " + str(int(total_budget / track_cost)))
