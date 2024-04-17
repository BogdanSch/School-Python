import turtle

def main():
  # Fullscreen the canvas
  screen = turtle.Screen()
  screen.setup(1.0, 1.0)

  # Begin!    
  t = turtle.Turtle()
  t.shape("turtle")

  # 1
  # for i in range(10):
  #   t.dot(i * 2)
  #   t.penup()
  #   t.forward(i * 2)
  #   t.pendown()
  #   print(i)

  # 2
  def drawSpiral(count):
    length = 100
    step = 2

    for i in range(count):
      t.pendown()

      for _ in range(4):
        t.forward(length - (i * step * 2))
        t.right(90)

      t.penup()
      t.forward(step)
      t.right(90)
      t.forward(step)
      t.left(90)
      
  # drawSpiral(50)
      
  #4
  def drawCircleSpiral(count):
    for dikte in range(1, count, 3):
      t.dot(dikte)
      t.penup()
      t.forward(dikte * 2)
      t.right(30)
      t.pendown()

  # drawCircleSpiral(40)
  #7
  def drawMaze(count):
    step = 5
    beginLength = 10
    
    for i in range(count):
      for side in range(4):
        t.forward(beginLength + step * i * side)
        t.right(90)

  drawMaze(20)
