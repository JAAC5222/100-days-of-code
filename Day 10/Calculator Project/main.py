import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

while True:
    print(art.logo)
    result = 0
    num1 = int(input("What's the first number?: "))
    valid_operation = False
    finish = False
    while not finish:
        while not valid_operation:
            print("+\n-\n*\n/")
            operation = input("Pick an operation: ")
            if operation in operations:
                valid_operation = True
                num2 = int(input("What's the second number?: "))
                result = operations[operation](num1, num2)
                print(f"{num1} {operation} {num2} = {result}")
            else:
                print("Invalid operation, please type a valid operation")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == "y":
            valid_operation = False
            num1 = result
        else:
            finish = True
            print("\n" * 20)