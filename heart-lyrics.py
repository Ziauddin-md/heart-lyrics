import math
import turtle
import random
import time

# --- Heart Equations ---
def hearta(k, scale):
    return 15 * math.sin(k)**3 * scale

def heartb(k, scale):
    return (12*math.cos(k) - 5*math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)) * scale

# --- Setup Screen ---
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("white")
screen.tracer(0, 0)
screen.colormode(255)

# --- Turtle 1: Heart Drawing ---
heart_turtle = turtle.Turtle()
heart_turtle.hideturtle()
heart_turtle.color("pink")
heart_turtle.pensize(3)
heart_turtle.penup()

base_scale = 20

# Draw Heart Outline
k_start = 0
heart_turtle.goto(hearta(k_start, base_scale), heartb(k_start, base_scale))
heart_turtle.pendown()
for i in range(6300):
    k = i / 100.0
    heart_turtle.goto(hearta(k, base_scale), heartb(k, base_scale))
heart_turtle.penup()
screen.update()

# Fill Heart Randomly
heart_turtle.pensize(1)
num_fill_lines = 1000
max_line_length = 30
for _ in range(num_fill_lines):
    start_x = random.uniform(-15*base_scale, 15*base_scale)
    start_y = random.uniform(-13*base_scale, 9*base_scale)
    angle = random.uniform(0, 2*math.pi)
    length = random.uniform(5, max_line_length)
    end_x = start_x + length*math.cos(angle)
    end_y = start_y + length*math.sin(angle)
    heart_turtle.goto(start_x, start_y)
    heart_turtle.pendown()
    heart_turtle.goto(end_x, end_y)
    heart_turtle.penup()
screen.update()

# --- Turtle 2: Lyrics Stacked Correctly ---
lyrics_turtle = turtle.Turtle()
lyrics_turtle.hideturtle()
lyrics_turtle.color("red")
lyrics_turtle.penup()

lyrics = [
    "Mera dil yahi bolaa",
    "Mera dil yahi bolaa",
    "Yaara raaj yeh usane",
    "Hai mujh par kholaa",
    "Ki hai ishq mohabbat",
    "Jiske dil mein",
    "Usko pasand karta",
    "Hai maula",
    "Mera dil yahi bolaa",
    "Mera dil yahi bolaa",
    "Yaara raaj yeh usane",
    "Hai mujh par kholaa",
    "Ki hai ishq mohabbat",
    "Jiske dil mein",
    "Usko pasand",
    "Karta hai maula",
    "Mera dil yahi bolaa",
    "Mera dil yahi bolaa",
    "Yaara raaj yeh usane",
    "Hai mujh par kholaa",
    "Ki hai ishq mohabbat",
    "Jiske dil mein",
    "Usko pasand",
    "Karta hai maula"
]

# Starting position (centered in heart)
start_x = 0
start_y = 150  # near top of heart
line_spacing = 30  # vertical spacing between lines

# Display lyrics line by line
for line in lyrics:
    words = line.split()
    line_text = ""
    for word in words:
        line_text += word + " "
        lyrics_turtle.clear()  # clear only current line
        lyrics_turtle.goto(start_x, start_y)
        lyrics_turtle.write(line_text, align="center", font=("Arial", 18, "bold"))
        screen.update()
        time.sleep(0.5)  # delay per word
    start_y -= line_spacing  # move to next line after full line is displayed

turtle.done()
