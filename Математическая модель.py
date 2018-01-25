
WIDTH = 900
HEIGHT = 1000
g = -9.81
t = 0.07
r = 10
y = 0
x = 1
uy = 2
ux = 3
t1 = 0.5
s = "   "
mol = []

Particles = [[HEIGHT*0.2,0.1*HEIGHT],[0,0],[0,0],[0,0]]
print(Particles[y][1])




class Molekula:
    def __init__(self,i,j):
        self.i ,self.j=i,j
        mol.append(self)

    def kick(self):
        Particles[uy][i] *= -1
        Particles[ux][i] *= -1
        Particles[uy][j] *= -1
        Particles[ux][j] *= -1
    def move(self):
        Particles[uy][i] += g * t
        Particles[y][i] += Particles[uy][i] * t + (g * t ** 2) / 2
        Particles[x][i] += ux * t
        if Particles[y][i] <= 0:
            if Particles[uy][i] < 0:
                Particles[uy][i] = -0.6 * Particles[uy][i]




for k in range(1, 100):
   i=0
   j=0
   for i in range (len(Particles[y])):
    j=i+1
    if ((j < len(Particles[y])) and (i != j)):
        for j in range(len(Particles[y])):
            j = i + 1
            print(i, j)

            if pow(((Particles[y][i] - Particles[y][j]) ** 2 + (Particles[x][i] - Particles[x][j]) ** 2), 0.5) <= r:
                a = Particles[uy][i]
                b = Particles[ux][i]
                print(Particles[uy][i],Particles[uy][j])
                Particles[uy][i] = Particles[uy][j]
                Particles[ux][i] = Particles[ux][j]
                Particles[uy][j] = a
                Particles[ux][j] = b
                print("kick")
                break

    Particles[uy][i] += g * t
    Particles[y][i] += Particles[uy][i] * t + (g * t ** 2) / 2
    Particles[x][i] += Particles[ux][i] * t
    if Particles[y][i] <= 0:
        if Particles[uy][i] < 0:
                Particles[uy][i] = -0.8 * Particles[uy][i]



    print("%.2f" % Particles[y][i], s, "%.2f" % Particles[uy][i], s, "%.2f" % t1)


