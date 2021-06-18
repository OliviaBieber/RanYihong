import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """初始化飞船，并设置其起始位置."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像，并获得它的矩形。
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 在屏幕底部中心开始每艘新船。
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 为船的中心存储一个十进制值。
        self.center = float(self.rect.centerx)
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        
    def center_ship(self):
        """在屏幕上船的中央."""
        self.center = self.screen_rect.centerx
        
    def update(self):
        """根据移动标志更新船的位置。"""
        # 更新船的中心值，而不是矩形。
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # 从self.center更新rect对象。
        self.rect.centerx = self.center

    def blitme(self):
        """把船画在它现在的位置。."""
        self.screen.blit(self.image, self.rect)
