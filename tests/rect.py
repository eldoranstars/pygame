import pygame
import random

for i in range(1,20):
    rect = pygame.Rect(0, 0, 100, 10)
    rect.centerx = random.randrange(0, 450, rect.width)

    print(rect.centerx)