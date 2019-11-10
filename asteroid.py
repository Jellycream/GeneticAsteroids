from pygame import Vector2, draw
from math import cos, sin, radians, degrees, degrees, hypot, atan2
from random import random, randint

import config as cfg


class Asteroid:
    def __init__(self, windowWidth, windowHeight, size=False, x=False, y=False, direction=False):
        self.width = windowWidth
        self.height = windowHeight
        self.pos = Vector2()

        # Sizes: 80, 40, 20
        self.size = 0

        # number of points in asteroid
        self.res = 5

        # If size not given with init, choose random size
        if not size:
            choice = randint(1, 3)
            self.res *= choice
            if choice == 1:
                self.size = 20
            elif choice == 2:
                self.size = 40
            elif choice == 3:
                self.size = 80
        else:
            self.res *= size
            if size == 1:
                self.size = 20
            elif size == 2:
                self.size = 40
            elif size == 3:
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

        self.spin = 0

        return

    def checkCollisions(self, bullets):
        for B in bullets:
            dist = hypot(self.pos.x - B.pos.x, self.pos.y - B.pos.y)
            if dist <= self.size/2:
                return B

        return False

    def split(self, bullet):
        splitdir = degrees(
            atan2(bullet.pos.y - self.pos.y, bullet.pos.x - self.pos.x))
        print(splitdir)
        if self.size == 80:
            return [Asteroid(self.width, self.height, 2, self.pos.x, self.pos.y, splitdir - 45),
                    Asteroid(self.width, self.height, 2, self.pos.x, self.pos.y, splitdir + 45)]
        elif self.size == 40:
            return [Asteroid(self.width, self.height, 1, self.pos.x, self.pos.y, splitdir - 45),
                    Asteroid(self.width, self.height, 1, self.pos.x, self.pos.y, splitdir + 45)]
        else:
            return False

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
        step = 360/self.res
        points = []
        i = 0
        while i < self.res:
            points.append(Vector2(self.pos.x + cos(radians(i*step + self.spin)) *
                                  self.size/2, self.pos.y + sin(radians(i*step + self.spin)) * self.size/2))
            i += 1

        draw.aalines(screen, cfg.white, True, points)

        self.spin += 1
        return
