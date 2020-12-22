import random

player_name = input("What is your name?\n")
print("There gonna be 10 rounds who will have highest points will win!!!")
player_points = 0
computer_points = 0
No_of_Rounds = 10

var = ['S','P','X']

while(No_of_Rounds > 0):
	print("%s Score:%d \t Computer Score:%d" %(player_name,player_points,computer_points))
	a = random.choice(var)
	while(True):
		b = input("Enter 'X' for Scissors, 'P' for Paper  ,  'S' for Stone\n")
		b = b.upper()
		if(b in var):
			break
		else:
			print('Enter the correct input\n')
	if (a==b):
		print("Draw!!")
		No_of_Rounds -= 1
	elif(a=='X' and b=='S'):
		print("You won this round")
		player_points += 1
		No_of_Rounds -= 1
	elif(a=='P' and b=='X'):
		print("You won this round")
		player_points += 1
		No_of_Rounds -= 1
	elif(a=='S' and b=='P'):
		print("You won this round")
		player_points += 1
		No_of_Rounds -= 1
	else:
		print("Computer Wins this round")
		computer_points += 1
		No_of_Rounds -= 1

print("Final Scores")
print("%s Score:%d \t Computer Score:%d" %(player_name,player_points,computer_points))

if (player_points > computer_points):
	print("\nCongrats!!! %s You won the game" %player_name)
elif(computer_points > player_points):
	print("\nYou lose the game\nBetter luck next time")
else:
	print("\nThe game is draw")