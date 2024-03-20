import turtle

screen = turtle.Screen()
screen.setup(1.0, 1.0)

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def drawTriangle():
    for _ in range(3):
        t.forward(20)
        t.right(120)

    t.penup()
    t.forward(30)
    t.pendown()

def main():
    for _ in range(4):
        drawTriangle()
    screen.mainloop()

#Uliana - ik vind het goed dat je  variebele voor turtle heeft toegevoegd
#Alex - Je code ziet er goed uit en ik vind jouw gebruik van python syntax echt goede