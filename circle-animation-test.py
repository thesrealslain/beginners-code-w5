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
    
    # Create a circle for the animation
    radius = 20
    circle = Circle(Point(200, 200), radius)
    circle.setFill("blue")
    circle.draw(win)
    
    # Animation loop
    for step in range(1, 6):  # Let's do 5 steps
        # Wait for user click to proceed to the next step
        instructions = Text(Point(200, 30), f"Step {step}: Click to Continue")
        instructions.draw(win)
        win.getMouse()
        instructions.undraw()  # Remove the step instruction text
        
        # Move the circle to the right
        move_distance = 50
        circle.move(move_distance, 0)
    
    # Display a final message
    final_message = Text(Point(200, 30), "Animation Complete")
    final_message.draw(win)
    
    # Wait for the user to click to close the window
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
