"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they 
will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and 
printing out that many copies of the previous message. 
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)
"""

def main():
    name = input("Please input name: ")
    age = int(input("Please input age: "))
    age_100 = 100-age
    times_repeat = int(input("How many times would you like this repeated? Input Number: "))
    return name, age, age_100, times_repeat


if __name__ == "__main__":
    name, age, age_100, times_repeat = main()
    print(f"{name}, you are {age} years old and will turn 100 in {age_100} years!\n"*times_repeat)
