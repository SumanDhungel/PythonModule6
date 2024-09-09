'''
#Write a function that returns a random dice roll between 1 and 6.
# The function should not have any parameters. Write a main program that rolls the dice
# until the result is 6. The main program should print out the result of each roll.
from random import randint

def dice_roll():
    return randint(1, 6)

def main():
    attempt = 0
    while True:
        result = dice_roll()
        attempt += 1
        print(f"Roll {attempt}: it is a {result}")
        if result == 6:
            print("Finally! You got a 6.")
            break
main()
'''

'''
#Modify the function above so that it gets the number of sides on the dice as a
# parameter. With the modified function you can for example roll a 21-sided role-playing
# dice. The difference to the last exercise is that the dice rolling in the main program
# continues until the program gets the maximum number on the dice, which is asked from
# the user at the beginning.
from random import randint
def dice_roll(sides):
    return randint(1, sides)

def main():
    sides = int(input("Enter the number of sides: "))
    attempt = 0
    while True:
        result = dice_roll(sides)
        attempt += 1
        print(f"Roll {attempt}: it is a {result}")
        if result == sides:
            print(f"Finally! You got a {sides}.")
            break
main()
'''
'''
#Write a function that gets the quantity of gasoline in American gallons and returns
# the number converted to litres. Write a main program that asks for a volume in gallons
# from the user and converts the value to liters. The conversion must be done by using
# the function. Conversions continue until the user inputs a negative value.
def litres_in_gallon(gallons):
    return gallons * 3.78541

def main():
    while True:
        gallons = float(input("Enter the volume in gallons (negative value to end): "))
        if gallons < 0:
            print("The program ended.")
            break
        litres = litres_in_gallon(gallons)
        print(f"{gallons} gallons is equal to {litres:.2f} litres.")

main()
'''
'''
#Write a function that gets a list of integers as a parameter. The function returns the
# sum of all the numbers in the list. For testing, write a main program where you create
#a list, call the function, and print out the value it returned.
def sum_of_list(numbers):
    return sum(numbers)

def main():
    user_list = []
    while True:
        user_input = input("Enter a number (or 'done' to finish): ")

        if user_input.lower() == "done":
            break
        try:
            number = int(user_input)
            user_list.append(number)
        except ValueError:
            print("That's not a valid number. Please try again.")

    result = sum_of_list(user_list)
    print("The sum of the list is:", result)
main()
'''
'''
#Write a function that gets a list of integers as a parameter. The function returns a
# second list that is otherwise the same as the original list except that all uneven
# numbers have been removed. For testing, write a main program where you create a list,
# call the function, and then print out both the original as well as the cut-down list.
def generate_list():
    numbers = []
    while True:
        user_input = input("Enter a number (or press enter to finish): ")
        if user_input == "":
            break
        numbers.append(int(user_input))
    return numbers

def remove_odd(numbers):
    return [num for num in numbers if num % 2 == 0]

def main():
    first_list = generate_list()
    second_list = remove_odd(first_list)
    print(f"Generated list: {first_list}")
    print(f"Even numbers from the list: {second_list}")

main()
'''
#Write a function that receives two parameters: the diameter of a round pizza in
# centimeters and the price of the pizza in euros. The function calculates and returns
# the unit price of the pizza per square meter. The main program asks the user to enter
#the diameter and price of two pizzas and tells the user which pizza provides better
# value for money (which of them has a lower unit price). You must use the function you
# wrote for calculating the unit prices.
import math

def calculate_unit_price(diameter_cm, price_euros):
    diameter_m = diameter_cm / 100
    radius_m = diameter_m / 2
    area_m2 = math.pi * radius_m ** 2
    unit_price_per_m2 = price_euros / area_m2
    return unit_price_per_m2

def main():
    diameter_cm_pizza1 = float(input("Enter the diameter of the first pizza in cm: "))
    price_euros1 = float(input("Enter the price of the first pizza in euros: "))
    diameter_cm_pizza2 = float(input("Enter the diameter of the second pizza in cm: "))
    price_euros2 = float(input("Enter the price of the second pizza in euros: "))

    unit_price1 = calculate_unit_price(diameter_cm_pizza1, price_euros1)
    unit_price2 = calculate_unit_price(diameter_cm_pizza2, price_euros2)

    print(f"Unit price per square meter for the first pizza: {unit_price1:.2f} euros/m2")
    print(f"Unit price per square meter for the second pizza: {unit_price2:.2f} euros/m2")

    if unit_price1 < unit_price2:
        print("The first pizza offers better value for money.")
    else:
        print("The second pizza offers better value for money.")
main()