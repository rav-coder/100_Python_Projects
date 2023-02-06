from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    heading.config(text='TIMER', fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text='')
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        heading.config(text='BREAK', fg=PINK)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        heading.config(text='BREAK', fg=RED)
    else:
        count_down(WORK_MIN * 60)
        heading.config(text='WORK', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(num):
    global reps, timer

    count_sec = num % 60
    if count_sec < 10:
        count_sec = '0' + str(count_sec)

    time = f"{int(num / 60)}:{count_sec}"
    canvas.itemconfig(timer_text, text=time)

    if num > 0:
        timer = window.after(1000, count_down, num - 1)
    else:
        reps += 1
        start_timer()
        text = ""
        for _ in range(int(reps / 2)):
            text += '✔'
        checkmark.config(text=text)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App ✔")
window.config(padx=100, pady=50, bg=YELLOW)

heading = Label(text="TIMER", font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
heading.grid(row=1, column=2)

checkmark = Label(font=(FONT_NAME, 15, 'bold'), fg=GREEN, bg=YELLOW)
checkmark.grid(row=4, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 132, text='00:00', fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=2, column=2)

start_b = Button(text='Start', highlightthickness=0, command=start_timer)
start_b.grid(row=3, column=1)

reset_b = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_b.grid(row=3, column=3)

window.mainloop()
