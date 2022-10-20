import pygame
import random

rect1 = pygame.Rect(0, 0, 100, 100)
rect2 = pygame.Rect(rect1.center, (rect1.width * 0.5, rect1.height * 0.5))
rect2.center = rect1.center


print(rect1.center, rect1.width, rect1.height)
print(rect2.center, rect2.width, rect2.height)