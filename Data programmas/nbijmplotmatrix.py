import numpy as np
import matplotlib.pyplot as plt

k = int(input("y "))
l = int(input("x "))

n = np.arange(k)
m = np.arange(l)

f, axarr = plt.subplots(nrows=k, ncols=l, sharex="col", sharey="row", squeeze=False)
t = np.linspace(0, 2 * np.pi, 100000 / (k * l))

for x in n:
    for y in m:
        axarr[x, y].plot(np.sin(x * t), np.cos(y * t))

cols = ["sin(x*{})".format(col) for col in range(l)]
rows = ["cos(y*{})".format(row) for row in range(k)]


for ax, col in zip(axarr[0], cols):
    ax.set_title(col)

for ax, row in zip(axarr[:, 0], rows):
    ax.set_ylabel(row, rotation=0, size="large")


print(n, m)
plt.show()
