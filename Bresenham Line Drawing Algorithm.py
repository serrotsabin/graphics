from tkinter import *
root = Tk()
root.title("BLA")
canvas = Canvas(root, width=500,height=500)

canvas.pack()

def bla(a,b,c):
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
            canvas.create_text(y,x,text=".",fill=c)
        else:
            canvas.create_text(x,y,text=".",fill=c)
        error = error + dy
        if error > 0:
            y = y + ystep
            error = error - dx

def bar(x,c):
    bla([x[0]-10,x[1]],[x[0]+10,x[1]],c)
    bla([x[0]-10,x[1]],[x[0]-10,450],c)
    bla([x[0]+10,x[1]],[x[0]+10,450],c)

ylabel=30
yc=10 # y axis ma huney number ko difference
day=["A","B","C","D"]
for i in range (10):
    canvas.create_text(30,ylabel,text=str(yc-i)+"0",font=("Times New Roman", 10)) # y axis ko numbers
    ylabel=ylabel+43
for i in range(len(day)):
    canvas.create_text(100+i*100,470,text=day[i],font=("Times New Roman", 10)) # x axis ko numbers
bla([50,50],[50,450],"black")   # x axis and y axis
bla([50,450],[450,450],"black")

a=[[54.55,51.61,53.96,53.76],"black"]


def plot(data,colour):# size of the plot garnu parne point ko list..kati ota plot garne bhanera
    coor=[0]*(len(data))
    for i in range(len(data)): #yo chai pathaeko data lai graph ko point ma convert garcha
        datax=int(100+i*100) #graph ma plot gareko X point haru bich ko calculation suppose first point 100 ma tespachi ko point 200
        datay=int(450-data[i]*4) # for y 
        canvas.create_text(datax,datay,text=data[i],font=("Times New Roman", 10),fill=colour) # y ko value  haru print gareko 
        coor[i]=[datax,datay+20] # graph ko pount calculate garepachi teslai list ma halcha ani pachi yo point haru bich line banaucha
    for i in range((len(data))):
        bar(coor[i],colour)




plot(a[0],a[1])


root.mainloop()
