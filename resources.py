######## resources.py ########
#
# This file contains functionality for handling resources
#

from imports import *

# Variables
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'resources')

SCREEN_WIDTH = 450
SCREEN_HEIGHT = 600

GRAVITY = 1/6 # Gravity in pixels per second where 1m is 10px

Font = pygame.font.Font

# Images
def load_image(name):
    """Load an image and return image object"""
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error:
        print (f'Cannot load image: {fullname}')
        raise SystemExit()
    return image, image.get_rect()

def load_images(names):
    """Load an array of image names and return image object array"""
    images = []
    rects = []
    for name in names:
        image, rect = load_image(name)
        images.append(image)
        rects.append(rect)
    return images, rects

# Sounds
def load_sound(name):
    """Loads sound and return sound object"""
    fullname = os.path.join(data_dir, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print (f'Cannot load sound: {fullname}')
        raise SystemExit()
    return sound
