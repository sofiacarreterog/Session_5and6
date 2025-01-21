name = input("What is your name? ")
print("hello", name)
age = input("How old are you? ")
try:
    # another way to format print is via f-strings
    print(f"{name}, you were born in {2024-int(age)}")
    # hola
    # division = int(age) /0
except ValueError:
    print("age must be a valid number")
    print(f"The value that you typed was {age}")
except ZeroDivisionError:
    print("You can't divide by zero")
except: #all other types of exceptions !
    print("No idea what else can go wrong, but just in case")
else: #in case no exceptions happened
    print("thanks for being a good sport and not trying to crash the app")
finally: #this runs in the end, no matter what
print("thanks for playing")
