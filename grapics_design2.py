import turtle as t
import colorsys
t.bgcolor('black')
t.tracer (50)
t.width(4)
h = 0.0

for i in range(300):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.005
    t.color(c)
    t.up()
    t.goto(0,0)
    t.fd(i-1)
    t.down()
    t.circle(i, 100)
    t.lt(45)
t.done()
