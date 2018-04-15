from tkinter import *
from random import *
g = 10
height=1000
y = 0
x = 1
uy = 2
ux = 3
t1 = 0.5
s = "   "
boo = "false"

while (boo != 'да'):
    print("Введите число частиц:")
    number = int(input())
    print("Введите время шага:")
    t = float(input())
    print("Введите коэффициент потерь:")
    kpoteri = float(input())
    print("Введите размер частицы:")
    r = int(input())
    print("Введите 'да', если всё верно, 'нет' в проивном случае:")
    boo = input()


Particles = [0,0] * 4
for i in range(4):
    Particles[i] = [0] * number

for z in range(0,number):
    Particles[y][z] = -70*z + randint(-5,+5)
    Particles[x][z]+= height/2+ randint(-10,+10)
    Particles[ux][z]=0
    Particles[uy][z]=0

def time_move(n):
    if n < 800:
        i = 0
        j = 0
        for i in range(number):

            Particles[uy][i] += round(g * t)
            Particles[y][i] += round(Particles[uy][i] * t)
            Particles[x][i] += round(Particles[ux][i] * t)
            if Particles[y][i] >=height-r :
                if Particles[uy][i] >0:
                    Particles[uy][i] = round(-kpoteri * Particles[uy][i])


            if Particles[x][i] >=height-r :
                if Particles[ux][i] >0:
                    Particles[ux][i] =round(-kpoteri*Particles[ux][i])
            if Particles[x][i] <=0 :
                if Particles[ux][i] <0:
                    Particles[ux][i] =round(-kpoteri*Particles[ux][i])


        for i in range(number):
            j=i+1
            for j in range(i+1,number):

             if (j <= number):
                length=round(pow(((Particles[y][i] - Particles[y][j]) ** 2 + (Particles[x][i] - Particles[x][j]) ** 2), 0.5))
                if (length <= 2 * r)and(length!=0):
                    a = round(
                        Particles[uy][i] * abs(((Particles[y][i] - Particles[y][j])) / length) + Particles[ux][i] * abs((
                            (Particles[x][i] - Particles[x][j])) / length))
                    b = round(Particles[uy][i] * abs((Particles[x][i] - Particles[x][j])) / length)
                    # print((Particles[x][i]))
                    # print((Particles[x][j]))
                    Particles[uy][i] = round(
                        Particles[uy][j] * abs(((Particles[y][i] - Particles[y][j])) / length)+ Particles[ux][j] * abs((
                            (Particles[x][i] - Particles[x][j])) / length))
                    Particles[uy][j] = a
                    if (Particles[x][i] > Particles[x][j]):
                        Particles[ux][i] += round(
                            Particles[uy][j] * abs(((Particles[y][i] - Particles[y][j])) / length) + Particles[ux][
                                j] * abs(((Particles[x][i] - Particles[x][j])) / length))
                        Particles[ux][j] += -b
                    if (Particles[x][i] < Particles[x][j]):
                        Particles[ux][i] += -round(
                            Particles[uy][j] * abs(((Particles[y][i] - Particles[y][j])) / length)+ Particles[ux][
                                j] * abs(((Particles[x][i] - Particles[x][j])) / length))
                        Particles[ux][j] += b
                    # print("kick")
                    break

        #time.sleep(0.1)

        canvas.delete(ALL)
        for ln in range(0, number):
            canvas.create_oval(Particles[x][ln] - r, Particles[y][ln] - r, Particles[x][ln] + r, Particles[y][ln] + r,
                                 fill='black', width=0)

        canvas.after(50, lambda: time_move(n + 1))
#
frame = Tk()
canvas = Canvas(frame, width=height, height=height, background="white")
canvas.grid()
canvas.after(50, lambda: time_move(0))
#
frame.mainloop()
