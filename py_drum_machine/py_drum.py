# https://youtu.be/F3J3PZj0zi0

import pygame
# Mixer is pygames sound efx and mixer tool
from pygame import mixer
pygame.init()   # initialize all imported pygame modules

#  Because the screen needs to be kind of wide, used these numbers
WIDTH = 1400
HEIGHT = 800

# Per Pete LeMaster, these are common RGB colors to add
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

# Setting up variable for the display
screen = pygame.display.set_mode([WIDTH, HEIGHT]) # Could insert numbers directly

# This next line is optional which sets the caption
pygame.display.set_caption('Beat Maker')

# This is a very common font to use or a ttf could be downloaded and used instead
label_font = pygame.font.Font('freesansbold.ttf', 32) # Roboto-Bold.ttf
# Can change fonts like this... pygame.font.Font("C:\Windows\Fonts\Arial.ttf",size)

# Using a common frame rate
fps = 60
timer = pygame.time.Clock()

# Main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill(black)

    # This listens for keyboard or mouse input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()