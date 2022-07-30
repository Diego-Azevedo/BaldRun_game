import pygame
from game.UI.interface import Interface
from game.level import Level
from game.entity.player import Player  #Player sera instanciado aqui, assim
from game.entity.enemy import Enemy

class Control():
    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Bald Run")

        try:
            self.__maps = ['versao_final/game/maps/map1.json', 'versao_final/game/maps/map2.json', 'versao_final/game/maps/map3.json'] 

        except FileNotFoundError:  
            self.__maps = ['versao_final\game\maps\map1.json', 'versao_final\game\maps\map2.json', 'versao_final\game\maps\map3.json']

        self.last_key = ''
        self.__current_map = 0

        self.__gameLoop = True
        

        self.__clock = pygame.time.Clock()
        self.__FPS = 60
        self.display = pygame.display.set_mode([1024, 768])
        self.background = pygame.image.load('versao_final/game/image/background/background1.png')

        

        self.__object_group = pygame.sprite.Group()
        self.__enemyGroup = pygame.sprite.Group()
        self.__blockGroup = pygame.sprite.Group()
        self.__doorGroup = pygame.sprite.Group()
        self.__goldendoorGroup = pygame.sprite.Group()

        self.__python_groups = [self.__object_group, self.__enemyGroup, self.__blockGroup, self.__doorGroup, self.__goldendoorGroup]

        self.__player = Player(200,50,self.__object_group)
        self.__level = Level(self.__player, self.__maps[self.__current_map], self.__python_groups)
        
    def start(self):
        self.__gameLoop = True
        while self.__gameLoop:
            self.__clock.tick(self.__FPS)  
            #self.display.fill((0,0,0))
            self.display.blit(self.background, (0, 0))
            #display.blit(ImageFundo, (0, 0))
            self.__level.run()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__gameLoop = False

                  
                
                if event.type == pygame.KEYDOWN:     
                    if event.key == pygame.K_d:
                        self.__player.mover_direita()
                        self.last_key = 'D'                   
                    if event.key == pygame.K_a:
                        self.__player.mover_esquerda()
                        self.last_key = 'A'                    
                    if event.key == pygame.K_w:
                        self.__player.mover_cima()
                        self.last_key = 'W'                   
                    if event.key == pygame.K_s:
                        self.__player.mover_baixo()
                        self.last_key = 'S'  
                   

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.__player.velocidadeX = 0
                    if event.key == pygame.K_a:
                        self.__player.velocidadeX = 0
                    if event.key == pygame.K_w:
                        self.__player.velocidadeY = 0        
                    if event.key == pygame.K_s:
                        self.__player.velocidadeY = 0




                if self.__player.teste_colisao(self.__doorGroup):
                    self.__current_map = self.__current_map + 1
                    pygame.sprite.Group.empty(self.__blockGroup)
                    pygame.sprite.Group.empty(self.__doorGroup)
                    pygame.sprite.Group.empty(self.__enemyGroup)

                    self.__level = Level(self.__player, self.__maps[self.__current_map], self.__python_groups)
                    print(self.__current_map)
                




                elif self.__player.teste_colisao(self.__goldendoorGroup):

                    win_loop = True
                    while win_loop:
                        for event in pygame.event.get():   
                            if event.type == pygame.QUIT:
                                self.__gameLoop = False
                                win_loop = False

                        self.display.fill((207, 207, 196))
                        font = pygame.font.Font('freesansbold.ttf', 72)
                        win_text = font.render("Você ganhou!", True, (0, 170, 0))
                        self.display.blit(win_text, (275,350))
                        pygame.display.update()



                elif self.__player.teste_colisao(self.__enemyGroup):

                    defeat_loop = True
                    while defeat_loop:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                self.__gameLoop = False
                                defeat_loop = False
                                

                        self.display.fill((46, 46, 46))
                        font = pygame.font.Font('freesansbold.ttf', 72)
                        defeat_text = font.render("GAME OVER", True, (255, 0, 0))
                        self.display.blit(defeat_text, (275, 350))
                        pygame.display.update()
                    
                    

                

            self.colision()
            self.__player.update()
            pygame.display.update()
            self.__enemyGroup.update()

            





    def colision(self):
        if self.__player.teste_colisao(self.__blockGroup):
            if self.last_key == 'D':
                self.__player.velocidadeX = 0
                self.__player.intencao_pos[0] -= 3
            if self.last_key == 'A':
                self.__player.velocidadeX = 0
                self.__player.intencao_pos[0] += 3
            if self.last_key == 'W':
                self.__player.velocidadeY = 0
                self.__player.intencao_pos[1] += 3
            if self.last_key == 'S':
                self.__player.velocidadeY = 0
                self.__player.intencao_pos[1] -= 3





    @property
    def maps(self):
        return self.__maps

        
