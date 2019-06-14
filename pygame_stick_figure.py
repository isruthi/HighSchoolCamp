"""
title: pygame_stick_figure
author: isruthi
date: 2019-06-14 10:55
"""

import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pi = 3.141592653

size = (400, 650)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First Pygame")

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    screen.fill(WHITE)
    # stick boi's face
    pygame.draw.circle(screen, BLACK, [200, 150], 100, 5)
    pygame.draw.ellipse(screen, BLACK, [150, 100, 20, 40])
    pygame.draw.ellipse(screen, BLACK, [225, 100, 20, 40])
    pygame.draw.arc(screen, BLACK, [150, 115, 100, 100], pi, 0, 5)
    # stick boi's torso
    pygame.draw.line(screen, BLACK, [200, 250], [200, 500], 5)
    # stick boi's right arm
    pygame.draw.line(screen, BLACK, [200, 325], [270, 360], 5)
    pygame.draw.line(screen, BLACK, [270, 360], [315, 325], 5)
    # stick boi's left arm
    pygame.draw.line(screen, BLACK, [130, 360], [200, 325], 5)
    pygame.draw.line(screen, BLACK, [85, 325], [130, 360], 5)
    # stick boi's right leg
    pygame.draw.line(screen, BLACK, [200, 500], [300, 575], 5)
    #stick boi's left leg
    pygame.draw.line(screen, BLACK, [100, 575], [200, 500], 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()