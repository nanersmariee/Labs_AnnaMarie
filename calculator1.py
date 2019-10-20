


"""repeat forever"""

from arithmetic1 import *
"""import arithmetic functions for calculator"""


while True:
    """read input"""
    input_string = input("Please enter parameters> ")
    print(input_string)

    """tokenize input"""
    tokens = (input_string.split(" "))

    print(tokens)

    """If token is Q - quitting"""
    if tokens[0] == "q":
        print("You are quitting")
        break
    
    # elif len(tokens) < 2:
    #     print("Not enough parameters entered")


    """Assigned token indexes (operators and num)"""
    if len(tokens) == 2:
        operator = tokens[0]
        num1 = tokens[1]
        num2 = 0
        print(operator, num1, num2)

    elif len(tokens) == 3:
        operator = tokens[0]
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        
        if operator == "+":
            result = add(num1,num2)
        elif operator == "-":
            result = subtract(num1,num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        elif operator == "pow" :
            result = power(num1,num2)
        elif operator == "mod":
            result = mod(num1,num2)
        print(result)





# add(float, float) → float

# Return the sum of the two inputs.
# subtract(float, float) → float
# Return the second number subtracted from the first.
# multiply(float, float) → float
# Multiply the two inputs together and return the result.
# divide(float, float) → float
# Divide the first input by the second and return the result.
# square(float) → float
# Return the square of the input.
# cube(float) → float
# Return the cube of the input.
# power(float, float) → float
# Raise the first input to the power of the second and return the result.
# mod(float, float) → float
# Divide the first input by the second input and return the remainder.






    # """assign 0 to token [3] if less than 2 numbers""" 
    # elif len(tokens) < 3:
    #     num2 = 0

    # else:
    #     num2 = (tokens[2]) 









    # elif tokens[0] == "+":
    #     print(add(tokens[1], tokens[2]))

    # elif tokens[0] == "-":
    #     print(tokens[1] - tokens[2]) 

    #     else:
    # # #     decide which math function to call based on first token































# """A prefix-notation calculator."""


# from arithmetic1 import *


# while True:
#     user_input = input("> ")
#     tokens = user_input.split(" ")

#     if "q" in tokens:
#         print("You will exit.")
#         break

#     elif len(tokens) < 2:
#         print("Not enough inputs.")
#         continue

#     operator = tokens[0]
#     num1 = tokens[1]

#     if len(tokens) < 3:
#         num2 = "0"

#     else:
#         num2 = tokens[2]

#     if len(tokens) > 3:
#         num3 = tokens[3]

#     # A place to store the return value of the math function we call,
#     # to give us one clear place where that result is printed.
#     result = None

#     if not num1.isdigit() or not num2.isdigit():
#         print("Those aren't numbers!")
#         continue

#     # We have to cast each value we pass to an arithmetic function from a
#     # a string into a numeric type. If we use float across the board, all
#     # results will have decimal points, so let's do that for consistency.

#     elif operator == "+":
#         result = add(float(num1), float(num2))

#     elif operator == "-":
#         result = subtract(float(num1), float(num2))

#     elif operator == "*":
#         result = multiply(float(num1), float(num2))

#     elif operator == "/":
#         result = divide(float(num1), float(num2))

#     elif operator == "square":
#         result = square(float(num1))

#     elif operator == "cube":
#         result = cube(float(num1))

#     elif operator == "pow":
#         result = power(float(num1), float(num2))

#     elif operator == "mod":
#         result = mod(float(num1), float(num2))

#     elif operator == "x+":
#         result = add_mult(float(num1), float(num2), float(num3))

#     elif operator == "cubes+":
#         result = add_cubes(float(num1), float(num2))

#     else:
#         result = "Please enter an operator followed by two integers."

#     print(result)


