import pygame
import math
from settings import *

class Player:
    def __init__(self):
        self.x = WINDOW_WIDTH//2 #X position of our character
        self.y = WINDOW_HEIGHT//2 #Y position of our character
        self.radius = 3 #Radius of our character.
        self.turnDirection = 0
        self.walkDirection = 0
        self.rotationAngle = 0
        self.moveSpeed = 2.5
        self.rotationSpeed = 2 * (math.pi / 180)

    def update(self):

        keys = pygame.key.get_pressed()

        self.turnDirection = 0
        self.walkDirection = 0

        if keys[pygame.K_RIGHT]:
            self.turnDirection = 1
        if keys[pygame.K_LEFT]:
            self.turnDirection = -1
        if keys[pygame.K_UP]:
            self.walkDirection = 1
        if keys[pygame.K_DOWN]:
            self.walkDirection = -1

        moveStep = self.walkDirection * self.moveSpeed
        self.rotationAngle += self.turnDirection * self.rotationSpeed
        self.x += math.cos(self.rotationAngle) * moveStep
        self.y += math.sin(self.rotationAngle) * moveStep

    def render(self, screen):
        #Draw the player on our screen using the x and y coordinates, and the radius.
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)

        #Draw a line from where the player is at to where the player is looking.
        #pygame.draw.line(screen, (255, 0, 0), (self.x, self.y), (self.x + math.cos(self.rotationAngle) * 50, self.y + math.sin(self.rotationAngle) * 50), 2)