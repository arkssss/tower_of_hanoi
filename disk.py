import pygame


class Disk:
    def __init__(self, screen, setting, gap):
        self.setting = setting
        self.screen = screen
        self.width = setting.disk_max_width - gap
        self.height = setting.disk_height
        self.order_number = 0
        # 建立矩形
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.not_reach_top = True
        self.not_reach_edge = True
        self.not_reach_bottom = True
        # 移动状态
        self.moving_active = False

    def init_pos(self, pillar_num, current_state):
        """确定圆盘的初始位置"""
        self.rect.centerx = current_state.pillars_x_pos[pillar_num]
        self.rect.bottom = current_state.pillars_top[pillar_num]

    def draw_disk(self, current_state):
        """绘制圆盘"""
        self.update_disk(current_state)
        # 如果圆盘移动处于激活状态，且没人移动,则移动
        # if self.moving_active:
        #     self.move_disk('one', 'two', current_state)
        pygame.draw.rect(self.screen, self.setting.disk_bg, self.rect)

    def update_disk(self, current_state):
        """"""
        pass

    def move_disk(self, from_direction, to_direction, current_state):
        # 将盘子从from_direction移到to_direction
        # 先移动到上方
        # 从外部调用则激活
        current_state.someone_is_moving = True
        if not self.moving_active:
            self.moving_active = True
        if self.not_reach_top:
            self.rect.top -= self.setting.disk_move_speed
            if self.rect.top <= self.setting.move_pos_FarFromTop:
                self.rect.top = self.setting.move_pos_FarFromTop
                self.not_reach_top = False
            return
        # 再水平移动
        if self.not_reach_edge:
            if current_state.pillars_x_pos[to_direction] > current_state.pillars_x_pos[from_direction]:
                self.rect.centerx += self.setting.disk_move_speed
                if self.rect.centerx >= current_state.pillars_x_pos[to_direction]:
                    self.rect.centerx = current_state.pillars_x_pos[to_direction]
                    self.not_reach_edge = False
            else:
                self.rect.centerx -= self.setting.disk_move_speed
                if self.rect.centerx <= current_state.pillars_x_pos[to_direction]:
                    self.rect.centerx = current_state.pillars_x_pos[to_direction]
                    self.not_reach_edge = False
            return
        # 再向下移动
        if self.not_reach_bottom:
            self.rect.bottom += self.setting.disk_move_speed
            if self.rect.bottom >= current_state.pillars_top[to_direction]:
                self.rect.bottom = current_state.pillars_top[to_direction]
                self.not_reach_bottom = False
            return

        # 移动结束 重置参数
        self.not_reach_edge = True
        self.not_reach_top = True
        self.not_reach_bottom = True
        self.moving_active = False
        current_state.someone_is_moving = False

