import pygame, sys, time, random
from pygame.locals import *

pygame.init()

windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Paint")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

windowSurface.fill(WHITE)

info = pygame.display.Info()
sw = info.current_w
sh = info.current_h

x = y = 0

dx = 5
dy = 2


while True:

    pygame.draw.polygon(windowSurface,BLUE,((0+x,250+y),(120+x,120+y),(55+x,55+y)))
    pygame.draw.polygon(windowSurface,RED,((0+x,150+y),(85+x,85+y),(100+x,175+y),(0+x,150+y)))
    pygame.draw.line(windowSurface,BLACK,(60+x,85+y), (120+x, 110+x), 6)
    pygame.draw.circle(windowSurface, GREEN , (75+x,100+y), 13, 0)

    x += dx
    y += dy

    if x - dx < 0 or x + dx > sw:
        dx = -dx
    if y - dy < 0 or y + dy > sh:
        dy = -dy


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

