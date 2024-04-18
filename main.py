#1=r, 2=s, 3=p
import os
import random
n = random.randint(1,3)

def crash():
  os.system("shutdown /p")
print("try not to hack, or else...")
u = int(input("Enter 1 for rock, 2 for scissors, 3 for paper"))

if n == 1:
  if u == 1:
    print("You chose rock, computer chose rock")
  elif u == 2:
    print("You chose scissor, computer chose rock. you lose")
  elif u == 3:
    print("You chose paper, computer chose rock. you win")
    
  elif u == 4:
    print("You chose ☬✞☬✞, computer chose rock. you hacked")
    crash()


if n == 2:
  if u == 1:
    print("You chose rock, computer chose scissor. you win")
  elif u == 2:
    print("You chose scissor, computer chose scissor")
  elif u == 3:
    print("You chose paper, computer chose scissor. you lose")
  elif u == 4:
    print("You chose ☬✞☬✞, computer chose scissor. you hacked")
    crash()


if n == 3:
  if u == 1:
    print("You chose rock, computer chose paper. you lose")
  elif u == 2:
    print("You chose scissor, computer chose paper. you win")
  elif u == 3:
    print("You chose paper, computer chose paper.")
  elif u == 4:
    print("You chose ☬✞☬✞, computer chose paper. you hacked")
    crash()