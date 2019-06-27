



# # A list of words that 
# potential_words = ["example", "words", "someone", "can", "guess"]

# word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase

# Make it a list of letters for someone to guess
current_word = ["w", "i", "n", "n", "e", "r" ]# TIP: the number of letters should match the word

# Some useful variables
all_guesses =[]
guesses = ['_', '_', '_','_','_','_',]
maxfails = 7
fails = 0
the_word = 'winner'
the_word = the_word.lower()

while fails < maxfails:
	guess = input("Guess a letter: ")

if guess in the_word:
    for i in range(0, 6):
        if guess == the_word[i]:
            guesses[i] = the_word
else:
    print("that was not in the word")
    all_guesses.append(guess)
    fails = fails+1
    print("You have " + str(maxfails - fails) + " tries left!")

	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!
    print(current_word)

