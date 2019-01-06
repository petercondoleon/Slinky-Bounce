######## imports.py ########
#
# This file contains imports used by most files

try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from socket import *
    from pygame.locals import *
except ImportError as err:
    print(f'Unable to load module: {err}')
    sys.exit(2)
