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
beats = 8
instruments = 6

def draw_grid():
    # The numbers below are coords from top left of screen [x, y, width, height]
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 200], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)
    boxes = []
    colors = [gray, white, gray]
    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (20, 30))
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (20, 130))
    kick_text = label_font.render('Bass Drum', True, white)
    screen.blit(kick_text, (20, 230))
    crash_text = label_font.render('Crash', True, white)
    screen.blit(crash_text, (20, 330))
    clap_text = label_font.render('Clap', True, white)
    screen.blit(clap_text, (20, 430))
    floor_text = label_font.render('Floor Tom', True, white)
    screen.blit(floor_text, (20, 530))
    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i * 100) + 100), (199, (i * 100) + 100), 3)

    for i in range(beats):
        for j in range(instruments):
            rect = pygame.draw.rect(screen, gray, [i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200) // beats), ((HEIGHT - 200) // instruments)], 5, 5)

# Main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill(black) # up to this point, this creates the back canvas
    draw_grid() # this draws the grid according to draw_grid() above

    # This listens for keyboard or mouse input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()