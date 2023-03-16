import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    BACKGROUND_COLOR = "#B1DDC6"


    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title("Flash Card v1.0")
        self.config(padx=50, pady=50, bg=self. BACKGROUND_COLOR)

        self.img_incorrect = tk.PhotoImage(file="./images/wrong.png")
        self.img_correct = tk.PhotoImage(file="./images/right.png")
        self.img_card_front = tk.PhotoImage(file="./images/card_front.png")
        self.img_card_back = tk.PhotoImage(file="./images/card_back.png")
        self._make_canvas()
        self._make_btn()

    def main(self):
        self.mainloop()

    def _make_btn(self):

        self.btn_correct = tk.Button(image=self.img_correct, highlightthickness=0,
                                     command=self.controller.btn_is_known)
        self.btn_correct.grid(row=1, column=0)
        self.btn_incorrect = tk.Button(image=self.img_incorrect, highlightthickness=0,
                                       command=self.controller.next_card)
        self.btn_incorrect.grid(row=1, column=1)

    def _make_canvas(self):
        self.canvas = tk.Canvas(width=800, height=526)
        self.canvas.config(bg=self.BACKGROUND_COLOR, highlightthickness=0)
        self.card_background = self.canvas.create_image(400, 263, image=self.img_card_front)
        self.card_title = self.canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
        self.canvas.grid(row=0, column=0, columnspan=2)

    def display_german_card(self, word):
        self.canvas.itemconfig(self.card_title, text="German", fill="black")
        self.canvas.itemconfig(self.card_word, text=word, fill="black")
        self.canvas.itemconfig(self.card_background, image=self.img_card_front)

    def display_english_card(self, word):
        self.canvas.itemconfig(self.card_title, text="English", fill="white")
        self.canvas.itemconfig(self.card_word, text=word, fill="white")
        self.canvas.itemconfig(self.card_background, image=self.img_card_back)


