'''
Richard feng
ICS3U
task: now there are two user and when one person inputs how many cards they gian the other player loses that much, until one has zero cards and then ask the user if they would like to start the program again
'''
# counting variable, just to keep track of how many times has passed in while loop
# to keep track of the lost cards of both players, we initialize a list
# same thing for cards, in order to keep track of both players, rathen than having two seperate variables, a list instead
counter = 0
lost_cards = []
cards = []

# welcome message
print("Welcome to your card invetory")
# this is the input, how many cards each player starts with originally
for i in range(2):
	cards.append(int(input("How many cards does Player {0} have?\n".format(i + 1))))


# while loop will continue to execute as long as the number of cards does not diminish to 0
while(cards[0] != 0 or cards[1] != 0):
	# runs twice one for each player
	for i in range(2):
		# checking to make sure one player didn't already win
		if(cards[0] != 0 and cards[1] != 0):
			# add the number of lost cards to the list
			lost_cards.append(int(input("How many cards did Player {0} lose in this round?\n".format(i + 1))))

			# if the number of cards lost is less than 0 or negative, then output that it is an invalid entry
			if(lost_cards[i-1] < 0):
				print("Error! Invalid Entry.")

			# check to see if lost cards is greater than actual cards they possess, if thats the case then you have to state that this isn't possible
			elif(lost_cards[i-1] > cards[i]):
				print("Error! You don't have {0} cards to lose.".format(lost_cards[i-1]))

			# if it satisfies none of the conditions above, or in other words that it is a positive integer less than the number of cards that player possesses, subtract the number of cards form how many cards that player has and add that same amount to the other player 
			# print the values
			# increment the counter variable as another orund has passed
			else:
				cards[i] -= lost_cards[i-1]
				cards[i-1] += lost_cards[i-1]
				print("Player 1 now has {0} cards.".format(cards[0]))
				print("Player 2 now has {0} cards.".format(cards[1]))
				counter += 1
		
				lost_cards.remove(lost_cards[0])
		
		# if they did win, output the number of orunds played and who won 
		# if the first player has 0 cards output the player 2 as the winner and vice versa
		# quit() to end the program
		else:
			print("You played {0} rounds.".format(counter))
			if(cards[0] == 0):
				print("Player 2 wins the game!")
				quit()

			else:
				print("Player 1 wins the game!")
				quit()

	


