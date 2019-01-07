#!/usr/bin/env python3
#
# Slinky Bounce
# An endless jumping game
# https://github.com/petercondoleon/Slinky-Bounce

VERSION = 0.1

from imports import *
from resources import *
from objects import *

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
score = 0

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Slinky Bounce")

    # Load Backgound
    bg, bg_rect = load_image("background.jpg")

    # Initialise objects
    ball = BouncyBall((math.pi/2, 1))
    platform1 = Platform()
    platform2 = Platform()
    platform1.rect = platform1.rect.move(random.randint(1,SCREEN_WIDTH), random.randint(1,SCREEN_HEIGHT))
    platform2.rect = platform2.rect.move(random.randint(1,SCREEN_WIDTH), random.randint(1,SCREEN_HEIGHT))

    # Labels
    scoreLabel = Label('Score: ', 10, 10, 18)
    scoreLabel.drawTo(screen)

    fpsLabel = Label('FPS: ', SCREEN_WIDTH-45, 5, 10)
    fpsLabel.drawTo(screen)

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
        ballSprite.draw(screen)

        platformSprites.update()
        platformSprites.draw(screen)

        scoreLabel.setText(f'Score: {score}')
        scoreLabel.drawTo(screen)

        fpsLabel.setText(f'FPS: {int(clock.get_fps())}')
        fpsLabel.drawTo(screen)

        # Old platform
        white = (255, 255, 255)
        pygame.draw.rect(screen, white, (225, 190, 50, 20))
        pygame.draw.circle(screen, white, (225, 200), 10, 10)
        pygame.draw.circle(screen, white, (275, 200), 10, 10)

        pygame.display.flip()

if __name__ == '__main__': main()
