import random
    #print(f' Your answer is {player1}')
#def gamefunction (player,playerE, playerP,EplayerP,weapon,weapon1,weapon2):
    #if player == weapon:
      #  if playerE == weapon1:
       #     playerP +=1
        #elif player2 == weapon2:
         #   EplayerP +=1
#   return playerP
import time

correctanswer = 0
gameover = False
outcome1 = ["rock","paper","scizzors"]
player1P = 0
player2P = 0


while gameover == False:
    player1 = input('Please choose your weapon: ')
    while correctanswer== 0:
        if (player1 == 'rock') or (player1 == 'scizzors') or (player1 == 'paper'):
          correctanswer == 1
          break
        else:
         player1 = input('The answer provided did not fit the required format (rock, paper, scizzors).\n ' 
                        'Please provide the required format: ')
    player2 = random.choice(outcome1)
    print(f'Player 1 has chosen {player1}')
    time.sleep(1)
    print(f'Player 2 has chosen {player2}')
    time.sleep(1.5)
    if player1 == 'rock':
        if player2 == 'scizzors':
            player1P += 1
            print('You received a point')
        elif player2 == 'paper':
            player2P += 1
            print('Your adversary received a point')
        else:
            print(f'Both of you had {player1}. No point was distributed this round.')
    elif player1 == 'paper':
        if player2 == 'rock':
            player1P +=1
            print('You received a point')
        elif player2 == 'scizzors':
            player2P +=1
            print('Your adversary received a point')
        else:
            print(f'Both of you had {player1}. No point was distributed this round.')
    elif player1 == 'scizzors':
        if player2 == 'paper':
            player1P +=1
            print('You received a point')
        elif player2 == 'rock':
            player2P +=1
            print('Your adversary received a point')
        else:
            print(f'Both of you had {player1}. No point was distributed this round.')
    time.sleep(1.5)
    print('The total score is')
    time.sleep(1.3)
    print(f'Player 1: {player1P}')
    time.sleep(0.8)
    print(f'Player 2: {player2P}')
    time.sleep(2)
    if player1P == 3:
        print('You have won the game')
        time.sleep(20)
    elif player2P == 3:
        print('Your enemy has won the game')
        time.sleep(20)






