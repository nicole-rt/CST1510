"""
Addition quiz
"""
import random

while True:

    number1 = random.randint(1,9)
    number2 = random.randint(1,9)

    answer = int(input(f"What is {number1} + {number2}? "))
      
    if answer == number1 + number2:
        print("Correct!")
        break
   
    else:
        print("Try again!")
    # print(f"Incorrect! The correct answer is {number1 + number2}. ")
    