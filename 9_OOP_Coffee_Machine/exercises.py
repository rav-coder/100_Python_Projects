# from turtle import Turtle, Screen
#
# john = Turtle()
# print(john)
# john.shape('turtle')
# john.color('red')
# john.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
#
# my_screen.exitonclick()
#

from prettytable import PrettyTable

table = PrettyTable()
table.align = 'r'
table.field_names = ['City', 'Province']
table.add_rows(
    [
        ['Calgary', 'Alberta'],
        ['Lethbridge', 'Alberta'],
        ['Vancouver', 'British Columbia'],
    ]
)

print(table)
