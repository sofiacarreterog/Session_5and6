#Creating a Random Library
from random import choice

#virutal bartender
drinks = [ "vodka", "whiskey", "gin", "tequila", "rum", "rakia", "sake"]
print("Welcome to the virtual pub")
name = input("I am the virtual bartender, how do I call you? ")
try:
    age = input(f"How old are you, {name}? ")
    age = int(age) #try to convert to a number
    if age >=21:
        legal = True
    elif age < 16:
        legal = False
    else:
        country = input(f"Based on your age, i have to ask where are you from, {name}?")
        legal = False
        if age >= 21:
         legal = True
        elif age >= 18 and country != "USA":
            legal = True
        elif age >= 16 and country == "Luxembourg":
            legal = True

    if age > 120 or age < 5 :
        print("Please do not lie ot the virtual bartender!")
    if legal:
        print("You are allowed to drink")
        print(f"Here is a {choice(drinks)} for you")
    else:
        print(f"Dear {name}, unfortunately I am not allowed to serve you")
except ValueError:
    print("Please give a valid age")