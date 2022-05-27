import random

num = random.randint(1, 10)

guess = int(input('Guess again'))
while (guess!= num):
   num= num + 1
   guess = int(input('Guess again'))

print('You win!') 
