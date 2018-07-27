from tkinter import *
import time
def dda(a,b,c):
    x0=a[0]
    y0=a[1]
    x1=b[0]
    y1=b[1]
    stepsize = abs(y1 - y0) > abs(x1 - x0)
    if stepsize:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    if y0 < y1:
        ystep = 1
    else:
        ystep = -1
    dx = x1 - x0
    dy = abs(y1 - y0)
    error = -dx / 2
    y = y0
    for x in range(x0, x1 + 1):
        if stepsize:
            canvas.create_text(y,x,text=".",fill=c ,font="Times 40 bold")
        else:
            canvas.create_text(x,y,text=".",fill=c, font="Times 40 bold")
        error = error + dy
        if error > 0:
            y = y + ystep
            error = error - dx

def one():
    v = [ 0 ,1, 1, 0, 0, 0, 0]
    draw(v)
def zero():
    v = [ 1 ,1, 1, 1, 1, 1, 0]
    draw(v)
def two():
    v = [ 1 ,1, 0, 1, 1, 0, 1]
    draw(v)
def three():
    v = [ 1 ,1, 1, 1, 0, 0, 1]
    draw(v)
def four():
    v = [ 0 ,1, 1, 0, 0, 1, 1]
    draw(v)
def five():
    v = [ 1 ,0, 1, 1, 0, 1, 1]
    draw(v)    
def six():
    v = [ 1 ,0, 1, 1, 1, 1, 1]
    draw(v)
def seven():
    v = [ 1 ,1, 1, 0, 0, 0, 1]
    draw(v)
def eight():
    v = [ 1 ,1, 1, 1, 1, 1, 1]
    draw(v)
def nine():
    v = [ 1 ,1, 1, 1, 0, 1, 1]
    draw(v)
    
def clear():
    drawa0()
    drawb0()
    drawc0()
    drawd0()
    drawe0()
    drawf0()
    drawg0()
def animation():
    zero()
    one()
    two()
    three()
    four()
    five()
    six()
    seven()
    eight()
    nine()
    clear()


def but():
    canvas.create_text(700,160 ,fill="black",font="Times 20 bold",text="a")
    canvas.create_text(700,300 ,fill="black",font="Times 20 bold",text="g")
    canvas.create_text(700,450 ,fill="black",font="Times 20 bold",text="d")

    canvas.create_text(830,250 ,fill="black",font="Times 20 bold",text="b")
    canvas.create_text(830,400 ,fill="black",font="Times 20 bold",text="c")

    canvas.create_text(570,250 ,fill="black",font="Times 20 bold",text="f")
    canvas.create_text(570,400 ,fill="black",font="Times 20 bold",text="e")


    canvas.create_oval(820,450,850,480,fill="red")
    a = Button(canvas, text="a 0", command= drawa0)
    a.place(x=600, y=520)
    a = Button(canvas, text="a 1", command= drawa1)
    a.place(x=600, y=550)

    a = Button(canvas, text="b 0", command= drawb0)
    a.place(x=630, y=520)
    a = Button(canvas, text="b 1", command= drawb1)
    a.place(x=630, y=550)

    a = Button(canvas, text="c 0", command= drawc0)
    a.place(x=660, y=520)
    a = Button(canvas, text="c 1", command= drawc1)
    a.place(x=660, y=550)

    a = Button(canvas, text="d 0", command= drawd0)
    a.place(x=690, y=520)
    a = Button(canvas, text="d 1", command= drawd1)
    a.place(x=690, y=550)

    a = Button(canvas, text="e 0", command= drawe0)
    a.place(x=720, y=520)
    a = Button(canvas, text="e 1", command= drawe1)
    a.place(x=720, y=550)

    a = Button(canvas, text="f 0", command= drawf0)
    a.place(x=750, y=520)
    a = Button(canvas, text="f 1", command= drawf1)
    a.place(x=750, y=550)

    a = Button(canvas, text="g 0", command= drawg0)
    a.place(x=780, y=520)
    a = Button(canvas, text="g 1", command= drawg1)
    a.place(x=780, y=550)
    
def drawa1():
    dda([625,180],[775,180],"red")
def drawa0():
    dda([625,180],[775,180],"white")

def drawb1():
    dda([800,200],[800,300],"red")
def drawb0():
    dda([800,200],[800,300],"white")
def drawc1():
    dda([800,350],[800,450],"red")
def drawc0():
    dda([800,350],[800,450],"white")

def drawd1():
    dda([625,475],[775,475],"red")
def drawd0():
    dda([625,475],[775,475],"white")

def drawe1():
    dda([600,350],[600,450],"red")
def drawe0():
    dda([600,350],[600,450],"white")

def drawf1():
    dda([600,200],[600,300],"red")
def drawf0():
    dda([600,200],[600,300],"white")

def drawg1():
    dda([625,325],[775,325],"red")
def drawg0():
    dda([625,325],[775,325],"white")


def draw(v):
    if (v[5] == 1):
        dda([600,200],[600,300],"red")#f
    else:
        dda([600,200],[600,300],"white")
    if (v[1] == 1):
        dda([800,200],[800,300],"red") #b 
    else:
        dda([800,200],[800,300],"white")
    if (v[4] == 1):
        dda([600,350],[600,450],"red") #e
    else:
        dda([600,350],[600,450],"white")
    if (v[2] == 1):
        dda([800,350],[800,450],"red") #c
    else:
        dda([800,350],[800,450],"white")
    if (v[0] == 1):
        dda([625,180],[775,180],"red") #a
    else:
        dda([625,180],[775,180],"white") 
    if (v[6] == 1):
        dda([625,325],[775,325],"red") #g
    else:
        dda([625,325],[775,325],"white")
    if (v[3] == 1):
        dda([625,475],[775,475],"red") #d
    else:
        dda([625,475],[775,475],"white")

    canvas.create_oval(820,450,850,480,fill="red")
    canvas.update()
    canvas.after(400)
    

master=Tk()
canvas_width=master.winfo_screenwidth()
canvas_height=master.winfo_screenheight()
canvas=Canvas(master,bg='white',width=canvas_width,height=canvas_height)
canvas.pack()
but()
a = Button(canvas, text="Animation", command= animation, height=3 ,width =10)
a.place(x=660, y=80)

a = Button(canvas, text="Clear", command= clear,height=2 ,width =7)
a.place(x=670, y=25)

k = Button(canvas, text="1", command= one ,height=3 ,width =5)
k.place(x=200, y=215)

k = Button(canvas, text="2", command= two ,height=3 ,width =5)
k.place(x=250, y=215)

k = Button(canvas, text="3", command= three ,height=3 ,width =5)
k.place(x=300, y=215)

k = Button(canvas, text="4", command= four ,height=3 ,width =5)
k.place(x=200, y=275)

k = Button(canvas, text="5", command= five ,height=3 ,width =5)
k.place(x=250, y=275)

k = Button(canvas, text="6", command= six ,height=3 ,width =5)
k.place(x=300, y=275)

k = Button(canvas, text="7", command= seven ,height=3 ,width =5)
k.place(x=200, y=335)

k = Button(canvas, text="8", command= eight ,height=3 ,width =5)
k.place(x=250, y=335)

k = Button(canvas, text="9", command= nine ,height=3 ,width =5)
k.place(x=300, y=335)

k = Button(canvas, text="0", command= zero ,height=3 ,width =5)
k.place(x=250, y=395)

canvas.create_text(270,500 ,fill="black",font="Times 20 bold",text="KEYPAD")
canvas.create_text(705,600 ,fill="black",font="Times 20 bold",text="Supply To Segment")

mainloop()
