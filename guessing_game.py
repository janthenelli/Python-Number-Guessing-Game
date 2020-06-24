# 
# Python Web Development Techdegree
# Project 1 - Number Guessing Game
# --------------------------------

import random
attempts = []
highscore = ''
	

def start_game():
	print("""\n----------------------------------------
  Welcome to the Number Guessing Game!
----------------------------------------\n""")
	num_guesses = 0
	random_num = random.randint(1, 10)
	global highscore
	if highscore:
			print("The highscore is {}, can you beat it?".format(highscore))
	while True:
		try:
			guess = int(input("Guess a number between 1 and 10:  "))
			if type(guess) != int:
				raise NameError
			if guess < 1 or guess > 10:
				raise ValueError
		except ValueError:
			print("Please enter a number between 1 and 10.")
		except NameError:
			print("Please enter a number between 1 and 10.")	
		else:
			if guess == random_num:
				num_guesses += 1
				print("\nGood job, you got it! The number was {} and it only took you {} guesses.\n".format(random_num, num_guesses))
				global attempts
				attempts.append(num_guesses)
				highscore = min(attempts)
				cont = input("Would you like to play again? (yes/no)  ")
				if cont.lower() == 'yes':
					start_game()
				else:
					print("\nThat's the end of the game, thanks for playing!\n")	
				break
			elif guess < random_num:
				num_guesses += 1
				print("The number is higher!")
			elif guess > random_num:
				num_guesses += 1
				print("The number is lower!")
	


# Kick off the program by calling the start_game function.
start_game()