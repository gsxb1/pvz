# 游戏的主逻辑
import pygame
import image
import sunflower
from const import *


class Game(object):
    def __init__(self, ds):
        self.ds = ds
        self.back = image.Image("../pic/other/back.png", 0, (0, 0), GAME_SIZE, 0)
        self.plants = []  # 向日葵列表
        self.summons = []  # 召唤物列表
        self.hasPlant = []
        for i in range(GAME_COUNT[0]):
            col = []
            for j in range(GAME_COUNT[1]):
                col.append(0)
            self.hasPlant.append(col)

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
            if plant.hasSummon():  # 如果植物身上有召唤物
                summon = plant.doSummon()  # 我来创建一个对象
                self.summons.append(summon)  # 由我的表格来管理
        for summon in self.summons:
            summon.update()

    def getIndexByPos(self, pos):
        x = (pos[0] - LEFT_TOP[0]) // GRID_SIZE[0]
        y = (pos[1] - LEFT_TOP[1]) // GRID_SIZE[1]
        return x, y

    def addSunFlower(self, x, y):
        if self.hasPlant[x][y] == 1:
            return
        self.hasPlant[x][y] = 1
        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]
        sf = sunflower.SunFlower(SUNFLOWER_ID, pos)
        self.plants.append(sf)

    def cheackLooct(self, mousePos):
        # 捡阳光
        # 遍历召唤物，查看他们可不可以拾取，获取召唤物的矩形，检查鼠标是否点击
        for summon in self.summons:
            if not summon.canLoot():
                continue
            rect = summon.getReact()
            if rect.collidepoint(mousePos):
                self.summons.remove(summon)
                return True
        return False


    def checkAddPlant(self, mousePos, objId):
        # 添加植物，获取鼠标点击位置，添加可种植植物的限制
        x, y = self.getIndexByPos(mousePos)
        if x < 0 or x >= GAME_COUNT[0]:
            return
        if y < 0 or y >= GAME_COUNT[1]:
            return
        if objId == SUNFLOWER_ID:
            self.addSunFlower(x, y)

    def mouseClickHandler(self, btn):
        mousePos = pygame.mouse.get_pos()
        if self.cheackLooct(mousePos):
            # 如果拾取了阳光，那就不能进行种植逻辑
            return
        if btn == 1:
            self.checkAddPlant(mousePos, SUNFLOWER_ID)

