"""
title: pygame_moving_stick_figure
author: isruthi
date: 2019-06-14 13:21
"""


import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pi = 3.141592653

size = (400, 650)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First Pygame")

done = False
clock = pygame.time.Clock()

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10


def draw_stick_figure(screen, x, y):
    # stick boi's face
    pygame.draw.circle(screen, BLACK, [200 + x, 150 + y], 100, 5)
    pygame.draw.ellipse(screen, BLACK, [150 + x, 100 + y, 20, 40])
    pygame.draw.ellipse(screen, BLACK, [225 + x, 100 + y, 20, 40])
    pygame.draw.arc(screen, BLACK, [150 + x, 115 + y, 100, 100], pi, 0, 5)

    # stick boi's torso
    pygame.draw.line(screen, BLACK, [200 + x, 250 + y], [200 + x, 500 + y], 5)

    # stick boi's right arm
    pygame.draw.line(screen, BLACK, [200 + x, 325 + y], [270 + x, 360 + y], 5)
    pygame.draw.line(screen, BLACK, [270 + x, 360 + y], [315 + x, 325 + y], 5)

    # stick boi's left arm
    pygame.draw.line(screen, BLACK, [130 + x, 360 + y], [200 + x, 325 + y], 5)
    pygame.draw.line(screen, BLACK, [85 + x, 325 + y], [130 + x, 360 + y], 5)

    # stick boi's right leg
    pygame.draw.line(screen, BLACK, [200 + x, 500 + y], [300 + x, 575 + y], 5)

    # stick boi's left leg
    pygame.draw.line(screen, BLACK, [100 + x, 575 + y], [200 + x, 500 + y], 5)


while not done:

    # User did something
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_speed = -3
    if keys[pygame.K_RIGHT]:
        x_speed = 3
    if keys[pygame.K_UP]:
        y_speed = -3
    if keys[pygame.K_DOWN]:
        y_speed = 3

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed

    # Reset x_speed and y_speed for the next frame
    x_speed = 0
    y_speed = 0

    screen.fill(WHITE)

    draw_stick_figure(screen, x_coord, y_coord)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()