import turtle
import pandas
FONT = ("Courier", 10, "normal")
# turtle only works with gif

screen = turtle.Screen()
screen.title("50 US States")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

all_data = pandas.read_csv('50_states.csv')
state_names = all_data.state.to_list()
# print(state_names)

running = True
correct_guess_count = 0
while running:
    answer = screen.textinput(title=f"{correct_guess_count}/50 Correct",
                              prompt=f"Write a state name:").title()
    if answer == 'Exit':
        running = False
        pandas.DataFrame(state_names).to_csv('missed_states.csv')
        break

    if correct_guess_count == 50:
        running = False
        tim = turtle.Turtle()
        tim.penup()
        tim.write("YOU WIN!", True, align="center", font=FONT)
        tim.hideturtle()

    for state in state_names:
        if answer.lower() == state.lower():
            correct_guess_count += 1
            x_cor = int((all_data[all_data.state == answer]).x)
            y_cor = int((all_data[all_data.state == answer]).y)
            # print(f"{x_cor}. {y_cor}")
            tim = turtle.Turtle()
            tim.penup()
            tim.setposition(x=x_cor, y=y_cor)
            tim.write(answer, True, align="center", font=FONT)
            tim.hideturtle()
            state_names.remove(state)


# def mouse_click_loc(x, y):
#     print(x, y)
#
# turtle.onscreenclick(mouse_click_loc)

