import numpy as np
import cv2
from datetime import datetime

from src import functions

data = np.load('src/Data/hw1.npy', allow_pickle=True)

img = functions.render(
    data[()]['verts2d'],
    data[()]['faces'],
    data[()]['vcolors'],
    data[()]['depth'],
    'flat'
)

cv2.imwrite(
    'images/img-flat-' + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg',
    cv2.cvtColor( (img*255).astype(np.uint8), cv2.COLOR_BGR2RGB)
) 