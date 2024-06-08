# 游戏的主逻辑
import pygame
import image
import sunflower
import data_object
from const import *


class Game(object):
    def __init__(self, ds):
        self.ds = ds
        self.back = image.Image("../pic/other/back.png", 0, (0, 0), GAME_SIZE, 0)
        self.plants = []    # 向日葵列表
        self.summons = []   # 召唤物列表
        self.hasPlant = []  # 掌控植物生成的哈希表
        self.gold = 100     # 金币数量
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
        print('gold: ', self.gold)
        self.back.update()
        for plant in self.plants:
            plant.update()
            if plant.hasSummon():  # 如果植物身上有召唤物
                summon = plant.doSummon()  # 我来创建一个对象
                self.summons.append(summon)  # 由我的表格来管理
        for summon in self.summons:
            summon.update()

    def getIndexByPos(self, pos):
        # 获取鼠标相对于花园的位置
        x = (pos[0] - LEFT_TOP[0]) // GRID_SIZE[0]
        y = (pos[1] - LEFT_TOP[1]) // GRID_SIZE[1]
        return x, y

    def addSunFlower(self, x, y):
        # 种植物，检测并修改哈希表的数值，将位置添加到向日葵列表
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
                self.gold += summon.getPrice()
                return True
        return False

    def checkAddPlant(self, mousePos, objId):
        # 检测是否可以种植植物，获取鼠标点击位置，添加可种植植物的位置限制，检测现在的金币数量是否能种植物
        x, y = self.getIndexByPos(mousePos)
        if x < 0 or x >= GAME_COUNT[0]:
            return
        if y < 0 or y >= GAME_COUNT[1]:
            return
        if self.gold < data_object.data[objId]["PRICE"]:
            return
        self.gold -= data_object.data[objId]["PRICE"]
        if objId == SUNFLOWER_ID:
            self.addSunFlower(x, y)

    def mouseClickHandler(self, btn):
        # 获取鼠标点击,bin的值为0代表左键，为1代表右键。获取鼠标位置
        mousePos = pygame.mouse.get_pos()
        if self.cheackLooct(mousePos):
            # 如果拾取了阳光，那就不能进行种植逻辑
            return
        if btn == 1:
            self.checkAddPlant(mousePos, SUNFLOWER_ID)

