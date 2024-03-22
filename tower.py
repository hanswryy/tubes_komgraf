# this is class for moving crane tower
import primitif.line
import primitif.basic
import primitif.utility
import primitif.transformasi
import primitif.matrix

class Crane:
    def __init__(self):
        self.draw()
    
    def draw(self):
        pass

class NewTowerFloor:
    def __init__(self, x, y, panjang, lebar):
        self.x = x
        self.y = y
        self.panjang = panjang
        self.lebar = lebar
        self.draw()

    def draw(self):
        pp = primitif.basic.persegi_panjang(self.x, self.y, self.panjang, self.lebar)
        # c as fill color
        c = [255, 0, 0, 255]
        # bd as boundary color (which is black)
        bd = [0,0,0,255]
        primitif.basic.draw_bentuk(pp, bd)
        primitif.basic.fillShape2(700, 410, c, 700+(int(self.panjang/2)), self.y)