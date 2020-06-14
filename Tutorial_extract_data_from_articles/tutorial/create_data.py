"""Generate dummy data."""

import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
import numpy as np
%matplotlib qt5

# data
x = np.linspace(1, 25, 100)
y1 = np.sin(x+2)*np.exp(-0.25*(x+2))
y2 = np.sin(x)*np.exp(-0.1*x)

# %%
fig = plt.figure(figsize=(3.386, 2))
ax = fig.add_subplot(111)
dummy = ax.plot(x, y1, color='black', label='black')
dummy = ax.plot(x, y2, color='red', label='red')
dummy = ax.set_xlabel('x axis')
dummy = ax.set_ylabel('y axis')
dummy = ax.legend()
ax.set_position(Bbox([[.2, .21], [.98, .98]]))


plt.savefig('raster_solid.png')
plt.savefig('vector_solid.pdf')


# %%
fig = plt.figure(figsize=(3.386, 2))
ax = fig.add_subplot(111)
dummy = ax.scatter(x, y1, s=2, color='black', label='black')
dummy = ax.scatter(x, y2, s=2, color='red', label='red')
dummy = ax.set_xlabel('x axis')
dummy = ax.set_ylabel('y axis')
dummy = ax.legend()
ax.set_position(Bbox([[.2, .21], [.98, .98]]))


plt.savefig('raster_scatter.png')
plt.savefig('vector_scatter.pdf')
