import pygame
BLACK = (0,0,0)
 
class Player(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 

        self.image = pygame.image.load("ufo.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        
    def moveRight(self, pixels):
        self.rect.x += pixels
    
    def moveUp(self, pixels):
        self.rect.y -= pixels
        
    def moveDown(self, pixels):
        self.rect.y += pixels
 
class Moon(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 

        self.image = pygame.image.load("moon.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, ([width, height]))

        self.rect = self.image.get_rect()
        
        
