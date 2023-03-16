import random
import pandas as pd


class Model:

    def __init__(self):
        self.current_word = ""
        try:
            df_word = pd.read_csv("./data/words_to_learn.csv", header=0)
        except FileNotFoundError:
            df_word = pd.read_csv("./data/de.csv")
            self.to_learn_list = df_word.to_dict(orient="records")
        else:
            self.to_learn_list = df_word.to_dict(orient="records")

    def set_new_word(self):
        self.current_word = random.choice(self.to_learn_list)
        return self.current_word

    def get_new_word(self):
        return self.current_word

    def remove_known_word(self, word):
        self.to_learn_list.remove(word)
