#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image

from code.Const import WIN_WIDTH, WIN_HEIGHT


class Entity(ABC): #Abstract class
    def __init__(self,name:str,position:tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/'+name+'.png').convert_alpha() #load the image from asset folder
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH,WIN_HEIGHT)) #resizes the image to the size of the window
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass
