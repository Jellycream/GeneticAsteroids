from pygame import Vector2, draw, Rect
from math import cos, sin, radians, degrees
from random import random, randint

import config as cfg


class Asteroid:
    def __init__(self, windowWidth, windowHeight, x=False, y=False, size=False, direction=False):
        self.width = windowWidth
        self.height = windowHeight
        self.pos = Vector2()

        # Sizes: 80, 40, 20
        self.size = 0

        # If size not given with init, choose random size
        if not size:
            choice = randint(1, 3)
            if choice == 1:
                self.size = 20
            if choice == 2:
                self.size = 40
            if choice == 3:
                self.size = 80
        else:
            if size == 1:
                self.size = 20
            if size == 2:
                self.size = 40
            if size == 3:
                self.size = 80
            else:
                print("invalid size defaulting to 1!")
                self.size = 20

        # Set speed as reciprocal of size
        self.speed = 80/self.size

        # If direction not given, set to random degree
        self.dir = direction or (random() * 360)

        # If x or y not given,
        if(not x or not y):
            rX = 0
            rY = 0
            if random() > 0.5:
                if random() > 0.5:
                    rX = self.width
                rY = random() * self.height
            else:
                if random() > 0.5:
                    rY = self.height
                rX = random() * self.width
            self.pos = Vector2(rX, rY)
        else:
            self.pos = Vector2(x, y)

        return

    def update(self):
        # change position by direction vector multiplied by speed
        move = Vector2(cos(radians(self.dir)) * self.speed,
                       sin(radians(self.dir)) * self.speed)
        self.pos += move

        # If asteroid is off screen wrap around to other side
        if self.pos.x > self.width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = self.width
        if self.pos.y > self.height:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = self.height

        return

    def draw(self, screen):
        # Draw ellipse at asteroids position
        rect = Rect(
            (self.pos.x - self.size/2, self.pos.y - self.size/2), (self.size, self.size))
        draw.ellipse(screen, cfg.white, rect, 1)
        return
