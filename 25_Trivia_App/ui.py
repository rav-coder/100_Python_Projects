from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self):
        self.quiz_brain = QuizBrain()

        self.window = Tk()
        self.window.title = "Quiz Now"
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text='Score: 0/0', fg="white", bg=THEME_COLOR, font=("Arial", 15))
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=500, height=400)
        self.card_question = self.canvas.create_text(
            250, 200,
            width=480,
            text="",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )

        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        cross_image = PhotoImage(file="images/false.png")
        self.unknown_button = Button(image=cross_image, highlightthickness=0, command=self.false_click)
        self.unknown_button.grid(row=2, column=0)

        checkmark_image = PhotoImage(file="images/true.png")
        self.known_button = Button(image=checkmark_image, highlightthickness=0, command=self.true_click)
        self.known_button.grid(row=2, column=1)

        self.next_q()
        self.window.mainloop()

    def next_q(self):
        if self.quiz_brain.still_has_questions():
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.card_question, text=self.quiz_brain.next_question())
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.card_question, text="End of Quiz!")
            self.unknown_button.config(state="disabled")
            self.known_button.config(state="disabled")

    def true_click(self):
        self.update_score(self.quiz_brain.check_answer("True"))

    def false_click(self):
        self.update_score(self.quiz_brain.check_answer("False"))

    def update_score(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score.config(text=f"Score: {self.quiz_brain.score}/{self.quiz_brain.question_number}")
        self.window.after(1000, self.next_q)

