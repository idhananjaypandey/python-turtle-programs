import turtle

def draw_branch(t, length):
    if length < 5:
        return
    else:
        t.forward(length)
        t.left(30)
        draw_branch(t, length * 0.7)
        t.right(60)
        draw_branch(t, length * 0.7)
        t.left(30)
        t.backward(length)

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.color("green")
t.width(2)
t.left(90)

draw_branch(t, 100)

screen.mainloop()
