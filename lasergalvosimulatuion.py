import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Laser Galvo Simulation")

# Set up colors
white = (255, 255, 255)

# Set up the laser galvo position
galvo_x, galvo_y = width // 2, height // 2

# Set up the speed of movement
speed = 5

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move the laser galvo
    if keys[pygame.K_LEFT]:
        galvo_x -= speed
    if keys[pygame.K_RIGHT]:
        galvo_x += speed
    if keys[pygame.K_UP]:
        galvo_y -= speed
    if keys[pygame.K_DOWN]:
        galvo_y += speed

    # Keep the laser galvo within the screen boundaries
    galvo_x = max(0, min(galvo_x, width))
    galvo_y = max(0, min(galvo_y, height))

    # Draw the screen
    screen.fill(white)
    pygame.draw.circle(screen, (255, 0, 0), (galvo_x, galvo_y), 5)  # Red dot represents the laser position
    pygame.display.flip()

    # Control the frames per second (FPS)
    pygame.time.Clock().tick(60)