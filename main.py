import pygame
from settings import *
from map import Map
from player import Player
from raycaster import Raycaster

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

map = Map()
player = Player()

clock = pygame.time.Clock()
raycaster = Raycaster(player, map)
background_image = pygame.image.load("background.png")


while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player.update()
    raycaster.castAllRays()

    screen.blit(background_image, (0, 0))

    #Uncomment to view the map on a 2D View.
    #screen.fill((255, 255, 255), 0)
    #map.render(screen)
    #player.render(screen)

    raycaster.render(screen)
    pygame.display.update()