def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

n1 = float(input("Enter 1st number "))

keep_going = True

while keep_going:
    operator = input('Choose an operator (+ - * /) ')
    n2 = float(input('Enter 2nd number '))

    if operator == '+':
        result = add(n1, n2)

    elif operator == '-':
         result = subtract(n1, n2)

    elif operator == '*':
         result = multiply(n1, n2)

    elif operator == '/':
         result = divide(n1,n2)

    else:
         print("Invalid operator.")
         operator = input('Choose an operator (+ - * /) ')


    print(f"{n1} {operator} {n2} = {result}")

    choice = input("Type 'y' to contiue or 'n' to start over, 'q' to quit: ")
    
    if choice.lower() == 'y':
        n1 = result

    elif choice.lower() == 'n':
         n1 = float(input('Enter 1st number '))
         

    elif choice == 'q':
            keep_going = False

        


