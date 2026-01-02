'''
Name: Rashmi Kaspal
CSC 201
Programming Project 4--skip3.py

Skip 3 Solitaire uses one long row of cards dealt on card at a time. The
objective is to consolidate the cards into one pile using the following
rules. Two adjacent cards or two cards that are 3 apart (ie two cards
inbetween) can be consolidated into one pile is they have the same
suit or the same rank.

Document Assistance: (who and what  OR  declare that you gave or received no assistance): Professor Mueller helped me to make clear function, mainly the secondClick



'''
from graphics2 import *
from board import CardRowBoard
from deck import Deck
from button import Button
import time
WINDOW_WIDTH = CardRowBoard.WINDOW_WIDTH
WINDOW_HEIGHT = CardRowBoard.WINDOW_HEIGHT
def showDirections():
    """
    Gives the directions for Skip 3 Solitaire. The "Click to begin" button
    must be clicked to continue to the game.

    """
    win = GraphWin("Directions", 700, 600)
    win.setBackground("white")
    string = ("Welcome to Skip-3 Solitaire\n\n"
                "The objective is to get all cards\n"
                "into the same pile following these rules.\n\n"
                "If two cards with the same suit or the same rank\n"
                "are either next to each other or have two cards\n"
                "between them, then click the two cards and the \n"
                "card clicked first will be placed on top of the\n"
                "card clicked second consolidating the piles.\n\n"
                "Good luck!")
    directions = Text(Point(win.getWidth()/ 2, win.getHeight()/2), string)
    directions.setSize(16)
    directions.draw(win)
    startButton = Button(Point(350, 525), 120, 40, "Click to begin")
    startButton.draw(win)
    startButton.activate()
    click = win.getMouse()
    while not startButton.isClicked(click):
        click = win.getMouse()
    win.close()

def setUpGame():
    """
    Draws the board and the button to deal the cards. It also initializes
    the board and deck of cards.
    
    Returns:
        tuple: the window for the game (GraphWin), the button to deal a card (BUtton),
                 the board for the game (CardRowBoard), and the deck of cards (Deck)
    
    """
    window = GraphWin('Skip3 Solitare', WINDOW_WIDTH ,WINDOW_HEIGHT)
    window.setBackground('green')
    
    dealCardButton = Button(Point(CardRowBoard.WINDOW_WIDTH - 100, CardRowBoard.WINDOW_HEIGHT - 30), 100, 40, "Deal Card")
    dealCardButton.draw(window)
    dealCardButton.activate()
    
    gameBoard = CardRowBoard()
    
    deck = Deck(False)
        
    return (window, dealCardButton, gameBoard, deck)


def giveMessage(window, words, numSecs):
    """
    Displays a message in the window for the number of seconds received
    
    Parameters:
        window (GraphWin): the window for the card game
        words (str): the message to be displayed in the window
        numSecs (int): the number of seconds to display the message
    """
    message = Text(Point(750, 400), words)
    message.setSize(18)
    message.setFill('red')
    message.draw(window)
    time.sleep(numSecs)
    message.undraw()
    
    
     


def startGame(window, dealCardButton, gameBoard, deck):
    """ 
    Starts the game by dealing two cards.
      If the button is not clicked, it gives an error message.
      
    Parameters:
    window (GraphWin): the window for the card game
    dealCardButton(Button): the button to deal the cards
    gameBoard(CardRowBoard): the platform to deal the cards
    deck(Deck): the deck of cards to deal
    """
    click = window.getMouse()

     
    while not dealCardButton.isClicked(click):
        giveMessage(window, "You must click on the deal button to start", 2)
        click = window.getMouse()

    gameBoard.addCard(deck.dealCard(), window)


def cardRank(card, moveToCard):
   '''Check ranks of both cards and check if they are equal

   Params:
   card(Card): first card to deal
   moveToCard(Card): second card to deal
   '''
   return card.getRank() == moveToCard.getRank()

def cardSuit(card, moveToCard):
    """Check suits of both cards and check if they are equal

   Params:
   card(Card): first card to deal
   moveToCard(Card): second card to deal
   """
    return card.getSuit() == moveToCard.getSuit()

def legalMove(card, moveToCard, gameBoard):
    """Checks if both selected cards follows the rule of the game.

   Params:
   card(Card): first card to deal
   moveToCard(Card): second card to deal
   gameBoard(CardRowBoard): the platform to deal the cards
   """

    if (cardRank(card, moveToCard) or cardSuit(card, moveToCard)) and (abs(gameBoard.getCardIndex(moveToCard) - gameBoard.getCardIndex(card)) == 3 or  abs(gameBoard.getCardIndex(moveToCard) - gameBoard.getCardIndex(card)) == 1):
        return True
    else:
        return False

    
def secondClick(window, dealCardButton, gameBoard, deck, card):
    """
    Take actions according to second click, 
    whether to move card or to give message
    
    Parameters:
    window (GraphWin): the window for the card game
    dealCardButton(Button): the button to deal the cards
    gameBoard(CardRowBoard): the platform to deal the cards
    deck(Deck): the deck of cards to deal
    card(Card): a card to play
    """
    #can make a whole new function
    click2 = window.getMouse()
    if gameBoard.isPointInCard(click2):
        moveToCard = gameBoard.getCardAtPoint(click2)
        if legalMove(card, moveToCard, gameBoard):
            gameBoard.moveCard(card, moveToCard)

        else:
            giveMessage(window, "Cards do not have legal moves", 2)
                    

    else:
        if dealCardButton.isClicked(click2) and not deck.isEmpty():
            gameBoard.addCard(deck.dealCard(), window)

        else:
            giveMessage(window, "Click either in button or cards", 2) #check thisss


def playGameUntilDeckIsEmpty(window, dealCardButton, gameBoard, deck):
    '''Plays until all the cards in the deck finishes

    Parameters:
    window (GraphWin): the window for the card game
    dealCardButton(Button): the button to deal the cards
    gameBoard(CardRowBoard): the platform to deal the cards
    deck(): the deck of cards to deal
    '''
    while not deck.isEmpty():
        click = window.getMouse()
        if gameBoard.isPointInCard(click):
            card = gameBoard.getCardAtPoint(click)
            
            secondClick(window, dealCardButton, gameBoard, deck, card)

        elif dealCardButton.isClicked(click):
            if dealCardButton.isClicked(click):
                gameBoard.addCard(deck.dealCard(), window)

        else:
            giveMessage(window, "You must click on the deal button or cards", 2) 




def playGameAfterDeckIsEmpty(window, dealCardButton, gameBoard):
    '''Plays even after every card of the deck is on the screen or end the game
    
    Parameters:
    window (GraphWin): the window for the card game
    dealCardButton(Button): the button to deal the cards
    gameBoard(CardRowBoard): the platform to deal the cards
    '''
        
    dealCardButton.setLabel("End Game")
    giveMessage(window, "Click end game to end the game or keep playing",2)



    click = window.getMouse()
    while not dealCardButton.isClicked(click):

        if gameBoard.isPointInCard(click):
            card = gameBoard.getCardAtPoint(click)

            click2 = window.getMouse()
            if gameBoard.isPointInCard(click2):
                moveToCard = gameBoard.getCardAtPoint(click2)
                if legalMove(card, moveToCard, gameBoard):
                    gameBoard.moveCard(card, moveToCard)

                else:
                    giveMessage(window, "Cards do not have legal moves", 2)
                    

            elif not dealCardButton.isClicked(click2):
                giveMessage(window, "Click either in button or cards", 2)
            else:
                break
          
        else:
            giveMessage(window, "Click either in button or cards", 2)

        click = window.getMouse()

 

def evaluatePerformance(window, gameBoard):
    '''Evaluates the performance of the game
    Opens a new window to show the results
    
    Parameters:
    window (GraphWin): the window for the card game
    gameBoard(CardRowBoard): the platform to deal the cards

    '''
    window = GraphWin("Evaluation", 700, 600)
    window.setBackground("white")

    if gameBoard.getNumCardsOnBoard() == 1:
        winText = Text(Point(300, 300), "You won!!!")
        winText.setSize(10)
        winText.draw(window)
    
    elif gameBoard.getNumCardsOnBoard() >= 2 and gameBoard.getNumCardsOnBoard()<=10:
        firstRunnerUpText = Text(Point(300, 300), '2- 10 piles left\nYou almost made it! Try again.')
        firstRunnerUpText.setSize(15)
        firstRunnerUpText.draw(window)
    
    
    elif gameBoard.getNumCardsOnBoard() >= 11 and gameBoard.getNumCardsOnBoard()<= 20:
        secondRunnerUpText = Text(Point(300, 300), ''' 11-20 piles left. 
                                          Try more, you will learn it one day!''')
        secondRunnerUpText.setSize(15)
        secondRunnerUpText.draw(window)

    else:
        loseText = Text(Point(300, 300), '''more than 20 piles left.
                                          You lost, learn to play!''')
        loseText.setSize(15)
        loseText.draw(window)

    window.getMouse()
    window.close()
 

def main():
    showDirections()
    
    window, dealCardButton, gameBoard, deck = setUpGame()
    startGame(window, dealCardButton, gameBoard, deck)
    playGameUntilDeckIsEmpty(window, dealCardButton, gameBoard, deck)
    playGameAfterDeckIsEmpty(window, dealCardButton, gameBoard)
    evaluatePerformance(window, gameBoard)

    
if __name__ == '__main__':
    main()    

