import random


	
while(True):
	s = int(input("Enter the number upto which u want to guess max=100\n"))
	if(s<=100):
		break
	else:
		print("Out of Range. Max no is 100")

a = random.randint(1,s)
No_of_Guesses = 5
flag = True

while(No_of_Guesses >= 0):
	b = int(input("Enter the number\n"))
	if(b==a):
		print("Congrats!! You entered the correct number")
		flag = False
		break
	elif(b > a):
		print("Ohho your number is greater than the correct number")
		No_of_Guesses -= 1
	else:
		print("Ohho your number is lesser than the correct number")
		No_of_Guesses -= 1


if(flag==True):
	print("The correct number was %d" %a)


