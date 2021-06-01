from tkinter import *
from tkinter.font import Font
import time
from tkinter.ttk import Combobox
from tkinter import messagebox

#-------------------------------------------------------------------------------------------------------
#Global Variable
oval =  [0]*10     #main big oval
blue =  [0]*10     #small colored oval
red =   [0]*10
green = [0]*10
tseep = [0]*2     #seeptime variable
tseep[0]=0 

#-------------------------------------------------------------------------------------------------------
# problem using backtracking
def start():
    
    V = 9
    graph = {}
#    '''.......  adjacency list  ........'''
#       6-------7------8
#       |     / |    / |
#       |   /   |   /  |
#       | /     | /    |
#       3-------4------5
#       |     / |    / |
#       |   /   |   /  |
#       | /     | /    |
#       0-------1------2
    graph={
            0: [1,4,3],
            1: [0,2,4,5],
            2: [1,5],
            3: [0,4,6,7],
            4: [0,1,3,5,7,8],
            5: [1,2,4,8],
            6: [3,7],
            7: [3,4,6,8],
            8: [4,5,7]}
    
    color=[]
    visit=[]
    degree=[]
    color=[3 for x in range(9)]    #use for mrv, mrv & degree 
    color[8]=4                     #use for mrv, mrv & degree 
    visit=[0 for x in range(9)]    #use for mrv, mrv & degree
    degree =[3,4,2,4,6,4,2,4,3]    #use for degree

        
     
#    ------------------------------------------comon for all algo------------------------------------------------------
    def isSafe( v, colour, c):             # is safe for vertex v
        for i in graph[v]:
            if colour[i] == c:
                return False
        return True
#   --------------------------------------------Backtraking algo-------------------------------------------------------
    
    def backColor(m, colour, v):              # A recursive utility function to solve m
        if v == V:
            return True

        for c in range(1, m + 1):
            if isSafe(v, colour, c) == True:
                colour[v] = c
                if c==1:
                    setcolor="deep pink"
                elif c==2:
                    setcolor="lime green"
                elif c==3:
                    setcolor="purple1"
                elif c==4:
                    setcolor="yellow"
                elif c==5:
                    setcolor="orange"

                time.sleep(tseep[0])
                canvas.itemconfig(oval[v+1],fill=setcolor)
                canvas.itemconfig(red[v+1],fill=setcolor)
                canvas.itemconfig(green[v+1],fill=setcolor)
                canvas.itemconfig(blue[v+1],fill=setcolor)
                canvas.update()
                
                if backColor(m, colour, v + 1) == True:
                    return True
                time.sleep(tseep[0])
                canvas.itemconfig(oval[v+1],fill="white")
                canvas.itemconfig(red[v+1],fill="deep pink")
                canvas.itemconfig(green[v+1],fill="lime green")
                canvas.itemconfig(blue[v+1],fill="purple1")
                canvas.update()
                colour[v] = 0
     
    def backtrakingColouring(m):
        colour = [0] * V
        if backColor(m, colour, 0) == None:
            print("NOT COLORED")
            messagebox.showwarning("Notification","Not possible to design.plz increase the number of color")
            return False
        print("Solution:")
        for c in colour:
            print(c)
        return True

#----------------------------------------------------Forward Traking-------------------------------------------

    def forwardColourUtil(m, colour, v):
        if v == V:
            return True

        for c in range(1, m + 1):
            if isSafe(v, colour, c) == True:
                colour[v] = c
                if c==1:
                    setcolor="deep pink"
                elif c==2:
                    setcolor="lime green"
                elif c==3:
                    setcolor="purple1"
        
                time.sleep(tseep[0])
                canvas.itemconfig(oval[v+1],fill=setcolor)
                canvas.itemconfig(red[v+1],fill=setcolor)
                canvas.itemconfig(green[v+1],fill=setcolor)
                canvas.itemconfig(blue[v+1],fill=setcolor)
                for i in graph[v]:
                    if(setcolor=="deep pink" and i>v):
                        canvas.itemconfig(red[i+1],fill="white")
                    elif(setcolor=="lime green" and i>v):
                        canvas.itemconfig(green[i+1],fill="white")
                    elif(setcolor=="purple1" and i>v):
                        canvas.itemconfig(blue[i+1],fill="white")
                canvas.update()
                
                if forwardColourUtil(m, colour, v + 1) == True:
                    return True
                time.sleep(tseep[0])
                canvas.itemconfig(oval[v+1],fill="white")
                canvas.itemconfig(red[v+1],fill="deep pink")
                canvas.itemconfig(green[v+1],fill="lime green")
                canvas.itemconfig(blue[v+1],fill="purple1")
                colour[v]=0
                for i in graph[v]:
                    if(colour[i]==1 and i<v):
                        canvas.itemconfig(red[v+1],fill="white")
                    if(colour[i]==2 and i<v):
                        canvas.itemconfig(green[v+1],fill="white")
                    if(colour[i]==3 and i<v):
                        canvas.itemconfig(blue[v+1],fill="white")
                    if( i>v):
                        canvas.itemconfig(red[i+1],fill="deep pink")
                        canvas.itemconfig(green[i+1],fill="lime green")
                        canvas.itemconfig(blue[i+1],fill="purple1")
                        for j in graph[i]:
                           if(colour[j]==1 and j<i):
                               canvas.itemconfig(red[i+1],fill="white")
                           if(colour[j]==2 and j<i):
                               canvas.itemconfig(green[i+1],fill="white")
                           if(colour[j]==3 and j<i):
                               canvas.itemconfig(blue[i+1],fill="white")
              
                canvas.update()
                

    def forwardingColouring(m):
        colour = [0] * V
        if forwardColourUtil(m, colour, 0) == None:
            return False


#-------------------------------------------------MRV---------------------------------------------------------
            
    def MRVColourUtil(m, colour, v):
        if v == V:
            return True

        for c in range(1, m + 1):
            minR=10000
            for i in range(0,9):
                if(minR>color[i]):
                    minR=color[i]
                    v=i
                    
            if isSafe(v, colour, c) == True:
                colour[v] = c
                color[v]=1000
                
                if c==1:
                    setcolor="deep pink"
                elif c==2:
                    setcolor="lime green"
                elif c==3:
                    setcolor="purple1"
               
                time.sleep(tseep[0])
                canvas.itemconfig(oval[v+1],fill=setcolor)
                canvas.itemconfig(red[v+1],fill=setcolor)
                canvas.itemconfig(green[v+1],fill=setcolor)
                canvas.itemconfig(blue[v+1],fill=setcolor)
                
                visit[v]=1
                for i in graph[v]:
                    if(setcolor=="deep pink" and visit[i]==0):
                        canvas.itemconfig(red[i+1],fill="white")
                    elif(setcolor=="lime green" and visit[i]==0):
                        canvas.itemconfig(green[i+1],fill="white")
                    elif(setcolor=="purple1" and visit[i]==0):
                        canvas.itemconfig(blue[i+1],fill="white")
                    color[i]= color[i]-1

                canvas.update()
                if MRVColourUtil(m, colour, v + 1) == True:
                    return True
                
                canvas.update()
                
    def MRVColouring(m):
        colour = [0] * V
        if MRVColourUtil(m, colour, 0) == None:
            return False

#-------------------------------------------------MRV  & Degree---------------------------------------------------------

    def MRVDGColourUtil(m, colour, v):
        if v == 7:
            return True

        for c in range(1, m + 1):
            minR=4
            maxD=-1        
            for i in range(0,9):
                if(minR>color[i]):
                    minR= color[i]
            for i in range(9):
                if(minR== color[i]):
                    if(maxD< degree[i]):
                        maxD= degree[i]
                        v=i

            if isSafe(v, colour, c) == True:
                colour[v] = c
                color[v]=1000
                
                if c==1:
                    setcolor="deep pink"
                elif c==2:
                    setcolor="lime green"
                elif c==3:
                    setcolor="purple1"
               
                time.sleep(tseep[0])
                canvas.itemconfig(oval[v+1],fill=setcolor)
                canvas.itemconfig(red[v+1],fill=setcolor)
                canvas.itemconfig(green[v+1],fill=setcolor)
                canvas.itemconfig(blue[v+1],fill=setcolor)
                
                visit[v]=1
                for i in graph[v]:
                    if(setcolor=="deep pink" and visit[i]==0):
                        canvas.itemconfig(red[i+1],fill="white")
                    elif(setcolor=="lime green" and visit[i]==0):
                        canvas.itemconfig(green[i+1],fill="white")
                    elif(setcolor=="purple1" and visit[i]==0):
                        canvas.itemconfig(blue[i+1],fill="white")
                    color[i]= color[i]-1

                canvas.update()
                
                if MRVDGColourUtil(m, colour, v + 1) == True:
                    return True

                canvas.update()
                

    def graphColouring(m):
        colour = [0] * V
        if MRVDGColourUtil(m, colour, 0) == None:
            return False
            
    
#    ======================================================================================================
#   ========================================================================================================
        
    tseep[0]=tseep[1].get()  #seep time getting
    m = int(combo.get())
    
    print("program check-",ii.get(),jj.get()) 
    print("color---",combo.get())   #color getting

#    condition check:
    if(ii.get()=='none1' and jj.get()=='none2'):    
        backtrakingColouring(m) 
        
    elif(ii.get()=='forward' and jj.get()=='none2'):
        forwardingColouring(m)
    
    elif(ii.get()=='forward' and jj.get()=='mrv'):
        MRVColouring(m)
        
    elif(ii.get()=='forward' and jj.get()=='mrv&degree'):
        graphColouring(m)
        print("md")

# -----------------------------------------------------------------------------------------------------------  
#------------------------------------------Button Function----------------------------------------------   

def reset():

    for i in range(1,10):
        canvas.itemconfig(oval[i],fill="white")
        canvas.itemconfig(blue[i],fill="purple1")
        canvas.itemconfig(red[i],fill="deep pink")
        canvas.itemconfig(green[i],fill="lime green")
        canvas.update()
   


#---------------------------------------------Design-----------------------------------------------
root = Tk()
root.title(".........................Map Coloring.....................")
root.geometry("650x410+650+90")
root.configure(bg="white")
canvas = Canvas(root, width=400, height=400,bg="white")
canvas.pack()
canvas.place(x=5, y=5)

frame = Frame(root, width=200,height=400,bg="white")
frame.pack()
frame.place(x=445, y=30)

buttonframe = Frame(root, width=250,height=100)
buttonframe.place(x=490, y=340)


def forwardDesign():
    # ...1..1...
    oval[1] = canvas.create_oval(120, 320, 70, 270, fill="white", outline="black", width=2)
    blue[1]=canvas.create_oval(95,295,80,280,fill="purple1",width=0)
    red[1]=canvas.create_oval(110,295,95,280,fill="deep pink",width=0)
    green[1]=canvas.create_oval(103,310,88,295,fill="lime green",width=0)
    # ...1..2...
    oval[2] = canvas.create_oval(220, 320, 170, 270, fill="white", outline="black", width=2)
    blue[2]=canvas.create_oval(195,295,180,280,fill="purple1",width=0)
    red[2]=canvas.create_oval(210,295,195,280,fill="deep pink",width=0)
    green[2]=canvas.create_oval(203,310,188,295,fill="lime green",width=0)
    # ...1..3...
    oval[3] = canvas.create_oval(320, 320, 270, 270, fill="white", outline="black", width=2)
    blue[3]=canvas.create_oval(295,295,280,280,fill="purple1",width=0)
    red[3]=canvas.create_oval(310,295,295,280,fill="deep pink",width=0)
    green[3]=canvas.create_oval(303,310,288,295,fill="lime green",width=0)
    # ...2..1...
    oval[4] = canvas.create_oval(120, 220, 70, 170, fill="white", outline="black", width=2)
    blue[4]=canvas.create_oval(95,195,80,180,fill="purple1",width=0)
    red[4]=canvas.create_oval(110,195,95,180,fill="deep pink",width=0)
    green[4]=canvas.create_oval(103,210,88,195,fill="lime green",width=0)
    # ...2..2...
    oval[5] = canvas.create_oval(220, 220, 170, 170, fill="white", outline="black", width=2)
    blue[5]=canvas.create_oval(195,195,180,180,fill="purple1",width=0)
    red[5]=canvas.create_oval(210,195,195,180,fill="deep pink",width=0)
    green[5]=canvas.create_oval(203,210,188,195,fill="lime green",width=0)
    # ...2..3...
    oval[6] = canvas.create_oval(320, 220, 270, 170, fill="white", outline="black", width=2)
    blue[6]=canvas.create_oval(295,195,280,180,fill="purple1",width=0)
    red[6]=canvas.create_oval(310,195,295,180,fill="deep pink",width=0)
    green[6]=canvas.create_oval(303,210,288,195,fill="lime green",width=0)
    # ...3..1...
    oval[7] = canvas.create_oval(120, 120, 70, 70, fill="white", outline="black", width=2)    
    blue[7]=canvas.create_oval(95,95,80,80,fill="purple1",width=0)
    red[7]=canvas.create_oval(110,95,95,80,fill="deep pink",width=0)
    green[7]=canvas.create_oval(103,110,88,95,fill="lime green",width=0)
    # ...3..2...
    oval[8] = canvas.create_oval(220, 120, 170, 70, fill="white", outline="black", width=2)
    blue[8]=canvas.create_oval(195,95,180,80,fill="purple1",width=0)
    red[8]=canvas.create_oval(210,95,195,80,fill="deep pink",width=0)
    green[8]=canvas.create_oval(203,110,188,95,fill="lime green",width=0)
    # ...3..3...
    oval[9] = canvas.create_oval(320, 120, 270, 70, fill="white", outline="black", width=2)
    blue[9]=canvas.create_oval(295,95,280,80,fill="purple1",width=0)
    red[9]=canvas.create_oval(310,95,295,80,fill="deep pink",width=0)
    green[9]=canvas.create_oval(303,110,288,95,fill="lime green",width=0)

def noneDesign():
    # ...1..1...
    oval[1] = canvas.create_oval(120, 320, 70, 270, fill="white", outline="black", width=2)
    # ...1..2...
    oval[2] = canvas.create_oval(220, 320, 170, 270, fill="white", outline="black", width=2)
    # ...1..3...
    oval[3] = canvas.create_oval(320, 320, 270, 270, fill="white", outline="black", width=2)
    # ...2..1...
    oval[4] = canvas.create_oval(120, 220, 70, 170, fill="white", outline="black", width=2)
    # ...2..2...
    oval[5] = canvas.create_oval(220, 220, 170, 170, fill="white", outline="black", width=2)
    # ...2..3...
    oval[6] = canvas.create_oval(320, 220, 270, 170, fill="white", outline="black", width=2)
    # ...3..1...
    oval[7] = canvas.create_oval(120, 120, 70, 70, fill="white", outline="black", width=2)
    # ...3..2...
    oval[8] = canvas.create_oval(220, 120, 170, 70, fill="white", outline="black", width=2)
    # ...3..3...
    oval[9] = canvas.create_oval(320, 120, 270, 70, fill="white", outline="black", width=2)


noneDesign()
# 1st
canvas.create_line(120, 95, 170, 95, fill="black", width=2)
canvas.create_line(220, 95, 270, 95, fill="black", width=2)
# 2nd
canvas.create_line(120, 195, 170, 195, fill="black", width=2)
canvas.create_line(220, 195, 270, 195, fill="black", width=2)
# 3rd
canvas.create_line(120, 295, 170, 295, fill="black", width=2)
canvas.create_line(220, 295, 270, 295, fill="black", width=2)

# 11st...colum.....line.....
canvas.create_line(95, 120, 95, 170, fill="black", width=2)
canvas.create_line(95, 220, 95, 270, fill="black", width=2)
# 22nd
canvas.create_line(195, 120, 195, 170, fill="black", width=2)
canvas.create_line(195, 220, 195, 270, fill="black", width=2)
# 33rd
canvas.create_line(295, 120, 295, 170, fill="black", width=2)
canvas.create_line(295, 220, 295, 270, fill="black", width=2)

# 111st.....digonal.......LINE...........
canvas.create_line(180, 115, 115, 180, fill="black", width=2)
canvas.create_line(280, 115, 215, 180, fill="black", width=2)
##222nd
canvas.create_line(180, 215, 115, 280, fill="black", width=2)
canvas.create_line(280, 215, 215, 280, fill="black", width=2)


#--------------------------------------Main Buttom----------------------------------------------------

f1 = Font(family="Times New Romad", size=14, weight="bold")  #,slant="italic",underline=1,overstrike=1)
title = Label(frame, text="Algo: Backtracking", fg="purple",bg="white", font=Font(family="Times New Romad", size=12, weight="bold",underline=1)).pack(side=TOP)

cv=[1,2,3,4,5]                      #color selection for backtraking
combo= Combobox(frame,values=cv,width=15)
combo.set(3)
combo.pack(side=TOP)

ii = StringVar()
ii.set('none1')
jj = StringVar()
jj.set('none2')

title1 = Label(frame, text="Filtering:", fg="green",bg="white",font=f1).pack(side=TOP)
r1 = Radiobutton(frame, text="None", fg="black",bg="white", value='none1', variable=ii,command=noneDesign).pack(side=TOP )
r2 = Radiobutton(frame, text="ForwardChecking", fg="black",bg="white", value='forward', variable=ii, command=forwardDesign).pack(side=TOP)
title2 = Label(frame, text="Ordering:", fg="green",bg="white", font=f1).pack(side=TOP)
r3 = Radiobutton(frame, text="None", fg="black",bg="white", value='none2', variable=jj).pack(side=TOP)
r4 = Radiobutton(frame, text="MRV", fg="black",bg="white", value='mrv', variable=jj,command=forwardDesign).pack(side=TOP)
r5 = Radiobutton(frame, text="MRVwithDegree", fg="black",bg="white", value='mrv&degree', variable=jj,command=forwardDesign).pack(side=TOP)

speed = Scale(frame,bg="plum1",fg="black", from_ = 0,highlightbackground="pink",highlightcolor="chartreuse2", to=5, orient=HORIZONTAL,resolution="0.1", length=150, width=5, sliderlength=15,	
troughcolor="white")
tseep[1]=speed
speed.pack()



b1=Button(buttonframe,text="Reset",bg="cadetblue1",height=1,width=5,command=reset).pack(side=LEFT)
b4=Button(buttonframe,text="Start",bg="chartreuse2",height=1,width=5,command=start).pack(side=LEFT)
#------------------------------------------------------------------------------------------------------
root.mainloop()