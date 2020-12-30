import numpy as np
import matplotlib.pyplot as plt

 #I advice 100 for a
a = int(input("render level = "))
tmax = float(input("tmax = "))
xmax = float(input("xmax = "))

x = np.linspace(0, xmax, a)
t = np.linspace(0, tmax, a)

def f(x,t):
    s = #your function
    return(s)

plt.figure()
plt.ion()
plt.plot([], [])

i = 0

while i<a:
    y = f(x, t[i])

    plt.clf()
    plt.title('Time = {} secondes'.format(t[i]))
    plt.plot(x, y)
    plt.xlim([0, xmax])
    plt.ylim([-10, 10])
    plt.pause(1/(a*tmax))
    i = i + 1
