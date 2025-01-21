name = input("What is your name? ")
print("hello", name)
age = input("How old are you? ")
print(name, "you were born in", 2024-int(age))
# another way to format print is via f-strings
print(f"{name}, you were born in {2024-int(age)}")
#The stuff that you want printed has to be put in curly brackets in order to avoid the space