'''
Name: Rashmi Kaspal
CSC 201
Programming Project 4--Card Class

The Card class represents one standard poker card from a poker deck. Each Card has an image, rank, and suit.
The card stores its position in a graphics window. It can be drawn and undrawn, moved a distance
in the x or y directions, and determine if a point is within the boundaries of the card.

Document Assistance (who and what or declare no assistance): Professor Mueller helped me with strategization to check the points and get suit and rank through slicing. 

'''
from graphics2 import *
import time

class Card:
    # Add your methods above __eq__
    def __init__(self, imageFilename):
        imageSplit = imageFilename.split('/')
        rankSplit =imageSplit[-1].split('.')
        rankAndSuit = rankSplit[0]

        if len(rankAndSuit) == 3:
            self._rank = int(rankAndSuit[:2])
            self._suit = rankAndSuit[-1]
        else:
            self._rank = int(rankAndSuit[0])
            self._suit = rankAndSuit[-1]

        self._image = Image(Point(0,0), imageFilename)
        
    def getRank(self):
        return self._rank
    
    def getSuit(self):
        return self._suit
    
    def getImage(self):
        return self._image
    
    def draw(self, window):
        self._image.draw(window)

    def undraw(self):
        self._image.undraw()

    def move(self, dx, dy):
        self._image.move(dx, dy)
    
    def containsPoint(self, point):
        center = self._image.getCenter()
        x = center.getX()
        y = center.getY()

        height = self._image.getHeight()
        width = self._image.getWidth()

        upPointX = x-width/2
        upPointY = y-height/2

        lowPointX = x+width/2
        lowPointY = y+height/2

        if point.getX() < upPointX or point.getX() > lowPointX or point.getY() < upPointY or point.getY() > lowPointY:
            return False
        return True
    
    def __str__(self):
        return f"suit = {self._suit}, rank = {self._rank}, center = {self._image.getCenter()}"
    

    
    def __eq__(self, cardToCompare):
        '''
        Allows users of the Card class to compare two cards using ==
        
        Params:
            cardToCompare (Card): the Card to check for equality with this Card
        
        Returns:
            True if the two cards have the same rank and suit. Otherwise, False
        '''
        return self._suit == cardToCompare._suit and self._rank == cardToCompare._rank
        
            


def main():  
    window = GraphWin("Card Class Testing", 500, 500)
    
    # create King of Hearts card
    fileName = 'cards/13h.gif'
    card = Card(fileName)

    # print card using __str__ and test getRank, getSuit, getImage
    print(card)
    print(card.getRank())
    if (isinstance(card.getRank(), int)):
        print('Rank stored as an int')
    else:
        print('Rank was not stored as an int. Fix it!')
    print(card.getSuit())
    print(card.getImage())
       
    # move card to center of window and display it
    card.move(250, 250)
    card.draw(window)
    
    # click only on the card should move it 100 pixels left
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(-100, 0)
    
    # click only on the card should move it 200 pixels right and 100 pixels down
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(200, 100)
    
    # print the card using __str__
    print(card)
    
    # stall 2 seconds
    time.sleep(2)
    
    # create 2 of Spades card
    fileName = 'cards/2s.gif'
    card2 = Card(fileName)

    # print card2 using __str__ and test getRank, getSuit
    print(card2)
    print(card2.getRank())
    print(card2.getSuit())
       
    # move card2 to center of window and display it
    card2.move(250, 250)
    card2.draw(window)
    
    # stall 2 seconds then remove both cards from the window
    time.sleep(2)
    card.undraw()
    card2.undraw()
    
    # stall 2 seconds then close the window
    time.sleep(2)
    window.close()
    
if __name__ == '__main__':
    main()
        
        