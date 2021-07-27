import turtle

def setup(pencil):
    pencil.color('blue')
    pencil.penup()
    pencil.goto(-200,100)
    pencil.pendown()

def koch(pencil, size, order):
   print(order) 

def main():
    pencil = turtle.Turtle()
    setup(pencil)
    turtle.tracer(100)

    order = 2

if __name__ == '__main__':
if __name__ == '__main__':