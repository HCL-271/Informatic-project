
import tkinter
g = 9.81
height=1000
t = 0.08
r = height/100
y = 0
x = 1
uy = 2
ux = 0
t1 = 0.5
s = "   "
mol = []
k=10

H = 200
Particles = [[height*0.8,height*0.9],[0,0],[0,0],[0,0]]
def time_move(n):
    if n < 800:
        i = 0
        j = 0
        for i in range(len(Particles[y])):
            j = i + 1
            Particles[uy][i] += g * t
            Particles[uy][i] += g * t
            Particles[y][i] += Particles[uy][i] * t + (g * t ** 2) / 2
            Particles[x][i] += Particles[ux][i] * t
            if Particles[y][i] >=height-r/2 :
                if Particles[uy][i] >0:
                    Particles[uy][i] = -0.8 * Particles[uy][i]
        print(Particles[y][0])
        print(Particles[uy][0])
        print(n)
        canvas.move(obj, ux*t, (Particles[uy][0]*t))
        canvas.move(obj1, ux * t, (Particles[uy][1] * t ))
        canvas.after(50, lambda: time_move(n + 1))
#
frame = tkinter.Tk()

canvas = tkinter.Canvas(frame, width=height, height=height, background="white")
canvas.grid()
#
obj = canvas.create_oval(height/2 - r, height-(H-r), height/2+r, height-(H+r), fill='black', width=0)
obj1 = canvas.create_oval(height/2 -r, height-(H/2-r), height/2 +r,height -(H/2+r), fill='black', width=0)
canvas.after(50, lambda: time_move(0))
#
frame.mainloop()
