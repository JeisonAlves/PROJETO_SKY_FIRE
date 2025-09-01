import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import COLOR_BLUE, WIN_WIDTH, COLOR_YELLOW, MENU_OPTION, COLOR_WHITE, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Menu:
    def __init__(self, window):
        # Menu image list
        self.window = window
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('MenuBg'))

    # Text definitions
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Chiller", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.wav')  # to set the menu music
        pygame.mixer_music.play(-1)  # to play and repeat the music

        while True:
            # For menu background parallax run
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            # Draw the name of the game on the screen
            self.menu_text(150, "SKY", COLOR_BLUE, (WIN_WIDTH / 2, 120))
            self.menu_text(150, "FIRE", COLOR_BLUE, (WIN_WIDTH / 2, 240))

            # Draw the menu options
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(50, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 400 + 35 * i))
                else:
                    self.menu_text(50, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 400 + 35 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():  # Quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:  # Keyboard events
                    if event.key == pygame.K_DOWN:  # key up pressed
                        menu_option = (menu_option + 1) % len(MENU_OPTION) # return to first option

                    if event.key == pygame.K_UP:  # Key down pressed
                        menu_option = (menu_option - 1) % len(MENU_OPTION) # return to last option

                    if event.key == pygame.K_RETURN:  # Enter key pressed
                        return MENU_OPTION[menu_option]
