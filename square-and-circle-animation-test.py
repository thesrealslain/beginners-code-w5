from graphics import *

def main():
    win = GraphWin("Step-by-Step Animation", 400, 400)
    win.setBackground("white")
    
    # Create a Text object for instructions
    instructions = Text(Point(200, 30), "Click to Start")
    instructions.setSize(14)
    instructions.draw(win)
    
    # Wait for the user to click to start the animation
    win.getMouse()
    instructions.undraw()  # Remove the instruction text
    
    # Create the first graphical component (e.g., a circle)
    circle = Circle(Point(100, 200), 20)
    circle.setFill("blue")
    circle.draw(win)
    
    # Create the second graphical component (e.g., a rectangle)
    rectangle = Rectangle(Point(150, 200), Point(200, 250))
    rectangle.setFill("green")
    rectangle.draw(win)
    
    # Initialize a variable to track the rectangle's color
    is_rectangle_green = True
    
    # Animation loop
    for step in range(1, 6):  # Let's do 5 steps
        # Wait for user click to proceed to the next step
        instructions = Text(Point(200, 30), f"Step {step}: Click to Continue")
        instructions.setSize(14)
        instructions.draw(win)
        win.getMouse()
        instructions.undraw()  # Remove the step instruction text
        
        # Modify the graphical components for each step
        if step % 2 == 0:
            # Move the circle to the right
            circle.move(50, 0)
        else:
            # Change the color of the rectangle
            if is_rectangle_green:
                rectangle.setFill("red")
                is_rectangle_green = False
            else:
                rectangle.setFill("green")
                is_rectangle_green = True
    
    # Display a final message
    final_message = Text(Point(200, 30), "Animation Complete")
    final_message.setSize(14)
    final_message.draw(win)
    
    # Wait for the user to click to close the window
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
