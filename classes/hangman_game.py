import random

import utils.wordbank as wordbank


class HangManGame:
    def __init__(self):
        self.hangman_word = random.choice(wordbank.word_list)
        self.blank_word = self.create_blanks()

    def create_blanks(self):
        blank_word = []
        for blanks in range(len(self.hangman_word)):
            blank_word.append('_')
        return blank_word
    def