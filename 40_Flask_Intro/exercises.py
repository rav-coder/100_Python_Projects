
# python decorators

def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1*n2


# functions can be passed around as arguments. they are first-class objects

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


result = calculate(multiply, 2, 3)
print(result)


# nested funcitons

# def outer_function():
#     print("I'm outer")
#
#     def inner_function():
#         print("I'm inner")
#
#     inner_function()
#
# outer_function()


# Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def inner_function():
        print("I'm inner")

    return inner_function  # return function as an output


inner = outer_function()
inner()



