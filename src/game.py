# 游戏的主逻辑
import image
import sunflower
from const import *

class Game(object):
    def __init__(self, ds):
        self.ds = ds
        self.back = image.Image("../pic/other/back.png", 0 ,(0,0), GAME_SIZE, 0)
        self.plants = []           #向日葵列表
        self.summons = []          #召唤物列表
        for i in range(GAME_COUNT[0]):
            for j in range(GAME_COUNT[1]):
                pos = LEFT_TOP[0] + i * GRID_SIZE[0], LEFT_TOP[1] + j * GRID_SIZE[1]
                sf = sunflower.SunFlower(3, pos)
                self.plants.append(sf)


    def draw(self):
        self.back.draw(self.ds)
        for plant in self.plants:
            plant.draw(self.ds)
        for summon in self.summons:
            summon.draw(self.ds)

    def update(self):
        self.back.update()
        for plant in self.plants:
            plant.update()
            if plant.hasSummon():                   #如果植物身上有召唤物
                summon = plant.doSummon()           #我来创建一个对象
                self.summons.append(summon)         #由我的表格来管理
        for summon in self.summons:
            summon.update()


