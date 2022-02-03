'''
Richard Feng
ICS3U - November 16, 2021
Task: Players try to guess all of the letters in a secret word.  As they guess correctly, letters are revealed in the secret word.  However, players can only guess an incorrect letter five times.  If the user guesses the secret word in time, then they won, otherwise they lost. Word Guessing Game 
'''
# import random library
import random as rand

# hangman words, word list, guess list by user, counter for if it reaches 5 the user loses and user_continue to determine if they would like to continue or not
master_list = ["salami", "pastrami", "olives", "cheese", "grapes", "wine", "crackers", "nuts", "fruits"]
word_list = []
guess_list = []
counter = 0
user_continue = "y"

# welcome message
print("Welcome to Word Guesser!")

# Instructions for the game
print("\nInstructions: Hangman game where you guess letters in a word. If you guess wrong 5 times, you lose, if you guess the correct letters in the word, you win. Hint, the words are ingredients on a charcuterie board. Have fun!\n")

# generate random word in the list and then put each individual letter of the word into a list
word = master_list[rand.randint(0,len(master_list) - 1)]
for i in range(len(word)):
	word_list.append(word[i])

# then create a guess list fo rthe user that is filled with asterisks first
for i in range(len(word_list)):
	guess_list.append("*")

print("Your word has {0} letters! Good Luck".format(len(word)))

# while the user wants to continue to play
while(user_continue == "y"):
	# as along as the guess isn't equal to the word they continue to guess, however, if they guess 5 times and still odn't get it they exit the loop
	while(guess_list != word_list and counter != 5):
		print(" ".join(guess_list))
		guess = str(input("Guess a letter:\n"))
		
		# check if the letter is in the word
		if(guess in word_list):
			if(guess not in guess_list):
				for i in range(len(word_list)):
					if(guess == word_list[i]):
						guess_list[i] = guess
			
			# if they already guessed it
			else:
				print("Hey! You already guessed {0} correctly!".format(guess))

		# it isn't in the word	
		else:
			print("Too bad! {0} is not in the word!".format(guess))
			counter += 1

	# if they reach 5 guesses that are incorrect, then they lost and get to choose if they want to play again, and the variables get re-initialized
	if counter == 5:
		print("".join(guess_list))
		print("Boo! You lost!")
		user_continue = str(input("Would you like to play again? (y/n)\n"))

		if(user_continue == "y"):
			counter = 0
			word = master_list[rand.randint(0,len(master_list) - 1)]
			word_list.clear()
			for i in range(len(word)):
				word_list.append(word[i])

			guess_list.clear()
			for i in range(len(word_list)):
				guess_list.append("*")

			print("Your word has {0} letters! Good Luck".format(len(word)))

	# they won and same thing, variables are re-initialized if they want to play again
	else:
		print("".join(guess_list))
		print("Yay! You won!")
		user_continue = str(input("Would you like to play again? (y/n)\n"))

		if(user_continue == "y"):
			counter = 0
			word = master_list[rand.randint(0,len(master_list) - 1)]
			word_list.clear()
			for i in range(len(word)):
				word_list.append(word[i])

			guess_list.clear()
			for i in range(len(word_list)):
				guess_list.append("*")

			print("Your word has {0} letters! Good Luck".format(len(word)))
