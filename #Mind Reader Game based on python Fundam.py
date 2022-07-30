#Mind Reader Game based on python Fundamentals by Govind 

import random

computer_score=0
player_score=0
valid_entries=['0','1']

while True :
  predict=random.randint(0,1)
  
  player_input=input('enter eighter 0 or 1 ')
  print('predict=',predict)
  
  while player_input not in valid_entries :
    print('invalid input')
    player_input=input('please enter eighter 0 or 1 ')
  player_input= int(player_input)
  if predict==player_input :
    computer_score=computer_score +1
    print("computer_score=",computer_score)
    print("player_score=",player_score)
  else :
    player_score=player_score + 1
    print("computer_score=",computer_score)
    print("player_score=",player_score)
  if player_score==10:
    print('congratulations you won')
    break
  elif computer_score==10:
    print('bad luck you lost')
    break