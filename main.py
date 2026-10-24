import turtle

t = turtle.Turtle()
colors = ['blue', 'black', 'red', 'yellow', 'green']
t.speed(10)

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

def draw_even_cooler_shape():
    for i in range(36):
        t.speed(10)
        draw_verycoolshape()
        t.left(10)

def draw_circle():
    for _ in range(60):
        t.forward(10)
        t.left(6)

def draw_olympic_ring(x, y, color):
    t.color(color)
    t.width(10)
    move(x, y)
    draw_circle()

def draw_olympic_logo():
    draw_olympic_ring(-240, 0, 'blue')
    draw_olympic_ring(-120, -70, 'yellow')
    draw_olympic_ring(0, 0, 'black')
    draw_olympic_ring(120, -70, 'green')
    draw_olympic_ring(240, 0, 'red')

def up():
    t.setheading(90)
    t.forward(10)

def left():
    t.setheading(180)
    t.forward(10)

def right():
    t.setheading(0)
    t.forward(10)

def down():
    t.setheading(270)
    t.forward(10)

def penup():
    t.penup()

def pendown():
    t.pendown()

def random_color():
    import random
    color = random.choice(colors)
    t.color(color)

def thickness_increase():
    t.width(t.width() + 1)

def thickness_decrease():
    if t.width() > 1:
        t.width(t.width() - 1)

# draw_olympic_logo()
t.screen.onkeypress(up, 'Up')
t.screen.onkeypress(left, 'Left')
t.screen.onkeypress(right, 'Right')
t.screen.onkeypress(down, 'Down')
t.screen.onkeypress(penup, 'p')
t.screen.onkeypress(pendown, 'd')
t.screen.onkeypress(random_color, 'c')
t.screen.onkeypress(thickness_increase, '+')
t.screen.onkeypress(thickness_decrease, '-')
t.screen.onkeypress(draw_square, 's')
t.screen.onkeypress(draw_pentagon, '5')
t.screen.onkeypress(draw_polygon, '6')
t.screen.onkeypress(draw_verycoolshape, 'v')
t.screen.onkeypress(draw_even_cooler_shape, 'e')
t.screen.onkeypress(draw_circle, '0')

t.screen.listen()
t.screen.mainloop()


