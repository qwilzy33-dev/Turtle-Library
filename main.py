import turtle

t = turtle.Turtle()

def draw_square():
    for _ in range(4):
        t.forward(100)
        t.left(90)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_pentagon():
    for _ in range(5):
        t.forward(100)
        t.left(72)

def draw_polygon(sides):
    for _ in range(sides):
        t.forward(100)
        t.left(360 / sides)

def draw_verycoolshape():
    for _ in range(24):
        draw_polygon(10)
        t.left(15)

for i in range(36):
    t.speed(10)
    draw_verycoolshape()
    t.left(10)
t.screen.mainloop()



