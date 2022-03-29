import utils.hangman_art as hangman_art
class Player:

    def __init__(self):
        self.lives = len(hangman_art.stages)
        self.guess_bank = []

    def show(self):
        print(self.lives)
        print(self.guess_bank)

    def bad_guess(self):
        self.lives -= 1
        print(hangman_art.stages[self.lives])

    def player_letter_validation(self):
        userinput = input("Type in a letter to start guessing! \n")
        while userinput.isalpha() is False and len(userinput) == 1:
            userinput = input("Please only guess one letter! \n").lower()
        return userinput