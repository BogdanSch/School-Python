import turtle

screen = turtle.Screen()
screen.setup(1.0, 1.0)

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def drawHouse(length, color):
  t.color(color)
  for _ in range(4):
    t.forward(length)
    t.left(90)
  
  t.left(90)
  t.forward(length)
  t.right(30)
  t.forward(length)
  t.right(120)
  t.forward(length)
  t.right(30)
  t.forward(length)
  t.left(90)

def main():
    drawHouse(100, "red")
    screen.mainloop()

#Uliana - Je kan beter nog functies maken voor het tekenen van de vierkanten en driehoeks
#Ada - Jouw code is schoon geschreven en je maakt gebruik van modules