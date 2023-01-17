#!/bin/bash

##### deprecated as I found fdupes #####
# https://github.com/adrianlopezroche/fdupes

########## breakdown of what's happening #######

# loops through files in the pwd 

# stores the first word of md5sum "$file" 
# (the md5 sum itself) into cksm variable 
# and everything else (here, the filename 
# which the md5sum command outputs again) in $_
## context
# read cksm throwaway < <(md5sum "$file"). 
# Using $_ is just a shorthand.

# stores the md5 as a value but as a label
# checks if the label exists in the array

################################################

declare -A arr
shopt -s globstar

for file in **; do
	[[ -f "$file" ]] || continue

	read cksm _ < <(md5sum "$file")

	if ((arr[$cksm]++)); then

		# Uncomment one option below
		####################################

		## prints an rm command for each duplicate ## 
		## allows you to manually remove them by   ##
		## Copy/Pasting							   ##
		# echo "rm $file"

		## Removes duplicate files autmatically    ##
		# rm $file

		## moves duplicates to trash 			   ##
		# mv $file ~/.local/share/Trash/files/
		

		####################################
	fi
done
