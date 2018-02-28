import time
import tkinter
g = 10
height=1000
t = 0.08
r = height/100
y = 0
x = 1
uy = 2
ux = 3
t1 = 0.5
s = "   "
mol = []
kpoteri = 0.9

Particles = [[0,height*0.5],[510,500],[0,0],[0,0]]
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
                    Particles[uy][i] =round(-kpoteri*Particles[uy][i])
            if Particles[x][i] >=height-r :
                if Particles[ux][i] >0:
                    Particles[ux][i] =round(-kpoteri*Particles[ux][i])
            if Particles[x][i] <=0 :
                if Particles[ux][i] <0:
                    Particles[ux][i] =round(-kpoteri*Particles[ux][i])


        for i in range(len(Particles[y])):
            j=i+1
            #print (Particles[y][0])
            #print(Particles[y][1])
            #print("  = =================")
            if (j <= 1):
                length=round(pow(((Particles[y][i] - Particles[y][j]) ** 2 + (Particles[x][i] - Particles[x][j]) ** 2), 0.5))
                if (length <= 2*r):
                    a = round(Particles[uy][i]*abs((Particles[y][i] - Particles[y][j]))/length)
                    b = round(Particles[uy][i]*abs((Particles[x][i] - Particles[x][j]))/length)
                    print((Particles[x][i]))
                    print((Particles[x][j]))
                    Particles[uy][i] = round(Particles[uy][j]*abs((Particles[y][i] - Particles[y][j]))/length)
                    Particles[uy][j] = a
                    if(Particles[x][i] > Particles[x][j]):
                        Particles[ux][i] += round(Particles[uy][j]*abs((Particles[x][i] - Particles[x][j]))/length)
                        Particles[ux][j] += -b
                    if (Particles[x][i] < Particles[x][j]):
                        Particles[ux][i] += -round(Particles[uy][j]*abs((Particles[x][i] - Particles[x][j]))/length)
                        Particles[ux][j] += b
                    print("kick")
                    break

        #time.sleep(0.1)
        canvas.move(obj, round(Particles[ux][0]*t), round(Particles[uy][0]*t))
        canvas.move(obj1, round(Particles[ux][1] * t), round(Particles[uy][1] * t ))
        canvas.after(50, lambda: time_move(n + 1))
#
frame = tkinter.Tk()

canvas = tkinter.Canvas(frame, width=height, height=height, background="white")
canvas.grid()
#
obj = canvas.create_oval(500-r+10,Particles[y][0] - r,500+r+10,  Particles[y][0]+r,  fill='black', width=0)
obj1 = canvas.create_oval(500-r,Particles[y][1] -r, 500+r, Particles[y][1] +r, fill='black', width=0)
canvas.after(50, lambda: time_move(0))
#
frame.mainloop()
