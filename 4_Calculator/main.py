
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = float(input("What's the first number?: "))
num2 = float(input("What's the second number?: "))

run = 'y'
result = 0

while run == 'y':
    if result != 0:
        num1 = result
        num2 = float(input("What's the second number?: "))
    
    for key in operations:
        print(key)

    operation_type = input("Select an operation from above: ")

    result = operations[operation_type](num1,num2)
    print(f"{num1} {operation_type} {num2} = {result}")
    
    run = input("Type 'y' to continue operation on the result or 'n' to exit: ")

if run == 'n':
    pass


