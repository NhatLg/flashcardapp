import pandas as pd
import tkinter as tk
import random

BACKGROUND_COLOR = "#B1DDC6"
df_to_learn = pd.read_csv("./data/de.csv", header=None)
df_done = pd.DataFrame()
initial_row = random.randint(0, len(df_to_learn))
next_row = random.randint(0, len(df_to_learn))

def put_back_to_learn():
    global next_row
    canvas.itemconfig(text_id1, text=df_to_learn.iloc[next_row, 0])
    next_row = random.randint(0, len(df_to_learn))


def put_to_done():
    global next_row
    df_done.append(df_to_learn.iloc[[initial_row]])
    df_to_learn.drop(initial_row)

    canvas.itemconfig(text_id1, text=df_to_learn.iloc[next_row, 0])
    next_row = random.randint(0, len(df_to_learn))

# --------------
#       UI
# --------------
window = tk.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# resources
img_incorrect = tk.PhotoImage(file="./images/wrong.png")
img_correct = tk.PhotoImage(file="./images/right.png")
img_card_front = tk.PhotoImage(file="./images/card_front.png")


canvas = tk.Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=img_card_front)
canvas.create_text(400, 150, text="German", font=("Ariel", 40, "italic"))
text_id1 = canvas.create_text(400, 263, text=df_to_learn.iloc[initial_row, 0], font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# button
btn_correct = tk.Button(image=img_correct, highlightthickness=0, command=put_to_done)
btn_correct.grid(row=1, column=0)
btn_incorrect = tk.Button(image=img_incorrect, highlightthickness=0, command=put_back_to_learn)
btn_incorrect.grid(row=1, column=1)

window.mainloop()


