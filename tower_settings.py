class Setting:
    def __init__(self):
        """初始化设置"""
        # 关于屏幕
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg = (200, 200, 200)
        self.screen_captions = "hanoi塔问题"
        # 关于柱子
        self.pillar_width = 20
        self.pillar_height = 400
        self.pillar_bg = (100, 25, 25)
        self.pillar_number = 3
        self.pillar_pos_FarFromTop = 300
        # 关于盘子
        self.disk_max_width = 200
        self.disk_height = 10
        self.disk_bg = (10, 10, 10)
        self.move_pos_FarFromTop = 200
        self.disk_move_speed = 1000
        self.disk_width_gap = 10
        self.disk_number = 10
        # 关于字体
        self.font_color = (100, 100, 100)
        self.init_content = "Already Moved: "+str(0)+" Times"


