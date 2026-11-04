def add(n1, n2):
    """Return n1 plus n2."""
    return n1 + n2


def subtract(n1, n2):
    """Return n2 taken away from n1."""
    return n1 - n2


def multiply(n1, n2):
    """Return n1 multiplied by n2."""
    return n1 * n2


def divide(n1, n2):
    """Return n1 divided by n2."""
    return n1 / n2


n1 = float(input("What's the first number? "))
keep_going = True

while keep_going:
    operator = input("Pick an operator (+ - * /): ")
    n2 = float(input("What's the next number? "))

    if operator == "+":
        result = add(n1, n2)
    elif operator == "-":
        result = subtract(n1, n2)
    elif operator == "*":
        result = multiply(n1, n2)
    elif operator == "/":
        result = divide(n1, n2)

    print(f"{n1} {operator} {n2} = {result}")

    choice = input("Type 'y' to continue with the result, or 'n' to start over: ")
    if choice == "y":
        n1 = result
    else:
        n1 = float(input("What's the first number? "))
        