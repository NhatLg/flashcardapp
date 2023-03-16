import pandas

from view import View
from model import Model

class Controller:

    def __init__(self):
        self.view = View(self)
        self.flip_timer = self.view.after(3000, func=self.flip_card)
        self.model = Model()
        self.next_card()

    def main(self):
        self.view.main()

    def next_card(self):
        self.view.after_cancel(self.flip_timer)
        print(self.model.set_new_word())
        current_word_de = self.model.set_new_word()["German"]
        self.view.display_german_card(current_word_de)
        self.view.after(3000, func=self.flip_card)

    def flip_card(self): # the flip side of the card is in English
        current_word_en = self.model.get_new_word()["English"]
        self.view.display_english_card(current_word_en)

    def btn_is_known(self):
        self.model.remove_known_word(self.model.get_new_word())
        data = pandas.DataFrame(self.model.to_learn_list)
        data.to_csv("data/words_to_learn.csv", index=False)
        self.next_card()


if __name__ == "__main__":
    flashcard = Controller()
    flashcard.main()
