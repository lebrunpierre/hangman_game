import random

import hangman_functions
import utils.wordbank as wordbank
import utils.hangman_art as hangman_art
import classes.hangman_game as hangman

import classes.player as player

new_player = player.Player()
new_hangman = hangman.HangManGame()
# print to view the attributes
# print(new_player.show())


while True:
    win_or_lose = new_hangman.fill_in_blanks(new_player)
    if win_or_lose is not None:
        break
