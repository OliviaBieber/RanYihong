import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理从船上发射的子弹的类."""

    def __init__(self, ai_settings, screen, ship):
        """在飞船当前位置创建一个子弹对象."""
        super(Bullet, self).__init__()
        self.screen = screen

        # 创建矩形(0,0)，然后设置正确的位置。
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # 为子弹的位置存储一个十进制值。
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # 更新子弹的小数点位置。
        self.y -= self.speed_factor
        #更新矩形位置。
        self.rect.y = self.y

    def draw_bullet(self):
        """把子弹拉到屏幕上。"""
        pygame.draw.rect(self.screen, self.color, self.rect)
