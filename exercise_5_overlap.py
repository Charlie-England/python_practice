"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the 
elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure 
this out at this point - we’ll get to it soon)
"""

import random

def get_list(length):
    return [random.randint(1,15) for x in range(length)]

def main():
    # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    a_len = random.randint(7,15)
    b_len = random.randint(7,15)

    a = get_list(a_len)
    b = get_list(b_len)

    a = set(a)
    b = set(b)
    if len(a) > len(b):
        c = [x for x in a if x in b]
    else:
        c = [x for x in b if x in a]
    print(c)
    print(a)
    print(b)

if __name__ == "__main__":
    main()