import numpy as np
import math
from src import conf

def interpolate_color(x1, x2, x, C1, C2):
    """
        Interpolate colour on a specified point between two points

        Arguments:
            x1: x coordinate (or y) of point no. 1
            x2: x coordinate (or y) of point no. 2
            x: x coordinate (or y) of point to calculate colour on
            C1: colour of point no. 1 (x1)
            C2: colour of point no. 2 (x2)

        Returns:
            Array: colour for point x
    """
    
    l = abs(x2-x)/abs(x2-x1)
    
    return np.add( np.multiply(l, C1), np.multiply(1-l, C2) )



def shade_triangle(img, verts2d, vcolors, shade_t):
    """
        TODO
    """
    
    Ymin = np.empty(3)
    Ymax = np.empty(3)
    sideGradient = np.empty(3)

    activeMarginalPoints = np.array([np.nan, np.nan, np.nan])


    for k in range(3):
        sideStart = k
        sideEnd = (k+1)<=2 and k+1 or 0

        Ymin[k] = min(verts2d[sideStart][1], verts2d[sideEnd][1])
        Ymax[k] = max(verts2d[sideStart][1], verts2d[sideEnd][1])

        if verts2d[sideEnd][0] == verts2d[sideStart][0]:
            sideGradient[k] = 0
        else:
            sideGradient[k] = (verts2d[sideEnd][1] - verts2d[sideStart][1])/(verts2d[sideEnd][0] - verts2d[sideStart][0])
    
    activeSides = np.where(Ymin == Ymin.min())[0]   # First 2 sides (first scan line begins on minimum Y)
    for side in activeSides:
        activeMarginalPoints[side] = _getMinXWhereY(verts2d, Ymin[side])

    for Y in range(int(Ymin.min()), int(Ymax.max()) + 1):     # Scan line
        
        for X in range(int(np.nanmin(activeMarginalPoints)), int(np.nanmax(activeMarginalPoints)) + 1):     # Draw between marginal points
            if shade_t == 'flat':
                #TODO
                img[int(Y)][int(X)] = vcolors[0]
            elif shade_t == 'gouraud':
                #TODO
                pass

        # Update active sides and marginal points
        for side in activeSides:
            if Ymax[side] == Y:
                activeSides = np.delete(activeSides, np.where(activeSides == side))
                activeMarginalPoints[side] = None

        for side, point in enumerate(activeMarginalPoints):
            if point is None:
                continue
            activeMarginalPoints[side] = point + 1/sideGradient[side]

        for side in np.where(Ymin == Y+1)[0]:
            activeSides = np.append(activeSides, side)
            activeMarginalPoints[side] = _getMinXWhereY(verts2d, Y+1)

    return img

    



def render(verts2d, faces, vcolors, depth, shade_t):
    """
        TODO
    """
    img = np.full( (conf.M, conf.N, 3) , conf.BACKGROUND)

    ## TODO sort faces by depth

    for face in faces:
        img = shade_triangle(
            img, 
            np.array([ verts2d[face[0]], verts2d[face[1]], verts2d[face[2]] ]),
            [ vcolors[face[0]], vcolors[face[1]], vcolors[face[2]] ],
            shade_t
        )

    return img



def _getMinXWhereY(verts2d, Y):
    """
        TODO
    """

    return np.amin(
        verts2d[
            np.where(verts2d[:,1] == Y)[0]
        ][:,0]
    )