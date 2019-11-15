from classes.game import Game
import pygame

print("***Welcome to Genetic Asteroids!***")

# Number of agents in sinle generation
genSize = 5

gen = 1

# Create window
screen = pygame.display.set_mode(
    [720, 400])

# create instances of asteroids games
agents = []
i = 0
while i < genSize:
    agents.append(Game(screen, i))
    i += 1

# The current agent that is being rendered
view = 0

# Initialize Pygame
pygame.init()


# Input handeling
def process_events():
        # Check events for quit command or esc key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'esc'

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return 'esc'

            if event.key == pygame.K_EQUALS:
                return 'next'

            if event.key == pygame.K_MINUS:
                return 'last'

    return False


# Game loop
running = True
while running:
    for agent in agents:
        # Keyboard handling
        keys = process_events()
        if(keys == 'esc'):
            running == False
            agent.quit()
            break
        elif(keys == 'last'):
            if(view <= 0):
                view = len(agents) - 1
            else:
                view -= 1
        elif(keys == 'next'):
            if(view >= len(agents) - 1):
                view = 0
            else:
                view += 1

        # Update and render game
        agent.update()

        # Only render one game
        if(agent.id == view):
            agent.render()

        pass


# Exit sequence
print("**Exiting game**")
