from tkinter import * # импротируемые модули
from random import *
g = 10       # ускорение свободного падения
height=1000 # регулировка размеров окна
y = 0       # переменные для перемещения по массивы
x = 1
uy = 2
ux = 3
boo = "false" # строковой с

while (boo != 'да'):          # ввод данных о частицах
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


Particles = [0,0] * 4  # создание массива
for i in range(4):
    Particles[i] = [0] * number

for z in range(0,number):      # заполнение массива начальными данными
    Particles[y][z] = -70*z + randint(-5,+5)
    Particles[x][z]+= height/2+ randint(-10,+10)
    Particles[ux][z]=0
    Particles[uy][z]=0

def time_move(n):
    if n < 800:
        i = 0
        j = 0
        for i in range(number):

            Particles[uy][i] += round(g * t)           # перемещение частиц по действием силы тяжести
            Particles[y][i] += round(Particles[uy][i] * t)
            Particles[x][i] += round(Particles[ux][i] * t)
            if Particles[y][i] >=height-r :
                if Particles[uy][i] >0:
                    Particles[uy][i] = round(-kpoteri * Particles[uy][i])


            if Particles[x][i] >=height-r : # проверка на соударение с боковой границей
                if Particles[ux][i] >0:
                    Particles[ux][i] =round(-kpoteri*Particles[ux][i])
            if Particles[x][i] <=0 :
                if Particles[ux][i] <0:
                    Particles[ux][i] =round(-kpoteri*Particles[ux][i])


        for i in range(number):        #  проверка соударения между частицами и его расчет
            j=i+1
            for j in range(i+1,number):

             if (j <= number):
                length=round(pow(((Particles[y][i] - Particles[y][j]) ** 2 + (Particles[x][i] - Particles[x][j]) ** 2), 0.5))
                if (length <= 2 * r)and(length!=0):
                    a = round(
                        Particles[uy][i] * abs(((Particles[y][i] - Particles[y][j])) / length) + Particles[ux][i] * abs((
                            (Particles[x][i] - Particles[x][j])) / length))
                    b = round(Particles[uy][i] * abs((Particles[x][i] - Particles[x][j])) / length)
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
                    break

        #time.sleep(0.1) вдруг понадобиться тормозить программу

        canvas.delete(ALL)      #  отрисовка частиц на новых позициях
        for ln in range(0, number):
            canvas.create_oval(Particles[x][ln] - r, Particles[y][ln] - r, Particles[x][ln] + r, Particles[y][ln] + r,
                                 fill='black', width=0)

        canvas.after(50, lambda: time_move(n + 1))     # повторение рекурсии
#
frame = Tk()          # создание холста
canvas = Canvas(frame, width=height, height=height, background="white")
canvas.grid()
canvas.after(50, lambda: time_move(0))
#
frame.mainloop()
