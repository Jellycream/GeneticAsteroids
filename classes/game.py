import pygame
from random import randint
from ship import Ship
from asteroid import Asteroid

import config as cfg


class Game:
    def __init__(self):
        # initialize game window
        self.screen_width = 720
        self.screen_height = 400
        self.screen = pygame.display.set_mode(
            [self.screen_width, self.screen_height])

        # Create ship
        self.ship = Ship(self.screen_width, self.screen_height)

        # Keep track of time between asteroid spawning
        self.lastSpawn = 0

        # Create asteroid list
        self.asteroids = [
            Asteroid(self.screen_width, self.screen_height)]

        # Setup game clock
        self.clock = pygame.time.Clock()

    def update(self):
        # Update full diplay surface
        pygame.display.flip()
        # Update and move ship
        self.ship.update()
        self.ship.move(pygame.time.get_ticks())

        # Check for ship asteroid collisions
        if self.ship.checkCollisions(self.asteroids, self.screen):
            self.restart()

        # Update all asteroids
        for A in self.asteroids:
            A.update()

            # Check for bullet asteroid collisions
            coll = A.checkCollisions(self.ship.bullets)
            if coll:
                # Remove colliding bullet
                self.ship.bullets.remove(coll)

                # If small asteroid just remove, else split
                if A.size == 20:
                    self.asteroids.remove(A)
                    continue
                else:
                    # Add children asteroids to list
                    for child in A.split(coll):
                        self.asteroids.append(child)

                    # Remove parent asteroid
                    self.asteroids.remove(A)
                    continue

        # If enough time has passed spawn a new asteroid
        if pygame.time.get_ticks() - self.lastSpawn >= 6000 and self.asteroidCount() <= 8:
            self.asteroids.append(
                Asteroid(self.screen_width, self.screen_height))
            self.lastSpawn = pygame.time.get_ticks()

        self.clock.tick(60)
        # Process events
        pygame.event.pump()

    def render(self):
        # Fill screen with black
        self.screen.fill(cfg.black)

        # Draw ship
        self.ship.draw(self.screen)

        # Draw all asteroids
        for A in self.asteroids:
            A.draw(self.screen)

    def process_events(self):
        # Check events for quit command or esc key
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
        return False

    def asteroidCount(self):
        count = 0
        for A in self.asteroids:
            if A.size == 20:
                count += 1
            elif A.size == 40:
                count += 3
            elif A.size == 80:
                count += 4

        return count

    def restart(self):
        # Replace data
        # Create ship
        self.ship = Ship(self.screen_width, self.screen_height)
        self.asteroids = [Asteroid(self.screen_width, self.screen_height)]

        # Setup game clock
        self.clock = pygame.time.Clock()
        return

    def quit(self):
        # quit the game
        pygame.quit()
        return
