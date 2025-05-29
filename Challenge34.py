import turtle

# Set up the screen
wn = turtle.Screen()

# Create the turtle
tom = turtle.Turtle()

# Define a function to draw a square
def square(length):
    for _ in range(4):  # loop 4 times
        tom.forward(length)
        tom.right(90)

# Ask the user for the length
size = int(input("Enter the length of the square: "))

# Draw the square
square(size)

# Keep the window open until clicked
wn.exitonclick()