######## objects.py ########
#
# This file contains game objects

from imports import *
from resources import *

class BouncyBall(pygame.sprite.Sprite):
    """A bouncy ball that bounces around
    Returns: bouncy ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('bouncy_ball.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect, self.vector)
        self.rect = newpos

    def calcnewpos(self, rect, vector):
        (angle, z) = vector
        (dx, dy) = (z*math.cos(angle), z*math.sin(angle))
        return rect.move(dx, dy)

class Platform(pygame.sprite.Sprite):
    """Platforms that can be jumped from
    Returns: platform object
    Functions:
    Attributes:"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('platform.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def update(self):
        return
