'''
Richard Feng
ICS3U - February 14, 2022
Task: Create an adventure game that allows the user to traverse through imaginary land such that at every location, the respective function gets called. 
Name of the setting: Transported to the world of VALORANT
File: main.py serves as the main function of the program.
'''

# importing random library for random decision making, time and os for wait and clear screen
import os
from time import sleep
import random

# importing class of each agent sort of like their own directory to keep track of ability usage, seperate file included
from agents import *

# importing functions of each agent on each map, seperate file included
from jett_campaign import *
from astra_campaign import *

# this is the main function 

# welcome message introduces what this game is about. takes place in a fictional video game setting: the world of Valorant. Valorant is a FPS game.
print("Welcome to the world of VALORANT. In this far away land, players are on teams of 5 competing against another team of 5. The goal of the T-side or the attackers is to plant the spike and protect it until the very last moment until it blows. The goal of the CT-side or the defenders is to defuse this spike to prevent it from exploding. Players choose agents equipped with different abilities to augment gameplay.\n")

# talks about the different agents in the game; these are just characters, however, referred to as agents in this game.
print("First, you need to choose an agent. An agent is a character with unique abilities and there are no two agents with the same abilities. Abilities are used to enhance gunplay and increase the chances of team success. It is also an opportunity to demonstrate your competence with utility usage. Please select one of the following agents to view their characteristics and abilities: Jett or Astra. If you wish to exit, please enter the following word: done.\n")

# this takes the users input of what agent/character they would like to play as
# different agents harbour different abilites meaning their roles will be different. Hence, a different playing experience for each character as all abilities are unique. However, in the aforementioned text on agent information agents can be spliut into groups and generally agents of the same group have similar playing experiences
agent_information = str(input())
# clears the screen to avoid too much text; will clear upon input from user
os.system("cls")

# this while loop will keep checking whether or not you want to continue to view agent information, when done it will exit
while(agent_information.lower() != "done"):
	if(agent_information == "jett"):
		jett_information()
		sleep(7)
		os.system("cls")
		agent_information = str(input("Enter another agent to view or enter done:\n"))
		os.system("cls") 

	elif(agent_information.lower() == "astra"):
		astra_information()
		sleep(7)
		os.system("cls")
		agent_information = str(input("Enter another agent to view or enter done:\n"))
		os.system("cls")
	else:
		error_response()
		agent_information = str(input("Enter another agent to view or enter done:\n"))

print("Now that you have a better understanding of some agents and their responsibilities, you will now choose one and complete tasks they may face during the game.\n")

# after learning abotu the agents, the user will unput an agent this wish to play
agent_select = input("Please select one of the agents from the following list: Jett or Astra.\n")

os.system('cls')

# if they chose jett, this will be jetts campaign
if(agent_select.lower() == "jett"):
	print("Cool. Let's go.\n")
	print("You will now be put in different situations to test your proficiences with Jett. You will need to make the correct decisions in every different situation on all 6 maps to prove you are truly a Jett main. Good Luck!\n")
	
	sleep(5)
	os.system('cls')

	kills = 8

	# calls the first map and needs to complete it as it will return true when once finished properly and when it returns the boolean value, it can then only move onto the next part
	if(jett_ascent()):
		# this is the second map that is beign called, same concept applies as the first one
		if(jett_bind()):
			# this is the third map, again same concept
			if(jett_breeze()):
				print("Well done! You've completed half of the maps meaning you're halfway to become a full-fledged Jett-main!\n")
				# after a little bit of forced locations selection, we now decide to let the user select between two maps which they would like to visit first
				map_selection = input("Enter the next map you would like to visit Haven or Split:\n")
				os.system("cls")

				# if it is haven, then have will be called, and the kills received during the time spent on haven will be recorded and announced at the very end (congrtulations message)
				# proceeding this, the following map will be called, in this instance, split, followed by icebox
				if(map_selection.lower() == "haven"):
					kills += jett_haven()
					jett_split()
					print("Now the next and final map: Icebox\n")
					jett_icebox()
                
				# same thing here but vice versa
				elif(map_selection.lower() == "split"):
					jett_split()
					kills += jett_haven()
					print("Now the next and final map: Icebox\n")
					jett_icebox()
                
				# universal error message
				else:
					error_response()
    
	# once having completed the jett campaign, they will receive a congratulations message that takes in paramaters kills which is the number of kills the user ahs got in total as this agent
	jett_congratulations(kills)

# if they chose astra, this will be astras campaign
elif(agent_select.lower() == "astra"):
	print("I am on a higher plane, chale. Literally.")
	print("You will now be put in different situations to test your proficiences with Astra. You will need to make the correct decisions in every different situation on all 6 maps to prove you are truly a Astra main. Good Luck!\n")
	
	sleep(5)
	os.system('cls')

	kills = 8

	# same thing here, ascent will be called first, followed by bind then breeze
	# only once they complete each map, will the function return true which will then allow them to move onto the next map
	if(astra_ascent()):
		if(astra_bind()):
			if(astra_breeze()):
				print("Well done! You've completed half of the maps meaning you're halfway to become a full-fledged Astra-main!\n")
				map_selection = input("Enter the next map you would like to visit Haven or Split:\n")

				# after having three maps forced upon them, they select the next one betweent two choices
				# if they choose haven first, split will be called automatically after
				if(map_selection.lower() == "haven"):
					kills += astra_haven()
					astra_split()
					print("Now the next and final map: Icebox\n")
					astra_icebox()
                
				# vice versa
				elif(map_selection.lower() == "split"):
					astra_split()
					kills += astra_haven()
					print("Now the next and final map: Icebox\n")
					astra_icebox()
                
				# universal error message
				else:
					error_response()
    
	# once the user has completed astra's campaign, the congratulations message will be played
	astra_congratulations(kills)

# if they chose something else, error message will be displayed
else:
	error_response()

# closing remarks called when everything else in the program has run smoothly
closing_message()