import pygame, sys, colors


class Button:

    def __init__(self, txt, location, action, argument, bg=colors.WHITE, fg=colors.BLACK,
                 size=(100, 50), font_name="Consolas", font_size=14):

        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size

        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action
        self.argument = argument

    def draw(self, screen):
        self.mouseover()

        self.surface.fill(self.bg)

        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        # Specify the color when the mouse cursor is over a button.
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = colors.CYAN

    def call_back(self):
        self.call_back_(self.argument)







