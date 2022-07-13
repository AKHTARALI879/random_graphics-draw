import turtle
import colorsys

turtle.Screen().bgcolor("#191919")

pent = turtle.Pen()
ht = 0
pent.speed(50)

for i in range(220):
    pent.width(i // 200 + 1)
    colour = colorsys.hsv_to_rgb(ht, 1, 0.9)
    pent.pencolor(colour)
    pent.forward(i)
    pent.circle(-i * 0.6, -45)
    pent.circle(-i * 0.6, -90)
    pent.circle(-i * 0.6, -45)
    pent.left(120)
    pent.backward(i)
    pent.circle(-i * 0.3, -30)
    pent.circle(-i * 0.3, -60)
    pent.circle(-i * 0.3, -30)
    ht += 0.005

turtle.done()
