# 向日葵类
import objectbase
import sunlight
class SunFlower(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super(SunFlower, self).__init__(id, pos)
        self.hasSunLight = False

    def preSummon(self):
        self.hasSunLight = True

    def hasSummon(self):
        return self.hasSunLight

    def doSummon(self):
        if self.hasSummon():
            self.hasSunLight = False
            return sunlight.SunLight(2, (self.pos[0] + 20, self.pos[1] - 10))