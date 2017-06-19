import random

guessesTaken = 0

print('Hello! Welcome to Guess My Number Game!')


number = random.randint(1, 100)
print( 'I am thinking of a number between 1 and 100.')
 
while guessesTaken < 10:
  print('Take a guess. You have 10 tries!!') 
  guess = input()
  guess = int(guess)

  guessesTaken = guessesTaken + 1

  if guess < number:
    print('Your guess is too low.') 

  if guess > number:
    print('Your guess is too high.')

  if guess == number:
    break

if guess == number:
  guessesTaken = str(guessesTaken)
  print('You guessed my number in ' + guessesTaken + ' guesses! Congratulations!!!')
   
if guess != number:
  number = str(number)
  print('Nope. The number I was thinking of was ' + number)