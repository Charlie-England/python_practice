"""
Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and 
one number to divide by (check). If check divides evenly into num, 
tell that to the user. If not, print a different appropriate message.
"""

def main():
    num = int(input("Input a number: "))
    if num % 4 == 0:
        return f"{num} is a multiple of 4"
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

def two_num():
    num = int(input("Input a number: "))
    check = int(input("Input a number to divide by: "))
    if num % check == 0:
        return f"{num} is multiple of {check}"
    else:
        return f"{num} is not a multiple of {check}"

if __name__ == "__main__":
    print(main())
    print(two_num())