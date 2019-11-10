from pygame import Vector2, draw, key, K_UP, K_LEFT, K_RIGHT, K_SPACE
from math import cos, sin, radians, degrees, sqrt, hypot
import json

from bullet import Bullet

import config as cfg


class Ship:
    def __init__(self, windowWidth, windowHeight):
        self.width = windowWidth
        self.height = windowHeight

        self.pos = Vector2(windowWidth/2, windowHeight/2)
        self.vel = Vector2()
        self.acc = 0
        self.maxVel = 4
        self.thrust = 0.1

        self.dir = -90
        self.dirDelta = -90
        self.turnSpeed = 4

        self.damp = 0.01

        self.size = 14

        self.bullets = []
        self.shootDelta = 0

    def checkCollisions(self, asteroids, screen):
        for A in asteroids:
            # Get distance from ships center and asteroids center
            centDist = hypot(self.pos.x - A.pos.x, self.pos.y - A.pos.y)

            # If within max distance for a collision, check all points for collision
            if centDist <= self.size + A.size/2:
                # Calculate points of ship
                p1 = Vector2(cos(radians(self.dir)) * self.size +
                             self.pos.x, sin(radians(self.dir)) * self.size + self.pos.y)
                p2 = Vector2(cos(radians(self.dir + 120)) * self.size +
                             self.pos.x, sin(radians(self.dir + 120)) * self.size + self.pos.y)
                p3 = Vector2(cos(radians(self.dir + 240)) * self.size +
                             self.pos.x, sin(radians(self.dir + 240)) * self.size + self.pos.y)

                # Calculate distance from asteroid center for each point in ship
                d1 = hypot(p1.x - A.pos.x, p1.y - A.pos.y)
                d2 = hypot(p2.x - A.pos.x, p2.y - A.pos.y)
                d3 = hypot(p3.x - A.pos.x, p3.y - A.pos.y)

                dists = [d1, d2, d3]

                # Check if any point is within the radius of the asteroid
                for d in dists:
                    if d <= A.size/2:
                        return True
            else:
                continue

        return False

    def update(self):
        # Add velocity to position
        self.pos += self.vel

        # Create acceleration vector and add it to velocity
        accVec = Vector2(
            cos(radians(self.dir)), sin(radians(self.dir)))
        accVec.scale_to_length(self.acc)

        self.vel += accVec
        self.acc *= 0

        # Limit velocity to maximum value
        if self.vel.magnitude() > self.maxVel:
            self.vel.scale_to_length(self.maxVel)

        # Apply dampening to velocity
        self.vel *= 1 - self.damp

        # If ship is off screen wrap around to other side
        if self.pos.x > self.width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = self.width
        if self.pos.y > self.height:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = self.height

        for B in self.bullets:
            B.update()
            if B.tick >= 100:
                self.bullets.remove(B)

        return

    def move(self, time):
        # Get state of all keys
        keys = key.get_pressed()

        # If up arrow pressed, set acceleration to thrust value
        if keys[K_UP]:
            self.acc = self.thrust
        # If right or left arrow pressed add or subtract respectivly to the direction delta
        if keys[K_RIGHT]:
            self.dirDelta += self.turnSpeed
        if keys[K_LEFT]:
            self.dirDelta -= self.turnSpeed

        # Add bullet to list if space key pressed and previous bullet was added more than 400 milliseconds before
        # Maximum number of bullets on screen at a time is 5
        if keys[K_SPACE] and time - self.shootDelta >= 400:
            self.shootDelta = time
            self.bullets.append(Bullet(self.width, self.height,
                                       cos(radians(self.dir)) * self.size + self.pos.x, sin(radians(self.dir)) * self.size + self.pos.y, self.dir))

        # Linearly interpolate (lerp) between current direction and the direction delta
        self.dir = self.lerp(self.dir, self.dirDelta, 0.1)
        return

    def draw(self, screen):
        # Create points of equilateral triangle around the center of the ship
        p1 = Vector2(cos(radians(self.dir)) * self.size +
                     self.pos.x, sin(radians(self.dir)) * self.size + self.pos.y)
        p2 = Vector2(cos(radians(self.dir + 120)) * self.size +
                     self.pos.x, sin(radians(self.dir + 120)) * self.size + self.pos.y)
        p3 = Vector2(cos(radians(self.dir + 240)) * self.size +
                     self.pos.x, sin(radians(self.dir + 240)) * self.size + self.pos.y)
        points = [p1, p2, p3]

        # Draw ship with antialiased lines
        draw.aalines(screen, cfg.white, True, points, 2)

        for B in self.bullets:
            B.draw(screen)

        return

    # Linear Interpolation helper function
    def lerp(self, a, b, f):
        return a + f * (b - a)
