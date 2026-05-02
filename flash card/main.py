BACKGROUND_COLOR = "#B1DDC6"
import pandas as pd
import random
from tkinter import *
random_element = {}
try:
    df = pd.read_csv('data/word_to_learn.csv')
except FileNotFoundError:
    df = pd.read_csv('data/french_words.csv')
records = df.to_dict('records')

def is_known():
    records.remove(random_element)
    pd.DataFrame(records).to_csv('data/word_to_learn.csv', index=False)
    random_fr()

def random_fr():
    global random_element, flip_timer
    window.after_cancel(flip_timer)
    random_element = random.choice(records)
    canvas.itemconfig(cart_title, text="French")
    canvas.itemconfig(card_word, text=random_element["French"])
    canvas.itemconfig(card_bg, image=car_fnt_image)
    flip_timer = window.after(3000, show_en)

def show_en():

    canvas.itemconfig(cart_title, text="English")
    canvas.itemconfig(card_word, text=random_element["English"])
    canvas.itemconfig(card_bg, image=car_bck_image)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, show_en)

canvas = Canvas(width=800, height=526)
car_fnt_image = PhotoImage(file="images/card_front.png")
car_bck_image = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=car_fnt_image)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

cart_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

cross_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross_img, highlightthickness=0, command=random_fr)
unknown_btn.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
btn_correct = Button(image=check_img, highlightthickness=0, command=is_known)
btn_correct.grid(row=1, column=1)

random_fr()
window.mainloop()