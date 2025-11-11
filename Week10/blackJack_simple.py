# -------------------------------------
# Title:        Black Jack Simple
# Author:       Clint MacDonald
# Date:         Nov. 11, 2025
# Purpose:      To program something quickly using libraries
# -------------------------------------

''' This version of blackjack does not use a real deck of cards, but randomizes between 1 and 13'''
#region IMPORTS
import tools
#endregion

#region DECLARATIONS
hand = []
MAX_ALLOWABLE_SCORE = 21
CARD_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
CARD_NAMES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
#endregion

#region FUNCTIONS
    #region INPUT FUNCTIONS
    #endregion

    #region CUSTOM FUNCTIONS
def getNumOfAces(player_hand):
    '''Determine how many aces are in a players hand'''
    num_aces = 0
    for card in player_hand:
        if card == 1: num_aces += 1
    return num_aces

def printHand(playerHand):
    print("You cards are:")
    for card in playerHand:
        print('%s' % CARD_NAMES[card - 1])


    #endregion

#endregion

#region MAIN PROGRAM

def main():
    '''Main program'''

    # deal 2 cards to the player
    hand.append(tools.getRandIntRange(1,13))
    hand.append(tools.getRandIntRange(1,13))

    keepGoing = True
    while keepGoing:
        # show hand
        printHand(hand)

        # give total (allowing for Aces)
        total = 0
        for card in hand:
            total += CARD_VALUES[card-1]

        num_aces = getNumOfAces(hand)
        if num_aces == 0:
            print("Your total is: %i" % total)
        else: 
            print("Your total is: %i or %i" % (total, total + 10))

        if total > MAX_ALLOWABLE_SCORE:
            print("You busted, you loser!")
            keepGoing = False
            continue

        # LOOP: ask the user if they want another card?
        # uncomment this for player choice
        # keepGoing = input("Do you want another card (y/n)?").strip().lower()[0] == 'y'

        # uncomment this for dealers choice
        if total > 15 or total + 10 > 15: keepGoing = False


        if keepGoing:
            hand.append(tools.getRandIntRange(1,13))



#endregion

main()
