######## objects.py ########
#
# This file contains game objects

from imports import *
from resources import *

class Label():
    """An object for creating labels on screen
    Returns: A label object
    Functions: blit
    Attributes: text, size, font, colour, x, y
    """

    def __init__(self, text='', x=0, y=0, size=16, colour=(0,0,0), fontName='freesansbold.ttf'):
        self.text = text
        self.font = Font(fontName, size)
        self.colour = colour
        self.x = x
        self.y = y
        self._update()

    def setText(self, text):
        "Changes the text of the label"
        self.text = text
        self._update()

    def setPos(self, x, y):
        "Changes the position of the label"
        self.x = x
        self.y = y
        self._update()

    def _update(self):
        self.textSurf = self.font.render(self.text, True, self.colour)
        self.textRect = self.textSurf.get_rect().move(self.x, self.y)

    def drawTo(self, surface):
        # Blit to surface at x, y position
        if isinstance(surface, pygame.Surface):
            surface.blit(self.textSurf, self.textRect)
        else:
            print(f'Unable to blit \'{self._text}\' label to \'{surface}\'.')

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
