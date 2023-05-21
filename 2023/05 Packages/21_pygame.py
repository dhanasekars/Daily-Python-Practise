""" 
Created on : 18/05/23 6:43 am
@author : ds  
"""
import pygame

#
# pygame.init()
#
#
# width = 800
# height = 600
# window = pygame.display.set_mode((width, height))
#
#
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         # window.fill((255, 255, 255))
#         pygame.draw.circle(window, (255, 0, 0), (400, 300), 75)
#         pygame.display.flip()
#
# pygame.quit()


import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Game")

# Set up the colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - player_size - 10

# Set up the game clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5

    # Clear the screen
    window.fill(BLACK)

    # Draw the player
    pygame.draw.rect(window, RED, (player_x, player_y, player_size, player_size))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
