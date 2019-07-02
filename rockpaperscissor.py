import random

while True:
	print("make your guess:", end=" ")
	guess = str(input())
	guess = guess.lower()
	choices = ['rock', 'paper' , 'scissors']
	computer_guess = random.choice(choices)
	print('you guessed' , guess)
	print('computer guessed', computer_guess)
	if guess in choices:
		if guess == computer_guess:
			print("its a tie!")
		elif guess == 'rock':
			if computer_guess == 'scissors':
				print("you win!")
			elif computer_guess == 'paper':
				print("you lose!")
		elif guess == 'paper':
			if computer_guess =='rock':
				print("you win!")
			elif computer_guess == 'scissors':
				print("you lose!")
		elif guess == 'scissors':
			if computer_guess == 'paper':
				print("you win!")
			if computer_guess == 'rock':
				print("you lose!")



