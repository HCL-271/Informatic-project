import time
import tkinter
import random
g = 10
height=1000
t = 0.08
r = height/100
kpoteri = 0.9
rand1 = random.randint(1,20)
rand2 = random.randint(1,20)
rand3 = random.randint(1,20)
rand4 = random.randint(1,20)
rand = random.randint(1,20)
y = 0
x = 1
uy = 2
ux = 3
t1 = 0.5
s = "   "
mol = []

Particles = [[0,height*0.3,height*0.4,height*0.7,height/5],[height/2+rand1,height/2-rand2,height/2-rand3,height/2+rand4,height/2-rand],[0,0,0,0,0],[0,0,0,0,0]]
def time_move(n):
    if n < 800:
        i = 0
        j = 0
        for i in range(len(Particles[y])):

            Particles[uy][i] += round(g * t)
            Particles[y][i] += round(Particles[uy][i] * t)
            Particles[x][i] += round(Particles[ux][i] * t)
            if Particles[y][i] >=height-r :
                if Particles[uy][i] >0:
                    print(Particles[uy][i])
                    Particles[uy][i] = round(-kpoteri * Particles[uy][i])


            if Particles[x][i] >=height-r :
                if Particles[ux][i] >0:
                    Particles[ux][i] =round(-kpoteri*Particles[ux][i])
            if Particles[x][i] <=0 :
                if Particles[ux][i] <0:
                    Particles[ux][i] =round(-kpoteri*Particles[ux][i])


        for i in range(len(Particles[y])):
            j=i+1
            for j in range(i+1,len(Particles[y])):

             if (j <= 4):
                length=round(pow(((Particles[y][i] - Particles[y][j]) ** 2 + (Particles[x][i] - Particles[x][j]) ** 2), 0.5))
                if (length <= 2*r):
                    a = round(Particles[uy][i]*abs((Particles[y][i] - Particles[y][j]))/length  + Particles[ux][i]*abs((Particles[x][i] - Particles[x][j]))/length)
                    b = round(Particles[uy][i]*abs((Particles[x][i] - Particles[x][j]))/length)
                    #print((Particles[x][i]))
                    #print((Particles[x][j]))
                    Particles[uy][i] = round(Particles[uy][j]*abs((Particles[y][i] - Particles[y][j]))/length + Particles[ux][j]*abs((Particles[x][i] - Particles[x][j]))/length)
                    Particles[uy][j] = a
                    if(Particles[x][i] > Particles[x][j]):
                        Particles[ux][i] += round(Particles[uy][j]*abs((Particles[x][i] - Particles[x][j]))/length + Particles[ux][j]*abs((Particles[x][i] - Particles[x][j]))/length)
                        Particles[ux][j] += -b
                    if (Particles[x][i] < Particles[x][j]):
                        Particles[ux][i] += -round(Particles[uy][j]*abs((Particles[x][i] - Particles[x][j]))/length + Particles[ux][j]*abs((Particles[x][i] - Particles[x][j]))/length)
                        Particles[ux][j] += b
                    #print("kick")
                    break

        #time.sleep(0.1)
        canvas.move(obj, round(Particles[ux][0]*t), round(Particles[uy][0]*t))
        canvas.move(obj1, round(Particles[ux][1] * t), round(Particles[uy][1] * t ))
        canvas.move(obj2, round(Particles[ux][2] * t), round(Particles[uy][2] * t))
        canvas.move(obj3, round(Particles[ux][3] * t), round(Particles[uy][3] * t))
        canvas.move(obj4, round(Particles[ux][4] * t), round(Particles[uy][4] * t))
        canvas.after(50, lambda: time_move(n + 1))
#
frame = tkinter.Tk()

canvas = tkinter.Canvas(frame, width=height, height=height, background="white")
canvas.grid()
#
obj = canvas.create_oval(Particles[x][0]-r,Particles[y][0] - r,Particles[x][0]+r,  Particles[y][0]+r,  fill='black', width=0)
obj1 = canvas.create_oval(Particles[x][1]-r,Particles[y][1] -r, Particles[x][1]+r, Particles[y][1] +r, fill='black', width=0)
obj2 = canvas.create_oval(Particles[x][2]-r,Particles[y][2] -r, Particles[x][2]+r, Particles[y][2] +r, fill='black', width=0)
obj3 = canvas.create_oval(Particles[x][3]-r,Particles[y][3] -r, Particles[x][3]+r, Particles[y][3] +r, fill='black', width=0)
obj4 = canvas.create_oval(Particles[x][4]-r,Particles[y][4] -r, Particles[x][4]+r, Particles[y][4] +r, fill='black', width=0)
canvas.after(50, lambda: time_move(0))
#
frame.mainloop()
