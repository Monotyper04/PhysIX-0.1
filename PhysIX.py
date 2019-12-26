from tkinter import *
import math
def roll():
    global dx
    global dy
    global ball_x
    global ball_y
    global dirX
    global dirY
    global grav
    global ForceFall

    def sign(x):
        if x > 0:
            return 1
        elif x == 0:
            return 0
        else:
            return-1
    
    dirX = sign(dx)
    dirY = sign(dy)
    ForceFall = mass * grav
    ball_x = ball_x + dx
    ball_y = ball_y + dy
    dy = dy + ForceFall 
    CCfriction = 1 - Cfriction
    friction = grav * CCfriction

    
    #elif dirY == 1:
       # dy = dy - ForceFall 

    
    if ball_x >= (screen_w - ball_Size_x + 5) or ball_x <= -5:
        dx = -dx * Bounce
        if ball_x > (screen_w  - ball_Size_x + 5):
            dx = dx - 2
        if ball_x < -5:
            dx = dx + 2
    if ball_y >= (screen_h  - ball_Size_y) or ball_y <=0:
        dy = -dy * Bounce
        dx = dx * friction
        if dy < 1.1 and dy > -1.1 and ball_y >= 500 :
            dy = 0
        if ball_y > (screen_h  - ball_Size_y + 5):
            dy = dy - 2
        if ball_y < -5:
            dy = dy + 2
    
    print(str(dx) + " , " + str(dy) + " , " + str(ForceFall))

    canv.coords(oval, ball_x, ball_y, ball_x + ball_Size_x, ball_y + ball_Size_y)
    form.after(15,roll)

screen_w = 800
screen_h = 600

form = Tk()
form.title("PhysIX 0.1")
canv = Canvas(form, width=screen_w, height=screen_h, bg="lightblue")
canv.pack()

ball_Size_x = 100
ball_Size_y = 100
ball_x = ball_Size_x + 10
ball_y = ball_Size_y + 10 # screen_h - ball_Size_y - 10 #   
dx = 10
dy = 0
mass = 1
grav = 1
Bounce = 0.65
Cfriction = 0.02

oval = canv.create_oval(ball_x, ball_y, ball_x + ball_Size_x, ball_y + ball_Size_y, fill="red")
form.after(0, roll)

form.mainloop()