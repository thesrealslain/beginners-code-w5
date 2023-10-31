from graphics import *

def clickToClose(win):
    win.getMouse()
    win.close()

def main():
    win = GraphWin("", 500, 400)
    skater = []

    # this the stick man creation 
    head = Circle(Point(200, 60), 20)
    head.setFill('white')
    head.draw(win)
    skater.append(head)

    body = Line(Point(200, 80), Point(190, 120))
    body.draw(win)
    skater.append(body)

    arms = Line(Point(150, 80), Point(230, 120))
    arms.draw(win)
    skater.append(arms)

    leg1 = Line(Point(190, 120), Point(240, 180))
    leg1.draw(win)
    skater.append(leg1)

    leg2 = Line(Point(190, 120), Point(150, 180))
    leg2.draw(win)
    skater.append(leg2)
    

    # Add grip tape
    grip_tape = Rectangle(Point(50, 172), Point(350, 180))
    grip_tape.setFill("brown")
    grip_tape.draw(win)
    skater.append(grip_tape)
    
    wheels = []
    wheel_radius = 10
    wheel_y = 190
    wheel_positions = [100, 300]
    
    for x in wheel_positions:
        wheel = Circle(Point(x, wheel_y), wheel_radius)
        wheel.setFill("black")
        wheel.draw(win)
        wheels.append(wheel)
        skater.append(wheel)
    
    # Add deck
    deck = Rectangle(Point(50, 170), Point(350, 172))
    deck.setFill("black")
    deck.draw(win)
    skater.append(deck)

    for i in range(15):
        win.getMouse()
        for obj in skater:
            obj.move(10, 0)

    win.getMouse()
    win.close()

    clickToClose(win)
main()
