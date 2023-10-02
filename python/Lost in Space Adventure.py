import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
WIDTH, HEIGHT = 800, 600

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Your 2D Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic goes here

    # Clear the screen
    screen.fill(BLACK)

    # Draw game objects here

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
