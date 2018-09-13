class CurrentState:
    def __init__(self, setting):
        """用于保存现阶段的数据"""
        # 初始状态下三根柱子的最顶端
        self.pillars_top = {
            'one': setting.pillar_pos_FarFromTop + setting.pillar_height,
            'two': setting.pillar_pos_FarFromTop + setting.pillar_height,
            'three': setting.pillar_pos_FarFromTop + setting.pillar_height,
        }
        self.pillars_x_pos = {}
        # 三根柱子中的disk栈
        self.pillars_stack = {
            'one': [],
            'two': [],
            'three': []
        }
        # self.pillars_one = []
        # self.pillars_two = []
        # self.pillars_three = []
        self.someone_is_moving = False
        self.final_step = []
        self.current_step = 0
        self.move_done = False

    def update_x_pos(self, pillars):
        # 保存三个pillars的x轴坐标
        name_lists = ['one', 'two', 'three']
        index = 0
        for pillar in pillars:
            self.pillars_x_pos[name_lists[index]] = pillar.rect.centerx
            index += 1

    def clear_stack(self):
        """清空圆盘栈"""
        self.pillars_stack['one'].clear()
        self.pillars_stack['two'].clear()
        self.pillars_stack['three'].clear()
