import pygame
from ship import Ship
from asteroid import Asteroid

import config as cfg


class Game:
    def __init__(self):
        # initialize game window
        self.screen_width = 900
        self.screen_height = 500
        self.screen = pygame.display.set_mode(
            [self.screen_width, self.screen_height])

        # Create ship
        self.ship = Ship(self.screen_width, self.screen_height)

        # Create asteroid list
        self.asteroids = [Asteroid(self.screen_width, self.screen_height), Asteroid(
            self.screen_width, self.screen_height)]

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

    def restart(self):
        # Replace data
        # Create ship
        self.ship = Ship(self.screen_width, self.screen_height)
        self.asteroids = [Asteroid(self.screen_width, self.screen_height), Asteroid(
            self.screen_width, self.screen_height)]

        # Setup game clock
        self.clock = pygame.time.Clock()
        return

    def quit(self):
        # quit the game
        pygame.quit()
        return
