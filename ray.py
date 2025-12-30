import math, pygame
from settings import *

def normalizeAngle(angle):
    angle = angle % (2 * math.pi)
    if (angle <= 0):
        angle = (2 * math.pi) + angle
    return angle

def distance_between(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2-y1))

class Ray:
    def __init__(self, angle, player, map):
        self.rayAngle = normalizeAngle(angle)
        self.player = player
        self.map = map

        self.is_facing_down = self.rayAngle > 0 and self.rayAngle < math.pi
        self.is_facing_up = not self.is_facing_down
        self.is_facing_right = self.rayAngle < 0.5 * math.pi or self.rayAngle > 1.5 * math.pi
        self.is_facing_left = not self.is_facing_right

        self.wall_hit_x = 0
        self.wall_hit_y = 0

        self.distance = 0

        self.color = 255

    def cast(self):
        found_horizontal_wall = False
        horizontal_hit_x = 0
        horizontal_hit_y = 0

        first_intersection_x = None
        first_intersection_y = None

        if self.is_facing_up:
            first_intersection_y = ((self.player.y) // TILESIZE) * TILESIZE - 0.01
        elif self.is_facing_down:
            first_intersection_y = ((self.player.y // TILESIZE) * TILESIZE) + TILESIZE

        first_intersection_x = self.player.x + (first_intersection_y - self.player.y) / math.tan(self.rayAngle)

        next_horizontal_x = first_intersection_x
        next_horizontal_y = first_intersection_y

        xa = 0
        ya = 0

        if self.is_facing_up:
            ya = -TILESIZE
        if self.is_facing_down:
            ya = TILESIZE

        xa = ya / math.tan(self.rayAngle)

        #check to see if the ray is inside the window
        while (next_horizontal_x <= WINDOW_WIDTH and next_horizontal_x >= 0 and
               next_horizontal_y <= WINDOW_HEIGHT and next_horizontal_y >= 0):
            if self.map.has_wall_at(next_horizontal_x, next_horizontal_y):
                found_horizontal_wall = True
                horizontal_hit_x = next_horizontal_x
                horizontal_hit_y = next_horizontal_y
                break
            else:
                next_horizontal_x += xa
                next_horizontal_y += ya

        #Testing the horizontal checking
        # self.wall_hit_x = horizontal_hit_x
        # self.wall_hit_y = horizontal_hit_y

        # VERTICAL CHECKING
        found_vertical_wall = False
        vertical_hit_x = 0
        vertical_hit_y = 0

        if self.is_facing_right:
            first_intersection_x = ((self.player.x // TILESIZE) * TILESIZE) + TILESIZE
        elif self.is_facing_left:
            first_intersection_x = ((self.player.x // TILESIZE) * TILESIZE) - 0.01

        first_intersection_y = self.player.y + (first_intersection_x - self.player.x) * math.tan(self.rayAngle)

        next_vertical_x = first_intersection_x
        next_vertical_y = first_intersection_y

        if self.is_facing_right:
            xa = TILESIZE
        elif self.is_facing_left:
            xa = -TILESIZE

        ya = xa * math.tan(self.rayAngle)

        # check to see if the ray is inside the window
        while (next_vertical_x <= WINDOW_WIDTH and next_vertical_x >= 0 and
               next_vertical_y <= WINDOW_HEIGHT and next_vertical_y >= 0):
            if self.map.has_wall_at(next_vertical_x, next_vertical_y):
                found_vertical_wall = True
                vertical_hit_x = next_vertical_x
                vertical_hit_y = next_vertical_y
                break
            else:
                next_vertical_x += xa
                next_vertical_y += ya

        # DISTANCE CALCULATION

        horizontal_distance = 0
        vertical_distance = 0

        if found_horizontal_wall:
            horizontal_distance = distance_between(self.player.x, self.player.y, horizontal_hit_x, horizontal_hit_y)
        else:
            horizontal_distance = 9999

        if found_vertical_wall:
            vertical_distance = distance_between(self.player.x, self.player.y, vertical_hit_x, vertical_hit_y)
        else:
            vertical_distance = 9999

        if horizontal_distance < vertical_distance:
            self.wall_hit_x = horizontal_hit_x
            self.wall_hit_y = horizontal_hit_y
            self.distance = horizontal_distance
            self.color = 160
        else:
            self.wall_hit_x = vertical_hit_x
            self.wall_hit_y = vertical_hit_y
            self.distance = vertical_distance
            self.color = 255

        self.distance *= math.cos(self.player.rotationAngle - self.rayAngle)

        self.color *= (60 / self.distance)
        if (self.color > 255):
            self.color = 255
        elif self.color < 0:
            self.color = 0

    def render(self, screen):
        # TEMP
        #pygame.draw.line(screen, (255, 0, 0), (self.player.x, self.player.y), (self.player.x + math.cos(self.rayAngle) *
        #50, self.player.y + math.sin(self.rayAngle) * 50))

        pygame.draw.line(screen, (255, 0, 0), (self.player.x, self.player.y), (self.wall_hit_x, self.wall_hit_y))
