import pygame
import time
import math

pygame.init()

screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height))

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

number = 1
position = (screen_width//2, screen_height//2)
segments = 1
direction = 1
step_size = 2
circle_radius = 1


def draw_number(screen, number, position, color=white, font_size=24):
    font = pygame.font.Font(None, font_size)
    text = font.render(str(number), True, color)
    screen.blit(text, position)


def right(position, step_size):
    return (position[0] + step_size, position[1])


def up(position, step_size):
    return (position[0], position[1] - step_size)


def left(position, step_size):
    return (position[0] - step_size, position[1])


def down(position, step_size):
    return (position[0], position[1] + step_size)


def isPrime(number):
    if number == 1:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def reset():
    global number, position, segments, direction
    number = 1
    position = (screen_width//2, screen_height//2)
    segments = 1
    direction = 1
    screen.fill(black)


reset()

running = True

while running:
    for _ in range(2):
        pygame.display.flip()
        for _ in range(segments):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if isPrime(number):
                color = white
                pygame.draw.circle(screen, color, position, circle_radius)

            if direction == 1:
                position = right(position, step_size)

            if direction == 2:
                position = up(position, step_size)

            if direction == 3:
                position = left(position, step_size)

            if direction == 4:
                position = down(position, step_size)

            number += 1

        direction += 1
        if direction > 4:
            direction = 1

    segments += 1
    if (segments >= screen_height/step_size) or (segments >= screen_width/step_size):
        reset()
        time.sleep(5)

pygame.quit()