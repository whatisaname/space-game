import pygame, random, pygame_menu
from sprites import Player, Moon

pygame.init()

# Define some colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLACK = (0,0,0)


# Creating a screen
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("useless space game")

# Adding a background
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (800, 700))

# Creating a group for sprites
all_sprites_list = pygame.sprite.Group()

# Creating the sprites
moon = Moon(LIGHTBLUE, 100, 100)
moon.rect.x = random.randrange(0, 700)
moon.rect.y = random.randrange(0, 500)

player = Player(LIGHTBLUE, 100, 100)
player.rect.x = 400
player.rect.y = 300



all_sprites_list.add(player)
all_sprites_list.add(moon)



# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

carryOn = True
lose = False

speed = 5
score = 0

while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
    
    # Game Logic below
    all_sprites_list.update()
    screen.fill(DARKBLUE)
    screen.blit(background, (0,0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_x]:
        carryOn = False
    if keys[pygame.K_UP]:
        player.moveUp(speed)
    if keys[pygame.K_DOWN]:
        player.moveDown(speed)
    if keys[pygame.K_RIGHT]:
        player.moveRight(speed)
    if keys[pygame.K_LEFT]:
        player.moveLeft(speed)
    
    if player.rect.x > 800:
        lose = True
    
    if player.rect.x < -80:
        lose = True
    
    if player.rect.y < -80:
        lose = True

    if player.rect.y > 600:
        lose = True
        

    
    if player.rect.colliderect(moon.rect):
        score += 1
        speed += 1
        moon.rect.x = random.randrange(0, 700)
        moon.rect.y = random.randrange(0, 500)
        print(score)
    
    if lose == True:
        moon.kill()
        player.kill()
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", 1, WHITE)
        screen.blit(text, (250,300))
        text = font.render("Final Score: " + str(score), 1, WHITE)
        screen.blit(text, (200,250))
        pygame.display.flip()
        pygame.time.wait(3000)
        carryOn=False
    

    # Adding texts below 
    font = pygame.font.Font("font.otf", 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (420,3)) 
    text = font.render("Speed: " + str(speed), 1, WHITE)
    screen.blit(text, (230,3)) 



    # --- Go ahead and update the screen with what we've drawn.
    all_sprites_list.draw(screen)
    
    
    pygame.display.flip()
    
    # --- Limit to 120 frames per second
    clock.tick(120)
pygame.quit()
