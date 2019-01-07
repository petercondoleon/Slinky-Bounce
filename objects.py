######## objects.py ########
#
# This file contains game objects

from imports import *
from resources import *
from physics import *

class Label():
    """An object for creating labels on screen
    Returns: A label object
    Functions: setText, setPos, draw
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

    def draw(self):
        # Blit to surface at x, y position
        screen = pygame.display.get_surface()
        screen.blit(self.textSurf, self.textRect)

class BouncyBall(PhysicsSprite):
    """A bouncy ball that bounces around
    Returns: bouncy ball object
    Functions:
    Attributes: """

    def __init__(self):
        PhysicsSprite.__init__(self)
        self.image, self.rect = load_image('bouncy_ball.png')

    def update(self):
        PhysicsSprite.update(self)
        # Check for boundaries
        if self.y > SCREEN_HEIGHT-60:
            print(f'before: {self.dy}')
            self.dy *= -1 # Bouces at half the velocity it fell
            print(f'after: {self.dy}')

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
