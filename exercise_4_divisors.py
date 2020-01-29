"""
Create a program that asks the user for a number and then 
prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides 
evenly into another number. For example, 13 is a divisor of 
26 because 26 / 13 has no remainder.)
"""

def main():
    user_num = int(input("Enter a number: "))
    count = 1
    rtrn_list = []
    while count <= user_num/2:
        if user_num % count == 0:
            rtrn_list.append(count)
        count+=1
    return rtrn_list

if __name__ == "__main__":
    print(main())