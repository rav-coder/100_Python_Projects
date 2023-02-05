
## Multiple ositional arguments
def add(*args):  # args is a tuple
    print(args[0])
    new_sum = 0
    for num in args:
        new_sum += num
    return new_sum


print(add(1, 2, 3))
print(add(1, 2, 6, 7, 7, 7))


## Multiple keyword arguments
def calculate(n, **kwargs):  # kwargs is a dictionary
    # print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=2, multiply=4)


class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')  # better to use get for dictionary as it doesnt throw an error
        self.model = kw.get('model')


my_car = Car(make='Nissan', model='GTR')
print(my_car.model)

my_car = Car(make='Mazda')
print(my_car.model)  # prints None
print(my_car.make)
