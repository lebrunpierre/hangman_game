import random

import hangman_functions
import utils.wordbank as wordbank
import utils.hangman_art as hangman_art

print(hangman_art.logo)
hangman_word = random.choice(wordbank.word_list).lower()
print(hangman_word)


win_or_lose = hangman_functions.user_evaluation(hangman_word)




