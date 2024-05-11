import turtle
import colorsys

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < 100:
        z = z**2 + c
        n += 1
    return n

width = 600
height = 600
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5

screen = turtle.Screen()
screen.setup(width, height)
screen.bgcolor("black")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.penup()
t.setposition(-width/2, -height/2)
t.pendown()

for y in range(height):
    for x in range(width):
        cy = ymin + (ymax - ymin) * y / (height - 1)
        cx = xmin + (xmax - xmin) * x / (width - 1)
        c = complex(cx, cy)
        m = mandelbrot(c)
        hue = 255 - int(255 * m / 100)
        t.color(colorsys.hsv_to_rgb(hue / 255.0, 1.0, 1.0))
        t.penup()
        t.goto(x - width / 2, y - height / 2)
        t.pendown()
        t.forward(1)
    if y % 20 == 0:
        screen.update()

screen.tracer(1)
screen.mainloop()
