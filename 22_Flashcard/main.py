from tkinter import *
import pandas, random

# Load data from csv
try:
    data_dict = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    data_dict = pandas.read_csv("data/french_words.csv").to_dict(orient="records")

word_dict = {}


# Button click
def new_word():
    global word_dict, flip_timer
    word_dict = random.choice(data_dict)
    french_word = word_dict.get("French")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(card_img, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    english_word = word_dict.get("English")
    canvas.itemconfig(card_word, text=english_word, fill="white")
    canvas.itemconfig(card_img, image=back_img)


# Save a new csv with unknown words
def word_known():
    data_dict.remove(word_dict)
    pandas.DataFrame(data_dict).to_csv('data/words_to_learn.csv', index=False)
    new_word()


# UI
BG_COLOR = '#B1DDC6'

window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BG_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
card_img = canvas.create_image(400, 263, image=front_img)

back_img = PhotoImage(file="images/card_back.png")

card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 270, text="word", font=("Arial", 50, "bold"))

canvas.config(bg=BG_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=new_word)
unknown_button.grid(row=1, column=0)

checkmark_image = PhotoImage(file="images/right.png")
known_button = Button(image=checkmark_image, highlightthickness=0, command=word_known)
known_button.grid(row=1, column=1)

new_word()

window.mainloop()
