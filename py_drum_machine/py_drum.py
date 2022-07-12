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
dark_gray = (50, 50, 50)
green = (0, 255, 0)
gold = (212, 175, 55)
blue = (0, 255, 255)

# Setting up variable for the display
screen = pygame.display.set_mode([WIDTH, HEIGHT]) # Could insert numbers directly

# This next line is optional which sets the caption
pygame.display.set_caption('Beat Maker')

# This is a very common font to use or a ttf could be downloaded and used instead
label_font = pygame.font.Font('freesansbold.ttf', 32) # Roboto-Bold.ttf
# Can change fonts like this... pygame.font.Font("C:\Windows\Fonts\Arial.ttf",size)
medium_font = pygame.font.Font('freesansbold.ttf', 24)


# Using a common frame rate
fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 6
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
bpm = 240
playing = True
active_length = 0
active_beat = 1
beat_changed = True

# load in sounds
hi_hat = mixer.Sound('sounds\kit2\hi hat.wav')
snare = mixer.Sound('sounds\kit2\snare.wav')
kick = mixer.Sound('sounds\kit2\kick.wav')
crash = mixer.Sound('sounds\kit2\crash.wav')
clap = mixer.Sound('sounds\kit2\clap.wav')
tom = mixer.Sound('sounds\kit2\\tom.wav')
pygame.mixer.set_num_channels(instruments * 3)


def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1:
            if i == 0:
                hi_hat.play()
            if i == 1:
                snare.play()
            if i == 2:
                kick.play()
            if i == 3:
                crash.play()
            if i == 4:
                clap.play()
            if i == 5:
                tom.play()

def draw_grid(clicks, beat):
    # The numbers below are coords from top left of screen [x, y, width, height]
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 200], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)
    boxes = []
    colors = [gray, white, gray]
    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (30, 30))
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (30, 130))
    kick_text = label_font.render('Bass Drum', True, white)
    screen.blit(kick_text, (30, 230))
    crash_text = label_font.render('Crash', True, white)
    screen.blit(crash_text, (30, 330))
    clap_text = label_font.render('Clap', True, white)
    screen.blit(clap_text, (30, 430))
    floor_text = label_font.render('Floor Tom', True, white)
    screen.blit(floor_text, (30, 530))
    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i * 100) + 100), (200, (i * 100) + 100), 3)

    for i in range(beats):
        for j in range(instruments):
            if clicks[j][i] == -1:
                color = gray
            else:
                color = green
            rect = pygame.draw.rect(screen, color, 
                                    [i * ((WIDTH - 200) // beats) + 205, (j * 100) + 5, ((WIDTH - 200) // beats) - 10,
                                     ((HEIGHT - 200) // instruments) - 10], 0, 3)
            pygame.draw.rect(screen, gold,
                                    [i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200) // beats),
                                     ((HEIGHT - 200) // instruments)], 5, 5)
            pygame.draw.rect(screen, black,
                                    [i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200) // beats),
                                     ((HEIGHT - 200) // instruments)], 2, 5)
            boxes.append((rect, (i, j)))

        active = pygame.draw.rect(screen, blue,
                                    [beat * ((WIDTH - 200) // beats) + 200, 0, ((WIDTH - 200) // beats), instruments * 100], 5, 3)
    return boxes

# Main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill(black) # up to this point, this creates the back canvas
    boxes = draw_grid(clicked, active_beat) # this draws the grid according to draw_grid() above
    
    # lower menu buttons
    play_pause = pygame.draw.rect(screen, gray, [50, HEIGHT - 150, 200, 100], 0, 5)
    play_text = label_font.render('Play/Pause', True, white)
    screen.blit(play_text, (70, HEIGHT - 130))
    
    if playing:
        play_text2 = medium_font.render('Playing', True, dark_gray)
    else:
        play_text2 = medium_font.render('Paused', True, dark_gray)
    screen.blit(play_text2, (70, HEIGHT - 100))

    if beat_changed:
        play_notes()
        beat_chaged = False

    # This listens for keyboard or mouse input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):  # This will check if we've clicked on any of the rectangles
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1
        if event.type == pygame.MOUSEBUTTONUP:
            if play_pause.collidepoint(event.pos):
                if playing:
                    playing = False
                elif not playing:
                    playing = True

    beat_length = 3600 // bpm

    if playing:
        if active_length < beat_length:
            active_length += 1
        else:
            active_length = 0
            if active_beat < beats - 1:
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True

    pygame.display.flip()
pygame.quit()