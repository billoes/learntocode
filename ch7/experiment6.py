import turtle


slowpoke = turtle.Turtle()
slowpoke.shape('turtle')
slowpoke.color('blue')

def make_shape(t,sides):
    angle=360/sides
    for i in range(0,sides):
        t.forward(100)
        t.right(angle)

make_shape(slowpoke,3)



turtle.mainloop()