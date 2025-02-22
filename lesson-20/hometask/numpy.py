import numpy as np
print(np.__version__)
np.show_config()
Z = np.zeros(10)
print(Z)
Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize))
%run `python -c "import numpy; numpy.info(numpy.add)"`
%run `python -c "import numpy; numpy.info(numpy.add)"`
Z = np.zeros(10)
Z[4] = 1
print(Z)
Z = np.arange(10,50)
print(Z)
Z = np.arange(50)
Z = Z[::-1]
print(Z)
Z = np.arange(9).reshape(3,3)
print(Z)
nz = np.nonzero([1,2,0,0,4,0])
print(nz)
Z = np.eye(3)
print(Z)
Z = np.random.random((3,3,3))
print(Z)
Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)
Z = np.random.random(30)
m = Z.mean()
print(m)
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
print(Z)
Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)
Z = np.diag(1+np.arange(4),k=-1)
print(Z)
Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)
print(np.unravel_index(100,(6,7,8)))
Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
print(Z)
Z = np.random.random((5,5))
Z = (Z - np.mean (Z)) / (np.std (Z))
print(Z)
color = np.dtype([("r", np.ubyte, 1),
                  ("g", np.ubyte, 1),
                  ("b", np.ubyte, 1),
                  ("a", np.ubyte, 1)])
                  Z = np.dot(np.ones((5,3)), np.ones((3,2)))
print(Z)

# Alternative solution, in Python 3.5 and above
Z = np.ones((5,3)) @ np.ones((3,2))
Z = np.arange(11)
Z[(3 < Z) & (Z <= 8)] *= -1
print(Z)
rint(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))
print(np.array(0) / np.array(0))
print(np.array(0) // np.array(0))
print(np.array([np.nan]).astype(int).astype(float))
Z = np.random.uniform(-10,+10,10)
print (np.copysign(np.ceil(np.abs(Z)), Z))
Z1 = np.random.randint(0,10,10)
Z2 = np.random.randint(0,10,10)
print(np.intersect1d(Z1,Z2))
