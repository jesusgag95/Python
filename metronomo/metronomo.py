import sys
import pygame
import time
from playsound import playsound

# General settings
background_colour = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
(width, height) = (800, 400)
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Metronomo')
screen.fill(background_colour)
font = pygame.font.Font('freesansbold.ttf', 300)


def metronome(bpm):
    counter = 0
    while True:
        if counter < 4:
            beat_sound = 1
            colour = black
            counter += 1
        else:
            beat_sound = 2
            colour = red
            counter = 1
        draw_screen(counter, colour, beat_sound)
        time.sleep(60/bpm)


def draw_screen(number, colour, sound):
    text = font.render(str(number), True, colour, background_colour)
    textRect = text.get_rect()
    textRect.center = (width // 2, height // 2)

    while True:
        screen.blit(text, textRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        # if sound != 1:
        #     playsound(
        #         'C:\\Users\\jesus\\OneDrive\\Documentos\\Python\\metronomo\\metronomeDown.wav')
        # else:
        #     playsound(
        #         'C:\\Users\\jesus\\OneDrive\\Documentos\\Python\\metronomo\\metronomeUp.wav')
        return


def run():
    bpm = int(input("Ingresa los bpm: "))
    metronome(bpm)


if __name__ == "__main__":
    run()
