import sys, pygame, time
from params import *
import game_classes
from math import cos, sin, pi

def rotate_copy_blit(surf, angle):
    new_surfs = []
    a = pi * angle / 180
    alpha = a / 2
    d_alpha = angle // 2
    screen.fill(black)
    for _ in range(360 // angle):
        new_surf = pygame.transform.rotate(surf, d_alpha)
        #new_surf.fill(white)
        new_rect = new_surf.get_rect()
        new_rect.center = ((400 + 200 * cos(alpha),
                            400 - 200 * sin(alpha)))
        screen.blit(new_surf, new_rect)
        alpha += a
        d_alpha += angle

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
screen.fill(black)
current = game_classes.Particle(400, 150)
surf = pygame.Surface((400, 300))
surf.set_colorkey(green)
surf.fill(green)

snowflake = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    surf.fill(green)
    if current.finished or current.intersect(snowflake):
        snowflake.append(current)
        current = game_classes.Particle(400, 150)
    else:
        current.update()
    new_surf = surf
    current.draw(new_surf, white)
    for dot in snowflake:
        dot.draw(new_surf, white)
    #surf_list = rotate_copy(surf, (400, 400), 200, 60)
    #for new_surf in surf_list:
    #    screen.blit(new_surf[0], new_surf[1])
    #screen.blit(pygame.transform.flip(surf, False, True), (400, 300))
    rotate_copy_blit(new_surf, 60)
    pygame.display.update()
    #clock.tick(60)
