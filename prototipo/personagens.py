import pygame
import math
import main
from equipamentos import *
from abc import ABC, abstractmethod



class Personagem(ABC, pygame.sprite.Sprite):
    def __init__(self, vida, dano, arma: Arma, *groups):
        super().__init__(*groups)
        self.__vida = vida
        self.__dano = dano
        self.__arma = arma


    @abstractmethod
    def update(self):
        pass

    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self,vida):
        self.__vida = vida

    @property
    def dano(self):
        return self.__dano
    @dano.setter
    def dano(self,dano):
        self.__dano = dano

    @property
    def arma(self):
        return self.__arma
    @arma.setter
    def arma(self, arma):
        return self.__arma




    def tomar_dano(self, qtdade_dano):
        self.__vida = self.__vida - qtdade_dano




class Player(Personagem):
    def __init__(self,vida ,dano ,arma, item: Item, *groups):
        super().__init__(vida,dano,arma, *groups)
        self.__item = Item

        self.image = pygame.image.load("arquivos/careca.png")  # carregando a imagem
        self.rect = pygame.Rect(40, 680, 20, 50)  # retangulo do player (posição x, y, altura, largura)
        self.velocidadeX = 0
        self.velocidadeY = 0
        self.intencao_pos = list(self.rect.center)

        #print(self.__vida)   #Erro aqui "AttributeError: 'Player' object has no attribute 'vida'"


    def tomar_dano(self,qtdade_dano):

        self.vida -= qtdade_dano
        if self.vida <= 0:
            main.menu_defeat()




    def update(self, *args):
        self.intencao_pos[0] += self.velocidadeX
        self.intencao_pos[1] += self.velocidadeY

    def mover_direita(self):
        if self.rect.right < 992:
            self.velocidadeX += 3
            self.intencao_pos[0] += self.velocidadeX

    def mover_esquerda(self):
        if self.rect.left > 32:
            self.velocidadeX -= 3
            self.intencao_pos[0] += self.velocidadeX

    def mover_cima(self):
        if self.rect.top > 40:
            self.velocidadeY -= 3
            self.intencao_pos[1] += self.velocidadeY

    def mover_baixo(self):
        if self.rect.bottom < 728:
            self.velocidadeY += 3
            self.intencao_pos[1] += self.velocidadeY

    def parar_horizontal(self):
        self.velocidadeX = 0
        if self.rect.left < 32:
            self.rect.left = 32

    def parar_vertical(self):
        self.velocidadeY = 0

    def autorizar_movimento(self):
        self.rect.center = self.intencao_pos

    def recusar_movimento(self):
        self.intecao_pos = list(self.rect.center)

    def teste_colisao(self, grupo):
        temp = self.rect.center
        self.rect.center = self.intencao_pos
        if not pygame.sprite.spritecollide(self, grupo, False):
            self.autorizar_movimento()

        else:
            self.rect.center = temp
            self.velocidadeX = 0
            self.velocidadeY = 0
            self.recusar_movimento()



class Enemy(Personagem):
    def __init__(self, vida, dano, arma, imagem, *groups):
        super().__init__(vida, dano, arma, *groups)

        self.image = imagem

        self.image = pygame.transform.scale(self.image, [20, 50])
        self.rect = self.image.get_rect()
        self.timer = 0


    def update(self,*args):
    # Comandos
        self.timer += 0.003
        self.rect.x = 512 + math.sin(self.timer) * 320

