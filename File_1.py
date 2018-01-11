H = 40.0
g = 9.81
t = 0.01
S = H
u = 0
mol = []
class Vector:
    def __init__(self, x, y,ux,uy)://Инициализируем координаты,начальную высоту, чкорости.
        self.x=x
          self.y =y 
          self.ux=ux
          self.uy=uy
          
    def __plus__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __minus__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mnoj__(self, other):
        return Vector(self.x * other, self.y * other)

    def __del__(self, other):
        return Vector(self.x / other, self.y / other)

    def __abs__(self):
        return (self.x**2+self.y**2)**(1/2)
     
     
   class Particle:
    def __init__(self, x, y):
        self.x, self.y,  self.ux=ux
          self.uy=uy
        mol.append(self)

    def move(self):
            self.x += self.v.x
            self.y += self.v.y
             self.uy-=g/100
           if (uy==0)&&(y==0):
                    print("STOP d"+i)

    def acc(self):
        a = Vector(0, g)
        for i in mol:
            if i is not self:
                z = Vector(i.x - self.x, i.y - self.y)
                r = a - z / abs(z) ** 8 + z / abs(z) ** 6
                if (abs(r) < 0.9*abs(z)) | (abs(r) > 1.1*abs(z)):
                    a = r
        self.v += a
     

d = Particle(0, H+10,0,0)
for i in range(1, 50):
      d.acc()
    d.move()
    print(d.x, d.y)
     
