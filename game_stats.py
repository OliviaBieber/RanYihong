class GameStats():
    """追踪外星人入侵的统计数据."""
    
    def __init__(self, ai_settings):
        """初始化数据。"""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # 以非活动状态开始游戏。
        self.game_active = False
        
        # 高分不应该被重置。
        self.high_score = 0
        
    def reset_stats(self):
        """初始化在游戏过程中可能改变的统计数据."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
