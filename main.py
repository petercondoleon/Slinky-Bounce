#!/usr/bin/env python3
#
# Slinky Bounce
# An endless jumping game
# https://github.com/petercondoleon/Slinky-Bounce

VERSION = 0.1

from imports import *
from resources import *
from objects import *

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption("Slinky Bounce")

    ## TODO: find a way to move this to resources.py
    def text_display(text, size, colour, x, y):
        textFont = pygame.font.Font('freesansbold.ttf', size)
        TextSurf, TextRect = text_objects(text, textFont, colour)
        TextRect = (x, y)
        screen.blit(TextSurf, TextRect)

    # Load Backgound
    bg, bg_rect = load_image("background.jpg")

    # Initialise objects
    ball = BouncyBall((math.pi/2, 1))
    platform1 = Platform()
    platform2 = Platform()
    platform1.rect = platform1.rect.move(random.randint(1,500), random.randint(1,600))
    platform2.rect = platform2.rect.move(random.randint(1,500), random.randint(1,600))

    ballSprite = pygame.sprite.RenderPlain(ball)
    platformSprites = pygame.sprite.RenderPlain((platform1, platform2))

    # Blit everything to the screen
    screen.blit(bg, (0, 0))
    pygame.display.flip()

    # Initialise clock
    clock = pygame.time.Clock()

    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    continue
                if event.key == K_RIGHT:
                    continue
                if event.key == K_SPACE:
                    continue
            elif event.type == KEYUP:
                continue

        screen.blit(bg, (0, 0))
        ballSprite.update()
        platformSprites.update()
        ballSprite.draw(screen)
        platformSprites.draw(screen)

        # Old font stuff
        black = (0, 0, 0)
        text_display('Score', 18, black, 10, 10)

        # Old platform
        white = (255, 255, 255)
        pygame.draw.rect(screen, white, (225, 190, 50, 20))
        pygame.draw.circle(screen, white, (225, 200), 10, 10)
        pygame.draw.circle(screen, white, (275, 200), 10, 10)

        pygame.display.flip()

if __name__ == '__main__': main()
