H = 40.0
g = -9.81
t = 0.07
r=0.1
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




for k in range(1, 10):
   for i in range (len(Particles[0])):
       j=2
       print(i,j)
       for j in range(len(Particles[0])):
        if pow(((Particles[y][i]-Particles[y][j]) **2 + (Particles[x][i]-Particles[x][j])**2),0.5)<=r:
            Particles[uy][i] *= -1
            Particles[ux][i] *= -1
            Particles[uy][j] *= -1
            Particles[ux][j] *= -1
            print("Kick")

        print(Particles[y][j])
        print(Particles[y][i])

        Particles[uy][i] += g * t
        Particles[y][i] += Particles[uy][i] * t + (g * t ** 2) / 2
        Particles[x][i] += ux * t
        if Particles[y][i] <= 0:
            if Particles[uy][i] < 0:
                Particles[uy][i] = -0.6 * Particles[uy][i]
   #print("%.2f" % Particles[y][j],s,"%.2f" % Particles[uy][j],s,"%.2f" % t1)

