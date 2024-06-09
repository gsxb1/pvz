# 豌豆射手类
import objectbase
import peabullet
class PeaShooter(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super(PeaShooter, self).__init__(id, pos)
        self.haspeabullet = False

    def preSummon(self):
        self.haspeabullet = True

    def hasSummon(self):
        return self.haspeabullet

    def doSummon(self):
        if self.hasSummon():
            self.haspeabullet = False
            return peabullet.PeaBullet(0, (self.pos[0] + 20, self.pos[1] + 50))