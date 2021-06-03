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
