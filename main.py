import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1600,1000), pygame.RESIZABLE)
pygame.display.set_caption("Money Game")
clock = pygame.time.Clock()

player_rect = pygame.Rect((400,400,65,65))
speed = 8.5

# Game Loop
while True:
    # **EVENT PHASE**
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()
    
    # Player movement
    if keys[pygame.K_LSHIFT]:
        speed = 4
    else:
        speed = 8.5
    if keys[pygame.K_w]:
        player_rect.y -= speed
    if keys[pygame.K_a]:
        player_rect.x -= speed
    if keys[pygame.K_s]:
        player_rect.y += speed
    if keys[pygame.K_d]:
        player_rect.x += speed
        
    screen.fill((75, 140, 45))
    pygame.draw.rect(screen, 'Brown4', player_rect)
    player_rect.clamp_ip(screen.get_rect())

    # Updates the screen with anything changed by user events
    pygame.display.update()

    # Tells game loop to only run 60 times per second
    clock.tick(60)

