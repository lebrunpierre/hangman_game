import random

import utils.wordbank as wordbank
import classes.player as player


class HangManGame:
    def __init__(self):
        self.hangman_word = random.choice(wordbank.word_list).lower()
        self.blank_word = self.create_blanks()

    def print_hangman(self):
        print(self.hangman_word)
        print(self.blank_word)

    def create_blanks(self):
        '''
        makes the blank word version of the hangman word
        :return:
        '''
        blank_word = []
        for blanks in range(len(self.hangman_word)):
            blank_word.append('_')
        return blank_word

    def fill_in_blanks(self, player):
        '''
        Fills in the blanks of the blank word
        Also, checks if user won or lost
        :param player:
        :return:
        '''
        is_letter_in_word = False
        player_letter = player.player_letter_validation()
        for letter in range(len(self.hangman_word)):
            if player_letter == self.hangman_word[letter]:
                self.blank_word[letter] = player_letter
                is_letter_in_word = True

        if not is_letter_in_word:
            return player.player_lives()

        print(self.blank_word)
        if '_' not in self.blank_word:
            print("Winner")
            return False
