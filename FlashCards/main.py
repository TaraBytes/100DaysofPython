from tkinter import *
import pandas
from random import randint

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "Japanese"
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/japanese_words.csv")
else:
    print("Loading previous word list.")
finally:
    words_dict = data.to_dict(orient="records")


def update_word():
    global current_card, timer
    window.after_cancel(timer)
    random_number = randint(0, len(words_dict)-1)
    current_card = words_dict[random_number]
    canvas.itemconfig(word_text, fill="black", text=current_card[LANGUAGE])
    canvas.itemconfig(language_text, fill="black", text=LANGUAGE)
    canvas.itemconfig(card, image=front_img)
    timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card, image=back_img)
    canvas.itemconfig(language_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=current_card["English"])


def learned():
    words_dict.remove(current_card)
    df = pandas.DataFrame(words_dict)
    df.to_csv("data/words_to_learn.csv", index=False)
    update_word()


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=front_img)
language_text = canvas.create_text(400, 150, text="", font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text="", font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

x_img = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_img, highlightthickness=0, command=update_word)
x_button.grid(column=0, row=1, sticky="N")

check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, highlightthickness=0, command=learned)
check_button.grid(column=1, row=1, sticky="N")

update_word()


window.mainloop()
