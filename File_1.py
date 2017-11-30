H = 40.0
g = 9.81
t = 0.01
S = H
u = 0
for i in range(1, 50):
     S = S - u*t - (g*(t**2))/2
        u -= g*t
             t1 *= i
             if S <= 0:
                if u > 0:
                    u = -1*u
             if S = 0 and u = 0:
                print("Stop", t1)
                  break

             print(S,u,t1)

