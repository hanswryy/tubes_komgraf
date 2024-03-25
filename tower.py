# this is class for moving crane tower
import primitif.line
import primitif.basic
import primitif.utility
import primitif.transformasi
import primitif.matrix
import bg

floors = []

# move all floor in floors down with transformasi.translate2D
def move_floors_down():
    for f in floors:
        f.translateTo(0, 3)

class Crane:
    shapes = []
    release = False
    x = 700

    def __init__(self):
        self.draw()
    
    def draw(self):
        # draw rectangle on top
        pp = primitif.basic.persegi_panjang(700, 25, 30, 100)
        bd = [0,0,0,255]
        primitif.basic.draw_bentuk(pp, bd)
        self.shapes.append(pp)

        sg = primitif.basic.segitiga(700, 125, 75, 50)
        self.shapes.append(sg)

        # rotate sg 180 degree
        iM = primitif.matrix.identity_matrix()
        tm = primitif.transformasi.rotate2D(180, 700, 100, iM)
        sg = primitif.transformasi.transformPoints2D(sg, tm)

        primitif.basic.draw_bentuk(sg, bd)

        # draw a circle on top of sg and pp
        circ = primitif.basic.lingkaran(700, 65, 5)
        primitif.basic.draw_bentuk(circ, bd)
        self.shapes.append(circ)

        # draw fake floor
        fake_floor = primitif.basic.persegi_panjang(700, 150, 110, 100)
        primitif.basic.draw_bentuk(fake_floor, bd)
        self.shapes.append(fake_floor)

    # function to translate all shape in shapes
    def translateTo(self, tx, ty):
        self.x += tx
        for s in self.shapes:
            # skip fake floor if release is true
            if self.release and s is self.shapes[-1]:
                continue
            iM = primitif.matrix.identity_matrix()
            tm = primitif.transformasi.translate2D(tx, ty, iM)
            s = primitif.transformasi.transformPoints2D(s, tm)
            primitif.basic.draw_bentuk(s)
    
    # release the fake floor
    def releaseFloor(self):
        self.release = True

    def drop(self):
        iM = primitif.matrix.identity_matrix()
        tm = primitif.transformasi.translate2D(0, 12, iM)
        self.shapes[-1] = primitif.transformasi.transformPoints2D(self.shapes[-1], tm)
        primitif.basic.draw_bentuk(self.shapes[-1])

class NewTowerFloor:
    pp = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        floors.append(self)

    def draw(self):
        self.pp = primitif.basic.persegi_panjang(self.x, self.y, 110,100)
        bd = [0,0,0,255]
        primitif.basic.draw_bentuk(self.pp, bd)

    def translateTo(self, tx, ty):
        # update x and y
        self.x += tx
        self.y += ty

        # translate the points
        iM = primitif.matrix.identity_matrix()
        tm = primitif.transformasi.translate2D(tx, ty, iM)
        self.pp = primitif.transformasi.transformPoints2D(self.pp, tm)
        primitif.basic.draw_bentuk(self.pp)
