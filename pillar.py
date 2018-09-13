import pygame
from pygame.sprite import Sprite


class Pillar(Sprite):
    def __init__(self, ai_setting, screen, pillars):
        """柱子的初始化"""
        super().__init__()
        self.setting = ai_setting
        # 关于屏幕的参数
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 初始化柱子的参数
        self.width = self.setting.pillar_width
        self.height = self.setting.pillar_height
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # 计算每个柱子的间隔 (number+1)*x + number*width = screen.width
        self.gap = int((self.screen_rect.width - self.setting.pillar_number * self.rect.width)/(self.setting.pillar_number + 1))
        # 计算此时的位置
        current_pillar = len(pillars)
        # 结果为 0 1 2 ..... pillar_number - 1
        # x y 分别表示矩形左上角顶点的坐标
        pillar_order = current_pillar % self.setting.pillar_number
        self.x = (pillar_order + 1) * self.gap + pillar_order * self.width
        self.y = self.setting.pillar_pos_FarFromTop
        # 更新圆柱位置
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_pillar(self):
        """画出pillar"""
        pygame.draw.rect(self.screen, self.setting.pillar_bg, self.rect)
