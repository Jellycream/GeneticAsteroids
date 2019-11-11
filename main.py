from classes.game import Game

print("***Welcome to Genetic Asteroids!***")

# create instance of asteroids game
app = Game()

running = True

# Game loop
while running:
    # Game quit handling
    if(app.process_events()):
        running == False
        app.quit()
        break

    # Update and render game
    app.update()
    app.render()

# Exit sequence
print("**Exiting game**")
