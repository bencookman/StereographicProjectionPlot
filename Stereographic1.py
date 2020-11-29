import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm


def DrawUnitCircle(ax):
    res = 100
    angs = np.linspace(0, 2*np.pi, res)

    xs = np.sin(angs)
    ys = np.cos(angs)

    ax.plot(xs, ys, "-", color="black")
    return


# Generate n^2 points on sphere of radius r
def SpherePoints(r, n):
    thetas = np.linspace(1/n, np.pi, n)
    phis = np.linspace(0, 2*np.pi, n)

    xs = r*np.outer(np.sin(thetas), np.cos(phis))
    ys = r*np.outer(np.sin(thetas), np.sin(phis))
    zs = r*np.outer(np.cos(thetas), np.ones(n))

    return [xs, ys, zs]


def P(x, y, s):
    newX = x/(1-s)
    newY = y/(1-s)

    return np.array([newX, newY])




# def PInv(x, y):
#     modSqu = np.power(x, 2) + np.power(y, 2)
#     fac = 1/(1 + modSqu)
#     Px = 2*x
#     Py = 2*y
#     Pz = modSqu - 1

#     return fac * np.array([Px, Py, Pz])


# def RatioBetween(val, start, end):
#     return (val-start)/(end-start)


r = 1
n = 50

xs, ys, zs = SpherePoints(r, n)

# Sphere
figS = plt.figure(1)
ax = figS.add_subplot(111, projection='3d')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

hsv1 = cm.get_cmap("hsv", 100)
ax.plot_surface(xs, ys, zs, cmap=hsv1, linewidth=0)

# Complex plane
figC = plt.figure(2)
ax1 = figC.add_subplot(111)

hsv2 = cm.get_cmap("hsv", 100)

Pxs, Pys = P(xs, ys, zs)

print("Pxs = ", Pxs)
print("Pys = ", Pys)

ax1.pcolormesh(Pxs, Pys, zs, cmap="hsv")


DrawUnitCircle(ax1)

plt.show()