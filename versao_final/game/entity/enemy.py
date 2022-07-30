import pygame
import math
from game.entity.character import Character
import random
class Enemy(Character):
    def __init__(self,pos, vida, dano,  *groups):
        super().__init__(vida, dano, *groups)

        self.__pos = pos

        try:
            self.image = pygame.image.load("versao_final/game/image/Enemy/enemy.png")  # carregando a imagem
        except FileNotFoundError:
            self.image = pygame.image.load("versao_final\game\image\Enemy\enemy.png") 
        self.rect = self.image.get_rect(topleft = self.__pos)
        self.__timer = 0
        self.__randpos = random.randint(200,400)
    def update(self,*args):
        self.__timer += 0.01
        self.rect.x = self.__pos[0] + math.sin(self.__timer)**3 * self.__randpos
        self.rect.y = self.__pos[1] + math.cos(self.__timer)**3 * self.__randpos
        