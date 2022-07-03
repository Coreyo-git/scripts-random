# user input
string = input("")

# Index for loop
x = 0

for i in string:
  if i.isupper():
    # appends an _ at index x 
    # and adds the remaining string after
    string = string[:x] + "_" + string[x:]
    
    # After inserting an _ 
    # the total string index increases by 1
    # Because of the new character
    x+=1 
    
  #increment index each loop
  x+=1
  
print(string.lower())
  
