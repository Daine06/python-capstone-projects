import pandas as pd  
import tkinter as tk
import random 

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv('data/french_words.csv')
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
else:
    dict_data = data.to_dict(orient='records')


########## Counter ##########
def is_known():
    dict_data.remove(current_card)
    data = pd.DataFrame(dict_data)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()

########## Switching cards ##########

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict_data)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text= current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text= current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back)
    

########## APP UI ##########
window = tk.Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

### Canvas ###
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file='./images/card_front.png')
card_back = tk.PhotoImage(file='./images/card_back.png')
card_background = canvas.create_image(400, 263, image= card_front)

card_title = canvas.create_text(400, 150, text="", font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text="", font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

### Images ###
right_img = tk.PhotoImage(file='images/right.png')
wrong_img = tk.PhotoImage(file='images/wrong.png')

### Buttons ###
unknown_button = tk.Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

right_button = tk.Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()

