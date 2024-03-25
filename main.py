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

# 1. New tower floor on coordinate (700, 150) just below crane
# 2. Tower floor stop at y : 550

wid = 1400
hei = 820

move = False
grnd = None
crane = None

def setup():
    # set the window to be fullscreen
    py5.size(wid, hei)
    py5.color_mode(py5.RGB, 255, 255, 255, 255)
    # create the background
    bg.clearScreen()

    # prepare the crane tower
    # TODO: create a class for the crane tower

    primitif.basic.draw_margin(wid, hei, 20)

    # create the ground
    global grnd
    grnd = primitif.basic.persegi_panjang(700, 750, wid, 300)
    primitif.basic.draw_bentuk(grnd, [0,0,0,255])

    global crane
    crane = tower.Crane()
    t1 = tower.NewTowerFloor(700, 550)
    t1.draw()
    
    # iM = primitif.matrix.identity_matrix()
    # tm = primitif.transformasi.rotate2D(45, 0, 0, iM)
    # print(tm)
    # tm = primitif.transformasi.scale2D(.5,.5, 0, 0, tm)
    # print(tm)
    # tm = primitif.transformasi.translate2D(200,0, tm)
    # print(tm)
    # persegi2 = primitif.transformasi.transformPoints2D(persegi,tm)
    # primitif.basic.draw_bentuk(persegi2)

turn = False
fx = None

def draw():
    # clear the screen every frame
    bg.clearScreen()
    
    # move crane to the right, if it reach x = 1200, move it to left
    global turn
    if crane.shapes[0][0][0] > 1000:
        turn = True
    elif crane.shapes[0][0][0] < 400:
        turn = False
    if turn:
        crane.translateTo(-10, 0)
    else:
        crane.translateTo(10, 0)

    # move all floor down
    global move
    if move:
        tower.move_floors_down()
        groundDown()
        crane.drop()
    else:
        # draw all floors
        for f in tower.floors:
            f.draw()
        # draw the ground if floors < 4
        if len(tower.floors) < 4:
            primitif.basic.draw_bentuk(grnd, [0,0,0,255])
            
    # stop floors 
    if tower.floors[-1].y > 647:
        # game over if the fake floor x is not in the range of the last floor
        if fx < tower.floors[-1].x - 110 or fx > tower.floors[-1].x + 110:
            # send game over message with py5 text in the middle of the screen
            py5.text("Game Over", wid/2, hei/2)
            # pause the screen
            py5.no_loop()

        # create new tower floor based on fake floor
        t = tower.NewTowerFloor(fx, 550)
        t.draw()

        move = False
        # remove fake floor from shapes in crane
        crane.shapes.pop()
        # restore fake floor
        restoreFakeFloor()

def groundDown():
    global grnd
    iM = primitif.matrix.identity_matrix()
    tm = primitif.transformasi.translate2D(0, 3, iM)
    grnd = primitif.transformasi.transformPoints2D(grnd, tm)
    primitif.basic.draw_bentuk(grnd, [0,0,0,255])

# restore fake floor for crane
def restoreFakeFloor():
    crane.release = False
    fake_floor = primitif.basic.persegi_panjang(crane.x, 150, 110, 100)
    crane.shapes.append(fake_floor)

def mouse_pressed():
    if py5.mouse_button == py5.LEFT:
        # move all floor down
        global move
        move = True
        crane.releaseFloor()
        global fx
        fx = crane.x
        # only left 4 floors, delete the sooner
        if len(tower.floors) > 3:
            del tower.floors[0]

py5.run_sketch()
