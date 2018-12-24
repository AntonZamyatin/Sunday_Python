import sys, pygame, time
from params import *
import game_classes

pygame.init()

screen = pygame.display.set_mode(SIZE)
screen.fill(black)

Field = game_classes.Field(screen, F_SIZE, CELL_WIDTH)
start = False

f = pygame.font.Font("ZCOOLXiaoWei-Regular.ttf", 20)
text1 = f.render("John Conway`s", True, green)
text2 = f.render("LIFE", True, green)
text3 = f.render("start/stop - SPACE", True, green)
text4 = f.render("mouse to sow a life", True, green)

last = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEMOTION or\
           event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] < F_SIZE[0] and\
               pygame.mouse.get_pos()[1] < F_SIZE[1]:
               if pygame.mouse.get_pressed()[0]:
                   Field.mouse_fill(* pygame.mouse.get_pos(), 33)
               elif pygame.mouse.get_pressed()[2]:
                   Field.mouse_fill(* pygame.mouse.get_pos(), 0)
        if event.type == pygame.KEYDOWN and\
           pygame.key.get_pressed()[pygame.K_SPACE]:
            start = not start
            if start:
                print("Start")
            else:
                print("Stop")

    if start and pygame.time.get_ticks() - last > DELAY:
        last = pygame.time.get_ticks()
        Field.update()

    Field.draw()
    screen.blit(text1, (605, 10))
    screen.blit(text2, (605, 40))
    screen.blit(text3, (605, 500))
    screen.blit(text4, (605, 540))
    pygame.display.update()
