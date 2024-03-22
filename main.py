import py5
import primitif.line
import primitif.basic
import primitif.utility
import primitif.transformasi
import primitif.matrix
import math
import config
import tower
import bg
import sys

wid = 1400
hei = 820

def setup():
    # set the window to be fullscreen
    py5.size(wid, hei)
    py5.color_mode(py5.RGB, 255, 255, 255, 255)
    
    sys.setrecursionlimit(1000000)

    # create the background
    bg.createBG()

    # prepare the crane tower
    # TODO: create a class for the crane tower

    primitif.basic.draw_margin(wid, hei, 20)
    # crane = tower.Crane()
    # t1 = tower.NewTowerFloor(700, 410, 20, 10)
    # iM = primitif.matrix.identity_matrix()
    # tm = primitif.transformasi.rotate2D(45, 0, 0, iM)
    # print(tm)
    # tm = primitif.transformasi.scale2D(.5,.5, 0, 0, tm)
    # print(tm)
    # tm = primitif.transformasi.translate2D(200,0, tm)
    # print(tm)
    # persegi2 = primitif.transformasi.transformPoints2D(persegi,tm)
    # primitif.basic.draw_bentuk(persegi2)

cc = 0

def draw():
    global cc
    if cc == 0:
        crane = tower.Crane()
        t1 = tower.NewTowerFloor(700, 410, 20, 10)
        cc = 1

def mouse_pressed():
    if py5.mouse_button == py5.LEFT:
        mx = py5.mouse_x
        my = py5.mouse_y
        c = py5.get_pixels(mx, my)
        print(py5.red(c), py5.green(c), py5.blue(c), py5.alpha(c))

py5.run_sketch()
