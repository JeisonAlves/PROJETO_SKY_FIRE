#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.constants import MOUSEMOTION
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import COLOR_BLUE, WIN_WIDTH, COLOR_YELLOW, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()  # select the menu image
        self.surf = pygame.transform.scale(self.surf, (800, 600))  # adjust the image for the window size
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.wav')  # select the music for the menu
        pygame.mixer_music.play(-1)  # play the music and -1 is to repeat


        while True:
            # DRAW THE GAME NAME AND THE TEXT MENU
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(150, "SKY", COLOR_BLUE, ((WIN_WIDTH / 2), 100))
            self.menu_text(150, "FIRE", COLOR_BLUE, ((WIN_WIDTH / 2), 220))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(50, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 430 + 35 * i))
                else:
                    self.menu_text(50, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 430 + 35 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Quit event
                    pygame.quit()  # Close Window
                    quit()  # end pygame

                if event.type == pygame.KEYDOWN: #Keydown event
                    if event.key == pygame.K_DOWN: # KEY DOWN
                        if menu_option < len(MENU_OPTION) -1: #while less than the maximum number of options
                            menu_option += 1 # go to the next option
                        else:
                            menu_option = 0 # return to first option

                    if event.key == pygame.K_UP:#Keydown event
                        if menu_option >0: #while greater than zero
                            menu_option -= 1 # go to the next option
                        else:
                            menu_option = len(MENU_OPTION) -1 # return to last option

                    if event.key == pygame.K_RETURN: #Enter event
                        return MENU_OPTION[menu_option]

                    #--------------IMPLEMENTAR EVENTOS DE MOUSE--------------

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Chiller", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
