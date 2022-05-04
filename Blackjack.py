import random
import time


class Cards:
    cardnumber = [2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    cardsuit = ['Spades','Hearts','Clubs','Diamonds']
    totalCards = []
    for i in cardnumber:
        pass
        for j in cardsuit:
            deckCreationTool = (i,j)
            totalCards.append(deckCreationTool)

firstgame = Cards()

#----------------------------------------------------------#

class Players:
    def __init__(self,player,playerbuy,playerCards,dealerCards,currentPotInvestment):
        self.player = player
        self.playercards = playerCards
        self.dealercards = dealerCards
        self.dealer = 'dealer'
        self.buyIn = playerbuy
        self.currentPotInvestment = currentPotInvestment
        self.remainingBuyIn = playerbuy - currentPotInvestment
        self.dealerbuy = playerbuy
        self.dealerCurrentPotInvestment = currentPotInvestment
        self.dealerRemainingBuy = playerbuy - currentPotInvestment
playercards = ''
currentplayers = Players("",0,playercards,'random2',0)

#------------------------------------------------------#

def shuffleDeck():
    random.shuffle(firstgame.totalCards)
    print('\nCards are being shuffled')
    print(f'The cards of {currentplayers.player} are {firstgame.totalCards[0]} and {firstgame.totalCards[1]} ')
    currentplayers.playercards = firstgame.totalCards[0] + firstgame.totalCards[1]
    print(f'The card that the dealer currently holds is {firstgame.totalCards[2]} \n')
    time.sleep(5)
    currentplayers.dealercards = firstgame.totalCards[2]
#------------------------------------------------------#
#defining point system
class PointSystem:
    def __init__(self,scoree,scoreePoints):
        self.scoree = scoree
        self.scoreePoints = scoreePoints
        self.AceLowScore = scoreePoints
        self.totalLowAce = 0
    def scoreIncrease (self):
        for i in self.scoree:
            self.scoreePoints == 0
            if (i == 2) or (i == 3) or (i == 4) or (i == 5) or (i == 6) or (i == 7) or (i==8) or (i == 9) or (i == 10):
            #if i == int:
                self.scoreePoints += i
            if (i == 'J') or (i == 'Q') or (i == 'K'):
                self.scoreePoints += 10
            if i == 'A':
                self.scoreePoints += 11
            else:
                pass
        for i in self.scoree:
            if i == 'A':
                self.AceLowScore += -10
            else:
                pass
        self.totalLowAce = self.scoreePoints + self.AceLowScore


#shuffleDeck()
#print(f'Important: {currentplayers.playercards}')
#player1Points = PointSystem(currentplayers.playercards,0)
#dealerPoints = PointSystem(currentplayers.dealercards,0)
#player1Points.scoreIncrease()
#print(f'points of player 1 are {player1Points.scoreePoints}')

#------------------------------------------------------#


#------------------------------------------------------#
class FullGame:
    playerexit = False
    gamechoice = ('hit','pass')
    answer = ''
    player1Points = ''
    dealerPoints = ''
    cardIncrease = 2
    newCard = ''
    restartDesire = ''
    Inferior = True

    def add_cards(self,playerSpecificCard,specificPlayerPoints,personDirectionText):
        FullGame.newCard = firstgame.totalCards[FullGame.cardIncrease + 1]
        FullGame.cardIncrease += 1
        playerSpecificCard += FullGame.newCard
        print(f'{personDirectionText} new card is {FullGame.newCard}')
        print(f'{personDirectionText} whole deck now consists of {playerSpecificCard}')
        specificPlayer = PointSystem(playerSpecificCard, 0)
        specificPlayerPoints.scoreIncrease()
        # player1Points = PointSystem(player,0)
        print(f'{personDirectionText} overall points are {specificPlayerPoints}')
        FullGame.newCard = ''
    def startgame(self):
        print('Welcome to Olivers Casino. This is the table where we play Blackjack.')
        currentplayers.player = input('What is your name?: ')
        while  FullGame.playerexit == False:
            FullGame.answer = ''
            FullGame.restartDesire = ''
            while currentplayers.buyIn <= 0:
                try:
                    currentplayers.buyIn = int(input('How much would you like to buy in?: '))
                except Exception:
                    print('Only whole numbers are accepted')
            currentplayers.currentPotInvestment = 0
            while currentplayers.currentPotInvestment <= 0:
                try:
                    currentplayers.currentPotInvestment = int(input('How much would you like to bet on this rounds pot?: '))
                    if currentplayers.currentPotInvestment > currentplayers.buyIn:
                        temp_var = 0
                        print('You cannot bet more money than what you have in your stack. ')
                        while temp_var ==0:
                            try:
                                currentplayers.currentPotInvestment = int(input('Please provide an acceptable value:'))
                            except Exception:
                                print('Only whole numbers are accepted')
                            if currentplayers.currentPotInvestment <= currentplayers.buyIn:
                                temp_var += 1

                except Exception:
                    print('Only whole numbers are accepted')
            currentplayers.buyIn -= currentplayers.currentPotInvestment

            shuffleDeck()
            player1Points = PointSystem(currentplayers.playercards, 0)
            dealerPoints = PointSystem(currentplayers.dealercards, 0)
            player1Points.scoreIncrease()
            dealerPoints.scoreIncrease()
            print(f'You currently have {player1Points.scoreePoints} points')
            print(f'The dealer currently has {dealerPoints.scoreePoints} points')
            #time.sleep()
            while FullGame.answer != 'pass':
                if player1Points.scoreePoints <= 21 or 1 <= player1Points.totalLowAce <= 21:
                    FullGame.answer = input('Would you like to hit or pass?: '.lower())
                    print('\n')
                    if FullGame.answer == 'hit':
                        FullGame.newCard = firstgame.totalCards[FullGame.cardIncrease+1]
                        FullGame.cardIncrease += 1
                        currentplayers.playercards += FullGame.newCard
                        print(f'You have received {FullGame.newCard}')
                        print(f'Your whole deck now consists of {currentplayers.playercards}')
                        player1Points = PointSystem (currentplayers.playercards,0)
                        player1Points.scoreIncrease()
                        if player1Points.AceLowScore < 0 :
                            print(f'Your overall points are {player1Points.scoreePoints} or {player1Points.totalLowAce}')
                        else:
                            print(f'Your overall points are {player1Points.scoreePoints}')
                        FullGame.newCard = ''
                else:
                    print('You have over 21 points. You are eliminated. ''\n'
                          f'The dealer has received your money in the pot, which is equal to {currentplayers.currentPotInvestment}')
                    time.sleep(2)
                    print(f'Your remaining balance is {currentplayers.buyIn}')
                    break
            if player1Points.scoreePoints > dealerPoints.scoreePoints:
                if player1Points.totalLowAce < player1Points.scoreePoints <=21:
                    print(f'As your score with a high Ace would be {player1Points.scoreePoints}, it is the score that we attributed you')
                elif player1Points.totalLowAce <= 21 < player1Points.scoreePoints:
                    player1Points.scoreePoints = player1Points.totalLowAce
                    print(f'As your score with a high Ace is above 21, only the score with your low Ace is considered {player1Points.scoreePoints}')
                else:
                    pass
                if player1Points.scoreePoints <=21:
                    print('You have decided to pass. The dealer will now return the hidden card')
                    while FullGame.Inferior == True:
                        FullGame.newCard = firstgame.totalCards[FullGame.cardIncrease + 1]
                        FullGame.cardIncrease += 1
                        currentplayers.dealercards += FullGame.newCard
                        print(f'Dealer has received {FullGame.newCard}')
                        print(f'The dealers deck now consists of {currentplayers.dealercards}')
                        dealerPoints = PointSystem(currentplayers.dealercards, 0)
                        dealerPoints.scoreIncrease()
                        print(f'The dealers overall points are {dealerPoints.scoreePoints}')
                        FullGame.newCard = ''
                        time.sleep(6.5)
                        if dealerPoints.scoreePoints > 17 or dealerPoints.scoreePoints > player1Points.scoreePoints:
                            FullGame.Inferior = False
                            print('\n')


                if player1Points.scoreePoints > 21:
                    pass
                if dealerPoints.totalLowAce <= 21 < dealerPoints.scoreePoints:
                    print(f'As the score of the dealer, with a high ace, would be {dealerPoints.scoreePoints}, ''\n'
                        f'only the score with the low ace is considered, which is {dealerPoints.totalLowAce}')
                    dealerPoints.scoreePoints = dealerPoints.totalLowAce
                if dealerPoints.scoreePoints >21:
                    print('Dealer has more than 21 points.' '\n'
                        f'You have received {currentplayers.currentPotInvestment*2}' '\n'
                        f'Your new balance is {currentplayers.buyIn+currentplayers.currentPotInvestment*2}')
                    time.sleep(3.5)
                    currentplayers.buyIn += currentplayers.currentPotInvestment*2
                elif 21 >= dealerPoints.scoreePoints > player1Points.scoreePoints:
                    print(f'Dealer has won this round with points totaling {dealerPoints.scoreePoints}, while you only had {player1Points.scoreePoints}' '\n'
                        f'The dealer has received your money in the pot, which is equal to {currentplayers.currentPotInvestment}')
                    time.sleep(3.5)
                    print(f'Your remaining balance is {currentplayers.buyIn}')
                    pass
                elif 21 > player1Points.scoreePoints > dealerPoints.scoreePoints:
                    print(f'You have won this round with points totaling {player1Points.scoreePoints}, while the dealer only had {dealerPoints.scoreePoints}''\n'
                        f'You have received {currentplayers.currentPotInvestment*2}''\n'
                        f'Your new balance is {currentplayers.buyIn+currentplayers.currentPotInvestment*2}')
                    currentplayers.buyIn += currentplayers.currentPotInvestment*2
                elif player1Points.scoreePoints == dealerPoints.scoreePoints:
                    print(f'This round is a tie. Both you and the dealer have a score of {player1Points.scoreePoints}')
                    currentplayers.buyIn += currentplayers.currentPotInvestment
                    print(f'Your balance remained at {currentplayers.buyIn}')
                time.sleep(3.5)

            else:
                print(
                    f'Dealer has won this round with points totaling {dealerPoints.scoreePoints}, while you only had {player1Points.scoreePoints}' '\n'
                    f'The dealer has received your money in the pot, which is equal to {currentplayers.currentPotInvestment}')
                time.sleep(3.5)
                print(f'Your remaining balance is {currentplayers.buyIn}')
                if player1Points.scoreePoints == dealerPoints.scoreePoints:
                    print(f'This round is a tie. Both you and the dealer have a score of {player1Points.scoreePoints}')
                    currentplayers.buyIn += currentplayers.currentPotInvestment
                    print(f'Your balance remained at {currentplayers.buyIn}')
            while FullGame.restartDesire not in ['yes','no']:
                FullGame.restartDesire = input('Would you like to restart the game? (yes/no): '.lower())
            if FullGame.restartDesire == 'yes':
                FullGame.playerexit = False
                print('\n')
            elif FullGame.restartDesire != 'yes':
                FullGame.playerexit = True
                print('\nBye bye!')






game1= FullGame()
game1.startgame()
