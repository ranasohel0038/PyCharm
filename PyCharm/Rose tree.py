import turtle
import math
import random
import time

# --- Setup Screen ---
screen = turtle.Screen()
screen.setup(width=600, height=700)
screen.title("Rose Flower Animation")
screen.bgcolor("#1a1a2e")
screen.tracer(0)

# --- Rose Drawing Turtle ---
t = turtle.Turtle()
t.hideturtle()
t.speed(0)


def draw_rose():
    """Draws a mathematical rose/flower pattern"""
    t.penup()
    t.goto(0, -80)
    t.setheading(90)
    t.pendown()

    # Stem
    t.pencolor("#2e7d32")
    t.pensize(8)
    t.goto(0, -220)

    # Leaves
    # Left Leaf
    t.penup()
    t.goto(0, -160)
    t.setheading(150)
    t.pendown()
    t.color("#2e7d32", "#4caf50")
    t.begin_fill()
    t.circle(60, 70)
    t.left(110)
    t.circle(60, 70)
    t.end_fill()

    # Right Leaf
    t.penup()
    t.goto(0, -130)
    t.setheading(30)
    t.pendown()
    t.begin_fill()
    t.circle(-60, 70)
    t.right(110)
    t.circle(-60, 70)
    t.end_fill()

    # Rose Petals (Spiral Geometry)
    t.penup()
    t.goto(0, -80)
    t.setheading(90)

    # Outer to inner layers
    layers = [
        (130, "#800020", "#b71c1c"),  # Dark Crimson outer
        (100, "#a0002a", "#d32f2f"),  # Bright Red middle
        (70, "#c62828", "#e53935"),  # Vivid Red
        (40, "#d32f2f", "#f44336"),  # Light Red inner
        (15, "#e53935", "#ff8a80")  # Center core
    ]

    for radius, border_color, fill_color in layers:
        t.color(border_color, fill_color)
        for i in range(6):
            t.penup()
            t.goto(0, 20)
            t.setheading(i * 60)
            t.forward(radius * 0.3)
            t.pendown()
            t.begin_fill()
            t.circle(radius, 80)
            t.left(100)
            t.circle(radius, 80)
            t.end_fill()


# --- Petal Particle Class ---
class FallingPetal:
    def __init__(self):
        self.reset()
        self.y = random.randint(-300, 300)  # Distribute initially

    def reset(self):
        self.x = random.randint(-280, 280)
        self.y = random.randint(320, 380)
        self.size = random.uniform(6, 12)
        self.speed = random.uniform(1.5, 3.5)
        self.sway_speed = random.uniform(0.02, 0.05)
        self.sway_amount = random.uniform(1.5, 3)
        self.angle = random.randint(0, 360)
        self.color = random.choice(["#d32f2f", "#e53935", "#ff5252", "#ff8a80"])

    def update(self):
        self.y -= self.speed
        self.x += math.sin(self.y * self.sway_speed) * self.sway_amount
        self.angle += 2

        if self.y < -320:
            self.reset()

    def draw(self, pen):
        pen.penup()
        pen.goto(self.x, self.y)
        pen.setheading(self.angle)
        pen.color(self.color)
        pen.pendown()
        pen.begin_fill()
        pen.circle(self.size, 90)
        pen.left(90)
        pen.circle(self.size, 90)
        pen.end_fill()


# --- Create Falling Petals ---
petals = [FallingPetal() for _ in range(25)]

# --- Main Animation Loop ---
petal_pen = turtle.Turtle()
petal_pen.hideturtle()
petal_pen.speed(0)

try:
    while True:
        screen.clear()
        screen.bgcolor("#1a1a2e")

        # Draw the main rose
        draw_rose()

        # Update & draw falling petals
        for p in petals:
            p.update()
            p.draw(petal_pen)

        screen.update()
        time.sleep(0.03)

except turtle.TurtleGraphicsError:
    pass