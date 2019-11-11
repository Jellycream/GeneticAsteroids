from pygame import Vector2, draw, Rect
from math import cos, sin, radians, degrees

import config as cfg


class Bullet:
    def __init__(self, windowWidth, windowHeight, x, y, direction):
        self.width = windowWidth
        self.height = windowHeight

        self.pos = Vector2(x, y)
        self.dir = direction

        self.speed = 6
        self.size = 4

        self.tick = 0

    def update(self):
        move = Vector2(cos(radians(self.dir)) * self.speed,
                       sin(radians(self.dir)) * self.speed)
        self.pos += move

        if self.pos.x > self.width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = self.width
        if self.pos.y > self.height:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = self.height

        self.tick += 1

        return

    def draw(self, screen):
        # Draw bullet at asteroids position
        rect = Rect(
            (self.pos.x - self.size/2, self.pos.y - self.size/2), (self.size, self.size))
        draw.ellipse(screen, cfg.white, rect)

        return
