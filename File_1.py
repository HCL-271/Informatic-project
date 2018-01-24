
H = 40.0
g = -9.81
t = 0.03
r=0.5
y=0
x=1
uy=2
ux=3
t1 = 0.07
s="   "
mol = []
Particles = [[H,0.5*H],[0,0],[0,0],[0,0]]
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
   for i in range (len(Particles[0])-1):
        j=i+1
        if j < 2:
            print(i, j)
            for j in range(len(Particles[0]) - 1):
                if pow(((Particles[y][0] - Particles[y][1]) ** 2 + (Particles[x][0] - Particles[x][1]) ** 2), 0.5) <= r:
                    Particles[uy][i] *= -1
                    Particles[ux][i] *= -1
                    Particles[uy][j] *= -1
                    Particles[ux][j] *= -1
                    print("Kick")
        Particles[uy][0] += g * t
        Particles[y][0] += Particles[uy][0] * t + (g * t ** 2) / 2
        Particles[x][0] += Particles[ux][0] * t
        if Particles[y][0] <= 0:
            if Particles[uy][0] < 0:
                Particles[uy][0] = -0.6 * Particles[uy][0]
        Particles[uy][1] += g * t
        Particles[y][1] += Particles[uy][1] * t + (g * t ** 2) / 2
        Particles[x][1] += Particles[ux][1] * t
        if Particles[y][1] <= 0:
            if Particles[uy][1] < 0:
                Particles[uy][1] = -0.6 * Particles[uy][1]
   print("%.2f" % Particles[y][1],s,"%.2f" % Particles[uy][1],s,"%.2f" % t1)
   print("%.2f" % Particles[y][0], s, "%.2f" % Particles[uy][0], s, "%.2f" % t1)
