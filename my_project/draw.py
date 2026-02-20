from BetterTurtle import Turtle

# Create a turtle object
t = Turtle()

# Set up the turtle
t.speed(0)  # Fastest speed
t.bgcolor("black")  # Set background color

# Draw a colorful spiral
colors = ["red", "yellow", "green", "blue", "purple", "orange"]
for i in range(36):
    t.color(colors[i % len(colors)])  # Cycle through colors
    t.forward(i * 10)  # Move forward
    t.left(45)  # Turn left

# Hide the turtle after drawing
t.hideturtle()

# Keep the window open
t.done()