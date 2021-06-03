import random
win = 0

while win<1:
  print("This is a rock, paper, scissor game.")
  user_input = input("Chose rock, paper, or scissors: ")
  print("You chose " + user_input)
  choice = ['rock', 'paper', 'scissors']
  oppen = random.randint(choice)
  