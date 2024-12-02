import math
import turtle
r=int(input('Please enter the radius: '))
ans=math.pi*r*2
print(ans,'is the cicumfrence of the radius of:',r)
pen=turtle.Turtle()
screen=turtle.Screen()
pen.circle(r)
pen.penup()
pen.goto(0,-100)
pen.pendown()
pen.write(str(ans)+' is your circumfrence.', font=("Comic Sans MS",
                                    20, "normal"))
screen.mainloop()

