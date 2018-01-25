import tkinter
g = -9.81
t = 0.07
r = 10
y = 0
x = 1
uy = 2
ux = 0
t1 = 0.5
s = "   "
mol = []

H = 200
Particles = [[H*0.2,0.1*H],[0,0],[0,0],[0,0]]
def time_move(n):
    if n < 800:

        canvas.move(obj, -ux*t, -(Particles[3][0]*t + g*t*t*0.5))
        canvas.move(obj1, -ux * t, -(Particles[3][0] * t + g * t * t * 0.5))
        canvas.after(50, lambda: time_move(n + 1))
#
frame = tkinter.Tk()

canvas = tkinter.Canvas(frame, width=300, height=300, background="black")
canvas.grid()
#
obj = canvas.create_oval(140, 10, 160, 30, fill='white', width=0)
obj1 = canvas.create_oval(140, 160, 160, 180, fill='white', width=0)
canvas.after(50, lambda: time_move(0))
#
frame.mainloop()
