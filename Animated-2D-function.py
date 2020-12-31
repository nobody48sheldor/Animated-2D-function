import numpy as np
import matplotlib.pyplot as plt

a = int(input("render level = "))
b = int(input("animation level = "))
tmax = float(input("tmax = "))
xmax = float(input("xmax = "))

x = np.linspace(0, xmax, a)
t = np.linspace(0, tmax, int(b*tmax))

def f(x,t):
    s = #your function
    return(s)

plt.figure()
plt.ion()
plt.plot([], [])

i = 0

while i<(a*tmax):
    y = f(x, t[i])

    plt.clf()
    plt.title('Time = {} secondes'.format(t[i]))
    plt.plot(x, y)
    plt.xlim([0, xmax])
    plt.ylim([-10, 10])
    plt.pause(1/(a*tmax))
    i = i + 1
