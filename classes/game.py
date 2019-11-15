import pygame
from random import randint
from ship import Ship
from asteroid import Asteroid

import config as cfg


class Game:
    def __init__(self, screen, id):
        self.id = id

        self.width = 720
        self.height = 400

        self.screen = screen

        # Create ship
        self.ship = Ship(self.width, self.height)

        # Keep track of time between asteroid spawning
        self.lastSpawn = 0

        # Create asteroid list
        self.asteroids = [
            Asteroid(self.width, self.height)]

        # Setup game clock
        self.clock = pygame.time.Clock()

        self.score = 0

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
                # Add to score
                self.score += 1

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
                Asteroid(self.width, self.height))
            self.lastSpawn = pygame.time.get_ticks()

        self.clock.tick(60)
        # Process events
        pygame.event.pump()

    def render(self):
        font = pygame.font.Font('assets/Ubuntu-Regular.ttf', 32)
        scoreText = font.render(str(self.score), True, cfg.white)
        scoreTextRect = scoreText.get_rect()
        scoreTextRect.center = (self.width - 32, 32)

        idText = font.render("#" + str(self.id), True, cfg.white)
        idTextRect = idText.get_rect()
        idTextRect.center = (32, 32)

        # Fill screen with black
        self.screen.fill(cfg.black)

        # Draw score and id
        self.screen.blit(scoreText, scoreTextRect)
        self.screen.blit(idText, idTextRect)

        # Draw ship
        self.ship.draw(self.screen)

        # Draw all asteroids
        for A in self.asteroids:
            A.draw(self.screen)

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
        self.ship = Ship(self.width, self.height)

        # Keep track of time between asteroid spawning
        self.lastSpawn = 0

        # Create asteroid list
        self.asteroids = [
            Asteroid(self.width, self.height)]

        # Setup game clock
        self.clock = pygame.time.Clock()

        self.score = 0
        return

    def quit(self):
        # quit the game
        pygame.quit()
        return
