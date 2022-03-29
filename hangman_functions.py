import utils.hangman_art as hangman_art


# evaluates user input
def user_evaluation(hangmanword, incorrect_guess=0):
    user_input_bank = []
    while incorrect_guess < len(hangman_art.stages):
        userinput = user_input_validation()
        if userinput in hangmanword:
            print('Good guess')
            user_input_bank.append(userinput)

        else:
            incorrect_guess += 1
            print("Wrong")
            print(hangman_art.stages[len(hangman_art.stages) - incorrect_guess])
    print("You lost")


def user_input_validation():
    userinput = input("Type in a letter to start guessing! \n")
    while userinput.isalpha() is False and len(userinput) == 1:
        userinput = input("Please only guess one letter! \n").lower()
    return userinput



def display(hangmanword):
    underscore = []
    for letter in range(len(hangmanword)):
        underscore.append('_')
    print(underscore)


