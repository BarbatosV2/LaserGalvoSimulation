import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Laser Galvo Simulation")

# Set up colors
white = (255, 255, 255)
red = (255, 0, 0)

# Set up the initial speed and movement speed multiplier
speed = 1

# Read input from txt files
def read_positions_from_files():
    with open('x.txt', 'r') as x_file, open('y.txt', 'r') as y_file:
        x_content = [float(line.strip()) for line in x_file.readlines()]
        y_content = [float(line.strip()) for line in y_file.readlines()]

        if x_content and y_content:
            return x_content, y_content


# Main game loop
x_positions, y_positions = read_positions_from_files()
if x_positions is None or y_positions is None:
    sys.exit()

index = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the laser galvo position
    galvo_x = int(x_positions[index])
    galvo_y = int(y_positions[index])

    # Draw the screen
    screen.fill(white)
    pygame.draw.circle(screen, red, (galvo_x, galvo_y), 10)  # Red dot represents the laser position
    pygame.display.flip()

    # Control the frames per second (FPS)
    pygame.time.Clock().tick(60)

    # Move to the next position
    index = (index + 1) % len(x_positions)
    pygame.time.delay(int(10 / speed))  # Delay based on the desired speed
