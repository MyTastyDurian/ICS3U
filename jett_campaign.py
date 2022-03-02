'''
Richard Feng
ICS3U - February 14, 2022
Task: Create an adventure game that allows the user to traverse through imaginary land such that at every location, the respective function gets called. 
Name of the setting: Transported to the world of VALORANT
File: game.py consist of all the functions that will be called from the main function. This can be referred to as the actual "body" of the code.
'''

# importing operating system library and time library to utilize for wait and clear screen
# import random module for selecting a random integer to introduce some variability to the code
import os
from time import sleep
import random

# import the parent class attributes
from agents import *

# this is the information regarding each agent or character. what's mentioned here is what their role is and what it is, what their abilities are, and a little about themselves
# these functions will be called accordingly, when the user would like to view a particular agent's information

def jett_information():
	'''
	jett information will be printed
	'''
	print("There is Jett, a duelist. From South Korea, Jett is well equipped with utility that will enhance her movement with updrafts that allow her to jump to heights normal agents can't go to, and a dash that allows her to dash away and escape danger in an instant. Temporary smokes that will momentarily cut down enemy vision. Her ultimate ability is 5 regenerating daggers upon receiving a kill. Provided along with her movment utility, these daggers can be used with 100% accuracy even mid-air. Duelists are self-sufficient fraggers that will create space on the site for their team and challenge individual duels whenever possible.\n")

	# this is the universal error reponse. I pretty much just implemented it anywhere that involves the user input followed by decision-making

def error_response():
	'''
	universal error response will be printed
	'''
	print("Sorry, we didn't quite catch what you were trying to say. Please take a look at spelling and the options provided.\n")

# this is the closing message when the user has completed one characters entire campaign. will be called at the very end of the program
def closing_message():
	'''
	the closing message upon completing one agents campaign will be printed
	'''
	print("Thank you for playing my game!\n")

# these are the options that will be called accordingly to the decision Jett makes on this particular location: Ascent
def jett_ascent_A():
	'''
	if they chose option A, feedback will be printed

	args:
		none
	
	returns:
		False boolean value stating that the choice was incorrect
	'''
	print("You're bold huh? Taking the duel right away. You have a decent plan, however, you generally want to force the enemy to approach you by threatnening to defuse the spike. Please try again.")

	return False

def jett_ascent_B():
	'''
	if they chose option B, feedback will be printed

	args:
		none
	
	returns:
		False boolean value stating that the choice was incorrect
	'''
	print("It was explicity mentioned in the situation that you have a good economy (amount of money you have to expend for abilities and guns the next round). You want to always prioritize winning the round if its possible, but when its not posssible economy always comes second.\n")

	return False

def jett_ascent_C():
	'''
	if they chose option C, feedback will be printed

	args:
		none
	
	returns:
		True boolean value stating that the choice was correct
	'''
	print("Hey! Look at you. You're a natural already. As chefs would say taste is king. In VALORANT, information is king. Gaining information always puts you at an advantage and smoking it to protect yourself is a greater idea to concel your location temporarily.\n")
	print("You are definitely ready for the next task!\n")

	return True

# when the user selects Jett as their agent/character, the map Ascent will be called first     
def jett_ascent():
	'''
	when the map is called, they will need to slect the right choices in order to move onto the next map: a situation then a choice given

	args:
		none
	
	returns:
		True boolean value stating that the choice was correct
	'''
	print("Welcome to the map Ascent!\n")
	print("You are CT meaning that you have to defuse the spike to prevent it from blowing. You are in a 1 v 1 situation with lots of time and a good economy, just now rotating from B to A heaven (no surprises here, jett baiting the entire team :thumbs_up:). You are on A site and the spike is planted in front of generator. Which of the following actions will you take? Will you A: Dash straight into A main and check if the enemy is there. B: Save your gun and save your economy. C: Smoke the bomb with one of your cloudbursts, tap the bomb to gain information on where the enemy is and wait for their appearance.\n")

	# ask for user input of what they would like to choose
	choice = input("Choose one of the following: A, B, or C.\n")
	os.system("cls")
	can_pass = False

	# will continue to run until user selects the right option
	while(can_pass != True):
		if(choice.lower() == "a"):
			can_pass = jett_ascent_A()
			choice = input("Choose one of the following: A, B, or C.\n")
			os.system("cls")

		elif(choice.lower() == "b"):
			can_pass = jett_ascent_B()
			choice = input("Choose one of the following: A, B, or C.\n")
			os.system("cls")

		elif(choice.lower() == "c"):
			can_pass = jett_ascent_C()
			sleep(6)
			os.system("cls")
		
		else:
			error_response()
			choice = input("Choose one of the following: A, B, C.\n")
			os.system("cls")

	return True

# followed by the selection of the agent Jett and the completion of the decision-making on the map Ascent, the next map that will be called is Bind	
def jett_bind():
	'''
	given multiple choices and a situation, allows user to choose one, will continue until user has made the right decision

	args:
		none
	
	returns:
		True boolean value stating that the choice was correct
	'''
	can_pass = False

	print("This time it is the start of the round. The barriers haven't even been lifted. You have 3900 credits. What would you like to buy?\n")
	print("There are a few options: A) Buy a vandal or phantom (primary rifle choice) with full shields. B) Buy a deagle with full shields. C) Don't buy anything and wait for one of your teamates to die and pick up their weapon.\n")
	sleep(8)
	os.system("cls")

	print("Choice A) These two guns are your primary rifles. The most expensive, but the most likely to give you the greatest return. The price of the guna dn the shields is 3900.\n")
	print("Choice B) The deagle is a pistol. It's not very efficient against rifles, however, it only costs 800. With the shields the total is 1800.\n")
	print("Choice C) The price of nothing is 0.\n")

	# allows user to chose from one of the provided choices
	buy = input("What would you like to buy? (A,B,C):\n")
	os.system("cls")

	# user will continue to choose until they get the right choice
	while(can_pass != True):
		if(buy.lower() == "a"):
			print("Great Choice. You always want to full buy when possible with a few exceptions where you will learn later on. However, given the context of this situation you made the right choice. You want to always gain an advantage on your opponent by having the better equpiment.\n")
			sleep(7)
			os.system("cls")
			can_pass = True

		elif(buy.lower() == "b"):
			print("If you have really good crosshair placement and in a lower rank than you're supposed to be in, this might work. However, you always want the advantage against your opponent, if you are able to full-buy (buy best equipment), do it. Please try again.\n")
			buy = input("What would you like to buy? (A,B,C):\n")
			os.system("cls")

		elif(buy.lower() == "c"):
			print("Poor choice. This is a great way to get your teamates to hate you. Always contribute to team without needing to sacrifice the lives of your teamates. Please try again.\n")
			buy = input("What would you like to buy? (A,B,C):\n")
			os.system("cls")
		
		else:
			error_response()
			sleep(5)
			os.system("cls")
			buy = input("What would you like to buy? (A,B,C):\n")
		
	print("Now that you have a weapon, we are able to eliminate some enemys. There are 5 here.\n")

	sleep(2)
	os.system("cls")

	jett.bladestorm_points = 1

	# awaits for user input of the enter-key, upon hitting the enter-key, they eliminate an enemy
	for i in range(5):
		garbage = input("Press the enter-key to kill an enemy.\n")
		print("That's {0} enemy(ies) killed!\n".format(i+1))
		jett.bladestorm_points += 1

	sleep(1)
	os.system("cls")

	print("Wow, an ACE. You killed the entire enemy team on your own. Congratulations!\n")
	print("Everytime you get a kill or defuse a spike, you get an ultimate point. If you get 7 ultimate points, you get Jett's ultimate ability: her bladestorm. You now have 6 ultimate points. 1 from the spike you first defused on Ascent. 5 from the 5 kills you got.\n")
	print("You will now be asked before every round if you want to activate your bladestorm. However, if you don't have 7 ult points, you won't be able to use it.\n")

	sleep(10)
	os.system("cls")

	return True

# Breeze is the third map that will be called
def jett_breeze():
	'''
	In a situation given againon a different map, choices need to be made correctly in order to move onto the next map

	args:
		none

	returns:
		True boolean value that the choice was correct
	'''
	can_pass = False
	jett.cloudburst = 2
	jett.updraft = 2
	jett.dash = 1

	print("You are in a clutch situation; a 1v3 situation where you need to win or else the enemy team wins.\n")
	print("You have a lot of utility, but no gun.\n")

	# asks for user input whether or not they would like to use their ultimate ability
	ult_activation = input("Do you want to use your ultimate ability? (bladestorm) Enter either yes or no:\n")
	os.system("cls")

	# will continue to run until they decide to use their ultimate ability as that is most beneficial
	while(can_pass != True):
		if(ult_activation.lower() == "yes"):
			print("You cannot use your bladestorm at this time as you only have: {0} ultimate points. Collect {1} more points to use your ultimate ability! There is a ult point on the opposite side of the map.\n".format(jett.bladestorm_points, 7 - jett.bladestorm_points))
			sleep(6)
			os.system("cls")
			can_pass = True

		elif(ult_activation.lower() == "no"):
			print("There is an ult point you can collect on the opposite side of the map.\n")
			sleep(4)
			os.system("cls")
			can_pass = True
			
		else:
			error_response()
			sleep(4)
			os.system("cls")
			ult_activation = input("Do you want to use your ultimate ability? (bladestorm) Enter either yes or no:\n")
			can_pass = False

	can_pass = False

	# will continue to run until they collect the ult orb as they don't have sufficient ult points to use the ultimate ability
	while(can_pass != True):
		collect_ult_point = input("Do you want to collect this last ult point? (yes/no)\n")
		os.system("cls")

		if(collect_ult_point.lower() == "yes"):
			jett.bladestorm_points += 1
			print("Horray! You now have {0} ult points.".format(jett.bladestorm_points))

			ult_activation = input("Do you want to use your ultimate ability? (bladestorm) Enter either yes or no:\n")
			os.system("cls")

			# make sure they ahve the sufficient points and they want
			if(ult_activation.lower() == "yes" and jett.bladestorm_points >= 7):
				print("Watch this!\n")
				print("Choose how you would like to entry onto the site with your utility. List all on one line seperated by one space the amount of utility you would like to use. (cloudburst updraft dash) e.g (2 1 1) (you have only a maximum of 2 cloudbursts, 2 updrafts, and 1 dash)\n")

				sleep(7)
				os.system("cls")
				
				# takes a string of integers and splits them into a list which is easier to access and utilize
				util_usage = []
				util_usage_string = input("Enter the number of abilities you would like to use:\n")
				os.system("cls")
				util_usage = util_usage_string.split()

				# will continue to run until user enters va lid input (numerical value)
				while(can_pass != True):
					# error handling
					# ensure that they aren't using mroe abilities than they actually have
					try:
						if(int(util_usage[0]) > jett.cloudburst):
							jett.cloudburst -= 2
							print("You can only use up to 2 cloudbursts.\n")
							sleep(2)
							os.system("cls")
						
						else:
							jett.cloudburst -= int(util_usage[0])
						
						if(int(util_usage[1]) > jett.updraft):
							jett.updraft -= 2
							print("You can only use up to 2 updrafts.\n")
							sleep(2)
							os.system("cls")
						
						else:
							jett.updraft -= int(util_usage[1])
						
						if(int(util_usage[2]) > jett.dash):
							jett.dash -= 1
							print("You can only use up to 1 dash.\n")
							sleep(2)
							os.system("cls")

						else:
							jett.dash -= int(util_usage[2])

						print("Nice now you're onto site and you killed all the remaining people with your great entry. Great job!\n")
						print("You have {0} cloudbursts, {1} updrafts, and {2} dash left after that round. No worries though, we will buy it back next round.\n".format(jett.cloudburst, jett.updraft, jett.dash))

						sleep(8)
						os.system("cls")
						can_pass = True

					# when the user inputs a string value rather than a integer
					except:
						print("Integer value expected that meets the criteria of a max of 2 cloudburst, 2 updrafts, and 1 dash.\n")
						sleep(2)
						os.system("cls")

						util_usage = []
						util_usage_string = input("Enter the number of abilities you would like to use:\n")
						os.system("cls")
						util_usage = util_usage_string.split()

				# always resets to 0 after using it
				jett.bladestorm_points = 0
			
			elif(ult_activation.lower() == "no"):
				print("Alright, then do your best with the free pistol you have.\n")
				print("However, in this moment of indecisiveness of not moving. The enemy Yoru comes behind to flank you and one taps you which results in your death. Please try again.\n")
				sleep(7)
				os.system("cls")
				can_pass = False

			# universal error response
			else:
				error_response()
				sleep(4)
				os.system("cls")
				ult_activation = input("Do you want to use your ultimate ability? (bladestorm) Enter either yes or no:\n")
				
		elif(collect_ult_point.lower() == "no"):
			print("Alright, then do your best with the free pistol you have.\n")
			print("However, in this moment of indecisiveness of not moving. The enemy Yoru comes behind to flank you and one taps you which results in your death. Please try again.\n")
			sleep(7)
			os.system("cls")
			can_pass = False

		else:
			error_response()
			sleep(4)
			os.system("cls")

	return True

# these are the options that will be called accordingly to the decision-making of Jett on this particular map Haven along with a some variability from the random module
def jett_haven_gun():
	'''
	will randomly generate a number of potential enemies to kill

	args:
		none
	
	returns
		number of enemies that were randomly generated, meanign number of enemies killed
	'''

	enemies = 0
	# generate randome number of enemies from 1 to 5
	enemies = random.randint(1,5)
	print("Hey look! There are {0} enemies!\n".format(enemies))
	sleep(1)
	os.system("cls")

	for i in range(enemies):
		a = input("Hit your enter-key to shoot them.\n")
		print("You killed {0} enemy(ies)!".format(i+1))

	sleep(2)
	os.system("cls")

	return enemies

def jett_haven_no_gun():
	'''
	print out that without a gun, death is inevitable

	args:
		none

	returns:
		0 referring to the number of kills gotten
	'''
	print("Without a gun, you're in trouble.\n")
	print("Unfortunately when you try to use your classic pistol which is free against the Yoru with an odin, it is inevitable that you lose.\n")

	sleep(5)
	os.system("cls")

	return 0

# upon completing the first three maps as Jett, the user will select between two maps. if the map they select is Haven, this function will be called. Or if they choose split first, this function will be called second
def jett_haven():
	'''
	creates a situation in which you encourage or discourage your teammate to see your team morale/spirit

	args:
		none

	returns:
		number of kills received on this map
	'''
	can_pass = False
	print("Welcome to the map Haven!\n")
	print("Your teamate Brimstone another controller player like Astra is in a 1v3 situation where if he loses, you lost the game. Do you encourage the Brimstone or do you preemptively type GG in chat believing that there is no way he'll be able to clutch this.\n")
	encouragement = input("Enter encourage/gg (encourage if you want to encourage him, gg if you think winning this is impossible):\n")

	os.system("cls")

	buy_probability = 0
	while(can_pass != True):
		if(encouragement.lower() == "encourage"):
			# will generate a random integer from the range listed
			buy_probability = random.randint(5, 15)
			print("Brimstone clutches after you encourage him.\n")
			print("Hey! Brimstone here. Thanks for the encouragement it kept my morale high and made me believe I could clutch.\n")
			sleep(3)
			os.system("cls")
			can_pass = True

		elif(encouragement.lower() == "gg"):
			# will generate a random integer from the range listed
			buy_probability = random.randint(-4, 6)
			print("Brimston does not clutch the round.\n")
			print("Instead he types in chat: my teamates are trash.\n")

			sleep(3)
			os.system("cls")
			can_pass = True

		else:
			error_response()
			sleep(4)
			os.system("cls")
			encouragement = input("Enter encourage/gg (encourage if you want to encourage him, gg if you think winning this is impossible):\n")

	print("Now it is the next round and you don't have enough credits for a full-buy. You ask Brimstone instead who has an extra 4500 credits after full-buying.\n")
	sleep(5)
	os.system("cls")

	# kills will be assigned accordingly to the returned value of each of the haven choices
	if(buy_probability > 5 and encouragement.lower() == "encourage"):
		print("Thanks! Looks like Brimstone recognized that encouragement and decided to buy you, nice!\n")
		kills = jett_haven_gun()

	elif(buy_probability == 5 and encouragement.lower() == "encourage"):
		print("I guess that after Brimstone clutched that he believes he brings more value to the team than you. Unlucky.\n")
		kills = jett_haven_no_gun()

	elif(buy_probability <= 5 and encouragement.lower() == "gg"):
		print("well, you probably should have encouraged the Brimstone instead and maybe he would have bought you.\n")
		kills = jett_haven_no_gun()

	elif(buy_probability > 5 and encouragement.lower() == "gg"):
		print("Wow I guess Brimstone was really nice and understands to set aside differences in order to win the game. Good teamate.\n")
		kills = jett_haven_gun()

	sleep(5)
	os.system("cls")

	return kills

# thse are the options that will be called accorindly to the decision-making of Jett on this paricular map Split 
def jett_split_A():
	'''
	prints feedback for the choice made

	args:
		none
	
	returns:
		false a boolean value that indicates the choice made was incorrect
	'''
	print("This is never a good idea to bait your teamates. Please try again.\n")
	sleep(2)
	os.system("cls")

	return False

def jett_split_B():
	'''
	prints feedback for the choice made

	args:
		none
	
	returns:
		true a boolean value that indicates the choice made was correct
	'''
	print("This is a great choice. If one site is strong in terms of defense, they are sacrificing the other site's defensive capabilities.\n")
	sleep(4)
	os.system("cls")

	return True
	
def jett_split_C():
	'''
	prints feedback for the choice made

	args:
		none
	
	returns:
		true a boolean value that indicates the choice made was correct
	'''
	print("If things aren't going accordingly to plan, switch it up. Play for picks. Throw the enemy team off. Great choice.\n")
	sleep(3)
	os.system("cls")

	return True

def jett_split():
	'''
	placed in yet another situation where they ahve to make the correct decision

	args:
		none

	returns:
		none
	'''
	# upon completing the first three maps as Jett, the user will select between two maps. if the map they select is Split, this function will be called. Or if they choose Haven first, this function will be called seconddef jett_split():
	can_pass = False

	print("Welcome to the map Split!\n")
	print("Your team finds themelves in a toroubling position. The enemy viper has B site on lockdown with her viper smoke creating a one-way in which only the enmy viper can see your feet, whereas you cannot see anything.\n")
	print("You team isn't able to entry site as whenever you try to dash in, you can one tapped instantly by the viper. What do you do in the situation?\n")
	print("A) Wait for your teamates to go in first and bait them in order to kill the Viper.\n")
	print("B) Go to A site instead.\n")
	print("C) Play for picks either down mid or anywhere on the map.\n")
	# user input of their choice based onthe situation
	choice = input("Enter your choice (A, B, or C):\n")
	os.system("cls")

	# will run through this until they have made the correct decision
	while(can_pass != True):
		if(choice.lower() == "a"):
			can_pass = jett_split_A()
			choice = input("Enter your choice (A, B, or C):\n")
			os.system("cls")

		elif(choice.lower() == "b"):
			can_pass = jett_split_B()

		elif(choice.lower() == "c"):
			can_pass = jett_split_C()

		else:
			error_response()
			choice = input("Enter your choice (A, B, or C):\n")
			os.system("cls")


# the final map is icebox which will be called when all other maps are completed
def jett_icebox():
	'''
	a tour/description of the location

	args:
		none

	returns:
		none
	'''
	print("Welcome to Icebox and the last map you'll be visting as Jett in the world of Valorant.\n")
	sleep(2)
	os.system("cls")
	print("As a reward for coming this far, instead of testing, well be giving oyu a tour of the map.\n")
	sleep(2)
	os.system("cls")
	print("Starting on the A site, there is a large elevated portion on the T-side of the map that is referred to as rafters. A zipline links that portion to the actual A site. On A there is elevated portion that the zipline leads to. Intricate maze setup created by the surrounding pipes and objects. There is another elevated portion that is referred to as CT side rafters and to the right of this is what's known as screens.\n")
	sleep(5)
	os.system("cls")
	print("Making our way over to mid, there is a large boiler that is elevated and to the right of this is a kitchen that leads all the way to B site.\n")
	sleep(3)
	os.system("cls")
	print("On B site you'll find it is directly connected to mid not just from Kitchen, but one other place as well. There is alo a long alley way that leads from CT side to B site with lots of crates and machinery to lift these crates found in between.\n")
	sleep(3)
	os.system("cls")
	print("The actual setting of the map as suggested by the name is a frozen abyus found in Russia. It is a secret Kingdom excavation site overtaken by the artic. Similar to a container port. Looking up you'll be able to see stars as well.\n")
	sleep(4)
	os.system("cls")

# this is the congratualtions message that will be called upon finishing the Jett campaign; it will list your accomplishments as Jett.
def jett_congratulations(kills):
	'''
	upon completing the jett campaign, you'll receive this message which is composed of what you've accomplished as jett

	args:
		kills the total number of kills received throughout the campaign

	returns:
		none
	'''
	print("Congratulations, you've completed the Jett campaign and you've demonstrated that you are more than capable of assuming the responsibility of a duelist and carry out Jett's will.\n")
	sleep(4)
	os.system("cls")
	print("Throughout your journey, you know how to act accordingly in post plant situations as CT side utilizing Jett's utility, demonstrated your knowledge about the economy in Valorant and what to buy, then upon demonstrating this you displayed individual raw aim skill by getting an ace, clutching a 1v3 situation, demonstrated your team spirit as a team player, and finally what to do when faced with adversity.\n")
	sleep(6)
	os.system("cls")
	print("Your journey as Jett, you've gotten {0} kills!".format(kills))
	sleep(2)
	os.system("cls")