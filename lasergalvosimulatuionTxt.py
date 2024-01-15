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


                         ##################
#------------------------# HARDWARE LISTS #------------------------#
                         ##################
    
    #1. Arduino Uno R1 https://www.phippselectronics.com/product/arduino-uno-r3-atmega16u2-development-board-with-usb-cable-compatible/?gclid=Cj0KCQiAhomtBhDgARIsABcaYymqEQgZF0yQfm2FBF7mmPPHZDrGlauMHYXxvQfUPL-22LLlBGu2gxYaAgrsEALw_wcB
    #2. 2 EasyDriver - Stepper Mortor https://www.makerstore.com.au/product/elec-easydriver/?utm_source=Google%20Shopping&utm_campaign=Google%20Merchant%20product%20feed&utm_medium=cpc&utm_term=3166&gad_source=1&gclid=Cj0KCQiAhomtBhDgARIsABcaYymEOtwgIpc4E9JwPaA1uqWSvIvWNbtAGy8XceeIlKvVLL0vVb8OcRgaAsmTEALw_wcB 
    #3. 12V Power Supply https://www.amazon.com.au/GTGUGR-Adjustable-Surveillance-Equipment-Selectable/dp/B0C16PS3D7/ref=asc_df_B0C16PS3D7/?tag=googleshopdsk-22&linkCode=df0&hvadid=650071461599&hvpos=&hvnetw=g&hvrand=5788551059392128089&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9070871&hvtargid=pla-2198230312470&psc=1&mcid=62e172ec2b163a5ebbc2d52d3fb1287d 
    #4. 22 Pins Connector https://www.amazon.com.au/120pcs-Multicoloured-Dupont-Breadboard-arduino/dp/B01EV70C78/ref=asc_df_B01EV70C78/?tag=googleshopdsk-22&linkCode=df0&hvadid=341743944651&hvpos=&hvnetw=g&hvrand=16620451294426328958&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9070871&hvtargid=pla-362913641420&psc=1&mcid=8097116d0577311481e3a4b0efd150d5 
    #5. 2 Mirrors
    #6. 2 Stepper Motors 
    #7. Laser Pointer 
    #8. Laser Driver... why do i need this????