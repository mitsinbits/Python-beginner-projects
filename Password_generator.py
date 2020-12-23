import random
import string

while(True):
	a = int(input('Enter the length of password you need. Min length is 6\n'))
	if(a<6):
		print("Enter the number greater than 6");
	else:
		break

password = ''
for x in range (0,1):
    password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
for y in range(a - 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
print(password)

 