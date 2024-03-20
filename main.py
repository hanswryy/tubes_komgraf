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
    
    # create the background
    bg.createBG()

    # prepare the crane tower
    # TODO: create a class for the crane tower

    primitif.basic.draw_margin(wid, hei, 20)
    t1 = tower.NewTowerFloor(700, 410, 100, 50)
    print(py5.get_pixels(750, 410).color())
    print(py5.get_pixels(751, 410).color())

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
