# button.py
# A simple button widget implemented better than Zelle's text example


from graphics2 import *

class Button:

    """
    A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns True if the button is active and p is inside it.
    
    instance variables:
        rect (Rectangle): the rectangle representing the button
        label (Text): the text on the button
        active (bool): indicates whether the button will react to clicks(True)
    """

    def __init__(self, center, width, height, label, color = "lightgray"):
        """
        Creates a rectangular button, eg:
        button = Button(Point(30,25), 20, 10, 'Quit')
        that is not activated
        
        Params:
            center (Point): the center point of the button
            width (int): the width of the button in pixels
            height (int): the height of the button in pixels
            words (str): the words to go on the button
            color (str): the color of the button
        """ 
        # calculate the points the rectangle needs
        point1, point2 = self._get_corner_points(center, width, height)
        # create the instance variables
        self._rect = Rectangle(point1,point2)
        self._rect.setFill(color)
        self._label = Text(center, label)
        self._active = False
        
    def _get_corner_points(self, center, width, height):
        # calculate the points the rectangle needs
        # from the center, width and height
        halfWidth = width/2.0
        halfHeight = height/2.0
        centerX = center.getX()
        centerY = center.getY()
        xMin = centerX - halfWidth
        xMax = centerX + halfWidth
        yMin = centerY - halfHeight
        yMax = centerY + halfHeight
        point1 = Point(xMin, yMin)
        point2 = Point(xMax, yMax)
        return point1, point2

    def draw(self,win):
        """
        Draws the button on the window
        
        Params:
            window (GraphWin): window where the button is drawn
        """
        self._rect.draw(win)
        self._label.draw(win)

    def undraw(self):
        """
        Undraws the button
        """
        self._rect.undraw()
        self._label.undraw()
        
    def getLabel(self):
        """
        gets the words on the button
        
        Returns:
            str: the words on the button
        """
        return self._label.getText()

    def setLabel(self, newText):
        """
        Sets the label's string of this button to the specified string.
        
        Params:
            newText (str): the new words to be used for the button's label
        """
        self._label.setText(newText)
        
    def isActive(self):
        """"
        Tells true/false is the button is activated (ie. accepting clicks)
        
        Returns:
            bool: True if the button is activated, otherwise False
        """
        return self._active

    def activate(self):
        """
        Sets this button to 'active'.
        """
        self._label.setFill('black')
        self._rect.setWidth(2)
        self._active = True

    def deactivate(self):
        """
        Sets this button to 'inactive'.
        """
        self._label.setFill('darkgrey')
        self._rect.setWidth(1)
        self._active = False
      
    def isClicked(self, point):
        """
        Determines if the button was clicked
        
        Params:
            point (Point): the point to check if it is inside this button
        
        Returns:
        """    
        xIsGood = self._rect.getP1().getX() < point.getX() < self._rect.getP2().getX()
        yIsGood = self._rect.getP1().getY() < point.getY() < self._rect.getP2().getY()
        return self._active and xIsGood and yIsGood

    def move(self, dx, dy):
        """
        Move the button by offsets dx and dy
        
        Params:
            dx (int): pixels to move horizontally
            dy (int): pixels to move vertically
        """
        self._rect.move(dx, dy)
        self._label.move(dx,dy)


    def __str__(self):
        """
        Creates and returns a string version of this button
        
        Returns:
            str: a string version of this button
        """
        corner1 = self._rect.getP1()
        text = "A button with top left corner at: " + str(corner1.getX()) \
               + "," + str(corner1.getY())
        text = text + " with label= " + self._label.getText()
        return text
    

def main():
    # text code to see if we're on track!
    window = GraphWin("Testing Buttons", 400, 400)
    window.setBackground('white')
    
    rollButton = Button(Point(200, 300), 150, 30, "Roll Dice", "red")
    rollButton.draw(window)
    print(rollButton)




if __name__ == '__main__':
    main()








