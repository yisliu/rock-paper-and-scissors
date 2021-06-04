import random
win = 0
chose = 0
rock = 0
scissor = 0
paper = 0

while win<1:
  choice = ['rock', 'paper', 'scissor']
  print("This is a rock, paper, scissor game.")
  user_input = str(input("Chose rock, paper, or scissor: "))
  print("You chose " + user_input)
  oppen = random.choice(choice)
  print("The computer chose: " + oppen)
  if (oppen == rock) and (user_input == scissor):
    print("The computer has won!")
    print("You lost.")
    win = 1
  elif (oppen == scissor) and (user_input == paper):
    print("The computer won!")
    print("You have lost.")
    win = 1
  elif (oppen == paper) and (user_input == rock):
    print("You have lost. And the computer has won!")
    win = 1
  else:
    print("You beat the computer! You have won!")
    win = 1