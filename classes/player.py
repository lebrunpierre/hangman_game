import utils.hangman_art as hangman_art


class Player:

    def __init__(self):
        self.lives = len(hangman_art.stages) -1

    def show(self):
        print(self.lives)

    def bad_guess(self):
        '''
        Keeps track of lives and prints current hangman
        :return:
        '''
        self.lives -= 1
        print(hangman_art.stages[self.lives])

    def player_letter_validation(self):
        '''
        Validates player inputs to make sure they are entering only one valid letter
        :return:
        '''
        userinput = input("Type in a letter to start guessing! \n").lower()

        while userinput.isalpha() is False or len(userinput) != 1:
            userinput = input("Please only guess one letter! \n").lower()
        return userinput

    def player_lives(self):
        '''
        Checks if user lost and will end the game
        :return:
        '''

        print("Bad guess")
        if self.lives == 0:
            print('You lost')
            return False
        else:
            self.bad_guess()
