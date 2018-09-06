from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
import numpy as np
from sphere import sphere
from discrep_2 import discrep_2

def average_g(triples):
    return np.mean([triple[2] for triple in triples])

def sample_spherical(npoints, ndim=3):
    vec = np.random.randn(ndim, npoints)
    vec /= np.linalg.norm(vec, axis=0)
    return vec.transpose()

#Triples = np.array(list(zip(X, Y, Z)))
npoints = 600

fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

Triples = np.array([p for p in sphere(npoints, [2, 3, 5])])
hull = ConvexHull(Triples)
triangles = hull.simplices
measure = discrep_2(triangles, Triples)
print(measure)

colors = np.array([average_g([Triples[idx] for idx in triangle]) for
                   triangle in triangles])

X = Triples[:, 0]
Y = Triples[:, 1]
Z = Triples[:, 2]

collec = ax1.plot_trisurf(mtri.Triangulation(X, Y, triangles),
        Z, shade=False, cmap=plt.get_cmap('RdYlBu'), array=colors)
collec.autoscale()



Triples = sample_spherical(npoints)
hull = ConvexHull(Triples)
triangles = hull.simplices
measure = discrep_2(triangles, Triples)
print(measure)

colors = np.array([average_g([Triples[idx] for idx in triangle]) for
                   triangle in triangles])

X = Triples[:, 0]
Y = Triples[:, 1]
Z = Triples[:, 2]

collec = ax2.plot_trisurf(mtri.Triangulation(X, Y, triangles),
        Z, shade=False, cmap=plt.get_cmap('RdYlBu'), array=colors)
collec.autoscale()

plt.show()



# plt.plot(points[:,0], points[:,1], 'o')
# plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
# plt.show()
