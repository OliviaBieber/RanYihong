import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化pygame、设置和屏幕对象。
    pygame.init()#初始化背景设置
    ai_settings = Settings()#全局设置
    screen = pygame.display.set_mode( #创建screen显示窗口
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")#标题
    
    # 制作播放按钮。
    play_button = Button(ai_settings, screen, "Play")
    
    # 创建一个实例来存储游戏统计数据和计分板。
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    
    #造一艘船，一堆子弹，一群外星人。
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # 创造外星人舰队。
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 启动游戏的主循环。
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
            aliens, bullets)
        
        if stats.game_active:
            #移动飞船
            ship.update()
            #更新子弹位置
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                bullets)
            #更新外星人
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                bullets)
        #更新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
            bullets, play_button)

run_game()
