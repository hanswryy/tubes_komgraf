# this is class for moving crane tower
import primitif.line
import primitif.basic
import primitif.utility
import primitif.transformasi
import primitif.matrix

class NewTowerFloor:
    def __init__(self, x, y, panjang, lebar):
        self.x = x
        self.y = y
        self.panjang = panjang
        self.lebar = lebar
        self.draw()

    def draw(self):
        pp = primitif.basic.persegi_panjang(self.x, self.y, self.panjang, self.lebar)
        primitif.basic.draw_bentuk(pp)