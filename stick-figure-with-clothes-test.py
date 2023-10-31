from graphics import *

def drawStickFigure():
    win = GraphWin("Enhanced Stick Figure", 400, 400)
    win.setBackground("white")
    
    head = Circle(Point(200, 60), 20)
    head.setWidth(2)
    head.draw(win)

    body = Line(Point(200, 80), Point(200, 140))
    body.setWidth(2)
    body.draw(win)

    arm1 = Line(Point(200, 100), Point(160, 120))
    arm1.setWidth(2)
    arm1.draw(win)

    arm2 = Line(Point(200, 100), Point(240, 120))
    arm2.setWidth(2)
    arm2.draw(win)

    leg1 = Line(Point(200, 140), Point(170, 180))
    leg1.setWidth(2)
    leg1.draw(win)

    leg2 = Line(Point(200, 140), Point(230, 180))
    leg2.setWidth(2)
    leg2.draw(win)
    
    # hat addition
    hat_top = Point(200, 30)  
    hat_left = Point(175, 40)  
    hat_right = Point(225, 40)  

    hat = Polygon(hat_top, hat_left, hat_right)
    hat.setFill("black")
    hat.draw(win)

    # calculate proportions for accessories
    accessory_size = 10
    
    # gloves additions
    left_glove = Circle(Point(160, 120), accessory_size)
    left_glove.setFill("blue")
    left_glove.draw(win)
    right_glove = Circle(Point(240, 120), accessory_size)
    right_glove.setFill("blue")
    right_glove.draw(win)
    
    # calculate shoe proportions
    shoe_height = 10
    shoe_width = 20
    
    # shoe additions
    left_shoe = Rectangle(Point(150, 170), Point(175, 180))
    left_shoe.setFill("brown")
    left_shoe.draw(win)
    right_shoe = Rectangle(Point(220, 170), Point(245, 180))
    right_shoe.setFill("brown")
    right_shoe.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    drawStickFigure()
