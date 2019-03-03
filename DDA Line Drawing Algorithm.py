from Tkinter import *

root = Tk()
root.title("DDA")
canvas = Canvas(root, width=1000,height=1000)

canvas.pack()

line = canvas.create_line(100,100,100,900)
line = canvas.create_line(100,900,900,900)

def dda(m,n):
    x0 = m[0] 
    x1 = n[0]
    y0 = m[1]
    y1 = n[1]
    x = x0
    y = y0
    dx = (x1 - x0)

    dy = (y1 - y0)

    if dx >= dy:
	stepsize = dx
    else:
	stepsize = dy

    xinc = int((x1 - x0)/stepsize)

    yinc =  int((y1 - y0)/stepsize)
    print (x,y)

    i=1;
    for i in range(stepsize):
       x = x+xinc
       y = y+yinc
       print (x,y)
       text = canvas.create_text(x,y,text = ".")

point=[[200,600],[400,400],[600,400],[800,600]]

for i in range(3):
    dda(point[i],point[i+1])
root.mainloop()
