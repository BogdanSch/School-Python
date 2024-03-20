import turtle

def main():
    # Fullscreen the canvas
    screen = turtle.Screen()
    screen.setup(1.0, 1.0)

    # Begin!
    t = turtle.Turtle()
    t.shape("turtle")

    # Opdracht 1
    # for _ in range(6):
    #     t.forward(50)
    #     t.right(60)

    # Opdracht 2
    # for _ in range(4):
    #     t.forward(200)
    #     t.right(90)

    # Opdracht 3
    # for _ in range(3):
    #     t.forward(100)
    #     t.right(120)

    # Opdracht 4:
    # for _ in range(10):
    #     t.right(-90)
    #     t.forward(20)
    #     t.right(90)
    #     t.forward(20)

    # Opdracht 5:
    length = 150
    for _ in range(4):
        t.right(45)
        t.forward(length)
        t.backward(length * 2)
        t.forward(length)


    screen.mainloop()
