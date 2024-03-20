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

wid = 1400
hei = 820

def setup():
    # set the window to be fullscreen
    py5.size(wid, hei)
    py5.color_mode(py5.RGB, 255, 255, 255, 255)

    # create the background
    bg.createBG()

    # prepare the crane tower
    # TODO: create a class for the crane tower

    primitif.basic.draw_margin(wid, hei, 20)
    crane = tower.Crane()
    t1 = tower.NewTowerFloor(700, 410, 100, 50)
    c = py5.get_pixels(750, 411)
    print(round(py5.red(c)*255/74), round(py5.green(c)*255/74), round(py5.blue(c)*255/74), c, "\n", py5.color(0, 0, 0, 255))

    # iM = primitif.matrix.identity_matrix()
    # tm = primitif.transformasi.rotate2D(45, 0, 0, iM)
    # print(tm)
    # tm = primitif.transformasi.scale2D(.5,.5, 0, 0, tm)
    # print(tm)
    # tm = primitif.transformasi.translate2D(200,0, tm)
    # print(tm)
    # persegi2 = primitif.transformasi.transformPoints2D(persegi,tm)
    # primitif.basic.draw_bentuk(persegi2)
    

def draw():
    pass

py5.run_sketch()
