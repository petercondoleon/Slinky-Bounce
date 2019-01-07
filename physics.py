
from imports import *

GRAVITY = 1/15 # Gravity in pixels per second where 1m is 15px

class PhysicsSprite(pygame.sprite.Sprite):
    """A sprite with physics properties
    Returns: A physics sprite
    Functions:
    Attributes:
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = Rect(0.0,0.0,0.0,0.0)
        self._x = 0
        self._y = 0
        self.dx = 0
        self.dy = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x
        self.rect[0] = int(x)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
        self.rect[1] = int(y)

    def update(self):
        "Updates the sprite based on physics"
        self.x += self.dx
        self.y += self.dy

        self.dy += GRAVITY

        #print(self.dy)
