import turtle

def main():
  # Fullscreen the canvas
  screen = turtle.Screen()
  screen.setup(1.0, 1.0)

  # Begin!    
  t = turtle.Turtle()
  t.shape("turtle")


  def drawSquare(directionX, directionY):
    for _ in range(0, 4):
      t.forward(100 * directionX)
      t.right(90 * directionY)

  # Opdracht 2
  # drawSquare(1, 1)
  # drawSquare(-1, 1)

  # Opdracht 3
  # drawSquare(1, -1)
  # drawSquare(-1, -1)

  # Oprdracht 4
  # t.right(-45)
  # t.forward(150)
  # t.right(90)
  # t.forward(80)
  # t.right(-90)
  # t.forward(80)
  # t.right(90)
  # t.forward(150)

  # Opdracht 5
  def drawStair(count):
    for _ in range(0, count):
      t.right(-90)
      t.forward(100)
      t.right(90)
      t.forward(100)
      t.right(90)
      t.forward(100)
      t.right(-90)
      t.forward(100)


  t.forward(100)
  drawStair(2)

  screen.mainloop()
