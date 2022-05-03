# Gets random cat facts and shows them on click

# Import TK Inter
from tkinter import *
import requests
import json

# Api Request things
API = 'http://localhost:5000'

MeowFact = "Meoww, waiting..."

### Function / Command / Actions ------ 

# Requests a new quote via API
# Loads it to JSON
def get_new_meow_quote():
    global MeowFact
    r = requests.get(API)
    r = r.json()
    # Selects response category data, index 0 of data
    MeowFact = r["data"][0]
    MeowFactLabel.config(text = MeowFact)

### UI Begins here ------ 

# Create TK inter window
CatWindow = Tk()
CatWindow.title("Cat Facts")

# Create Label for fact text
MeowFactLabel = Label(CatWindow, text = MeowFact, bg = "white", bd = 100, font =("Arial", 10))
MeowFactLabel.pack()  

# Create New Quote Button
GetNewFactButton = Button(CatWindow, text = "Get new fact meow!", command = get_new_meow_quote)
GetNewFactButton.pack()

# Start main loops
CatWindow.mainloop()

