######## objects.py ########
#
# This file contains game objects

from imports import *
from resources import *

class Label():
    "An object for creating labels on screen"
    def __init__(self, text='', x=0, y=0, size=16, colour=(0,0,0), fontName='freesansbold.ttf'):
        self.text = text
        self.font = Font(fontName, size)
        self.colour = colour
        self.x = x
        self.y = y
        self.size = size
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

    def setSize(self, size):
        self.size = size
        self._update()

    def _update(self):
        self.textSurf = self.font.render(self.text, True, self.colour)
        self.textRect = self.textSurf.get_rect().move(self.x, self.y)

    def draw(self):
        # Blit to surface at x, y position
        screen = pygame.display.get_surface()
        screen.blit(self.textSurf, self.textRect)

class PhysicsSprite(pygame.sprite.Sprite):
    "A sprite that allows easier manipulation of movement"
    def __init__(self, imageName):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(imageName)
        self.width, self.height = self.rect[2], self.rect[3]
        self._x, self._y, self.dx, self.dy = (0,0,0,0)
        self._obeys_gravity = False
        self._hitbox = self.rect

    @property
    def obeys_gravity(self):
        "Whether the physics object is affected by gravity"
        return self._obeys_gravity

    @obeys_gravity.setter
    def obeys_gravity(self, bool):
        self._obeys_gravity = bool

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

    @property
    def hitbox(self):
        "The rect used for detecting collisions"
        return self._hitbox

    @hitbox.setter
    def hitbox(self, rect):
        self._hitbox = rect

    def collides_with(self, sprite):
        "Returns true if this object is colliding with sprite"
        return self.hitbox.colliderect(sprite.hitbox)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        if self.obeys_gravity: self.dy += GRAVITY

class Spikes(PhysicsSprite):
    "Spikes that ends the game"
    def __init__(self, x=0, y=0):
        PhysicsSprite.__init__(self, 'spikes.png')
        self.x, self.y = x, y

    def update(self):
        PhysicsSprite.update(self)

class Platform(PhysicsSprite):
    "Platforms that can be jumped from"
    def __init__(self, x=0, y=0):
        PhysicsSprite.__init__(self, 'platform.png')
        self.x, self.y = x, y

    def update(self):
        PhysicsSprite.update(self)

class Player(PhysicsSprite):
    "The Slinky Bounce player"
    def __init__(self):
        PhysicsSprite.__init__(self, 'player.png')
        self.sound = load_sound('boing.wav')
        self.move_speed = 6
        self.obeys_gravity = True
        self.is_alive = True

    def bounce(self, amount):
        "Bounces the player by an amount"
        self.dy = -amount
        self.sound.play()

    def top_collides_with(self, sprite):
        "Returns true if the bottom of player contacts sprite"
        hb = self.hitbox
        hitbox_top = Rect(hb.left, hb.top, hb.width, 8)
        return hitbox_top.colliderect(sprite.hitbox)

    def bottom_collides_with(self, sprite):
        "Returns true if the top of player contacts sprite"
        hb = self.hitbox
        hitbox_bottom = Rect(hb.left, hb.top+56, hb.width, 8)
        return hitbox_bottom.colliderect(sprite.hitbox)

    def update(self):
        # Check for boundaries
        PhysicsSprite.update(self)
        if self.y > SCREEN_HEIGHT-self.height:
            # Player died
            self.obeys_gravity = False
            self.dy = 0
            self.is_alive = False
        if self.x > SCREEN_WIDTH-self.width/2:
            self.x = -self.width/2
        if self.x < -self.width/2:
            self.x = SCREEN_WIDTH-self.width/2

    def handle_event(self, event):
        "Handles pygame events specific to the player"
        if event.type == KEYDOWN and self.is_alive:
            if event.key == K_LEFT:
                self.dx = -self.move_speed
            if event.key == K_RIGHT:
                self.dx = self.move_speed
            if event.key == K_SPACE:
                return
        if event.type == KEYUP:
            if event.key == K_LEFT and self.dx == -self.move_speed:
                self.dx = 0
            if event.key == K_RIGHT and self.dx == self.move_speed:
                self.dx = 0
