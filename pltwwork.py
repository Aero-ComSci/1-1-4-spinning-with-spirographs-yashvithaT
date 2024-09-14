
import turtle as trtl

painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()

painter.pencolor("medium orchid")
x = -200
y = 0
move_x = 1
move_y = 1

while x < 0:
    while y < 100:
        x += move_x
        y += move_y
        painter.goto(x, y)
    move_y = -1

    while y > 0:
        x += move_x
        y += move_y
        painter.goto(x, y)
    move_y = 1

    if x >= 0:
        break  
x = 0
y = 0
move_x = 1
move_y = 1

while x < 200:
    while y < 100:
        x += move_x
        y += move_y
        painter.goto(x, y)
    move_y = -1

    while y > 0:
        x += move_x
        y += move_y
        painter.goto(x, y)
    move_y = 1

    if x >= 200:
        break  
painter.penup()
painter.goto(200, 0)  
painter.pendown()

x = 200
y = 0
move_x = -1
move_y = -1

while x > -100:
    while y > -100:
        x += move_x
        y += move_y
        painter.goto(x, y)
    move_y = 1

    while y < 0:
        x += move_x
        y += move_y
        painter.goto(x, y)
    move_y = -1

    if x <= -100:
        break  

while True:
    x = -200
    y = 0
    move_x = 1
    move_y = 1

    while x < 0:
        while y < 100:
            x += move_x
            y += move_y
            painter.goto(x, y)
        move_y = -1

        while y > 0:
            x += move_x
            y += move_y
            painter.goto(x, y)
        move_y = 1

        if x >= 0:
            break  
    x = 0
    y = 0
    move_x = 1
    move_y = 1

    while x < 200:
        while y < 100:
            x += move_x
            y += move_y
            painter.goto(x, y)
        move_y = -1

        while y > 0:
            x += move_x
            y += move_y
            painter.goto(x, y)
        move_y = 1

        if x >= 200:
            break  
    painter.penup()
    painter.goto(200, 0)  
    painter.pendown()

    x = 200
    y = 0
    move_x = -1
    move_y = -1

    while x > -100:
        while y > -100:
            x += move_x
            y += move_y
            painter.goto(x, y)
        move_y = 1

        while y < 0:
            x += move_x
            y += move_y
            painter.goto(x, y)
        move_y = -1

        if x <= -100:
            break 

