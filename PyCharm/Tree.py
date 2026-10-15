import turtle
import math
import time

# Set up screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Moving Tree in the Wind")
screen.bgcolor("#e0f7fa")
screen.tracer(0)  # Turn off automatic updates for smooth animation

# Create turtle for drawing and animating
tree = turtle.Turtle()
tree.hideturtle()
tree.pensize(2)
tree.speed(0)
tree.left(90)  # Point upwards


def draw_branch(x, y, length, angle, depth):
    if depth == 0:
        return

    # Move to starting position
    tree.penup()
    tree.goto(x, y)
    tree.pendown()

    # Calculate end point of the branch using trigonometry
    rad = math.radians(angle)
    x2 = x + length * math.cos(rad)
    y2 = y + length * math.sin(rad)

    # Color gradient: brown for trunk, green for leaves
    if depth > 3:
        tree.pencolor("#5d4037")  # Trunk color
    else:
        tree.pencolor("#4caf50")  # Leaf color

    tree.goto(x2, y2)

    # Recursive calls for smaller branches (with slight wind sway offset)
    wind_sway = math.sin(time.time() * 3 + depth) * 2

    draw_branch(x2, y2, length * 0.7, angle - 20 + wind_sway, depth - 1)
    draw_branch(x2, y2, length * 0.7, angle + 20 + wind_sway, depth - 1)


# Main animation loop
try:
    while True:
        tree.clear()

        # Draw ground
        tree.penup()
        tree.goto(-300, -180)
        tree.pendown()
        tree.pencolor("#388e3c")
        tree.pensize(20)
        tree.goto(300, -180)

        # Draw the tree with dynamic wind sway
        tree.pensize(4)
        base_angle = 90 + math.sin(time.time() * 2) * 5  # Main trunk swaying back and forth
        draw_branch(0, -180, 100, base_angle, 8)

        screen.update()
        time.sleep(0.02)
except turtle.TurtleGraphicsError:
    # Handles window closing gracefully
    pass