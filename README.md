[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SkD24yV8)
# 1.1.4Spirographs

*Complete the following.*

1. Compare and contrast zero-iteration conditions and infinite loops.
   Zero Iteration Conditions- Condition that always will evaluate to false, or at least will the first time. Code never runs because it never starts.

Infinite Loops- Sequence of instructions that loops endlessly because condition is not met or code never breaks.

Both- Both are dependent on conditions and have a loop structure.





2. A link to your code where you solve the following problem. Take the screen size of 800px. Create code or algorithm that always places the object(s), up to 5, in the center an equal distance from one another and from the edges of the screen.
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






3. Concentric Squares -- Add a screenshot of your result and the code to create it on your repo.
Objective: Write a Python program using the turtle module to draw a pattern of concentric squares. The pattern should be created using nested loops.
![image](https://github.com/user-attachments/assets/116c3dc5-3acf-4350-a22d-fc20558c8362)


Instructions:

Setup the Turtle Environment:
Import the turtle module.
Create a turtle object.
Set the turtle speed to the fastest setting.
Draw Concentric Squares:
Use a nested loop to draw multiple squares.
The outer loop should control the number of squares.
The inner loop should draw each square.
Each square should be slightly larger than the previous one.
Customize the Pattern:
Use different colors for each square.
Ensure the squares are centered on the screen.
Example Output:

The turtle should draw a series of squares, each one larger than the last, creating a pattern of concentric squares.

Hints:

Use the penup() and pendown() methods to move the turtle without drawing.
Use the color() method to change the turtle’s color.
Use the forward() and right() methods to draw the sides of the squares.


4. Complete the steps 17, 18 and 19 from [mypltw use clever to sign on](https://pltw.read.inkling.com/a/b/5310c007377c46e28d745961310f0c2e/p/728c751a6c4145bea0ea83c5058fb9f9#44b0003a2ee14fcc9865e7bb5faec747)
5. Answer to step 21
6. Insert a screenshot or picture of the algorith you used for your tokenizer on the previous activity.
7. Give an example of an undecidable problem, attach code.
   


