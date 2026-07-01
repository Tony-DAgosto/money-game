import pygame
from sys import exit

pygame.init()

# CONSTANTS
WORLD_WIDTH = 5000
WORLD_HEIGHT = 5000
screen = pygame.display.set_mode((1600,1000), pygame.RESIZABLE)
clock = pygame.time.Clock()
player_rect = pygame.Rect((WORLD_WIDTH // 2,WORLD_HEIGHT // 2,65,65))
speed = 8

landmark_list = [
    pygame.Rect(400, 400, 100, 100),
    pygame.Rect(500, 1400, 100, 100),
    pygame.Rect(375, 2900, 100, 100),
    pygame.Rect(675, 3400, 100, 100),
    pygame.Rect(800, 4700, 100, 100),
    pygame.Rect(1650, 400, 100, 100),
    pygame.Rect(2250, 1700, 100, 100),
    pygame.Rect(3650, 2200, 100, 100),
    pygame.Rect(4400, 900, 100, 100),
    pygame.Rect(1650, 3300, 100, 100),
    pygame.Rect(2650, 2650, 100, 100),
    pygame.Rect(3050, 700, 100, 100),
    pygame.Rect(4200, 4650, 100, 100),
    pygame.Rect(3700, 3950, 100, 100),
    pygame.Rect(4800, 4700, 100, 100)
]

pygame.display.set_caption("Money Game")
# Game Loop
while True:
    # **EVENT PHASE**
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # **UPDATE PHASE**
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()

    # Player movement
    if keys[pygame.K_LSHIFT]:
        speed = 4
    else:
        speed = 8
   # HORIZONTAL PLAYER MOVEMENT
    if keys[pygame.K_a]:
        player_rect.x -= speed
    if keys[pygame.K_d]:
        player_rect.x += speed

    

    # RESOLVE PLYR HORIZ MVMNT
    for landmark in landmark_list:
        if player_rect.colliderect(landmark) and (keys[pygame.K_a] or keys[pygame.K_d]):
            if player_rect.x > landmark.x:
                player_rect.left = landmark.right
            if player_rect.x < landmark.x:
                player_rect.right = landmark.left

    # VERTICAL PLAYER MOVEMENT
    if keys[pygame.K_w]:
        player_rect.y -= speed
    if keys[pygame.K_s]:
        player_rect.y += speed

    # RESOLVE PLYR VERT MVMNT
    for landmark in landmark_list:
        if player_rect.colliderect(landmark) and (keys[pygame.K_w] or keys[pygame.K_s]):
            if player_rect.y > landmark.y:
                player_rect.top = landmark.bottom
            if player_rect.y < landmark.y:
                player_rect.bottom = landmark.top
            
    player_rect.clamp_ip(pygame.Rect(0,0,WORLD_WIDTH,WORLD_HEIGHT))

    camera_x = player_rect.centerx - (screen.get_width() // 2)
    camera_y = player_rect.centery - (screen.get_height() // 2)

    # Keeps camera from showing black void
    camera_x = max(0, min(camera_x, WORLD_WIDTH - screen.get_width()))
    camera_y = max(0, min(camera_y, WORLD_HEIGHT - screen.get_height()))

    # **DRAW PHASE**
    screen.fill((75, 140, 45))

    for landmark in landmark_list:
        draw_landmark = landmark.move(-camera_x, -camera_y)
        pygame.draw.rect(screen, 'Gray60', draw_landmark)
        

    draw_player_rect = player_rect.move(-camera_x, -camera_y)
    pygame.draw.rect(screen, 'Brown4', draw_player_rect)

    # Updates the screen with anything changed by user events
    pygame.display.update()

    # Tells game loop to only run 60 times per second
    clock.tick(60)
