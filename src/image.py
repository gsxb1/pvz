# 实现图片类
import pygame

class Image(pygame.sprite.Sprite):
    def __init__(self, pathFmt, pathIndex, pos, size = None, pathIndexCount = 0):
        self.pathFmt = pathFmt
        self.pathIndex = pathIndex
        self.pos = list(pos)
        self.size = size
        self.pathIndexCount = pathIndexCount
        self.updateImage()

    def updateImage(self):
        path = self.pathFmt
        if self.pathIndexCount != 0:
            path = path % self.pathIndex
        self.image = pygame.image.load(path)
        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)

    def updateSize(self, size):
        self.size = size
        self.updateImage()

    def updateIndex(self, pathIndex):
        self.pathIndex = pathIndex
        self.updateImage()


    def getReact(self):
        # 获取图片本身的大小
        rect = self.image.get_rect()
        rect.x, rect.y = self.pos
        return rect

    def doLeft(self):
        self.pos[0] -= 0.3

    def draw(self, ds):
        # 绘制图像
        ds.blit(self.image, self.getReact())
