######## objects.py ########
#
# This file contains game objects

from imports import *
from resources import *

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

class Player(pygame.sprite.Sprite):
    """A sprite with physics properties
    Returns: A physics sprite
    Functions:
    Attributes:
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('bouncy_ball.png')
        self.width = self.rect[2]
        self.height = self.rect[3]
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

    def bounce(self, amount):
        "Bounces the player"
        self.dy = -amount

    def move_left(self, speed):
        "Moves the player left"
        self.dx = -speed

    def move_right(self, speed):
        "Moves the player right"
        self.dx = speed

    def update(self):
        # Physics
        self.x += self.dx
        self.y += self.dy
        self.dy += GRAVITY

        # Check for boundaries
        if self.y > SCREEN_HEIGHT-self.height:
            self.bounce(6.5)
        elif self.x > SCREEN_WIDTH-self.width/2:
            self.x = -self.width/2
        elif self.x < -self.width/2:
            self.x = SCREEN_WIDTH-self.width/2
