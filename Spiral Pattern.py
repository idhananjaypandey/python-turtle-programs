import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(360):
    t.pencolor(colors[i % 6])
    t.width(i/100 + 1)
    t.forward(i)
    t.left(59)
    
turtle.done()
