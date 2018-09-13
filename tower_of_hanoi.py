import pygame
import game_function_for_hanoi
from displayboard import DisplayBoard
from pillar import Pillar
from pygame.sprite import Group
from tower_settings import Setting
from current_state import CurrentState


def run_hanoi():
    """主函数"""
    # 倒入配置文件
    pygame.init()
    ai_setting = Setting()
    # 现行状态参数类初始化
    state = CurrentState(ai_setting)
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption(ai_setting.screen_captions)
    # 柱子列表
    pillars = Group()
    # 显示面板
    show_board = DisplayBoard(screen, ai_setting, ai_setting.init_content)
    # 新建柱子
    if len(pillars) == 0:
        while len(pillars) < ai_setting.pillar_number:
            pillar = Pillar(ai_setting, screen, pillars)
            pillars.add(pillar)
            # 更新圆柱的x坐标
            state.update_x_pos(pillars)
    # 初始化圆盘栈
    game_function_for_hanoi.init_disk_stack(state, screen, ai_setting)
    # 运行递归
    game_function_for_hanoi. hanoi(state, 'one', 'two', 'three', ai_setting.disk_number)
    # 初始化圆盘栈
    state.clear_stack()
    state.pillars_top['one'] = ai_setting.pillar_pos_FarFromTop + ai_setting.pillar_height
    game_function_for_hanoi.init_disk_stack(state, screen, ai_setting)
    while True:
        game_function_for_hanoi.check_event()
        game_function_for_hanoi.update_screen(screen, ai_setting, pillars, state, show_board)


run_hanoi()


