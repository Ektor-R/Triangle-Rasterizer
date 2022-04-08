import numpy as np
import cv2
from matplotlib import pyplot as plt
from datetime import datetime
import math

from src import functions

data = np.load('src/Data/hw1.npy', allow_pickle=True)
verts2d = data[()]['verts2d']
vcolors = data[()]['vcolors']
faces = data[()]['faces']
depth = data[()]['depth']

"""

img = functions.render(verts2d, faces, vcolors, depth, 'flat')

plt.imshow(img)
plt.show()

cv2.imwrite('images/img-' + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.png', cv2.cvtColor( (img*255).astype(np.uint8), cv2.COLOR_BGR2RGB) ) 

"""



"""

img = np.full( (512, 512, 3) , [1., 1., 1.])

img = functions.shade_triangle(
    img,
    [ verts2d[faces[100][0]], verts2d[faces[100][1]], verts2d[faces[100][2]] ],
    [ vcolors[faces[100][0]], vcolors[faces[100][1]], vcolors[faces[100][2]] ],
    'flat'
)

plt.imshow(img)
plt.show()

"""

#"""
img = np.full( (10, 10, 3) , [1., 1., 1.])

img = functions.shade_triangle(
    img,
    np.array( [ [1., 7.], [4., 2.], [7. ,6.] ] ),
    [ [0.4, 0.2, 0.2], [0.4, 0.2, 0.2], [0.4, 0.2, 0.2] ],
    'flat'
)

plt.imshow(img)
plt.grid(color='b')
plt.show()

#"""