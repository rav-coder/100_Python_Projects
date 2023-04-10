from time import sleep


def decorator_func(function):
    def wrapper_func():
        sleep(2)  # do something before
        function()  # maybe run the function twice
        # do something after

    return  wrapper_func

# wrap another function and give it additional functionality


@ decorator_func
def say_hello():
    print("Hello")


def say_bye():
    print("Bye!")


say_bye()  # say_bye gets triggered immediately since it does not have the decorator unlike say_hello


# decorator is basically, syntactic sugar
deco_func = decorator_func(say_bye)
deco_func()

