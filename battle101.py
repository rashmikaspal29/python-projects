"""
 Name: Rashmi Kaspal 
 CSC 201
 Programming Project 3
 
 Description: This program builds a simple game by importing different elements, 
               using  both while and for loop and different fuctions returning its 
               value to the main.

Additions: material used: pygame documentation 

            import(import pygame , from pygame import mixer),
            initialize(pygame.init(), pygame.mixer.init()),
            background sound(pygame.mixer.music.load("backgroundsound.wav"),pygame.mixer.music.play(-1) ) 
            elements sounds: 
            
            (asteroidSound = pygame.mixer.Sound("asteroidhit.wav"), asteroidSound.play()),
            (fuelSound = pygame.mixer.Sound("fuelhit.wav"), fuelSound.play()), 
            (blackSound = pygame.mixer.Sound("blackholehit.wav"), blackSound.play())

            conclusion sounds : (pygame.mixer.music.load("winner.wav"), pygame.mixer.music.play(-1)), 
                                (pygame.mixer.music.load("loser.wav"), pygame.mixer.music.play(-1))
     
 Document Assistance: (who and what  OR  declare that you gave or received no assistance): Professor Muller helped us with the idea of win window and lose window. 
                                                                                            For bonus, we read pygame documentation from pygame.org. 
"""

from graphics2 import *
import time
import random
import math

import pygame 
from pygame import mixer


#initializing pygame so that we can use sound
pygame.init()
pygame.mixer.init()
 
SPACESHIP_SPEED = 25
ASTEROID_SPEED = 0.16
FUEL_SPEED = 0.56
BLACKHOLE_SPEED = 0.67
NUM_WIN = 6
STALL_TIME = 0.001
THRESHOLD = 50
LOSE_POINTS = 2
WIN_POINTS = 1

    
from graphics2 import *


#calculate distance 
def distanceBetweenPoints(point1, point2):
    '''Calculates the distance between two points
    
    Params:
        point1 (Point): the first point
        point2 (Point): the second point
    
    Returns:
        float: the distance between the two points
    '''
    dx = point2.getX() - point1.getX()
    dy = point2.getY() - point1.getY()
    return math.sqrt(dx**2 + dy**2)


#removes the object collided with spaceship
def isCloseEnoughI(spaceShip, asteroidImg):
    '''
    Determines if the asteroids are close enough to the spaceShip to say the asteroids
    hit the spaceShip.
    
    Params:
        spaceShip (Image): the image of the spaceShip
        asteroidImg (Image): the image of the asteroid
    
    Returns:
        bool: True if the asteroids hits the spaceShip
    '''
    distance = distanceBetweenPoints(spaceShip.getCenter(), asteroidImg.getCenter())
    if distance < THRESHOLD:
        return True
    else:
        return False
    
def isCloseEnoughII(spaceShip, fuelImg):
    '''
    Determines if the spaceShip is close enough to the fuel to say the spaceShip
    caught the fuel.
    
    Params:
        spaceShip (Image): the image of the spaceShip
        fuelImg (Image): the image of the asteroid
    
    Returns:
        bool: True if the spaceShip catches the fuel.

    '''
    distance = distanceBetweenPoints(spaceShip.getCenter(), fuelImg.getCenter())
    if distance < THRESHOLD:
        return True
    else:
        return False
    


#instructions on a first window
def instructions():

    '''
    Shows an instructions of the game in a window
    '''

    # setup the game 
    window = GraphWin("SPACE BATTLE 101", 600,600)
    firstBackGround = Image(Point(300, 300), "stars.gif")
    firstBackGround.draw(window)
    directions = Text(Point(300, 300),f'''Fly the spaceship, gain the fuel and avoid the asteroids
    Use arrow keys to maneuver your spaceship.
    If you collide with an asteroid, you lose {LOSE_POINTS} points.
     You earn {WIN_POINTS} point for each fuel you catch.
     To win, earn {NUM_WIN} points
              
AVOID the blackhole!!!
    If you collide with it,
   then its
   GAME OVER !!!
              
    Click to start the game--->''')
    directions.setSize(12)
    directions.draw(window)
    directions.setTextColor("white")
    directions.setFace("arial")
    directions.setStyle("bold")
    



    window.getMouse()
    window.close()

 
    
#moving elements:
        
def moveAsteroids(asteroidList):
    '''
    Moves every asteroid one ASTEROID_SPEED unit down the window
    
    Params:
        asteroidList (list): the list of falling asteroids

    '''
    
    for asteroid in asteroidList:
        asteroid.move(0, ASTEROID_SPEED)


        
def moveFuel(fuelList):

    '''
    Moves every fuel one FUEL_SPEED unit down the window
    
    Params:
        fuelList (list): the list of moving fuels horizontally

    '''
    
    for fuel in fuelList:
        fuel.move(FUEL_SPEED, 0)


        
def moveBlackHole(blackList):
    
    '''
    Moves every blackhole one BLACKHOLE_SPEED unit down the window
    
    Params:
        blackList (list): the list of falling blackhole

    '''
    
    for black in blackList:
        black.move(0, BLACKHOLE_SPEED)
        
        

#to move SPACESHIP        
def moveShip(window, spaceShip):

    '''
    Each time the left arrow key is pressed the spaceShip moves SPACESHIP_SPEED units left and
    each time the right arrow key is pressed the spaceShip moves SPACESHIP_SPEED units right.

    Each time the upper arrow key is pressed the spaceShip moves SPACESHIP_SPEED units up and
    each time the lower arrow key is pressed the spaceShip moves SPACESHIP_SPEED units down.
    
    Params:
        window (GraphWin): the window where game play takes place
        spaceShip (Image): the space ship image

    '''

    keyPressed = window.checkKey()
    pointLocation = spaceShip.getCenter()
    
    #for x-axis
    if keyPressed == 'Left' and pointLocation.getX() > 30:
        spaceShip.move(-SPACESHIP_SPEED,0)
        
    elif keyPressed == 'Right' and pointLocation.getX() < 650:  
        spaceShip.move(SPACESHIP_SPEED,0)
        
    #for y- axis
    if keyPressed == 'Up' and pointLocation.getY() > 30:
        spaceShip.move(0,-SPACESHIP_SPEED)
         
    elif keyPressed == 'Down' and pointLocation.getY() < 650:
        spaceShip.move(0, SPACESHIP_SPEED)
    
    
    
#adding elements:
        
def addAsteroids(window):

    '''
    Adds one asteroid to the top of the window at a random location
    
    Params:
        window (GraphWin): the window where game play takes place
    
    Returns:
        Image: the asteroid added to the window
    '''

    xPosition = random.randrange(40, 500)
    asteroidImg = Image(Point(xPosition, -50), 'asteroid.gif')
    asteroidImg.draw(window)
    return asteroidImg

def addFuel(window):

    '''
    Adds one fuel to the left of the window at a random location
    
    Params:
        window (GraphWin): the window where game play takes place
    
    Returns:
        Image: the fuel added to the window
    '''
    yPosition = random.randrange(30, 500)
    fuelImg = Image(Point(-50, yPosition), 'fuel.gif')
    fuelImg.draw(window)
    return fuelImg


def addBlackHole(window):

    '''
    Adds one blackhole to the top of the window at a random location
    
    Params:
        window (GraphWin): the window where game play takes place
    
    Returns:
        Image: the blackhole added to the window
    '''
    xPosition = random.randrange(60, 530)
    blackImg = Image(Point(xPosition, -60), 'blackhole.gif')
    blackImg.draw(window)
    return blackImg


#game loop so that game continues in loop 
def gameLoop(window, spaceShip):

    '''
    Loop continues until the score is NUM_WIN or 
    collide with blackhole. 

    Params:
        window (GraphWin): the window where game play takes place
        spaceShip (Image): the space ship image
    '''

    gameContinue = True
    asteroidList = []
    fuelList = []
    blackList = []

    #score initialization and drawing scoreNum
    score = 0
    scoreNum = Text(Point(350, 70), "Score: 0")
    scoreNum.draw(window)
    scoreNum.setTextColor("white")
    scoreNum.setSize(28)
    scoreNum.setFace("arial")
    scoreNum.setStyle("bold")


    #Bg Sound: #add bg sound right before while loop 
    pygame.mixer.music.load("backgroundsound.wav")
    pygame.mixer.music.play(-1) # (-1) helps the sound to go on forever
    

    while score < NUM_WIN and gameContinue == True :
        moveShip(window, spaceShip)
        
        if random.randrange(1350) < 3:
            asteroids = addAsteroids(window)
            asteroidList.append(asteroids)
            
        moveAsteroids(asteroidList)
            
        if random.randrange(1400) < 2:
            fuel = addFuel(window)
            fuelList.append(fuel)
            
        moveFuel(fuelList)
            
        if random.randrange(1500) < 1:
            black = addBlackHole(window)
            blackList.append(black)
            
        moveBlackHole(blackList)


        #for making elements disappear

        for asteroid in asteroidList:
            if asteroid.getCenter().getY() > 800:
                asteroidList.remove(asteroid)
                

        for asteroid in asteroidList:
            if isCloseEnoughI(spaceShip, asteroid):
                asteroid.undraw()
                asteroidList.remove(asteroid)
                score = score - LOSE_POINTS
                scoreNum.setText("Score: " + str(score)) #score updates
                asteroidSound = pygame.mixer.Sound("asteroidhit.wav")
                asteroidSound.play()

        for fuel in fuelList:
            if fuel.getCenter().getX() > 900:
                fuelList.remove(fuel)
                

        for fuel in fuelList:
            if isCloseEnoughII(spaceShip, fuel):
                fuel.undraw()
                fuelList.remove(fuel)
                score = score + WIN_POINTS
                scoreNum.setText("Score: " + str(score))
                fuelSound = pygame.mixer.Sound("fuelhit.wav")
                fuelSound.play()

        for black in blackList:
            if isCloseEnoughII(spaceShip, black):
                black.undraw()
                blackList.remove(black)
                gameContinue = False

                blackSound = pygame.mixer.Sound("blackholehit.wav")
                blackSound.play()

                gameOver = Text(Point(350, 350),"GAME OVER")
                gameOver.draw(window)
                gameOver.setSize(20)
                gameOver.setTextColor("white")
                gameOver.setFace("arial")
                gameOver.setStyle("bold")
                gameOver.setSize(45)



        time.sleep(STALL_TIME)

    time.sleep(2)
    window.close()
    pygame.mixer.music.stop()
    
    # after whileloop 
    # show win or lose window
    if score >= NUM_WIN: 
        winWin()
    else:
        loseWin()

    window.close()

# you win window
def winWin():

    '''
    Opens to say that the player won the game.

    '''
    window = GraphWin("WINNER!", 600,600)
    winBg = Image(Point(300, 300), "winner.gif")
    winBg.draw(window)
    
    #for you win sound
    pygame.mixer.music.load("winner.wav")
    pygame.mixer.music.play(-1)
    time.sleep(5)
    window.close()

#you lose window
def loseWin():

    '''
    Opens to say that the player lost the game.

    '''

    window = GraphWin("LOSER!", 600,600)
    LoseBg = Image(Point(300, 300), "youLost.gif")
    LoseBg.draw(window)
    message = Text(Point(300, 70), "YOU LOST!!!")
    message.setSize(30)
    message.draw(window)
    message.setTextColor("white")
    message.setStyle("bold")
    message.setFace("arial")
    message.setSize(45)

    #for you lost sound
    pygame.mixer.music.load("loser.wav")   
    pygame.mixer.music.play(-1)
    
    time.sleep(4)
    window.close()




def main():
    instructions()
    # setup the game 
    window = GraphWin("Save your ship!!!",700,700)
    background = Image(Point(350, 350), "background.gif")
    background.draw(window)

     
    spaceShip = Image(Point(100, 350), "spaceship1.gif")
    spaceShip.draw(window)
    
    gameLoop(window, spaceShip)
    

main()

