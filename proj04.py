##############################################################################
#   Computer Project 4
#
#   Algorithm (Brief Description)
#    set variables
#    prompt for word/phrase
#    get rid of spaces to get into loop
#    use function enumerate and slicing to control guess dashed string
#    use loops to error check: symbols/numbers
#    use counter to keep track of number of guesses
#    if/else: you won/you lose
##############################################################################   


# initializes variables #
guesses = 0 # counter for iterations
guess_str = "" # inital value for guessed characters string
guess_char = " " # initial value for guessed character/phrase
current_str = "" #initial value for current string

# prints rules of game #
print("Hangman: guess letters until you can guess the whole word or phrase."
"\nIn this game you get six tries.")

# asks player for word/phrase to be guessed #
user_str = input("\nEnter a word or a phrase: ")
# takes spaces out of input #
user_str_nospace = user_str.replace(" ","")
# first loop - while user enters character that is not a letter #
while user_str_nospace.isalpha() == False:
    # print error message #
    print("Error: Only letters are allowed as input!")
    # asks for word/phrase to be guessed #
    user_str = input("\nEnter a word or a phrase: ")
    user_str_nospace = user_str.replace(" ","")
# prints user's word/phrase #
print("Phrase:", user_str)
# determines number of '-' to put and where spaces will be #
for i, ch in enumerate(user_str):
    if ch.isalpha():
        current_str = current_str+'-'
    else:
        current_str = current_str + ' '

# prints length of user's input in '-'s #
print("Current:", current_str)
print(guesses, "guesses so far out of 6")
# second loop - main loop of program
while guesses < 6 and user_str != current_str and\
guess_char.lower() != user_str.lower() and len(guess_char) == 1:
    guess_char = input("\nGuess a letter or whole word/phrase: ")
    # third loop - while character is not a letter - error check #
    if guess_char.lower() != user_str.lower() and len(guess_char) == 1:
        # loop for error checking - only letters allowed #
        while guess_char.isalpha() == False:
            print("Error: Only letters and spaces are allowed as input!")
            print(guesses, "guesses so far out of 6")
            guess_char = input("\nGuess a letter or whole word/phrase: ")
        # determines if the char guessed is in the word/phrase to be guessed #
        if guess_char.lower() not in user_str.lower():
            print("Letter not in phrase.")
        # loop associates index values with their character #
        for i, ch in enumerate(user_str):
            # if character is in user's word/phrase #
            if guess_char == ch.lower() or guess_char == ch.upper():
                # builds guess string by slicing #
                current_str = current_str[:i]+ch+current_str[(i+1):]
        print ("Current: ",current_str)
        # adds 1 to guess counter #
        guesses += 1
        guess_str = guess_str+guess_char
        print(guesses, "guesses so far out of 6:",guess_str)
# loops determining winning or losing game #
if user_str.lower() == current_str.lower()\
or user_str.lower() == guess_char.lower():
    print("You won!")
else:
    print("You lost!")
    print("The word/phrase was:", user_str)
       
# Questions
# Q1:	7
# Q2:	7
# Q3:	7
# Q4:	5
# Q5:	7    
    