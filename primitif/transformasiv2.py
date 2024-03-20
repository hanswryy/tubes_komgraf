import numpy as np
import math

def translate2D(tx, ty, tm):
    pass

def scale2D(sx, sy, refx, refy, tm):
    pass

def rotate2D(a, refx, refy):
    pass

def transformPoints2D(pts, tm):
    i, _  = pts.shape
    
    for k in range(i):
        tmp = tm[0][0] * pts[k,0] + tm[0][1] * pts[k,1] + tm[0][2]
        pts[k,1] = tm[1][0] * pts[k,0] + tm[1][1] * pts[k,1] + tm[1][2]
        pts[k,0] = tmp

    return pts