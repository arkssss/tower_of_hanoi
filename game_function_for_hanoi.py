import sys
import pygame
from disk import Disk


def check_event():
    """桌面的事件监听函数"""
    # 必须要加关闭事件，否则会卡死
    for event in pygame.event.get():
        # 关闭事件
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(screen, ai_setting, pillars, current_state, show_board):
    """桌面刷新函数"""
    screen.fill(ai_setting.screen_bg)
    show_board.draw_board()
    # 绘制柱子
    for pillar in pillars:
        pillar.draw_pillar()
    # 绘制圆盘
    draw_disks(current_state)
    # 按步骤绘制
    draw_by_step(current_state, show_board)
    pygame.display.flip()


def init_disk_stack(current_state, screen, setting):
    """初始化柱子栈，默认在第一个柱子"""
    while len(current_state.pillars_stack['one']) < setting.disk_number:
        # gap为盘子宽度差
        gap = len(current_state.pillars_stack['one']) * setting.disk_width_gap
        disk = Disk(screen, setting, gap)
        disk.init_pos('one', current_state)
        # 圆盘的底部等于柱子的顶部
        disk.rect.bottom = current_state.pillars_top['one']
        # 更新状态类的第一个柱子最顶端的像素
        current_state.pillars_top['one'] -= setting.disk_height
        # 给盘子编号
        disk.order_number = setting.disk_number - len(current_state.pillars_stack['one'])
        current_state.pillars_stack['one'].append(disk)


def draw_disks(current_state):
    """画圆盘组"""
    for disk in current_state.pillars_stack['one']:
        disk.draw_disk(current_state)
    for disk in current_state.pillars_stack['two']:
        disk.draw_disk(current_state)
    for disk in current_state.pillars_stack['three']:
        disk.draw_disk(current_state)


def hanoi(current_state, from_pillar, help_pillar, to_pillar, n):

    if n == 1:
        index = find_disk(current_state, from_pillar, n)
        if index is not None:
            # if not current_state.someone_is_moving:
                # current_state.pillars_stack[from_pillar][index].move_disk(from_pillar, to_pillar, current_state)
                # 入栈出栈操作
            # 移动
            step = {
                'number': n,
                'from': from_pillar,
                'to': to_pillar
            }
            current_state.final_step.append(step)
            current_state.pillars_stack[to_pillar].append(current_state.pillars_stack[from_pillar].pop())
    else:
        hanoi(current_state, from_pillar, to_pillar, help_pillar, n-1)
        index = find_disk(current_state, from_pillar, n)
        if index is not None:
            # if not current_state.someone_is_moving:
                # current_state.pillars_stack[from_pillar][index].move_disk(from_pillar, to_pillar, current_state)
                # 入栈出栈操作
            # 移动
            # 移动
            step = {
                'number': n,
                'from': from_pillar,
                'to': to_pillar
            }
            current_state.final_step.append(step)
            current_state.pillars_stack[to_pillar].append(current_state.pillars_stack[from_pillar].pop())
        hanoi(current_state, help_pillar, from_pillar, to_pillar, n-1)


def find_disk(current_state, pillar, order_number):
    """从pillar中找到编号为order_number的disk"""
    # print("123")
    # print(current_state.pillars_stack[pillar])
    # for index, disk in current_state.pillars_stack[pillar]:
    #     if disk.order_number == order_number:
    #         return index
    length = len(current_state.pillars_stack[pillar])
    index = 0
    while index < length:
        if current_state.pillars_stack[pillar][index].order_number == order_number:
            return index
        index += 1


def draw_by_step(current_state, show_board):
    """按保存的路径绘制"""
    length = len(current_state.final_step)
    # print(current_state.final_step[0])
    if length:
        order_number = current_state.final_step[0]["number"]
        from_dire = current_state.final_step[0]["from"]
        to_dire = current_state.final_step[0]["to"]
        index = find_disk(current_state, from_dire, order_number)
        current_state.pillars_stack[from_dire][index].move_disk(from_dire, to_dire, current_state)
        # 此时移动结束
        if current_state.someone_is_moving is False:
            # current_state.pillars_stack[from_dire]
            current_state.current_step += 1
            show_board.update_board("Already Moved: "+str(current_state.current_step)+" Times")
            current_state.pillars_stack[to_dire].append(current_state.pillars_stack[from_dire][index])
            current_state.pillars_top[to_dire] -= current_state.pillars_stack[from_dire][index].rect.height
            current_state.pillars_top[from_dire] += current_state.pillars_stack[from_dire][index].rect.height
            current_state.final_step.pop(0)
    else:
        # 移动结束
        show_board.update_board("Done !" +
                                "Total Moved: "+str(current_state.current_step)+" Times")
        current_state.move_done = True




