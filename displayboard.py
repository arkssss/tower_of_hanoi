import pygame


class DisplayBoard:
    def __init__(self, screen, ai_setting, display_content=""):
        self.screen_bg = ai_setting.screen_bg
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.SysFont(None, 48)
        self.font_color = ai_setting.font_color
        self.display_content = display_content
        self.prep_dis()

    def prep_dis(self):
        content = str(self.display_content)
        self.content_image = self.font.render(content, True, self.font_color, self.screen_bg)
        self.rect = self.content_image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top + 20

    def draw_board(self):
        self.screen.blit(self.content_image, self.rect)

    def update_board(self, dis_content):
        self.display_content = dis_content
        self.prep_dis()


