import math
import turtle
def function():
    r=int(input('\nPlease enter the radius: '))
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
    user=input('\nDo you want to use this again? y or n: ')
    if user=='y':
        function()
    else:
        print('\nThanks you. See you soon!\n\n')
        
function()

