from graphics import *

def main():
    win = GraphWin("Step-by-Step Animation", 400, 400)
    win.setBackground("white")
    
    # Create a Text object for instructions
    instructions = Text(Point(200, 30), "Click to Start")
    instructions.draw(win)
    
    # Wait for the user to click to start the animation
    win.getMouse()
    instructions.undraw()  # Remove the instruction text
    
    # Create a rectangle for the animation
    initial_width = 20
    initial_height = 40
    x = 200
    y = 200
    rectangle = Rectangle(Point(x - initial_width/2, y - initial_height/2), Point(x + initial_width/2, y + initial_height/2))
    rectangle.setFill("green")
    rectangle.draw(win)
    
    # Animation loop
    for step in range(1, 6):  # Let's do 5 steps
        # Wait for user click to proceed to the next step
        instructions = Text(Point(200, 30), f"Step {step}: Click to Scale")
        instructions.draw(win)
        win.getMouse()
        instructions.undraw()  # Remove the step instruction text
        
        # Scale the rectangle (increase width and height)
        scale_factor = 1.2
        rectangle.undraw()
        initial_width *= scale_factor
        initial_height *= scale_factor
        rectangle = Rectangle(Point(x - initial_width/2, y - initial_height/2), Point(x + initial_width/2, y + initial_height/2))
        rectangle.setFill("green")
        rectangle.draw(win)
    
    # Display a final message
    final_message = Text(Point(200, 30), "Animation Complete")
    final_message.draw(win)
    
    # Wait for the user to click to close the window
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
