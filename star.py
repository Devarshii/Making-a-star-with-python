import turtle
import time

tp=turtle.Turtle()
screen= turtle.Screen()
screen.bgcolor('#000000')
screen.update()
colour_set=['red','green','blue','yellow','purple']
turtle.title("Star")
tp.pensize(4)
tp.penup()
tp.setpos(-90,30)
tp.pendown()
for i in range(5):
     tp.pencolor(colour_set[i])
     tp.forward(200)
     tp.right(144)
tp.penup()
tp.setpos(80,-140)
tp.pendown()
tp.ht()
turtle.done()
turtle.mainloop 