import turtle as trtl
trtl.setup(800, 800)
trtl.speed(0)
trtl.hideturtle()
trtl.penup()
trtl.goto(-300,0)
trtl.pendown()
for i in range(5):
    trtl.circle(50)
    trtl.penup()
    trtl.forward(150)
    trtl.pendown()


wn = trtl.Screen()
wn.mainloop()
