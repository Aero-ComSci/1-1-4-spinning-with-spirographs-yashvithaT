import turtle as trtl
import random

t = trtl.Turtle()
G = 30 
G_move = 20 

t.speed(20)


for i in range(G): 
    current_size = G + i * G_move 
    t.penup()
    t.goto(-current_size / 2, current_size / 2)  
    t.pendown()
#fun colors!!!
    t.color(random.choice(["medium purple", "light blue", "orchid", "violet", "medium orchid", "steel blue"]))
    
    for _ in range(4):  
        t.forward(current_size)
        t.right(90)
        


wn = trtl.Screen()
wn.mainloop()
